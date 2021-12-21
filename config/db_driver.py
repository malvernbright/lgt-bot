from pymongo import MongoClient

# Create a mongo client

# client = MongoClient("mongodb://localhost:27017")
client = MongoClient("mongodb+srv://lazycoder:9cZdyy1WULAxT2cs@cluster0.zhcie.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Create a db
db = client["bot_conversations"]

# Create a collection

known_col = db["conversations"]
unknown_col = db["unknown_col"]

polls = db["polls"]

print(db.list_collection_names())

# for x in known_col.find():
#     print(x)


def save_polls(poll: dict):
    bot_polls = polls.insert_one(poll)
    return bot_polls


def save_known_conversations(conversation: dict):
    bot_conversation = known_col.insert_one(conversation)
    return bot_conversation


def save_unknown_conversations(conversation: dict):
    bot_conversation = unknown_col.insert_one(conversation)
    return bot_conversation
