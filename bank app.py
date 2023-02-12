#some parts were written during class only some parts were added by me
class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'


class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            return amount
        else:
            return "Please enter valid value"

    def charge(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'

bank = Bank()

c = bank.create_customer('John', 'Brown')
print(c)
a = bank.create_account(c)
a2 = bank.create_account(c)
print(a)
deposited = a.deposit(100)
deposited = a.deposit(200)
print(deposited)
charged = a.charge(50)
print(charged)

c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)
print(bank)
