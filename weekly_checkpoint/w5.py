balance = int(input("how much money do you have? "))
book = {}
in_str = input("Add some expense or income records with description and amount:")
# make in_str to a list of strings
in_list = in_str.split(', ')
book = {i.split()[0]: int(i.split()[1]) for i in in_list}
balance += sum(book.values())
print("Here's your expense and income records:")
for i in book:
    print("You {} {} dollars.".format(i, book[i]))
print("Now you have {} dollars.".format(balance))