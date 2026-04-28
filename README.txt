Project_Jisua_2026020118

파일 구성:
- main.py: 실행 파일
- base_crawler.py: 공통 크롤러 클래스
- reddit_crawler.py: Reddit 크롤러
- quora_crawler.py: Quora 크롤러
- reddit_ai_posts.xlsx: Reddit 수집 결과
- quora_ai_answers.xlsx: Quora 수집 결과
- quora_debug.html: Quora 디버그 HTML
- requirements.txt: 실행에 필요한 Python 패키지 목록

실행 방법:
1. 압축을 풉니다.
2. 터미널에서 이 폴더로 이동합니다.
3. 필요한 패키지를 설치합니다.
   pip install -r requirements.txt
4. 실행합니다.
   python main.py

참고:
- Reddit 크롤링 중 사람 인증 화면이 나오면 브라우저에서 인증을 완료한 뒤 터미널에서 Enter를 누르면 됩니다.
- Quora 크롤링은 브라우저에서 직접 로그인한 뒤 Enter를 눌러야 진행됩니다.
- Chrome 브라우저가 설치되어 있어야 합니다.
