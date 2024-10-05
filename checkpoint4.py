balance = int(input("how much money do you have? "))
description, amount = input("Add an expense or income record with description and amount:").split()
balance += int(amount)
print("Now you have {} dollars.".format(balance))