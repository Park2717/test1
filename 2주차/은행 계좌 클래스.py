# 은행 계좌 클래스

class Account:
    def __init__(self, passward, first_money):
        self.__password = passward
        self.__balance = first_money
    def deposit(self, deposit):
        self.__balance += deposit
        print("money:",self.__balance)
    def withdraw(self, passward, minus):
        if self.__password == passward:
            if self.__balance >= minus:
                self.__balance -= minus
                print("money:",self.__balance)
            else:
                print("Not enough money")
        else:
            print("Wrong passward")
    def transfer(self, passward, take, howmuch):
        if self.__password == passward:
            if self.__balance >= howmuch:
                self.__balance -= howmuch
                take.__balance += howmuch
                print("money:",self.__balance)
            else:
                print("Not enough money!!")
        else:
            print("Wrong passward")
    def showBalance(self, passward):
        if self.__password == passward:
            print("money:",self.__balance)
        else:
            print("Wrong passward")

account1 = Account(123, 0)
account2 = Account(312, 0)

account1.deposit(300) # money : 300
account1.withdraw(123, 400) # Not enough money!!
account1.transfer(123, account2, 200) # money : 100
account1.showBalance(123) # 100
#account2.deposit(100)
print('-'*20)
account2.showBalance(312) # 200
account2.withdraw(312, 200) # 0
