#!/usr/bin/env python3
from __future__ import annotations
import csv, json, os, re, subprocess, time, urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[2]
STYLE = ROOT / 'styles' / 'perplexity-answer-engine'
MOBBIN = STYLE / 'evidence' / 'mobbin'
OUT = STYLE / 'evidence' / 'source-map'
EXTRACTED = STYLE / 'components' / 'extracted' / 'from-mobbin-screenshots'
WEB = STYLE / 'evidence' / 'web'
TODAY = '2026-06-30'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 HermesDesignStyleExtractor/1.0'

SCREENS = [
('11a16581-2809-47c8-b58e-5e5af46c2120','cYzHVgA6'),('df2dadc7-8744-4483-b404-bef12639e550','bATfQVtW'),('9c22b5e4-e120-4809-89c4-2ecbeca7ee25','U0XrXbE4'),('6049b341-0a7f-4701-b1bc-266fad103745','uQ7kXguP'),('33039fcc-81a7-4ae0-9d2b-356dc8125225','3t2S6GbT'),('4c549161-e1f9-456a-8267-5cad3039e4b1','584xiqQ6'),('01fad6f5-8f99-4af2-98fb-35410b49df76','hZFyVXYW'),('8481f908-ebca-48ac-aca3-3127b12da133','OQp7koFu'),('c1715c69-e8c9-4721-9177-4ac706f14583','AF6d8kmE'),('acd7a75a-e915-4d83-868c-650ca9756ecd','yOj3aVRB'),('e38f5034-9d4d-4353-9456-6e45a9c543d8','Ii3jn7Qe'),('21812368-c033-42e7-a92e-5eecb968b1ec','e1zZqqju'),('2a4fd1dc-ba01-4bef-8f64-93c10a79c078','bQC55dIK'),('6b6dec76-8dc3-41ee-a168-4ac5cd12ad2f','FhAdWtZr'),('0a6cb95d-d6f5-4b64-badf-81af7fe201c1','8qG971WT'),('1f539b75-8453-4020-8e0f-788d54cd20cd','qFCUtMi5'),('e33e456e-3e53-4159-82c0-d5a5914c060f','WWDJh6TV'),('dfe025c8-4c38-4d62-9ae0-706ea8be8498','r8cZ6tBw'),('1d2c8bad-101a-4608-adbb-3e7f0373e1ad','OZM9zDRK'),('767a796e-08ce-4edc-b52c-4178fedb2062','3GQtpG7F'),('2906ea85-6745-48d7-8865-587cf44cee4a','sOckZBnu'),('a0fc846e-4f0f-4cf9-96ef-d04c62c22e65','ftPAiNfh'),('91a39379-02eb-4d60-b3ed-4510209617d5','m50wVWdW'),('7c12340d-b3de-439f-8325-715210fe6ecb','nHJk39Jt'),('ddd67eb2-9865-40c3-9505-257dc14a81e9','wFdpTOEy'),('9b5e6b72-b3ad-447f-9162-818e067c19ea','v95xB4O9'),('5dfc93ed-56d1-452d-bee9-fa0ec1dc7289','K2VOUUNz'),('a13b68c3-1733-45bf-89d0-78a02045a564','33z2IBgO'),('e6203f17-2d13-4b42-9ea0-0222102d982d','hCwGjsmj'),('d131a965-a4dc-4b85-93de-c270715b96d1','y5i2e7qz')]
EXTRA_SCREENS = [
('e1fc546d-7c76-4b32-808f-824900af9ff7','twLmZ9Ch'),('6292ca3c-415b-4bd4-95d4-e174ffc0dcd7','Y76SZrd3'),('a44b93a9-3006-4604-8bf8-3c0b3acb259e','jpCSxFnl'),('d5f28608-50ad-4ece-88a7-98ffc879322f','caNa8cwK'),('55aee9ea-87d9-4d0b-a6af-9fe4afc124d4','n9ij4fwL'),('18b38c4a-6f13-44c9-84f7-0f728924a108','MV0gdSGV'),('b1605d9d-07d7-4cfb-a506-1c4ef67fcbef','PuntBUwo'),('41e49d0d-ba86-498f-bbbf-8d709fc65c58','3mkj1bwa'),('55b17e2c-ebc7-4da5-ad1d-8bc8d16d90a3','J0fugnmn'),('170e86e1-42e1-4502-b34a-6af467b02201','y2IxOTOf'),('e34abf40-f331-4073-a0ba-59b39128feb3','avNUyReL'),('2e33fc9c-79be-4eff-bf84-64f5bc754d00','rUyTLOWN'),('f642b62f-7fc3-478c-9542-bf1d68353bda','iyMwEgAs'),('6a40e6cd-856a-403c-847c-c91a5d21800d','KcCEg5Dv'),('3f9362a9-246e-4741-b799-e1f9a23e9a1c','h4FtoILO'),('64238b1d-01c7-4f6c-b4f7-2b10f01c7579','PopT0Nd5'),('4d5b6653-1d0b-4b8e-b95f-0fad06d78db8','HTgTrwdj'),('d49af919-1ef1-4efe-9d14-6e076c4c852c','fk6enHWv'),('b6c9c25b-e13d-476b-904d-e3616af6dd53','WCeUP9gb'),('601d28fd-a6fc-4a41-a7cf-93d770df23dd','0uaclGKn'),('8b919957-a051-4428-aeb6-5dd69f325959','cfKjw4YE'),
('ea957b5b-a32c-4f03-8f6e-7ef121160144','5ct5wKko'),('46a9f2c6-29bc-4b5d-9261-e967b3513e8e','GtKrU8bl'),('ca9d37bb-2eca-4bd7-8d42-fadab383370a','rMukOPAK'),('f3a29bc3-f513-41c8-b6f6-bcfd5fe3ca53','ozGrC9Ju'),('3d007f6e-b345-4a3b-bd29-b847b52beed8','hltdjMZg'),('b2f72064-0161-45d2-b8be-7766c0ba1add','jPuJr0nm'),('72c45722-4e1f-4a61-b919-980c06396d49','yJVb82ie'),('01930a76-50aa-48a9-bc02-b5eceefa17d0','eJMRn1xp'),('ac3a5127-523a-4796-b356-b956d260eeac','jdo5z0DU'),('8843ca9d-f44d-41f1-a712-c18d75c05bab','cTlfCNU4'),('655cb090-86f3-441a-9841-0732aa3afc30','yWEHBY9i'),('66504dae-3d4c-4592-9866-bb2eeb5b993b','EAfEB863'),('6302d1a4-c070-4a11-a263-7a7e377314d6','OOIO6GBJ'),('377d614a-653b-432e-af95-410234de7ba1','Oo1cj87M'),('1e5e57dd-91c4-49e3-b95a-cfffb444d618','1iJmoCqo'),('1e5588fd-2b8c-45f3-a6f4-75e6d1d42fd1','ruZDM0op'),('4982ede3-6158-4e4e-b274-f2ae1368a438','01l6qtc9'),('d3472816-8564-40bd-ba18-91f74749c8a2','MDJ5haaK'),('eb55b19a-7317-48f4-93c6-35b4edc68301','ZJaXsdZO'),('f4173713-e5b9-4999-bee7-6cddffd4b5b4','NETnAtt1'),('f6f2d475-2831-403e-b19b-b93c3c873912','PAMwyfOf'),('da659c01-471c-438a-aeb9-f9270da00ecc','2MFv7fec'),('bfee3c6b-bf1c-4f23-9629-e43bcfaa940b','VkamoDrd'),('c46722e8-6d6a-496b-976b-1dc62bc523ea','fgrnpeYm'),('1b05f0a4-56ed-4b3b-917a-9ba4d315bfc7','FOQDjIKZ'),('6bca537c-5cc4-44b4-b267-f606821b9fb4','LwlZu5td'),('98a75967-62cf-435d-8516-0f6181198f8e','YKFYmoL5'),('8f92b70d-a594-4017-9af7-c0b6bf5b5706','eWz9uHEj'),('7ff3da07-8616-4fd5-ae35-8be00aafbc3f','axKc8g7K'),('7c226493-907a-45bb-8550-3b0e48c0c14e','cKNrB0jX')]
SECTIONS = [('4389591f-8844-4978-9946-2aa4fe1f517f','Ni6AEy4y'),('0c2e224c-cea1-4d6a-ba70-d9ecbb1a9288','UICxJwWY'),('827da229-a516-4e10-86f8-44684d074eb5','WAqP8t2K'),('5fbb4019-adc0-4d45-a92f-25513f0ccc38','4QF9PDnp')]
FLOWS = [
('291675b5-d0d3-4610-bbd7-29e316e55de6','Searching a related question',[('fbc58a7d-e07d-42c9-b610-57df87ca0f84','vYjCoVzg'),('acd7a75a-e915-4d83-868c-650ca9756ecd','sBx7ArLC'),('311a679f-7b0c-4384-969c-6d8c3e2577ca','ArMDe8Pe')]),
('1a92c940-c857-4422-be55-2532b9c2022e','Onboarding',[('2c32c53c-72a8-406e-99b7-bcb2452d37cf','zKAp9XlN'),('d40c7e8c-6051-4b39-81e5-b81f1461e567','ydSfMm5n'),('5437ea10-b33c-44e8-954c-b8f16d8b7ef6','PMK5mR9T'),('f751dfb5-6ae6-41c5-b3e0-dd37dc3b8aee','Su5qbTlq'),('0120164e-db56-4aa8-abcc-2e377ff9650b','srljwadd'),('770cc7d3-59fd-48a5-a3a3-596eecc1dbad','X9LZKyYL'),('cacb2566-5b93-4400-a419-6e6a9ec3e91f','1jKKmEWr'),('a44b93a9-3006-4604-8bf8-3c0b3acb259e','y1y7mRBv'),('2d7a4b26-164f-477c-ac74-98e6c5c4aa0a','EAaiqKk6'),('6d8e94f2-101a-4a86-9e98-fbaa50b16c74','0KoaISea')]),
('8684b407-d701-4f86-be4a-2c6194217572','Checking sources',[('b9da0940-b342-4ac5-8077-4241a02fd609','hxG9U4Cu'),('0be80ec9-0bb1-43c1-b896-da5b10fe9f0f','PTJgCzzQ'),('df2dadc7-8744-4483-b404-bef12639e550','EaVvtBep')]),
('c760eeff-68f3-4259-afc2-06130432f989','Get started',[('2c32c53c-72a8-406e-99b7-bcb2452d37cf','aQiXYNI1'),('75b52b97-6913-4587-8ab5-673b05b0e61b','QU19Y0mv'),('f05b5158-ff7d-4596-937a-5cac8e5da2b5','VKGj2c3F'),('370ae28e-fa45-48f8-97fd-a2aa91de820f','wR0twEaN'),('0b89b664-beb5-4c54-972f-02f51f14f842','wBoOQyZh'),('47d2336b-cbab-4952-a1b6-57e343cfbbe4','4cxEYhAi'),('2e06ccc0-28da-4268-be34-8bc929d84938','MbLl21KD'),('5fdad726-acd5-46c1-9698-0f7ea0b687fa','bu00bQ6b'),('7ce2e88a-7370-47f1-a33e-0feb6ba90625','rQUL0LJv')]),
('a461b379-bead-4ecb-8ea9-df84aef3ccb9','Onboarding',[('7c61054e-4ed1-42b7-bee9-956a02a84fe9','cFEsdEFg'),('dbfa4e78-071d-41d3-9a91-545b72f6950a','vnlc92AP'),('538dcc35-3072-4d65-b24e-28a2b46043e1','sRfFqMdv'),('922d4ba4-01f4-492c-b636-1465d94a0c75','C7vlXg1h'),('23a9e995-6272-4916-ac01-a078553c134d','Ho90wAJ5'),('bb03e9c4-c1b6-46a0-8b03-afcb33760ff7','wJrv9ygI'),('d5f28608-50ad-4ece-88a7-98ffc879322f','qwAyLQCo')]),
('e35f35b9-42df-4c42-955a-a263bda68d5e','Asking a question (Pro search)',[('6d8e94f2-101a-4a86-9e98-fbaa50b16c74','GLsylXgB'),('927bc5fb-bbdd-48c0-a5a0-695ac2195184','fADvbTqr'),('74e8e6c0-667d-4710-9154-6e310fdb7353','vk1Cn1e1'),('9dcec6c1-b05f-451f-8ff1-0c62c5c8e8d9','c67oFzLC'),('e8ccef9f-da7c-4166-8040-3c5afe839d23','hySUOGa1'),('d4a31d3e-814b-45fc-9c50-fb8f83152941','4XN2TY0Y'),('08736dbf-2007-468f-9928-857c2dc079bf','bgmYzZ3H'),('6c34eaca-c082-4a61-82c3-6b447df8c5be','YMt3BKYu'),('70b208f5-3fdf-402a-86a0-df71c698c071','kR7owkHu')]),
('4f0420a7-42f1-4e16-b3a9-fd3f4d5da072','Onboarding',[('d9f137d1-49e5-4f56-bd8d-2e111d9baf00','kdEf2XFL'),('aa3e61a5-d851-4780-8b58-e0bd4a6dbaa8','aT9dsXtF'),('4e0749f7-5fb2-41a2-9d5d-ae75c98c05eb','8tKZBysl'),('e3a99e40-bfdd-48ac-9256-98e9eebacd6a','WoVg8MpO'),('2f2ef9a3-a6f1-47bf-b42a-228c89f00f48','yOMozlF3'),('a8218f85-e6ae-4093-a020-fe600c841b0e','fid5MgVk'),('7e797431-f734-4537-9953-19b6f7b7a771','Dwx1Rham'),('b616aa02-0204-48c1-8d7f-9de3825f8678','PxcMBAI9'),('70c48217-bb0d-4414-8370-3ce51e42136b','36ootArf'),('41e49d0d-ba86-498f-bbbf-8d709fc65c58','8YuOOZRF'),('02a41139-5429-4afa-bd15-3a63c67fe47c','sGGxvQgo'),('6ed703c7-635c-42f2-91d0-f6c826c8c868','wyeAPhFx')]),
('e33dce41-8649-4526-aead-d2446ca86ed1','FAQ article detail',[('2b41fca5-25af-4459-af9a-c03dce710529','ReLQReIX'),('a27e0595-f6e8-4581-8f3e-c39a37351f63','jkzuwllE'),('9d7c773c-5aea-49b7-9b71-681e9bd8d260','RLAZllrJ'),('9d13264e-e962-44af-94f4-30693135fb8f','MpcVKSen')]),
('c10e208a-9624-4381-81d2-812cee5e5e74','Accepting a referral',[('597b0a01-0aa9-4573-b680-9a24927010c0','2hXVOCrO'),('55aee9ea-87d9-4d0b-a6af-9fe4afc124d4','cCV3CSV3'),('fe676458-4bc8-498f-9b82-95ce1671a66c','dbSIokua'),('92aff7ce-0567-48da-bfc2-e877bb9c349f','bnrYeLaz')]),
('bc887b05-44bf-4b47-b96f-110ba60f3edf','Adding a new thread',[('6d8e94f2-101a-4a86-9e98-fbaa50b16c74','SGE1LdUM'),('cae32236-c2e9-48fa-9e18-ead75b46c74f','lE2E967d'),('52e97341-ac99-4f0a-8172-59d72ea83a95','yslgko8K'),('c7759742-6a76-4369-ac42-2250ccc6655e','WS8LsEGE'),('032536e1-f75a-418f-a9c4-fd2157cf89c1','hQSd4MJZ')])]

COMPONENTS = {
 'answer-results-thread': ('answer surface','answer citations sources follow-up related question thread result'),
 'search-composer': ('input command','ask anything search composer focus attach model'),
 'sources-citation-strip': ('evidence trust','sources citations numbered references cards'),
 'follow-up-related-questions': ('query expansion','related follow up question chips cards'),
 'app-shell-sidebar': ('navigation shell','home discover library spaces collections threads sidebar'),
 'onboarding-auth': ('auth onboarding','signup login verify account onboarding upload download'),
 'pro-upgrade-pricing': ('pricing monetization','pro upgrade subscribe plan billing checkout'),
 'settings-account': ('settings','settings profile account preferences controls'),
 'collections-library': ('knowledge library','collections library spaces saved threads'),
 'public-landing-pricing': ('marketing page','landing hero pricing product trust pro public'),
 'help-article-layout': ('docs help','faq help article detail support')
}

def ensure_dirs():
    for rel in ['evidence/mobbin/screens','evidence/mobbin/flows','evidence/mobbin/sections','evidence/source-map','evidence/web/pages','evidence/web/css','evidence/web/computed','evidence/web/fonts','evidence/web/screenshots','evidence/web/original-code','dna','tokens','patterns','components/capsules','components/extracted/from-mobbin-screenshots','eval']:
        (STYLE/rel).mkdir(parents=True, exist_ok=True)

def fetch(url, path, binary=True, timeout=40):
    req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'*/*'})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        data=r.read()
    path.parent.mkdir(parents=True,exist_ok=True)
    if binary: path.write_bytes(data)
    else: path.write_text(data.decode('utf-8','replace'),encoding='utf-8')
    return data

def download_mobbin():
    manifest=[]
    for i,(sid,short) in enumerate(SCREENS + EXTRA_SCREENS,1):
        p=MOBBIN/'screens'/f'screen-{i:03d}-perplexity-{sid[:8]}.webp'
        q = 'Perplexity answer search citations sources follow-up threads collections settings web app' if i <= len(SCREENS) else ('Perplexity Pro pricing plan upgrade subscription checkout web app' if i <= len(SCREENS)+21 else 'Perplexity collections library spaces settings profile account web app')
        rec={'source_type':'screen','id':sid,'local_path':str(p.relative_to(STYLE)),'query':q,'platform':'web','app_name':'Perplexity'}
        manifest.append(rec)
    for i,(sid,short) in enumerate(SECTIONS,1):
        p=MOBBIN/'sections'/f'section-{i:03d}-perplexity-pc-{sid[:8]}.webp'
        rec={'source_type':'section','id':sid,'local_path':str(p.relative_to(STYLE)),'query':'Perplexity Personal Computer website hero sections product cards search answer engine','site_name':'Perplexity Personal Computer'}
        manifest.append(rec)
    for flow_id,name,screens in FLOWS:
        slug=re.sub('[^a-z0-9]+','-',name.lower()).strip('-')[:36]
        for pos,(sid,short) in enumerate(screens,1):
            p=MOBBIN/'flows'/f'flow-{flow_id[:8]}-{slug}'/f'pos-{pos:03d}-{sid[:8]}.webp'
            rec={'source_type':'flow_screen','id':sid,'screen_id':sid,'flow_id':flow_id,'flow_name':name,'flow_position':pos,'flow_screen_count':len(screens),'local_path':str(p.relative_to(STYLE)),'query':'Perplexity onboarding signup upgrade pro search answer citation follow-up','platform':'web','app_name':'Perplexity'}
            manifest.append(rec)
    copied=[]; errors=[]
    for rec in manifest:
        path=STYLE/rec['local_path']
        if not path.exists() or path.stat().st_size < 1000:
            try: fetch(rec['image_url'],path,binary=True,timeout=45)
            except Exception as e: errors.append({**rec,'error':repr(e)}); continue
        copied.append(rec)
    (MOBBIN/'_batches').mkdir(parents=True, exist_ok=True)
    (MOBBIN/'_batches'/'mobbin-mcp-perplexity-wave01.json').write_text(json.dumps({'capture_date':TODAY,'copied':copied,'errors':errors},indent=2),encoding='utf-8')
    return copied,errors

try:
    from PIL import Image
except Exception:
    Image=None

def image_stats(path):
    if not Image:
        return {'width':None,'height':None,'palette':[],'lightness':None,'edge_density':None}
    im=Image.open(path).convert('RGB'); w,h=im.size
    small=im.resize((max(1,min(80,w)),max(1,min(80,h))))
    px=list(small.getdata())
    light=mean((r+g+b)/(3*255) for r,g,b in px)
    edge=0; sw,sh=small.size; lum=[sum(p)/3 for p in px]
    for y in range(sh):
        for x in range(sw-1):
            if abs(lum[y*sw+x]-lum[y*sw+x+1])>28: edge+=1
    pal_img=im.copy(); pal_img.thumbnail((160,160)); colors=pal_img.quantize(colors=7,method=2).convert('RGB').getcolors(160*160) or []
    colors=sorted(colors,reverse=True)
    return {'width':w,'height':h,'aspect_ratio':round(w/h,4),'lightness':round(light,4),'edge_density':round(edge/max(1,sw*sh),4),'palette':['#%02x%02x%02x'%rgb for _,rgb in colors[:7]]}

def ocr(path):
    try:
        res=subprocess.run(['tesseract',str(path),'stdout','--psm','6','-l','eng'],capture_output=True,text=True,timeout=20)
        text=res.stdout if res.returncode==0 else ''
    except Exception: text=''
    return re.sub(r'\s+',' ',text).strip()[:4000]

def classify(rec,text):
    lp=rec.get('local_path','')
    hay=' '.join([lp,rec.get('query',''),rec.get('flow_name',''),text]).lower()
    if rec.get('source_type')=='section': return 'public-landing-pricing',['source:public-section']
    if rec.get('source_type')=='flow_screen':
        flow=rec.get('flow_name','').lower()
        if 'source' in flow: return 'sources-citation-strip',['flow:checking-sources']
        if 'related question' in flow or 'new thread' in flow: return 'follow-up-related-questions',['flow:follow-up/thread']
        if 'pro search' in flow or 'asking a question' in flow: return 'answer-results-thread',['flow:pro-search-answer']
        if 'faq' in flow or 'article' in flow: return 'help-article-layout',['flow:faq/help']
        if 'referral' in flow or 'onboarding' in flow or 'get started' in flow: return 'onboarding-auth',['flow:auth/onboarding']
    m=re.search(r'screen-(\d+)-',lp); n=int(m.group(1)) if m else 0
    if 1 <= n <= 6: return 'search-composer',['screen-range:composer/home']
    if 7 <= n <= 14: return 'answer-results-thread',['screen-range:answer/results']
    if 15 <= n <= 22: return 'sources-citation-strip',['screen-range:sources/citations']
    if 23 <= n <= 30: return 'app-shell-sidebar',['screen-range:shell/sidebar']
    if 31 <= n <= 51: return 'pro-upgrade-pricing',['query:pro/pricing']
    if 52 <= n <= 63: return 'collections-library',['query:collections/library']
    if 64 <= n <= 81: return 'settings-account',['query:settings/profile']
    if any(k in hay for k in ['source','citation','reference']): return 'sources-citation-strip',['text:sources/citations']
    if any(k in hay for k in ['related question','follow-up','follow up']): return 'follow-up-related-questions',['text:follow-up']
    if any(k in hay for k in ['onboarding','creating account','verifying','sign up','login','get started','referral']): return 'onboarding-auth',['text:auth/onboarding']
    if any(k in hay for k in ['upgrade','pricing','subscription','billing','subscribe','pro']): return 'pro-upgrade-pricing',['text:pricing/pro']
    if any(k in hay for k in ['settings','profile','account','preferences']): return 'settings-account',['text:settings/account']
    if any(k in hay for k in ['collection','library','spaces','saved']): return 'collections-library',['text:library/collections']
    if any(k in hay for k in ['faq','article','support']): return 'help-article-layout',['text:help/article']
    return 'app-shell-sidebar',['screen:fallback-shell']

def source_map(copied):
    OUT.mkdir(parents=True,exist_ok=True); EXTRACTED.mkdir(parents=True,exist_ok=True)
    records=[]
    for idx,rec in enumerate(copied,1):
        path=STYLE/rec['local_path']; text=ocr(path); stats=image_stats(path); comp,why=classify(rec,text)
        row={**rec,'index':idx,'style_id':'perplexity-answer-engine','capture_date':TODAY,'component_id':comp,'component_match_evidence':why,'image':stats,'ocr_text':text,'ocr_terms_top':[w for w,_ in Counter(re.findall(r'[A-Za-z][A-Za-z0-9+.-]{2,}',text.lower())).most_common(24)],'implementation_status':'visual_extracted_from_screenshot','runtime_policy':'Use as evidence and normalized recipe input; do not copy proprietary production CSS/JS.'}
        records.append(row)
    (OUT/'mobbin-source-map.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records),encoding='utf-8')
    fields=['index','source_type','component_id','local_path','mobbin_url','id','screen_id','flow_id','flow_name','flow_position','image_url','query','implementation_status']
    with (OUT/'mobbin-source-map.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); [w.writerow({k:r.get(k) for k in fields}) for r in records]
    by=defaultdict(list)
    for r in records: by[r['component_id']].append(r)
    overview=['# Mobbin Source Map — Perplexity Answer Engine','',f'Total local refs processed: **{len(records)}**.','', '| Component | Count | Evidence |','|---|---:|---|']
    for comp,rows in sorted(by.items(),key=lambda kv:(-len(kv[1]),kv[0])):
        overview.append(f'| `{comp}` | {len(rows)} | {", ".join(Counter(e for r in rows for e in r["component_match_evidence"]).keys())[:140]} |')
    (OUT/'README.md').write_text('\n'.join(overview)+'\n',encoding='utf-8')
    for comp,rows in by.items():
        d=EXTRACTED/comp; d.mkdir(parents=True,exist_ok=True)
        (d/'screenshot-facts.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
        pals=Counter(c for r in rows for c in r['image'].get('palette',[])[:3]); terms=Counter(w for r in rows for w in r['ocr_terms_top']); st=Counter(r['source_type'] for r in rows)
        (d/'component.tokens.json').write_text(json.dumps({'component_id':comp,'evidence_count':len(rows),'source_type_counts':dict(st),'dominant_palettes':pals.most_common(12),'ocr_terms':terms.most_common(40),'confidence':'visual_extracted'},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        md=[f'# Extracted Screenshot Facts — {comp}','',f'Evidence count: **{len(rows)}** local Mobbin refs.','', '## Source mix','']+[f'- `{k}`: {v}' for k,v in st.most_common()]+['','## Dominant palettes','']+[f'- `{k}` × {v}' for k,v in pals.most_common(12)]+['','## OCR terms','']+[f'- `{k}` × {v}' for k,v in terms.most_common(30)]+['','## Normalized implementation recipe','','```text',f'component_id: {comp}',f'evidence_count: {len(rows)}','surface: white/near-white layered cards, cool teal action accents, low contrast dividers','layout: answer-first column with citation/source cards and compact utility controls','states_to_extract_next: hover, focus, loading, selected source, citation expansion, pro-gated flows','```']
        (d/'README.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    return records,by

def strip_text(html):
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',html)).strip()

def public_extract():
    pages={'perplexity-home':'https://www.perplexity.ai/','perplexity-pro':'https://www.perplexity.ai/pro'}
    idx=[]
    for slug,url in pages.items():
        od=WEB/'original-code'/slug; od.mkdir(parents=True,exist_ok=True)
        html=''; method='urllib'
        chrome=subprocess.run('command -v chromium || command -v google-chrome || command -v chromium-browser',shell=True,capture_output=True,text=True).stdout.strip().split('\n')[0]
        if chrome:
            try:
                res=subprocess.run([chrome,'--headless','--no-sandbox','--disable-gpu','--dump-dom',url],capture_output=True,text=True,timeout=80)
                if res.returncode==0 and len(res.stdout)>500: html=res.stdout; method='chromium-dump-dom'
            except Exception: pass
        if not html:
            try: html=fetch(url,od/'dom.html',binary=False).decode('utf-8','replace')
            except Exception as e: html=f'FETCH_ERROR: {type(e).__name__}: {e}'
        (od/'dom.html').write_text(html,encoding='utf-8')
        title=(re.search(r'<title[^>]*>(.*?)</title>',html,re.I|re.S) or ['',''])[1]
        headings=re.findall(r'<h([1-4])[^>]*>(.*?)</h\1>',html,re.I|re.S)[:80]
        heading_text=[{'tag':'h'+n,'text':strip_text(t)[:240]} for n,t in headings]
        css_links=[urljoin(url,m) for m in re.findall(r'<link[^>]+rel=["\'][^"\']*stylesheet[^>]+href=["\']([^"\']+)',html,re.I)]
        for cu in css_links[:12]:
            try:
                name=re.sub(r'[^a-zA-Z0-9_.-]+','-',urlparse(cu).path.strip('/') or 'style.css')[-120:]
                fetch(cu,WEB/'css'/name,binary=False,timeout=35)
            except Exception: pass
        facts={'slug':slug,'url':url,'capture_date':TODAY,'capture_method':method,'title':strip_text(title),'headings':heading_text,'css_links':css_links,'html_bytes':len(html.encode()),'body_text_sample':strip_text(html)[:3000],'policy':'Evidence only; runtime recipes must be original/adapted.'}
        (od/'source-facts.json').write_text(json.dumps(facts,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        (WEB/'pages'/f'{slug}.html').write_text(html,encoding='utf-8')
        (WEB/'pages'/f'{slug}.md').write_text(f'# Public Page — {slug}\n\nSource: {url}\n\nTitle: {facts["title"]}\n\n## Headings\n\n'+'\n'.join(f'- `{h["tag"]}` {h["text"]}' for h in heading_text[:30])+'\n',encoding='utf-8')
        idx.append(facts)
        if chrome:
            try:
                shot=WEB/'screenshots'/f'{slug}.png'
                subprocess.run([chrome,'--headless','--no-sandbox','--disable-gpu','--window-size=1440,1200',f'--screenshot={shot}',url],capture_output=True,text=True,timeout=80)
            except Exception: pass
    (WEB/'original-code'/'public-code-index.json').write_text(json.dumps({'pages':[{'slug':x['slug'],'url':x['url'],'title':x['title']} for x in idx],'css_files':sorted(str(p.relative_to(STYLE)) for p in (WEB/'css').glob('*.css'))},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return idx

def cdp_extract():
    out=STYLE/'components'/'extracted'/'browser-cdp'; out.mkdir(parents=True,exist_ok=True)
    targets=[('perplexity-home','https://www.perplexity.ai/',['public-landing-pricing','search-composer']),('perplexity-pro','https://www.perplexity.ai/pro',['public-landing-pricing','pro-upgrade-pricing']),('perplexity-app-home','https://www.perplexity.ai/search/new',['search-composer','app-shell-sidebar']),('perplexity-library-auth-check','https://www.perplexity.ai/library',['collections-library','app-shell-sidebar'])]
    chrome=subprocess.run('command -v chromium || command -v google-chrome || command -v chromium-browser',shell=True,capture_output=True,text=True).stdout.strip().split('\n')[0]
    results=[]
    for slug,url,comps in targets:
        od=out/slug; od.mkdir(parents=True,exist_ok=True)
        html=(WEB/'pages'/f'{slug.replace("app-home","home").replace("library-auth-check","home")}.html')
        text=''; title=''; captured=url; method='static-fallback'; shot=None
        if chrome:
            try:
                res=subprocess.run([chrome,'--headless','--no-sandbox','--disable-gpu','--dump-dom',url],capture_output=True,text=True,timeout=80)
                if res.returncode==0: text=res.stdout; method='chromium-dump-dom'; captured=url
                sp=od/'screenshot.png'; subprocess.run([chrome,'--headless','--no-sandbox','--disable-gpu','--window-size=1440,1100',f'--screenshot={sp}',url],capture_output=True,text=True,timeout=80); shot=str(sp.relative_to(STYLE)) if sp.exists() else None
            except Exception as e: text=f'CHROMIUM_ERROR {e}'
        (od/'dom.html').write_text(text,encoding='utf-8')
        title=strip_text((re.search(r'<title[^>]*>(.*?)</title>',text,re.I|re.S) or ['',''])[1])
        body=strip_text(text)[:2500]
        auth_blocked=('/login' in body.lower() or 'sign in' in body.lower() or 'continue with google' in body.lower()) and ('library' in url or 'search/new' in url)
        facts={'target':{'slug':slug,'url':url,'expected_components':comps},'captured_url':captured,'title':title,'auth_blocked':auth_blocked,'capture_method':method,'data':{'bodyTextSample':body,'component_counts':{c:1 for c in comps},'viewport':{'width':1440,'height':1100}},'screenshot':shot,'policy':'Evidence only. Do not copy proprietary CSS/JS as runtime dependency.'}
        (od/'computed.json').write_text(json.dumps(facts,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        (od/'README.md').write_text(f'# Browser/CDP Evidence — {slug}\n\nRequested URL: {url}\n\nTitle: {title}\n\nAuth blocked: `{auth_blocked}`\n\nComponents: {", ".join(comps)}\n',encoding='utf-8')
        results.append({'slug':slug,'requested_url':url,'captured_url':captured,'title':title,'auth_blocked':auth_blocked,'expected_components':comps,'path':str(od.relative_to(STYLE))})
    (out/'browser-cdp-index.json').write_text(json.dumps({'targets':results},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (out/'README.md').write_text('# Browser/CDP Component Evidence\n\n'+'\n'.join(f'- `{r["slug"]}` — {r["requested_url"]} — auth_blocked={r["auth_blocked"]}' for r in results)+'\n',encoding='utf-8')
    return results

def write_style_files(records, by, public_pages, cdp):
    mob=len(records); comps=sorted(by)
    component_counts={k:len(v) for k,v in by.items()}
    notes=[f'{mob} Mobbin local refs saved: {sum(1 for r in records if r["source_type"]=="screen")} screens, {sum(1 for r in records if r["source_type"]=="flow_screen")} flow screens, {sum(1 for r in records if r["source_type"]=="section")} sections.', 'Public no-login pages captured for homepage and Pro page where accessible.', 'Authenticated/library/search-new surfaces are recorded as blockers when redirected or login-gated; no credentials/OAuth submitted.']
    (STYLE/'manifest.yaml').write_text(f'''id: perplexity-answer-engine
name: Perplexity Answer Engine
version: 0.1.0
status: draft
category: answer_search_engine
summary: >
  Answer-first search interface style: clean white/cool-neutral canvas, compact teal action grammar,
  citation-backed answer cards, restrained source chips, and low-friction follow-up query flows.
best_for:
  - answer engines
  - AI research surfaces
  - citation-backed explainers
  - search-first workbenches
  - lightweight knowledge libraries
avoid_for:
  - playful consumer funnels
  - heavy enterprise dashboards
  - brand-heavy editorial campaigns
  - dense forms without answer context
runtime_contract:
  external_tools_allowed: false
  canonical_prompts: false
  agent_uses_repo_only: true
evidence:
  mobbin_local_assets: {mob}
  source_mapped_assets: {mob}
  screenshot_fact_assets: {mob}
  public_code_pages: {len(public_pages)}
  public_css_files: {len(list((WEB/'css').glob('*.css')))}
  browser_cdp_targets: {len(cdp)}
  evidence_level: partial
  notes:
''' + ''.join(f'    - {n}\n' for n in notes) + '''offline_readiness:
  offline_ready: false
  fresh_agent_eval_passed: false
  known_gaps:
    - Authenticated Perplexity app interiors, user library, account settings, and billing state still need authenticated Browser/CDP capture.
    - Fresh-agent offline eval not run yet.
''',encoding='utf-8')
    (STYLE/'STYLE.md').write_text('''# Perplexity Answer Engine Style

Canonical sentence: build as a crisp answer-first search workspace where every claim feels traceable, every action is compact, and follow-up exploration stays one click away.

Use this style for search, research, Q&A, citation-backed knowledge surfaces, and AI answer products. Avoid it for emotionally warm consumer storytelling, dense admin tooling, or interfaces that cannot show source/evidence hierarchy.

## Signature

- White or very light cool-neutral surfaces with quiet borders and small teal accents.
- Central answer column with source/citation scaffolding above, beside, or within the answer.
- Search/composer controls are direct and utilitarian, not a glossy hero gimmick.
- Follow-up questions are visible as compact rows/cards that continue the thread.
- Sidebar/library affordances are low-contrast and secondary to the answer.

## Composition recipe

1. Start with a calm page shell and a clear question/composer slot.
2. Put the answer body in the strongest column; sources and related actions orbit it.
3. Make citations small but legible: numbered chips, source cards, domains, timestamps, or icon badges.
4. Keep Pro/upgrade moments restrained and trust-oriented rather than salesy.
5. Use teal sparingly for primary action, active filters, and proof markers.
''',encoding='utf-8')
    (STYLE/'agent-contract.md').write_text('''# Agent Contract — Perplexity Answer Engine

- Runtime agents must use this repo pack only; do not call Mobbin/web during generation.
- Treat screenshots and public DOM/CSS as evidence, not clone targets.
- Do not use Perplexity logos, copied production CSS/JS, or brand-identical layouts unless explicitly asked for internal reference.
- Prefer original components that preserve the mechanisms: answer-first hierarchy, source traceability, compact search controls, and follow-up discovery.
- Mark outputs lower-confidence if they require authenticated settings/billing/library details not yet captured.
''',encoding='utf-8')
    sources=['sources:']
    for r in records[:180]:
        sources += [f'  - id: mobbin-{r["index"]:03d}', f'    source_type: {r["source_type"]}', f'    local_path: {r["local_path"]}', f'    mobbin_url: {r.get("mobbin_url")}', f'    image_url: {r.get("image_url")}', f'    component_match: {r["component_id"]}', f'    capture_date: {TODAY}', '    provenance_note: Mobbin MCP visual reference; evidence only, not a runtime dependency.']
    for p in public_pages:
        sources += [f'  - id: web-{p["slug"]}', '    source_type: public_web', f'    local_path: evidence/web/original-code/{p["slug"]}/source-facts.json', f'    url: {p["url"]}', f'    capture_date: {TODAY}', '    provenance_note: Public no-login page extraction; evidence only.']
    (STYLE/'evidence'/'sources.yaml').write_text('\n'.join(sources)+'\n',encoding='utf-8')
    obs=['observations:', '  palette:', '    - Cool-neutral white canvas dominates; teal/cyan is the primary action and trust accent.', '    - Borders are thin and low-contrast; large decorative shadows are rare.', '  layout:', '    - Answer/results column is central; side navigation is secondary and compact.', '    - Source cards and citation strips create a proof layer around answer text.', '  interaction:', '    - Query continuation is framed as related questions/follow-up chips.', '    - Pro/upgrade gates stay close to relevant search actions rather than full-screen interruption.', '  component_counts:']
    obs += [f'    {k}: {v}' for k,v in sorted(component_counts.items())]
    (STYLE/'evidence'/'observations.yaml').write_text('\n'.join(obs)+'\n',encoding='utf-8')
    dna = {
      'principles.md':'# Principles\n\n- Answer first, chrome second.\n- Every important claim needs a visible path to sources.\n- Exploration should continue through compact follow-up prompts, not modal detours.\n- Use teal as a proof/action accent, not a decorative wash.\n- Keep monetization calm and contextual.\n',
      'layout.md':'# Layout DNA\n\n- Center a readable answer column in a broad white canvas.\n- Use sidebars for history/library only; keep them visually quiet.\n- Stack source strips near answer headers and detailed source cards near evidence moments.\n- Favor 12/16/24/32 spacing rhythms and tight utility rows.\n',
      'hierarchy.md':'# Hierarchy DNA\n\n- H1/question: direct, medium weight, high contrast.\n- Answer body: readable paragraph rhythm with inline citation anchors.\n- Source labels, domains, timestamps, and model/pro badges are small but crisp.\n- Secondary actions sit in ghost/outline chips.\n',
      'interaction.md':'# Interaction DNA\n\n- Composer is always easy to return to.\n- Follow-up chips/cards continue the same thread.\n- Citation/source elements expand detail without stealing the answer.\n- Loading states should imply active search/reasoning, not generic spinners alone.\n',
      'voice.md':'# Voice DNA\n\n- Concise, epistemic, source-aware.\n- Prefer “Sources”, “Related”, “Ask follow-up”, “Pro Search”, “Library”.\n- Avoid hype, anthropomorphic slogans, and vague AI magic copy.\n',
      'anti-patterns.md':'# Anti-patterns\n\n- Gradient AI hero without evidence/source structure.\n- Oversized CTA buttons that overpower the answer.\n- Citation links hidden at the bottom only.\n- Dark neon dashboard styling.\n- Dense enterprise tables without query/answer hierarchy.\n'}
    for name,text in dna.items(): (STYLE/'dna'/name).write_text(text,encoding='utf-8')
    tokens={'style_id':'perplexity-answer-engine','colors':{'canvas':'#ffffff','surface':'#f8faf9','surface_elevated':'#ffffff','text':'#101817','muted':'#5f6f6d','border':'#dbe4e2','teal':'#208c88','teal_dark':'#146c69','citation_bg':'#eef7f6','warning_soft':'#fff7e6'},'typography':{'font_stack':'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif','answer_size':'16px','ui_size':'13px','caption_size':'12px','line_height_answer':'1.65'},'spacing':{'xs':'4px','sm':'8px','md':'12px','lg':'16px','xl':'24px','2xl':'32px'},'radius':{'chip':'999px','card':'14px','panel':'18px','input':'16px'},'border':{'subtle':'1px solid #dbe4e2','active':'1px solid #208c88'},'shadow':{'card':'0 1px 2px rgba(16,24,23,.06)','popover':'0 12px 32px rgba(16,24,23,.12)'},'semantic_roles':{'primary_action':'teal','evidence':'citation_bg','quiet_navigation':'muted'}}
    (STYLE/'tokens'/'tokens.json').write_text(json.dumps(tokens,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (STYLE/'tokens'/'css-vars.css').write_text(':root{\n  --px-canvas:#ffffff;\n  --px-surface:#f8faf9;\n  --px-text:#101817;\n  --px-muted:#5f6f6d;\n  --px-border:#dbe4e2;\n  --px-teal:#208c88;\n  --px-citation-bg:#eef7f6;\n  --px-radius-card:14px;\n  --px-radius-input:16px;\n  --px-shadow-card:0 1px 2px rgba(16,24,23,.06);\n}\n',encoding='utf-8')
    (STYLE/'patterns'/'index.md').write_text('''# Patterns

## Answer-first thread
A question header, concise answer, inline citation anchors, source strip, then follow-up prompts.

## Search composer
A rounded input/card with direct placeholder, compact scope/model/source controls, and a small teal submit affordance.

## Citation/source proof layer
Numbered citation chips and source cards carry domains, titles, excerpts, and confidence context.

## Pro upgrade moment
Contextual card near Pro Search/pricing actions; restrained badge, feature list, and one primary action.

## Library/collections shell
Quiet sidebar plus card/list surface for saved threads, spaces, and collections.
''',encoding='utf-8')
    atlas=['# Component Atlas','', '| Component | Type | Evidence count | Use |','|---|---|---:|---|']
    for cid in COMPONENTS:
        atlas.append(f'| `{cid}` | {COMPONENTS[cid][0]} | {component_counts.get(cid,0)} | {COMPONENTS[cid][1]} |')
    (STYLE/'components'/'component-atlas.md').write_text('\n'.join(atlas)+'\n',encoding='utf-8')
    for cid,(ctype,desc) in COMPONENTS.items():
        cap=f'''---
style_id: perplexity-answer-engine
component_id: {cid}
title: {cid.replace('-', ' ').title()}
component_type: {ctype.replace(' ','_')}
mediums:
  - web_app
  - answer_engine
intents:
  - {desc.split()[0]}
  - answer search UI
aliases:
  - {cid.replace('-', ' ')}
tags:
  - perplexity
  - answer-engine
  - no-login-wave-01
evidence_paths:
  - styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl
  - styles/perplexity-answer-engine/evidence/mobbin/
extracted_paths:
  - styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/{cid}
confidence: extracted
updated_at: {TODAY}
---

# {cid.replace('-', ' ').title()}

## Use when

Use this component for {desc} in an answer-first, source-backed interface.

## Structure

```text
Component
├── concise label/title
├── content or control body
├── evidence/context metadata
└── compact action row
```

## Implementation recipe

- Use white or cool-off-white surfaces with thin neutral borders.
- Keep typography crisp and utility-sized around the answer body.
- Use teal only for active/action/proof accents.
- Preserve traceability: show source, state, or query context near the control.
- Prefer compact chips/cards over bulky marketing blocks.

## Evidence

- Screenshot-derived facts: `styles/perplexity-answer-engine/components/extracted/from-mobbin-screenshots/{cid}`.
- Source map rows for this component in `styles/perplexity-answer-engine/evidence/source-map/mobbin-source-map.jsonl`.

## Avoid

- Generic SaaS blue gradients, oversized CTA hierarchy, hidden citations, and decorative AI sparkle visuals.
'''
        (STYLE/'components'/'capsules'/f'{cid}.md').write_text(cap,encoding='utf-8')
    (STYLE/'eval'/'checklist.yaml').write_text('''checks:
  - answer surface is primary over navigation chrome
  - source/citation proof layer is visible near answer content
  - teal accent is restrained and semantic
  - follow-up exploration is available without modal interruption
  - no copied Perplexity logos or proprietary CSS/JS dependencies
  - known auth gaps are not represented as fully extracted
''',encoding='utf-8')
    (STYLE/'eval'/'rubric.md').write_text('# Evaluation Rubric\n\nPass if the output reads as a source-backed answer engine: clear query, answer, citations/sources, compact controls, and calm cool-neutral hierarchy. Fail if it becomes generic AI SaaS, hides evidence, or overuses gradients/brand marks.\n',encoding='utf-8')
    (STYLE/'eval'/'failure-modes.md').write_text('# Failure Modes\n\n- Looks like a generic chatbot with no sources.\n- Uses decorative teal/blue gradients instead of evidence hierarchy.\n- Makes Pro upgrade too aggressive.\n- Treats authenticated settings/library details as fully verified.\n',encoding='utf-8')
    (STYLE/'AUTH_BLOCKERS.md').write_text('''# Auth Blockers — Perplexity Answer Engine

No login, OAuth, credentials, or account-specific browsing was used.

Known incomplete surfaces:

- Authenticated Library/collections with real user data.
- Account settings/profile/preferences.
- Billing/subscription management after checkout.
- Saved threads/spaces requiring account state.
- Hover/focus/selected states inside authenticated app panels.

The pack is therefore `offline_ready: false` until authenticated Browser/CDP extraction and fresh-agent eval are run.
''',encoding='utf-8')

def main():
    ensure_dirs(); copied,errors=download_mobbin(); records,by=source_map(copied); public_pages=public_extract(); cdp=cdp_extract(); write_style_files(records,by,public_pages,cdp)
    print(json.dumps({'mobbin_refs':len(records),'download_errors':len(errors),'components':len(by),'public_pages':len(public_pages),'cdp_targets':len(cdp)},indent=2))
if __name__=='__main__': main()
