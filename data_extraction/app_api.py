import requests
from bs4 import BeautifulSoup
from data_extraction.astrology.mappings import astrology
from data_extraction.astrology.db_connection import connect
import json
from flask import Flask, request, jsonify
from data_extraction.helpers.google_translate import translate
from data_extraction.generic.scrape import query_response
flask_app = Flask(__name__)

'''Astrology Predictions'''


@flask_app.route('/dump_predictions', methods=['POST'])
def dump_predictions():

    try:
        input_json = json.loads(request.data)
        category = input_json["category"].strip()  # eg. horoscope
        date = input_json["date"].strip()
        # contact = input_json["contact"]

    except KeyError as e:
        except_msg = "Missing key : " + e.message
        resp_dict = {
            "status":
                {
                    "code": 101,
                    "message": except_msg
                }
        }
        return jsonify(resp_dict)

    try:

        collection = connect("astrology", category, True)
        base_url = astrology[category]["url"]
        for signs in astrology[category]["zodiac_signs"]:
            url = base_url.replace("%s", signs.strip())
            # print url
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            items = soup.select(".rashiphal div")
            prediction = items[0].text.strip().split("\n")[0]
            # print(items[0].text.strip().split("\n")[0])

            dict = {"zodiac_sign": signs, "prediction": prediction, "date": date}
            x = collection.insert_one(dict)
        response = {"status": 1,
                    "message": "data dumped successfully"}
        return jsonify(response)

    except Exception, e :

        print str(e)
        response = {"status": "0", "message": "Processing error"}
        return jsonify(response)


'''Astrology Predictions'''


@flask_app.route('/get_predictions', methods=['POST'])
def get_predictions():
    try:
        input_json = json.loads(request.data)

        zodiac_sign = input_json["zodiac_sign"].strip() # eg. Taurus
        category = input_json["category"].strip()  # eg. horoscope
        date = input_json["date"].strip()
        # contact = input_json["contact"]

    except KeyError as e:
        except_msg = "Missing key : " + e.message
        resp_dict = {
            "status":
                {
                    "code": 101,
                    "message": except_msg
                }
        }
        return jsonify(resp_dict)
    try:
        collection = connect("astrology", category)
        doc = collection.find_one({"zodiac_sign":zodiac_sign})
        prediction = doc["prediction"]
        sign = doc["zodiac_sign"]
        date_s = doc["date"]
        response = {"status" : "successfull",
                    "zodiac_sign" : zodiac_sign,
                    "prediction": prediction
                    }
        return jsonify(response)

    except Exception, e :

        print str(e)
        response = {"status": "0", "message": "Processing error"}
        return jsonify(response)


'''Translation from Googlee'''


@flask_app.route('/get_translation', methods=['POST'])
def get_translation():
    try:
        input_json = json.loads(request.data)

        source_lang = input_json["source_lang"].strip() # eg. Taurus
        target_lang = input_json["target_lang"].strip()  # eg. horoscope
        sentence = input_json["sentence"].strip()
        # contact = input_json["contact"]

    except KeyError as e:
        except_msg = "Missing key : " + e.message
        resp_dict = {
            "status":
                {
                    "code": 101,
                    "message": except_msg
                }
        }
        return jsonify(resp_dict)

    try:
        t9n = translate(sentence, source_lang, target_lang)
        resp_dict = {"translation": t9n,
                     "source_lang": source_lang,
                     "target_lang": target_lang,
                     "sentence": sentence,
                     "status": "successfull"}
        return jsonify(resp_dict)

    except Exception, e:

        print str(e)
        response = {"status": "0", "message": "Processing error"}
        return jsonify(response)


'''Generic Responses from Google Search'''


@flask_app.route('/get_generic_answers', methods=['POST'])
def get_generic_answers():
    try:
        input_json = json.loads(request.data)

        source_lang = input_json["source_lang"].strip()
        target_lang = input_json["target_lang"].strip()
        query = input_json["query"].strip()
        # contact = input_json["contact"]

    except KeyError as e:
        except_msg = "Missing key : " + e.message
        resp_dict = {
            "status":
                {
                    "code": 101,
                    "message": except_msg
                }
        }
        return jsonify(resp_dict)

    try:
        url, answer = query_response(query, source_lang, target_lang)
        src_answer = translate(answer, target_lang, source_lang)
        resp_dict = {"answer": answer,
                     "answer_" + str(source_lang): src_answer,
                     "suggested_url": url,
                     "source_lang": source_lang,
                     "target_lang": target_lang,
                     "sentence": query,
                     "status": "successful"}
        return jsonify(resp_dict)

    except Exception, e:

        print str(e)
        response = {"status": "0", "message": "Processing error"}
        return jsonify(response)






