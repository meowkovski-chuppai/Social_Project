# Social Media Analytics Project

AI 활용 패턴 분석을 위해 Reddit과 Quora의 텍스트 데이터를 수집하는 Python 크롤링 프로젝트입니다.

## Files

- `main.py`: 실행 진입점
- `base_crawler.py`: 공통 크롤러 클래스
- `reddit_crawler.py`: Reddit 크롤러
- `quora_crawler.py`: Quora 크롤러
- `reddit_ai_posts.xlsx`: Reddit 수집 결과
- `quora_ai_answers.xlsx`: Quora 수집 결과
- `quora_debug.html`: Quora 디버그 HTML
- `presentation.html`: 발표 자료 HTML
- `requirements.txt`: 실행에 필요한 패키지 목록

## Run

```bash
pip install -r requirements.txt
python main.py
```

## Notes

- Reddit 크롤링 중 사람 인증 화면이 나오면 브라우저에서 인증을 완료한 뒤 터미널에서 Enter를 누르면 됩니다.
- Quora 크롤링은 브라우저에서 직접 로그인한 뒤 Enter를 눌러야 진행됩니다.
- Chrome 브라우저가 설치되어 있어야 합니다.
