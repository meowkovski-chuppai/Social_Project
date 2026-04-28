from base_crawler import BaseCrawler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import re


class RedditCrawler(BaseCrawler):

    def __init__(self, subreddits=None):
        super().__init__()
        if subreddits is None:
            self.subreddits = ['ChatGPT', 'PromptEngineering', 'artificial', 'ClaudeAI']
        else:
            self.subreddits = subreddits

    def crawl(self):
        """전체 크롤링 실행"""
        self.start()

        for sub in self.subreddits:
            print(f'\n=== r/{sub} 크롤링 시작 ===')
            self.crawl_subreddit(sub)

        self.to_excel('reddit_ai_posts.xlsx')
        self.close()

    def crawl_subreddit(self, subreddit):
        """서브레딧 하나 크롤링 - 텍스트 기반 파싱"""
        url = f'https://www.reddit.com/r/{subreddit}/'
        self.open(url)
        self.wait_for_human_verification()
        self.scroll_down(10)
        self.parse()

        # 포스트 찾기
        posts = self.doc.find_all('article')
        print(f'[r/{subreddit}] 포스트 수: {len(posts)}')

        count = 0
        for p in posts:
            try:
                text = p.text.strip()
                if len(text) < 10:
                    continue

                lines = text.split('\n')
                lines = [l.strip() for l in lines if l.strip()]

                # 제목: 가장 긴 줄이 보통 제목
                title = ''
                author = ''
                for l in lines:
                    if l.startswith('u/'):
                        author = l.split('•')[0].strip()
                    elif len(l) > 20 and not l.startswith('u/') and 'ago' not in l:
                        if len(l) > len(title):
                            title = l

                if not title:
                    continue

                # 링크 추출
                link = ''
                a_tags = p.find_all('a', href=True)
                for a in a_tags:
                    href = a.get('href', '')
                    if '/comments/' in href:
                        if href.startswith('/'):
                            link = 'https://www.reddit.com' + href
                        else:
                            link = href
                        break

                # 댓글 수, 업보트 - 텍스트에서 추출
                upvotes = ''
                comments = ''
                for l in lines:
                    if 'comment' in l.lower():
                        comments = l.strip()
                    if re.match(r'^\d+\.?\d*[kK]?$', l.strip()):
                        upvotes = l.strip()

                self.data.append({
                    'source': f'r/{subreddit}',
                    'title': title,
                    'author': author,
                    'upvotes': upvotes,
                    'comments': comments,
                    'link': link
                })
                count += 1

            except:
                pass

        print(f'[r/{subreddit}] {count}개 데이터 수집 완료')

    def wait_for_human_verification(self):
        """Reddit 사람 인증 화면이 나오면 사용자가 직접 인증하도록 대기"""
        title = self.driver.title.lower()
        page_text = self.driver.page_source.lower()

        if 'prove your humanity' in title or 'prove your humanity' in page_text:
            print('[Reddit] 사람 인증 화면이 감지되었습니다.')
            print('[Reddit] 브라우저에서 인증을 완료한 뒤 Enter를 눌러주세요.')
            input('[Reddit] 인증 완료 후 Enter: ')
            sleep(3)


if __name__ == '__main__':
    crawler = RedditCrawler(['ChatGPT', 'PromptEngineering'])
    crawler.crawl()
