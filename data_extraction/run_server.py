from data_extraction.app_api import flask_app
if __name__ == '__main__':
    flask_app.run(port=9002, host="0.0.0.0")