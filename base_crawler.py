from seleniumbase import Driver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
import pandas as pd


class BaseCrawler:

    def __init__(self):
        self.driver = None
        self.doc = None
        self.data = []

    def start(self):
        self.driver = Driver(browser='Chrome', uc=True)
        print('브라우저 시작됨')

    def open(self, url):
        self.driver.get(url)
        sleep(5)
        print(f'페이지 열림: {url}')

    def parse(self):
        self.doc = BeautifulSoup(self.driver.page_source, 'html.parser')
        return self.doc

    def scroll_down(self, times=10):
        for n in range(times):
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            sleep(0.5)
        sleep(2)
        print(f'{times}번 스크롤 완료')

    def to_excel(self, filename):
        df = pd.DataFrame(self.data)
        df.to_excel(filename, index=False)
        print(f'엑셀 저장 완료: {filename} ({len(self.data)}행)')
        return df

    def close(self):
        if self.driver:
            self.driver.quit()
            print('브라우저 종료됨')
