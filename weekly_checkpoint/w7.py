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

def initialize():
    global initial_money
    global records
    records = []
    #read the initial_money and records from a file
    try:
        with open('/home/justforfun/Learning-Python/weekly_checkpoint/record.txt', 'r') as fh:
            file_li = fh.readlines()
            balance_str = file_li[0].strip()
            #make sure balance is a number
            assert is_valid_integer(balance_str), 'balance is not a number'
            initial_money = int(balance_str)
            for line in file_li[1:]:
                desc, amount = line.split()
                desc = desc.strip()
                amount = amount.strip()
                #make sure amount is a number
                assert is_valid_integer(amount), 'amount is not a number'
                records.append((desc, int(amount)))
    except FileNotFoundError:
        print("record.txt file not found.")
        initial_money = int(input("How much money do you have? "))
    except AssertionError as e:
        #invalid format of the record file
        print(e, ':invalid record, deleting the content of the file')
        with open('/home/justforfun/Learning-Python/weekly_checkpoint/record.txt', 'w') as fh:
            pass
        initial_money = handle_balance_input()
        
    except Exception as e:
        #can't read the file
        initial_money = handle_balance_input()
        
def add(records, initial_money):
    in_str = input("Add some expense or income records with description and amount (format: 'item amount'): ")
    in_list = in_str.split(', ')
    for item in in_list:
        try:
            desc = item.split()[0]
            amount = item.split()[1]
            amount = int(amount)
            records.append((desc, amount))
            initial_money += amount
        except IndexError:
            #item can't be split into two parts
            print(f"Invalid format for record: '{item}'. Please use the format \"item amount\" like \"breakfast -50\". \nFail to add a record.")
        except ValueError:
            #int() can't convert the amount to an integer
            print(f"Invalid value for money: '{amount}'. Please use an integer. \nFail to add a record.")
    return initial_money
    
def delete(records, initial_money):
    try:
        assert len(records) > 0, 'No record to delete.'
        in_str = input("Please enter the description of the record you want to delete:").strip()
        assert not(is_valid_integer(in_str)), 'Invalid format. Description is not a string, Fail to delete a record.'
    except AssertionError as e:
        print(e)
        return initial_money
    candidata = []
    for x in records:
        #put all the records with the same description into a list
        if(x[0] == in_str):
            candidata.append(x)
    #if there's no such record
    if len(candidata) == 0:
        print(f"There's no such record with description '{in_str}'. Fail to delete a record.")
    #has only one record with the description
    elif(len(candidata) == 1):
        records.remove(candidata[0])
        initial_money -= candidata[0][1]
    else:
        amt_str = input("There are multiple records with the same description. Please enter the amount of the record you want to delete:")
        amt = int(amt_str)
        for x in candidata:
            if(x[1] == amt):
                records.remove(x)
                initial_money -= amt
                break
        else:
            #if there's no such record with the amount
            print(f"No record with description '{in_str}' and amount '{amt}'.")
    return initial_money
def save():
    global initial_money
    global records
    #write the initial_money and records to a file
    file_path = os.path.join(os.path.dirname(__file__), 'record.txt')
    fh = open(file_path, 'w')
    #write the initial_money first then the records
    fh.write(str(initial_money) + '\n')
    for desc, amount in records[:-1]:
        fh.write(desc + ' ' + str(amount) + '\n')
    #the last record should not have a new line
    if(len(records)): fh.write(records[-1][0] + ' ' + str(records[-1][1]))
    fh.close()
    
initialize()
command = input("What do you want to do? (add / view / delete / exit)?")
legal_commands = ['add', 'view', 'delete', 'exit']
while True:
    if command == 'add':
        initial_money = add(records, initial_money)
    elif command == 'view':
        print("Description          Amount")
        print("==================== ======")
        for desc, amount in records:
            print(f"{desc:<20} {amount:>5}")
        print("==================== ======")
        print("Now you have {} dollars.".format(initial_money))
    elif command == 'delete':
        initial_money=delete(records, initial_money)
    elif command == 'exit':
        break
    else:
        print("Invalid command. Try again.")
    command = input("What do you want to do? (add / view / delete / exit)?")
save()