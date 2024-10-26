def add(expence_list, balance):
    in_str = input("Add some expense or income records with description and amount:")
    in_list = [(i.split()[0], int(i.split()[1])) for i in in_str.split(', ')]
    expence_list += in_list
    balance += sum([i[1] for i in in_list])
    return balance
    
def delete(expence_list, balance):
    in_str = input("Please enter the description of the record you want to delete:")
    candidata = []
    for x in expence_list:
        if(x[0] == in_str):
            candidata.append(x)
    if len(candidata) == 0:
        print("No such record found.")
    elif(len(candidata) == 1):
        expence_list.remove(candidata[0])
        balance -= candidata[0][1]
    else:
        amt_str = input("There are multiple records with the same description. Please enter the amount of the record you want to delete:")
        amt = int(amt_str)
        for x in candidata:
            if(x[1] == amt):
                expence_list.remove(x)
                balance -= amt
                break
        else:
            print("No such record found.")
    return balance
balance = int(input("how much money do you have? "))
command = input("What do you want to do? (add / view / delete / exit)?")
legal_commands = ['add', 'view', 'delete', 'exit']
expence_list = []
while True:
    if command == 'add':
        balance = add(expence_list, balance)
    elif command == 'view':
        print("Description          Amount")
        print("==================== ======")
        for desc, amount in expence_list:
            print(f"{desc:<20} {amount:>5}")
        print("==================== ======")
        print("Now you have {} dollars.".format(balance))
    elif command == 'delete':
        balance=delete(expence_list, balance)
    elif command == 'exit':
        break
    else:
        print("Invalid command.")
    command = input("What do you want to do? (add / view / delete / exit)?")