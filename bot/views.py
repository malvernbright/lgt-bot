import emoji
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from config.chatbot import chatbot


@csrf_exempt
def index(request):

    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()
        
        responded = False
        
        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()
        
        bot_response = chatbot.get_response(incoming_msg)
        if incoming_msg.find(str(bot_response)):
            
            response_data = bot_response.serialize()
            json_data = response_data["text"]
            msg.body(json_data)
            responded = True
        if not responded:
            msg.body("Sorry, I don't understand. Send 'hello' for a list of commands.")

        return HttpResponse(str(resp))
