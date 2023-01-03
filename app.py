import os

from flask import Flask, request, jsonify

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

chatbot = ChatBot('Training Example')
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Greetings!",
    "Hello",
])

trainer.train([
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
])

trainer.train([
    "How to get to the event",
    "You can get to the event by taking the bus. You can find timetables on star.fr",
])

restaurantResponse = "You can find a lot of restaurants in the city center. If you want to eat something more traditional, you can go to the crêperie 'Crêperie La Gavotte' located at 41 Rue Saint-Georges."
restaurantQuestions = [
    "Where can I eat?",
    "Where can I find a restaurant?",
    "Where can I find a good restaurant?",
    "Where can I find a good place to eat?",
    "Where's a good place to eat around here?",
    "I'm looking for a restaurant, any recommendations?",
    "I'm starving, where can I find some food?",
    "Where can I get a meal in this area?",
    "I need to find a spot for dinner, any ideas?",
    ]

for question in restaurantQuestions:
    trainer.train([
        question,
        restaurantResponse
    ])


trainer.train([
    "How to get to the city center",
    "You can get to the city center by taking the bus or the subway. The main bus station is République.",
])

trainer.train([
    "Where to sleep",
    "You can find a lot of hotels in the city center. I recommend you the hotel 'Balthazar Hôtel & Spa' located at 19 "
    "Rue Maréchal Joffre.",
])

trainer.train([
    "How to get to the airport",
    "You can get to the airport by taking the C6 bus. You can find timetables on star.fr",
])

trainer.train([
    "How to get to the train station",
    "You can get to the train station by taking the C1, C2 11 buses or the two lines of the subway. You can find "
    "timetables on star.fr",
])

trainer.train([
    "How much is a bus ticket",
    "A bus ticket costs 1.50€. You can buy it on the bus or at the ticket machine.",
    "Where can I buy a ticket",
    "You can buy a ticket on the bus or at the ticket machine.",
    "Where is the ticket machine",
    "You can find the ticket machine at every subway station.",
])

trainer.train([
    "How much is a subway ticket",
    "A subway ticket costs 1.50€. You can buy it on the bus or at the ticket machine.",
])


@app.route("/", methods=["POST"])
def hello_world():
    content = request.json
    bot_response = chatbot.get_response(content["message"])
    return jsonify({"message": str(bot_response)})

if __name__ == "__main__":
    app.run(debug=True)
