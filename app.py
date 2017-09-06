from flask import Flask
from flask import request, jsonify
from flask import render_template
from claudinha_text.ascii_text import play
from time import strftime
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/message', methods=['GET'])
def default_message():
    input_text = strftime('Hora: %H:%M:%S')
    play(input_text)
    return jsonify(
        {
            "msg": input_text
        }
    )


@app.route('/message/<string:input_text>/', methods=['POST'])
def input_message(input_text):
    
    play(input_text, request.args.get('color', 'white'))

    return jsonify(
        {
            "msg": input_text
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
