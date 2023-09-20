import csv

from PyInquirer import prompt

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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as file:
        fieldsname = ["amount", "label", "spender"]
        writer = csv.DictWriter(file, fieldsname)
        writer.writerow(infos)
    print("Expense Added !")
    return True


