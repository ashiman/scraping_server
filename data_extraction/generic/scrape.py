# coding=utf-8
import requests
from bs4 import BeautifulSoup
from data_extraction.helpers.google_translate import translate


def query_response(query, src_lang, targ_lang):
    flag = 0
    answer = None
    suggested_urls = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    search_item = translate(query, src_lang, targ_lang).strip()
    google_url = "http://www.google.de/search?q=" + search_item

    response = requests.get(google_url)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.select(".r a")

    sc_url = items[0].get("href").split("=")[1].split("&")[0]

    for item in items:
        suggested_urls.append(item.get("href").split("=")[1].split("&")[0])
    print("-----> " + sc_url)

    while True:

        for suggested_url in suggested_urls:
            response = requests.get(suggested_url, headers=headers)
            page = response.content
            soup = BeautifulSoup(page, "html.parser")
            paragraphs = soup.find_all(["p", "br"])
            print paragraphs[0].text
            for para in paragraphs:
                text = para.text.strip()
                if len(text.split()) > 25:
                    print text
                    answer = text
                    sc_url = suggested_url
                    flag = 1
                    break


            if flag == 1:
                break
        if flag == 1:
            break
    return sc_url, answer


if __name__ == '__main__':
    query_response(u"कर्नाटका के मुख्य मंत्री कौन है ?", "hi", "en")

