# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import codecs
import itertools
from bs4 import BeautifulSoup
from lxml import html
f = codecs.open("data/bharatdiscovery_data.txt", "a", "utf-8")

option = webdriver.ChromeOptions()
option.add_argument("— incognito")

base_url = u"http://bharatdiscovery.org/india/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4" \
           u"%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A5%8D%E0%A4%AF_%E0%A4%9C%E0%A5%8D%E0%A4%9E%E0%A4%BE%E0%A4%A8_" \
           u"%s "

for p in range(2,60):
    browser = webdriver.Chrome(executable_path="/Users/reverie-pc/Downloads/chromedriver", chrome_options=option)
    url = base_url.replace("%s", str(p))

    browser.get(url)
    item = browser.find_element_by_xpath("//*[@id='quiz0']/p/input")
    item.click()

    soup = BeautifulSoup(browser.page_source, "lxml")
    correct = soup.find_all("input", {"title": "ग़लत"})
    ques = soup.find_all("div", {"class": "header"})

    for i, j in itertools.izip(ques, correct):
        f.write(i.text.strip() + "\t" + j.next_element.text.strip() + "\n")
    browser.quit()
