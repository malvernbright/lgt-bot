import emoji
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from config.chatbot import chatbot
from config.questions import questions

from new_questions.models import NewQuestions
from new_questions.forms import QuestionsForm
from config.db_driver import save_known_conversations, save_unknown_conversations, save_polls, polls


@csrf_exempt
def index(request):
    y = {}
    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()

        responded = False

        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()

        bot_response = chatbot.get_response(incoming_msg)
        response_data = bot_response.serialize()
        if incoming_msg.find(str(bot_response)):
            json_data = response_data["text"]
            msg.body(json_data)
            save_known_conversations(response_data)
            responded = True

        # if "poll" or "polls" or "vote" or "votes" in incoming_msg:
        #     for question in questions:
        #         msg.body(question)
        #     # for i, question in enumerate(questions):
        #     #     print(question)
        #     #     answer = incoming_msg
        #     #     msg.body(question)
        #     #     y[question] = answer
        #     #     if i == len(questions) - 1:
        #     #         print("Done")
        #     #         save_polls(y)
        #     #         for x in polls.find():
        #     #             print(f"Poll results: {x}")
        #     responded = True

        if not responded:
            msg.body(
                "Sorry, we will answer that question later.\nKindly send us your contact details so that our team can "
                "help you further. "
                "Thank you.")
            save_unknown_conversations(response_data)

        return HttpResponse(str(resp))
