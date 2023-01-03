import os

from flask import Flask, request, jsonify

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

chatbot = ChatBot('Training Example')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english", )


@app.route("/", methods=["POST"])
def hello_world():
    content = request.json
    bot_response = chatbot.get_response(content["message"])
    return jsonify({"message": str(bot_response)})

if __name__ == "__main__":
    app.run(debug=True)
