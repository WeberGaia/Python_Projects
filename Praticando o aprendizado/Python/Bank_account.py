class Account:

    def header(self, name, ID):
        header0 = "=" * len(name)
        header1 = "=" * 29
        print(header1 + header0)
        header2 = "Welcome to WG Investing, Ms. {}"
        print(header2.format(name))
        print(header1 + header0)
        print("ID: {}\n".format(ID))

    # Constructor Method
    def __init__(self, name, id, credit_limit):
        self.__name = name
        self.__ID = id
        self.__credit_limit = credit_limit
        self.__bank_balance = 0.0


    def deposit(self, value):
        self.__bank_balance += value

    def bank_draft(self, value):
        if value < 0:
            print("Sorry! You can't draft negative values")
        elif value > self.__bank_balance:
            print("Sorry! Bank draft bigger than bank statement")
        else:
            self.__bank_balance -= value

    @property
    def bank_statement(self):
        return print("The bank statement is U${}".format(self.__bank_balance))

    @property
    def name(self):
        return self.__name

    @property
    def ID(self):
        return self.__ID
