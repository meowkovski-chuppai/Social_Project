from base_crawler import BaseCrawler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint


class QuoraCrawler(BaseCrawler):

    def __init__(self, queries=None):
        super().__init__()
        if queries is None:
            self.queries = ['AI usage daily work', 'how to use ChatGPT effectively', 'AI productivity tools']
        else:
            self.queries = queries

    def crawl(self):
        """Quora 크롤링: 로그인 → 각 검색어로 검색 → 텍스트 수집"""
        self.start()

        # 수동 로그인
        self.open('https://www.quora.com/')
        print('[Quora] 브라우저에서 직접 로그인 해주세요')
        input('[Quora] 로그인 완료 후 엔터를 누르세요...')

        for query in self.queries:
            print(f'\n=== "{query}" 검색 크롤링 시작 ===')
            try:
                self.crawl_search(query)
            except Exception as e:
                print(f'[Quora] "{query}" 에러: {e}')
                continue

        self.to_excel('quora_ai_answers.xlsx')
        self.close()

    def crawl_search(self, query):
        """검색 결과 페이지에서 질문 제목 + 답변 텍스트 수집"""
        search_url = f'https://www.quora.com/search?q={query.replace(" ", "+")}&type=answer'
        self.driver.get(search_url)
        sleep(5)
        print(f'페이지 열림: {search_url}')
        self.scroll_down(10)
        sleep(2)
        self.parse()

        full_text = self.doc.get_text(separator='\n')
        lines = full_text.split('\n')
        clean_lines = [l.strip() for l in lines if l.strip()]

        # 질문 찾기 (? 로 끝나는 줄)
        questions = []
        for l in clean_lines:
            if l.endswith('?') and len(l) > 20:
                questions.append(l)

        # 긴 텍스트 = 답변
        answers = []
        skip_words = ['Skip to', 'Continue with', 'Terms of Service',
                       'Quora+', 'Add question', 'All types']
        for l in clean_lines:
            if len(l) > 100:
                if not any(s in l for s in skip_words):
                    answers.append(l)

        print(f'[Quora] 질문 {len(questions)}개, 답변 텍스트 {len(answers)}개')

        # 질문 목록 저장
        for q in questions:
            self.data.append({
                'source': 'Quora',
                'search_query': query,
                'type': 'question',
                'text': q,
            })

        # 답변 텍스트 저장
        for a in answers:
            self.data.append({
                'source': 'Quora',
                'search_query': query,
                'type': 'answer',
                'text': a[:2000],
            })

        print(f'[Quora] 총 {len(self.data)}개 데이터 누적')


if __name__ == '__main__':
    crawler = QuoraCrawler([
        'AI usage daily work',
        'how to use ChatGPT effectively',
        'AI productivity tools',
        'how people use AI',
        'AI in business'
    ])
    crawler.crawl()
