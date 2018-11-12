import requests
import requests
from lxml import html
import codecs
import urllib2
from bs4 import BeautifulSoup
import itertools
import codecs
import re

que_ans_dict = {}


f = codecs.open("data/everythingforcity_data.txt", "a", "utf-8")
base_url = "http://www.everythingforcity.com/quiz/epics-quiz/mahabharata-quiz-%s.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response = requests.get("http://www.everythingforcity.com/quiz/epics-quiz/mahabharata-quiz.html", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

mydivs_que = soup.findAll("h4", {"class": "bold-blue"})

mydivs_ans = soup.findAll("a", onclick = re.compile(r'/*Y/*'))


for i, j in itertools.izip(mydivs_que,mydivs_ans):
    print(i.text.split("\n")[0].strip() + "\t" + j.text.strip() + "\n")
    f.write(i.text.split("\n")[0].strip() + "\t" + j.text.strip() + "\n")


for p in range(2,4):
    url = base_url.replace("%s", str(p))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    response = requests.get(url, headers=headers)
    # print(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    mydivs_que = soup.findAll("h4", {"class": "bold-blue"})
    mydivs_ans = soup.findAll("a", onclick=re.compile(r'/*Y/*'))
    for i, j in itertools.izip(mydivs_que, mydivs_ans):
        print(i.text.split("\n")[0].strip() + "\t" + j.text.strip() + "\n")
        f.write(i.text.split("\n")[0].strip() + "\t" + j.text.strip() + "\n")