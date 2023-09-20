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
    involved_questions = {
            "type":"checkbox",
            "name":"involved",
            "message":"Select involved names",
            "choices":[{'name': i, 'checked': True if i == infos['spender'] else False, 'disabled': True if i == infos['spender'] else False} for i in get_names()],
        }

    involved = prompt(involved_questions)
    involved['involved'] += [infos['spender']]
    amount = -(float)(infos['amount']) / len(involved['involved'])

    with open('expense_report.csv', 'a', newline='') as file:
        fieldsname = ["amount", "label", "spender"]
        writer = csv.writer(file)
        for i in involved['involved']:
            writer.writerow([amount if i != infos['spender'] else infos['amount'], infos['label'], i])

    print("Expense Added !")

    return True


