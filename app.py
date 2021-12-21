from chatterbot.chatterbot import ChatBot
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import yaml

app = Flask(__name__)


@app.route("/bot/", methods=['POST', 'GET'])
def home():
    """
    The first thing we need to do in our chatbot is obtain the message 
    entered by the user. This message comes in the payload of the POST request 
    with a key of ’Body’. We can access it through Flask’s request object
    """
    incoming_msg = request.values.get('Body', '').lower()

    resp = MessagingResponse()
    msg = resp.message()

    user_text = request.args.get('msg')
    if incoming_msg.find(str(user_text)):
        bot_response = ChatBot.get_response(incoming_msg)
        msg.body(yaml.dump(bot_response, default_flow_style=False, explicit_start="text"))
        responded = True
    if not responded:
        msg.body('I didn\'t get you, please try again.')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
