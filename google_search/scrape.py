import requests
from bs4 import BeautifulSoup

search_item = "astrology taurus today in hindi"
base = "http://www.google.de"
url = "http://www.google.de/search?q=" + search_item
# sc_url = ""

response = requests.get(url)
# print response.content
soup = BeautifulSoup(response.content, "html.parser")
# print (soup.prettify())

# for a in soup.find_all('a', href=True):
#     print "Found the URL:", a['href']



items = soup.select(".r a")

sc_url = items[0].get("href").split("=")[1].split("&")[0]
for item in soup.select(".r a"):
    # sc_url = item.get("href").split("=")[1].split("&")[0]

    print(item.get("href").split("=")[1].split("&")[0])
print("-----> " + sc_url)
response = requests.get(sc_url)


page = response.content
soup = BeautifulSoup(response.content, "html.parser")
items = soup.select(".rashiphal div")
for item in items:
    try:
        print(item.text)
        print("next")
    except:
        continue
# dump = dump_text(page)
# print dump
