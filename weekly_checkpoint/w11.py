import os
class  Record:
class Records:
class Category:
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
        file_path = os.path.join(os.path.dirname(__file__), 'record.txt')
        with open(file_path, 'r') as fh:
            file_li = fh.readlines()
            balance_str = file_li[0].strip()
            #make sure balance is a number
            assert is_valid_integer(balance_str), 'balance is not a number'
            initial_money = int(balance_str)
            for line in file_li[1:]:
                cate, desc, amount = line.split()
                cate = cate.strip()
                desc = desc.strip()
                amount = amount.strip()
                #make sure amount is a number
                assert is_valid_integer(amount), 'amount is not a number'
                records.append((cate, desc, int(amount)))
    except FileNotFoundError:
        print("record.txt file not found.")
        initial_money = int(input("How much money do you have? "))
    except AssertionError as e:
        #invalid format of the record file
        print(e, ':invalid record, deleting the content of the file')
        with open('weekly_checkpoint/record.txt', 'w') as fh:
            pass
        initial_money = handle_balance_input()
        
    except Exception as e:
        #can't read the file
        initial_money = handle_balance_input()
def initialize_categories():
    global category_list, flatten_category_list
    category_list = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    flatten_category_list = flatten_list(category_list)
def view_categories(category_list, level=0):
    #recursively print the categories
    for child in category_list:
        if isinstance(child, list):
            view_categories(child, level+1)
        else:
            print('  '*level +'-'+ child)
def add(records, initial_money):
    in_str = input("Add some expense or income records with category, description and amount (format: 'category item amount'): ")
    in_list = in_str.split(', ')
    for item in in_list:
        try:
            cate = item.split()[0]
            assert cate in flatten_category_list, f"Invalid category: '{cate}'. Please use the categories in the list. \nFail to add a record."
            desc = item.split()[1]
            amount = item.split()[2]
            amount = int(amount)
            records.append((cate, desc, amount))
            initial_money += amount
        except AssertionError as e:
            print(e)
        except IndexError:
            #item can't be split into two parts
            print(f"Invalid format for record: '{item}'. Please use the format \"item amount\" like \"breakfast -50\". \nFail to add a record.")
        except ValueError:
            #int() can't convert the amount to an integer
            print(f"Invalid value for money: '{amount}'. Please use an integer. \nFail to add a record.")
    return initial_money
def view(records):
    print("Category        Description          Amount")
    print("=============== ==================== ======")
    for cate, desc, amount in records:
        print(f"{cate:<15} {desc:<20} {amount:>5}")
    print("===========================================")
    print("Now you have {} dollars.".format(initial_money))
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
def flatten_list(li):
    if type(li) == list:
        ret_val = []
        for item in li:
            ret_val.extend(flatten_list(item))
        return ret_val
    else:
        return [li]
def find_subcate(category, categories):
    if type(categories) == list:
        for v in categories:
            result = find_subcate(category, v)
            if result == True:
                index = categories.index(v)
                if index + 1 < len(categories) and \
                        type(categories[index + 1]) == list:
                    return flatten_list(categories[index:index + 2])
                else:
                    # return only itself if no subcategories
                    return [v]
            if result != []:
                return result
    return True if categories == category else []
def find(records):
    in_str = input("Please enter the description of the record you want to find:").strip()
    subcate = find_subcate(in_str, category_list)
    #output
    print("Category        Description          Amount")
    print("=============== ==================== ======")
    for cate, desc, amount in records:
        if cate in subcate:
            print(f"{cate:<15} {desc:<20} {amount:>5}")
    print("===========================================")
    print("Now you have {} dollars.".format(initial_money))
def save():
    global initial_money
    global records
    #write the initial_money and records to a file
    file_path = os.path.join(os.path.dirname(__file__), 'record.txt')
    with open(file_path, 'w') as fh:
        #write the initial_money first then the records
        fh.write(str(initial_money) + '\n')
        for cate, desc, amount in records[:-1]:
            fh.write(f"{cate} {desc} {amount}\n")
        #the last record should not have a new line
        if len(records):
            fh.write(f"{records[-1][0]} {records[-1][1]} {records[-1][2]}")
    
initialize()
initialize_categories()
print(flatten_category_list)
command = input("What do you want to do? (add / view / delete / view categories / find / exit )?")
legal_commands = ['add', 'view', 'delete', 'exit', 'view_categories', 'find']
while True:
    if command == 'add':
        initial_money = add(records, initial_money)
    elif command == 'view':
        view(records)
    elif command == 'delete':
        initial_money=delete(records, initial_money)
    elif command == 'exit':
        break
    elif command == 'view categories':
        view_categories(category_list)
    elif command == 'find':
        find(records)
    else:
        print("Invalid command. Try again.")
    command = input("What do you want to do? (add / view / delete / view categories / find /exit)?")
save()
