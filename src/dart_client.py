import os, requests

BASE = 'https://opendart.fss.or.kr/api'

class DartClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('DART_API_KEY')
        if not self.api_key:
            raise RuntimeError('DART_API_KEY 환경변수가 필요합니다.')

    def get(self, endpoint, **params):
        params = {'crtfc_key': self.api_key, **params}
        r = requests.get(f'{BASE}/{endpoint}.json', params=params, timeout=60)
        r.raise_for_status()
        data = r.json()
        if data.get('status') != '000':
            raise RuntimeError(f"DART API error {data.get('status')}: {data.get('message')}")
        return data
