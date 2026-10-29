class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    myacc = Account()
    myacc.deposit(100)
    print("Balance:", myacc.balance)
    myacc.withdraw(30)
    print("Balance:", myacc.balance)


if __name__ == "__main__":
    main()
