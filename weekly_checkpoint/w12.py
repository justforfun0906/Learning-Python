import os
import sys
class  Record:
    """Represents a record with category, description and amount."""
    def __init__(self, category, description, amount):
        self._category = category
        self._description = description
        self._amount = amount
class Records:
    """Maintains a list of records."""
    category_list = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    flatten_category_list = ['expense', 'food', 'meal', 'snack', 'drink', 'transportation', 'bus', 'railway', 'income', 'salary', 'bonus']
    def __init__(self):
        #read the initial_money and records from a file
        self.categories = Categories()
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'record.txt')
            with open(file_path, 'r') as fh:
                file_li = fh.readlines()
                balance_str = file_li[0].strip()
                #make sure balance is a number
                assert Categories.is_valid_integer(balance_str), 'balance is not a number'
                self._initial_money = int(balance_str)
                self._records = []
                for line in file_li[1:]:
                    cate, desc, amount = line.split()
                    cate = cate.strip()
                    desc = desc.strip()
                    amount = amount.strip()
                    #make sure amount is a number
                    assert Categories.is_valid_integer(amount), 'amount is not a number'
                    self._records.append(Record(cate, desc, int(amount)))
        except FileNotFoundError:
            print("record.txt file not found.")
            self._initial_money = Categories.handle_balance_input()
        except AssertionError as e:
            #invalid format of the record file
            print(e, ':invalid record, deleting the content of the file')
            with open('weekly_checkpoint/record.txt', 'w') as fh:
                pass
            self._initial_money = Categories.handle_balance_input()
        except Exception as e:
            print(e)
            #can't read the file
            self._initial_money = Categories.handle_balance_input()
    def save(self):
        #write the initial_money and records to a file
        file_path = os.path.join(os.path.dirname(__file__), 'record.txt')
        with open(file_path, 'w') as fh:
            #write the initial_money first then the records
            fh.write(str(self._initial_money) + '\n')
            for record in self._records[:-1]:
                fh.write(f"{record._category} {record._description} {record._amount}\n")
            #the last record should not have a new line
            if len(self._records):
                fh.write(f"{self._records[-1]._category} {self._records[-1]._description} {self._records[-1]._amount}")
    def add(self, in_str):
        in_list = in_str.split(', ')
        for item in in_list:
            try:
                cate = item.split()[0]
                assert cate in Records.flatten_category_list, f"Invalid category: '{cate}'. Please use the categories in the list. \nFail to add a record."
                desc = item.split()[1]
                amount = item.split()[2]
                amount = int(amount)
                self._records.append(Record(cate, desc, amount))
                self._initial_money += amount
                self.save() #save the record after adding a record
            except AssertionError as e:
                print(e)
            except IndexError:
                #item can't be split into two parts
                print(f"Invalid format for record: '{item}'. Please use the format \"item amount\" like \"breakfast -50\". \nFail to add a record.")
            except ValueError:
                #int() can't convert the amount to an integer
                print(f"Invalid value for money: '{amount}'. Please use an integer. \nFail to add a record.")
    def view(self):
        print("Category        Description          Amount")
        print("=============== ==================== ======")
        for record in self._records:
            print(f"{record._category:<15} {record._description:<20} {record._amount:>5}")
        print("===========================================")
        print("Now you have {} dollars.".format(self._initial_money))
    def delete(self, in_str):
        try:
            assert len(self._records) > 0, 'No record to delete.'
            in_str = in_str.strip()
            assert not(self.categories.is_valid_integer(in_str)), 'Invalid format. Description is not a string, Fail to delete a record.'
        except AssertionError as e:
            print(e)
            return
        candidata = []
        for x in self._records:
            #put all the records with the same description into a list
            if(x._category == in_str):
                candidata.append(x)
        #if there's no such record
        if len(candidata) == 0:
            print(f"There's no such record with description '{in_str}'. Fail to delete a record.")
        #has only one record with the description
        elif(len(candidata) == 1):
            self._records.remove(candidata[0])
            self._initial_money -= candidata[0]._amount
            self.save()
    def find(self, in_str):
        subcate = self.categories.find_subcate(in_str)
        #output
        print("Category        Description          Amount")
        print("=============== ==================== ======")
        for record in self._records:
            if record._category in subcate:
                print(f"{record._category:<15} {record._description:<20} {record._amount:>5}")
        print("===========================================")
        print("Now you have {} dollars.".format(self._initial_money))
class Categories:
    """Maintain the category list and provide some methods"""
    _category_list = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
    _flatten_category_list = ['expense', 'food', 'meal', 'snack', 'drink', 'transportation', 'bus', 'railway', 'income', 'salary', 'bonus']
    def __init__(self):
        self._category_list = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
        self._flatten_category_list = ['expense', 'food', 'meal', 'snack', 'drink', 'transportation', 'bus', 'railway', 'income', 'salary', 'bonus']
    def view(self, category_list, level=0):
        #recursively print the categories
        for child in category_list:
            if isinstance(child, list):
                self.view(child, level+1)
            else:
                print('  '*level +'-'+ child)
    def find_subcate(self, category):
        def find_subcate_gen(category, category_list, found=False):
            if type(category_list) == list:
                for index, child in enumerate(category_list):
                    yield from find_subcate_gen(category, child, found)
                    if child == category and index + 1 <len(category_list) and type(category_list[index+1]) == list:
                        found = True
                        yield from find_subcate_gen(category, category_list[index+1], found)
            else:
                if category_list == category or found:
                    yield category_list
        return list(find_subcate_gen(category, self._category_list))
    
    @staticmethod
    def is_valid_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    @staticmethod
    def handle_balance_input():
        str = input("How much money do you have? ")
        try:
            assert Categories.is_valid_integer(str), 'balance is not a number'
        except AssertionError as e:
            print(e, ', set balance to 0 by default')
            return 0
        return int(str)
    
categories = Categories()
records = Records()
while True:
    command = input("Enter a command (add/view/view categories/delete/find/exit): ")
    if(command == 'add'):
        records.add(input("Add some expense or income records with category, description and amount (format: 'category item amount'): "))
    elif(command == 'view'):
        records.view()
    elif(command == 'view categories'):
        categories.view(categories._category_list)
    elif(command == 'delete'):
        records.delete(input("Enter the description of the record you want to delete: "))
    elif(command == 'find'):
        records.find(input("Enter the description of the record you want to find: "))
    elif(command == 'exit'):
        records.save()
        break
    else:
        sys.stderr.write("Invalid command. Please enter again.")
