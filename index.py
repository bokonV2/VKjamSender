from flask import Flask, render_template, request, send_from_directory
import os

from jamSender.index import jamSender


app = Flask(__name__)
app.register_blueprint(jamSender, url_prefix="/jamSender")
app.secret_key = "d23by4wy53qu64uqa"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='favicon.ico')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
