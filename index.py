from flask import Flask, render_template, request

from jamSender.index import jamSender


app = Flask(__name__)
app.register_blueprint(jamSender, url_prefix="/jamSender")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
