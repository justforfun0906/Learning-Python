import os
def is_valid_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def handle_balance_input():
    str = input("How much money do you have? ")
    try:
        assert is_valid_integer(str), 'balance is not a number'
    except AssertionError as e:
        print(e, ', set balance to 0 by default')
        return 0
    return int(str)

def init():
    global balance
    global expence_list
    expence_list = []
    #read the balance and expence_list from a file
    try:
        with open('/home/justforfun/Learning-Python/weekly_checkpoint/record.txt', 'r') as fh:
            file_li = fh.readlines()
            balance_str = file_li[0].strip()
            #make sure balance is a number
            assert is_valid_integer(balance_str), 'balance is not a number'
            balance = int(balance_str)
            for line in file_li[1:]:
                desc, amount = line.split()
                desc = desc.strip()
                amount = amount.strip()
                #make sure amount is a number
                assert is_valid_integer(amount), 'amount is not a number'
                expence_list.append((desc, int(amount)))
    except FileNotFoundError:
        print("record.txt file not found.")
        balance = int(input("How much money do you have? "))
    except AssertionError as e:
        #invalid format of the record file
        print(e, ':invalid record, deleting the content of the file')
        with open('/home/justforfun/Learning-Python/weekly_checkpoint/record.txt', 'w') as fh:
            pass
        balance = handle_balance_input()
        
    except Exception as e:
        #can't read the file
        balance = handle_balance_input()
        
def add(expence_list, balance):
    in_str = input("Add some expense or income records with description and amount (format: 'item amount'): ")
    in_list = in_str.split(', ')
    for item in in_list:
        try:
            desc = item.split()[0]
            amount = item.split()[1]
            amount = int(amount)
            expence_list.append((desc, amount))
            balance += amount
        except IndexError:
            #item can't be split into two parts
            print(f"Invalid format for record: '{item}'. Please use the format \"item amount\" like \"breakfast -50\". \nFail to add a record.")
        except ValueError:
            #int() can't convert the amount to an integer
            print(f"Invalid value for money: '{amount}'. Please use an integer. \nFail to add a record.")
    return balance
    
def delete(expence_list, balance):
    try:
        assert len(expence_list) > 0, 'No record to delete.'
        in_str = input("Please enter the description of the record you want to delete:").strip()
        assert not(is_valid_integer(in_str)), 'Invalid format. Description is not a string, Fail to delete a record.'
    except AssertionError as e:
        print(e)
        return balance
    candidata = []
    for x in expence_list:
        #put all the records with the same description into a list
        if(x[0] == in_str):
            candidata.append(x)
    #if there's no such record
    if len(candidata) == 0:
        print(f"There's no such record with description '{in_str}'. Fail to delete a record.")
    #has only one record with the description
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
            #if there's no such record with the amount
            print(f"No record with description '{in_str}' and amount '{amt}'.")
    return balance
def closing():
    global balance
    global expence_list
    #write the balance and expence_list to a file
    file_path = os.path.join(os.path.dirname(__file__), 'record.txt')
    fh = open(file_path, 'w')
    #write the balance first then the expence_list
    fh.write(str(balance) + '\n')
    for desc, amount in expence_list[:-1]:
        fh.write(desc + ' ' + str(amount) + '\n')
    #the last record should not have a new line
    if(len(expence_list)): fh.write(expence_list[-1][0] + ' ' + str(expence_list[-1][1]))
    fh.close()
    
init()
command = input("What do you want to do? (add / view / delete / exit)?")
legal_commands = ['add', 'view', 'delete', 'exit']
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
        print("Invalid command. Try again.")
    command = input("What do you want to do? (add / view / delete / exit)?")
closing()