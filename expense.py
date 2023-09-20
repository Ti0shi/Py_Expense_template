import csv

from PyInquirer import prompt


def get_names():
    names = []
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            names += row

    return names


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices":get_names()
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    names = get_names()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as file:
        fieldsname = ["amount", "label", "spender"]
        writer = csv.DictWriter(file, fieldsname)
        writer.writerow(infos)
    print("Expense Added !")
    return True


