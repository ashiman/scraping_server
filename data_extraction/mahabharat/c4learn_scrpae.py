import requests
import requests
from lxml import html
import codecs
import urllib2
from bs4 import BeautifulSoup
import itertools
import codecs

que_ans_dict = {}
super_super_parent = None
two_ans = ""
an = []
f = codecs.open("data/c4learn_data.txt", "a", "utf-8")
base_url = "http://www.c4learn.com/civilservices/history-mcq/mahabharata-multiple-choice-questions-set-1/%s/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response = requests.get("http://www.c4learn.com/civilservices/history-mcq/mahabharata-multiple-choice-questions-set-1/", headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
# print(soup)
mydivs_que = soup.findAll("div", {"class": "mtq_question_text"})
mydivs_ans = soup.findAll("div", {"alt": "Correct"})
for ans in mydivs_ans:

    parent = ans.find_parent()
    super_parent = parent.find_parent()
    if super_super_parent == super_parent.find_parent():
        sib = parent.find_next_sibling()

        an[-1] = an[-1] + " " + sib.text.strip()

        print(sib.text)

    else:
        super_super_parent= super_parent.find_parent()
        sib = parent.find_next_sibling()
        an.append(sib.text.strip())

print(an)
# mydivs_desc = soup.findAll("div", {"itemprop": "text"})
#
for i, j in itertools.izip(mydivs_que, an):
    print(i.text, j,)
    f.write(i.text.strip() + "\t" + j.strip() + "\n")


for p in range(2,9):
    super_super_parent = None
    an = []
    url = base_url.replace("%s", str(p))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    response = requests.get(url, headers=headers)
    # print(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup)
    mydivs_que = soup.findAll("div", {"class": "mtq_question_text"})
    mydivs_ans = soup.findAll("div", {"alt": "Correct"})
    for ans in mydivs_ans:

        parent = ans.find_parent()
        super_parent = parent.find_parent()
        if super_super_parent == super_parent.find_parent():
            sib = parent.find_next_sibling()

            an[-1] = an[-1] + " " + sib.text.strip()

            print(sib.text)

        else:
            super_super_parent = super_parent.find_parent()
            sib = parent.find_next_sibling()
            an.append(sib.text.strip())

    for i, j in itertools.izip(mydivs_que, an):
        print(i.text, j,)
        f.write(i.text.strip() + "\t" + j.strip() + "\n")