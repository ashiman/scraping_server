import requests
import requests
from lxml import html
import codecs
import urllib2
from bs4 import BeautifulSoup
import itertools
import codecs

que_ans_dict = {}

f = codecs.open("data/funtrivia_data.txt", "a", "utf-8")
base_url = "http://www.funtrivia.com/en/Religion/Mahabharata-16805_%s.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response = requests.get("http://www.funtrivia.com/en/Religion/Mahabharata-16805.html", headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
# print(soup)
mydivs_que = soup.findAll("span", {"itemprop": "name"})
mydivs_ans = soup.findAll("b", {"itemprop": "text"})
mydivs_desc = soup.findAll("div", {"itemprop": "text"})

for i,j,k in itertools.izip(mydivs_que,mydivs_ans,mydivs_desc):
    print(i.text, j.text, k.text)
    f.write(i.text.strip() + "\t" + j.text.strip() + "\t" + k.text.strip() + "\n")

for p in range(2,14):
    url = base_url.replace("%s", str(p))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    response = requests.get(url, headers=headers)
    # print(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup)
    mydivs_que = soup.findAll("span", {"itemprop": "name"})
    mydivs_ans = soup.findAll("b", {"itemprop": "text"})
    mydivs_desc = soup.findAll("div", {"itemprop": "text"})
    for i, j, k in itertools.izip(mydivs_que, mydivs_ans, mydivs_desc):
        print(i.text, j.text, k.text)
        f.write(i.text.strip() + "\t" + j.text.strip() + "\t" + k.text.strip() + "\n")




# for div in mydivs:
#     print(div.text.strip())

# t = soup.find_all(itemprop="name").get_text()
# print t
