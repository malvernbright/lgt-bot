from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


chatbot = ChatBot(
    "Ask Devolution",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'empty',
            'output_text': ''
            },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, we will answer that question later.\nKindly send us your contact details so that our team can help you further. '
                     'Thank you.',
            'maximum_similarity_threshold': 0.9
            },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
            }
        ],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri='sqlite:///botdata.sqlite3')


trainer = ChatterBotCorpusTrainer(chatbot)
# trainer = ListTrainer(chatbot)
trainer.train("./config/conversations.yml")

# trainer.train([
#     'Hi',
#     'Hello, my name is *Ask Devolution*. Please let me know how I can help you.',
#     'I need your assistance regarding my order',
#     'Please, Provide me with your order id',
#     'I have a complaint.',
#     'Please elaborate, your concern',
#     'How long it will take to receive an order ?',
#     'An order takes 3-5 Business days to get delivered.',
#     'Okay Thanks',
#     'No Problem! Have a Good Day!'
#     ])

