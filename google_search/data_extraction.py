from lxml import html


def cleanup_text(text):
    if not text.startswith("<") and not text.startswith(".") and not text.startswith("#") and not text.startswith("img.wp") \
            and not text.startswith(".") and not text.startswith("float") and not text.startswith("int"):
        if "{" in text or ";" in text or "#" in text:
            pass
        else:
            return text
    else:
        return ""


def dump_text(page):
    dump = ""
    dump_list = []
    # page = requests.get(url.encode("utf-8"))
    # print page.text
    root = html.fromstring(page)
    tree = root.getroottree()
    # print "tree --> " + str(tree)
    result = root.xpath('//*')
    # print "result --> " +str(result)
    for r in result:
        try:
            # print(tree.getpath(r))
            xp = tree.getpath(r)
            child = r.getchildren()
            # print xp
            if "/script" not in xp:
                # print root.xpath(xp)[0].element
                text = root.xpath(xp + "//text()")
                if text:
                    clean_text = cleanup_text(text[0].strip())

                    if clean_text is "" or clean_text is None:
                            continue

                    # if len(clean_text.split(" "))<4:
                    #     # print clean_text + "\t" + str(len(clean_text.split(" ")))
                    #     continue
                    if clean_text in dump_list:
                        continue
                    dump_list.append(clean_text)


                    # print xp + "\t" + clean_text
                    # fw.write(xp + "\t" + clean_text + "\n")
        except:
            continue
    dump = "\n".join(dump_list)
    return dump