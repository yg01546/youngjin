import io, zipfile, xml.etree.ElementTree as ET
import requests
from dart_client import BASE

def find_sk_hynix(api_key):
    r = requests.get(f'{BASE}/corpCode.xml', params={'crtfc_key': api_key}, timeout=60)
    r.raise_for_status()
    z = zipfile.ZipFile(io.BytesIO(r.content))
    root = ET.fromstring(z.read('CORPCODE.xml'))
    for item in root.findall('list'):
        name=(item.findtext('corp_name') or '').strip()
        stock=(item.findtext('stock_code') or '').strip()
        if name == 'SK하이닉스' or stock == '000660':
            return (item.findtext('corp_code') or '').strip()
    raise RuntimeError('SK하이닉스 corp_code를 찾지 못했습니다.')
