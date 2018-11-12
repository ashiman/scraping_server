# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def translate(sentence, source_lang="hi", target_language="en"):
    url = "https://translate.google.com/m?hl=hi&sl=%s&tl=%s&ie=UTF-8&q=%s" % (source_lang, target_language, sentence)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.select_one(".t0").text

    except:
        return ""


if __name__ == '__main__':
    t9n = translate("मेरा नाम आस्था है.", "hi", "en")
    print(t9n)
