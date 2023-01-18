from Bank_account import Account

name = "Weber"  # input("Digit your full name: ")
ID = "123456789-10"  # input("Digit your ID: \n")

holder = Account(name, ID, 1000.0)  # Object
holder.header(holder.name, holder.ID)  # Header

holder.deposit(5000)  # Do deposit in bank
statement = holder.bank_statement
holder.bank_draft(3000)
statement2 = holder.bank_statement
