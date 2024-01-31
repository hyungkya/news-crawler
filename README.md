Naver Open API를 이용해 검색결과 - 링크들 - 을 받아와서 해당 링크들의 기사 원문만 추출해서 문장단위로 파싱해주는 간단한 스크립트입니다.

1) OS나 IDE 환경변수에 Naver API 키값들을 "X-Naver-Client-Id", "X-Naver-Client-Secret" 각각 추가해주시고
2) naver_crawler.py 에 query 부분을 수정하면서 실행하면 sentences.csv로 결과가 나옵니다.
