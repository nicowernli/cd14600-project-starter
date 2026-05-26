# balance.py

from transaction.transaction_category import TransactionCategory
from balance.balance_observer import IBalanceObserver

class Balance:
    """Singleton to track the balance."""

    _instance = None
    
    def __init__(self):
        self._net_balance = 0.0
        self._observers = []  # List to hold registered observers

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Balance()
        return cls._instance

    def reset(self):
        self._net_balance = 0.0

    def add_income(self, amount):
        self._net_balance += amount

    def add_expense(self, amount):
        self._net_balance -= amount

    def apply_transaction(self, transaction):
        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)
        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)
        else:
            raise ValueError("Invalid transaction category")

        self.notify_observers(transaction)

    def get_balance(self):
        return self._net_balance

    def summary(self):
        return f"Net Balance: ${self._net_balance:.2f}"

    def register_observer(self, observer: IBalanceObserver):
        self._observers.append(observer)

    def notify_observers(self, transaction):
        for observer in self._observers:
            observer.update(self._net_balance, transaction)
    

