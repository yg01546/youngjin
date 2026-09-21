import os, json, pathlib
from dart_client import DartClient
from corp_code import find_sk_hynix

YEARS=range(2021,2026)
out=pathlib.Path('data/raw'); out.mkdir(parents=True,exist_ok=True)
key=os.environ['DART_API_KEY']; client=DartClient(key); corp=find_sk_hynix(key)
pathlib.Path('data/corp_code.json').write_text(json.dumps({'corp_code':corp,'stock_code':'000660','corp_name':'SK하이닉스'},ensure_ascii=False,indent=2),encoding='utf-8')
for year in YEARS:
    data=client.get('fnlttSinglAcntAll',corp_code=corp,bsns_year=str(year),reprt_code='11011',fs_div='CFS')
    (out/f'financials_{year}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print('수집 완료',corp)
