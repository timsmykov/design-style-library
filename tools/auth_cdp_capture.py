#!/usr/bin/env python3
"""Capture authenticated/browser CDP evidence for design-style-library.

Captures observable DOM/computed style/screenshots from the already-open Chrome
profile. It never reads cookies/localStorage, never prints credentials, and treats
all captured material as design evidence only, not runtime source dependency.
"""
from __future__ import annotations
import base64, json, re, sys, time, urllib.request
from pathlib import Path
import websocket

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
  ('anthropic-claude','claude-new','https://claude.ai/new'),
  ('perplexity-answer-engine','perplexity-home','https://www.perplexity.ai/'),
  ('notion-document-os','notion-home','https://www.notion.so/'),
  ('linear-operational-workspace','linear-home','https://linear.app/'),
  ('vercel-developer-control-plane','vercel-dashboard','https://vercel.com/dashboard'),
  ('figma-collaborative-canvas','figma-files','https://www.figma.com/files/'),
  ('raycast-command-native','raycast-account','https://www.raycast.com/account'),
  ('cursor-ai-ide','cursor-dashboard','https://cursor.com/dashboard'),
  ('airbnb-marketplace-warm-consumer','airbnb-home','https://www.airbnb.com/'),
  ('stripe-trust-commerce','stripe-dashboard','https://dashboard.stripe.com/'),
  ('metamask-crypto-wallet-trust','metamask-portfolio','https://portfolio.metamask.io/'),
]
JS = r'''
(() => {
 const props=['display','position','boxSizing','width','height','paddingTop','paddingRight','paddingBottom','paddingLeft','marginTop','marginRight','marginBottom','marginLeft','fontFamily','fontSize','fontWeight','lineHeight','color','backgroundColor','borderTopColor','borderTopWidth','borderRadius','boxShadow','gap','gridTemplateColumns','flexDirection','alignItems','justifyContent','overflow'];
 const clean=s=>(s||'').replace(/\s+/g,' ').trim().slice(0,800);
 const cssPath=(el)=>{const parts=[];let n=el;while(n&&n.nodeType===1&&parts.length<6){let s=n.tagName.toLowerCase(); if(n.id){s+='#'+n.id.replace(/[^a-zA-Z0-9_-]/g,'');parts.unshift(s);break} const cls=[...n.classList].slice(0,2).map(c=>'.'+c.replace(/[^a-zA-Z0-9_-]/g,''));s+=cls.join('');parts.unshift(s);n=n.parentElement} return parts.join(' > ')};
 const styleOf=(el)=>{const cs=getComputedStyle(el); const out={}; for(const p of props) out[p]=cs[p]; const vars={}; for(const name of Array.from(cs).filter(x=>x.startsWith('--')).slice(0,80)) vars[name]=cs.getPropertyValue(name).trim(); return {props:out, cssVars:vars}};
 const selectors='header,nav,aside,main,section,article,form,input,textarea,button,a,[role="button"],[role="textbox"],[role="dialog"],[class*="sidebar" i],[class*="panel" i],[class*="card" i],[class*="command" i],[class*="editor" i],[class*="dashboard" i],[class*="workspace" i],[class*="settings" i]';
 const els=[...document.querySelectorAll(selectors)].filter(el=>{const r=el.getBoundingClientRect();return (r.width>8&&r.height>8)||clean(el.innerText||el.textContent)}).slice(0,160);
 return {url:location.href,title:document.title,readyState:document.readyState,viewport:{width:innerWidth,height:innerHeight,scrollX,scrollY},bodyTextSample:clean(document.body.innerText).slice(0,2500),rootStyle:styleOf(document.documentElement),bodyStyle:styleOf(document.body),elements:els.map(el=>{const r=el.getBoundingClientRect();return {tag:el.tagName.toLowerCase(),role:el.getAttribute('role'),type:el.getAttribute('type'),ariaLabel:el.getAttribute('aria-label'),href:(el.getAttribute('href')||'').slice(0,300),text:clean(el.innerText||el.textContent),className:String(el.className||'').slice(0,300),path:cssPath(el),rect:{x:Math.round(r.x),y:Math.round(r.y),width:Math.round(r.width),height:Math.round(r.height)},style:styleOf(el)}})};
})()
'''
class CDP:
 def __init__(self, ws): self.ws=websocket.create_connection(ws,timeout=30); self.i=0
 def call(self,m,p=None):
  self.i+=1; self.ws.send(json.dumps({'id':self.i,'method':m,'params':p or {}}))
  while True:
   msg=json.loads(self.ws.recv())
   if msg.get('id')==self.i:
    if 'error' in msg: raise RuntimeError(msg['error'])
    return msg.get('result')
 def close(self): self.ws.close()
def browser_ws(): return json.loads(urllib.request.urlopen('http://127.0.0.1:9224/json/version',timeout=5).read().decode())['webSocketDebuggerUrl']
def create_target(url='about:blank'):
 b=CDP(browser_ws())
 try: return b.call('Target.createTarget',{'url':url,'newWindow':False,'background':True})['targetId']
 finally: b.close()
def target_ws(tid):
 for t in json.loads(urllib.request.urlopen('http://127.0.0.1:9224/json/list',timeout=5).read().decode()):
  if t.get('id')==tid: return t['webSocketDebuggerUrl']
 raise RuntimeError('target not found')
def classify_barrier(v):
 text=((v.get('title') or '')+' '+(v.get('bodyTextSample') or '')+' '+(v.get('url') or '')).lower()
 if any(x in text for x in ['payment','billing','business details','verify your identity','verification required','kyc']): return 'restricted_billing_or_kyc_barrier'
 if any(x in text for x in ['sign in','sign up','log in','login','continue with google','get started','create account']): return 'login_or_signup_barrier'
 return 'captured_surface'
def capture(targets):
 tid=create_target(); c=CDP(target_ws(tid)); index=[]
 try:
  c.call('Page.enable'); c.call('Runtime.enable')
  for style,slug,url in targets:
   out=ROOT/'styles'/style/'evidence/authenticated/browser-cdp'/slug; out.mkdir(parents=True,exist_ok=True)
   c.call('Page.navigate',{'url':url}); time.sleep(7)
   for _ in range(10):
    state=c.call('Runtime.evaluate',{'expression':'document.readyState','returnByValue':True}).get('result',{}).get('value')
    if state=='complete': break
    time.sleep(1)
   time.sleep(2)
   val=c.call('Runtime.evaluate',{'expression':JS,'returnByValue':True,'awaitPromise':True,'timeout':30000}).get('result',{}).get('value') or {}
   html=c.call('Runtime.evaluate',{'expression':'document.documentElement.outerHTML','returnByValue':True,'timeout':20000}).get('result',{}).get('value','')
   shot_data=None
   try:
    shot_data=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']
   except Exception as e:
    shot_data=None
   (out/'dom.html').write_text(html,encoding='utf-8')
   outcome=classify_barrier(val)
   (out/'computed.json').write_text(json.dumps({'style_id':style,'target_slug':slug,'requested_url':url,'captured_url':val.get('url'),'title':val.get('title'),'outcome':outcome,'policy':'authenticated observable evidence only; no credentials/cookies/localStorage captured; do not reuse proprietary source as runtime dependency','data':val},indent=2,ensure_ascii=False),encoding='utf-8')
   if shot_data:
    (out/'screenshot.png').write_bytes(base64.b64decode(shot_data))
   readme=f"# Auth/CDP Evidence — {slug}\n\nRequested: {url}\nCaptured: {val.get('url')}\nTitle: {val.get('title')}\nOutcome: `{outcome}`\n\nFiles: `dom.html`, `computed.json`, `screenshot.png`.\n\nPolicy: evidence only; no secrets/cookies/localStorage captured.\n"
   (out/'README.md').write_text(readme,encoding='utf-8')
   index.append({'style_id':style,'slug':slug,'requested_url':url,'captured_url':val.get('url'),'title':val.get('title'),'outcome':outcome,'path':str(out.relative_to(ROOT))})
 finally:
  try: c.close()
  except Exception: pass
 return index
if __name__=='__main__':
 selected=sys.argv[1:]
 targets=[t for t in TARGETS if not selected or t[0] in selected or t[1] in selected]
 idx=capture(targets)
 out=ROOT/'orchestration/auth-wave/auth-wave-01-capture-index.json'
 out.write_text(json.dumps(idx,indent=2,ensure_ascii=False),encoding='utf-8')
 print(json.dumps(idx,indent=2,ensure_ascii=False))
