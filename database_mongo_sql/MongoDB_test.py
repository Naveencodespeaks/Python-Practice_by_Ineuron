import pymongo
client = pymongo.MongoClient("mongodb+srv://Naveen_ineuron:Harekrishna123@cluster.q5kz7vl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sainaven",
    "email_id": "sainaveen005@gmail.com",
    "surname": "Adepu"
}


d = {
    "name": "sainaven",
    "email_id": "sainaveen005@gmail.com",
    "surname": "Adepu"
}

d = {
    "name": "sainaven",
    "email_id": "sainaveen005@gmail.com",
    "surname": "Adepu"
}
d = {
    "name": "sainaven",
    "email_id": "sainaveen005@gmail.com",
    "surname": "Adepu"
}
d = {
    "name": "sainaven",
    "email_id": "sainaveen005@gmail.com",
    "surname": "Adepu"
}
d = {
    "name": "sainaven",
    "email_id": "sainaveen005@gmail.com",
    "surname": "Adepu"
}
d = {
    "name": "sainaven",
    "email_id": "sainaveen005@gmail.com",
    "surname": "Adepu"
}


db1 = client['monotest']
coll = db1['test']
coll.insert_one(d)