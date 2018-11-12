# coding=utf-8
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import codecs
import itertools
import requests
from bs4 import BeautifulSoup

'''Collection of links and questions'''
from lxml import html
from selenium.webdriver.common.keys import Keys
# f = codecs.open("data/quora_ques.txt", "a", "utf-8")
# f2 = codecs.open("data/quora_links.txt", "a", "utf-8")
# url = "https://www.quora.com/topic/Mahabharata-Hindu-epic/all_questions"
#
# option = webdriver.ChromeOptions()
# option.add_argument("— incognito")
#
# driver = webdriver.Chrome(executable_path="/Users/reverie-pc/Downloads/chromedriver", chrome_options=option)
# driver.get(url)
# SCROLL_PAUSE_TIME = 4.0
# # driver.execute_script("window.scrollTo(0, Y)")
#
# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# #
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         # break
#         # Scroll down to bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         # Wait to load page
#         time.sleep(SCROLL_PAUSE_TIME)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             # Scroll down to bottom
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             # Wait to load page
#             time.sleep(SCROLL_PAUSE_TIME)
#             new_height = driver.execute_script("return document.body.scrollHeight")
#             if new_height == last_height:
#                 break
#     last_height = new_height
#
# soup = BeautifulSoup(driver.page_source, "lxml")
# ques = soup.find_all("span", {"class": "ui_story_title ui_story_title_medium "})
#
# links = soup.find_all("a", {"class": "question_link"})
#
# for q in ques:
#     # print q.text.strip()
#     f.write(q.text.strip() + "\n")
#
# for l in links:
#     print l['href']
#     # print(l.text.strip())
#     f2.write(l["href"].strip() + "\n")

'''Fetching data from links'''

f = codecs.open("data/quora_links.txt", "r", "utf-8")
f2 = codecs.open("data/quora_que_ans.txt", "a", "utf-8")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response = requests.get("https://www.quora.com/Which-yuga-does-Ramayan-belong-to", headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
# print(soup)
lines = f.readlines()
# q = soup.findAll("span", {"class": "rendered_qtext"})
# for j in q:
#     print j.text

for line in lines:
    if "unanswered" not in line.strip():
        url = "https://www.quora.com" + line.strip()
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        mydivs_ans = soup.findAll("div", {"class": "ui_qtext_expanded"})

        f2.write(line.strip().split("/")[1].replace("-", " ") + "\t")
        for a in mydivs_ans:
            # print a.text.strip()
            f2.write(a.text.strip() + "\t")
        f2.write("\n")
