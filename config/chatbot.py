from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot(
    "Ewige ChatBot",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'empty',
            'output_text': ''
            },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'i honestly have no idea how to respond to that',
            'maximum_similarity_threshold': 0.9
            },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
            }
        ],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri='sqlite:///botdata.sqlite3')


trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./config/conversations.yml")