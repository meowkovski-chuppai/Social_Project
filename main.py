from reddit_crawler import RedditCrawler
from quora_crawler import QuoraCrawler


def crawl_reddit():
    """Reddit 크롤링 - AI 관련 서브레딧에서 포스트 수집"""
    subreddits = ['ChatGPT', 'PromptEngineering', 'artificial', 'ClaudeAI']
    crawler = RedditCrawler(subreddits)
    crawler.crawl()


def crawl_quora():
    """Quora 크롤링 - AI 활용 관련 질문 + 답변 수집"""
    queries = [
        'AI usage daily work',
        'how to use ChatGPT effectively',
        'AI productivity tools',
        'how people use AI',
        'AI in business'
    ]
    crawler = QuoraCrawler(queries)
    crawler.crawl()


if __name__ == '__main__':
    print('=' * 50)
    print('AI 활용 관련 소셜미디어 크롤링')
    print('=' * 50)
    print('1. Reddit 크롤링')
    print('2. Quora 크롤링')
    print('3. 전부 실행')
    print('=' * 50)

    choice = input('선택 (1/2/3): ')

    if choice == '1':
        crawl_reddit()
    elif choice == '2':
        crawl_quora()
    elif choice == '3':
        crawl_reddit()
        crawl_quora()
    else:
        print('1~3 중에 선택해주세요')
