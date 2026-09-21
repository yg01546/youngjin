# SK하이닉스 DART 재무분석

OpenDART API로 SK하이닉스(000660)의 최근 5개 완료 사업연도 연결재무제표를 수집하고 재무비율을 계산해 GitHub Pages 대시보드로 제공합니다.

## 설정
Repository Settings → Secrets and variables → Actions → New repository secret에서 `DART_API_KEY`에 OpenDART 40자리 인증키를 등록하세요.

## 데이터 흐름
OpenDART → Python ETL → JSON/CSV → GitHub Actions → GitHub Pages
