import csv

from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    with open('users.csv', 'a') as file:
        file.write(infos['name'])
    print("User Added !")

    return True
