"""This module serves as the entry point for the program."""
from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer_factory import BalanceObserverFactory
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome
from transaction.transaction_command import IncomeCommand, ExpenseCommand, CommandManager

def main():
    print("Adding transactions...")
   
    # TODO: Create balance and add observers
    balance = Balance.get_instance()
    print_observer = BalanceObserverFactory.create_observer("print")
    low_balance_observer = BalanceObserverFactory.create_observer("low_balance_alert", threshold=100)
    manager = CommandManager()
    
    balance.register_observer(low_balance_observer)
    balance.register_observer(print_observer)

    # Create standard transactions
    transactions = [
        Transaction(100, TransactionCategory.INCOME),
        Transaction(50, TransactionCategory.EXPENSE),
        Transaction(200, TransactionCategory.INCOME),
        Transaction(75, TransactionCategory.EXPENSE),
    ]

    # Create an external income transaction (via Adapter pattern)
    freelance_income = ExternalFreelanceIncome(1200, "INV-98765", "Mobile App Project")
    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()

    all_transactions = transactions + [adapted_transaction]

    # TODO: Apply all transactions to balance
    for transaction in all_transactions:
        command = IncomeCommand(balance, transaction.amount) if transaction.category == TransactionCategory.INCOME else ExpenseCommand(balance, transaction.amount)
        manager.execute(command)

if __name__ == "__main__":
    main()
