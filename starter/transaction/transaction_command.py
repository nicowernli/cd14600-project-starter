from transaction.transaction import Transaction, TransactionCategory

class ICommand:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

    def undo(self):
        raise NotImplementedError("Subclasses must implement this method")

class IncomeCommand(ICommand):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def execute(self):
        self.balance.apply_transaction(Transaction(self.amount, TransactionCategory.INCOME))

    def undo(self):
        self.balance.apply_transaction(Transaction(self.amount, TransactionCategory.EXPENSE))  # Undoing income is like adding an expense

class ExpenseCommand(ICommand):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def execute(self):
        self.balance.apply_transaction(Transaction(self.amount, TransactionCategory.EXPENSE))

    def undo(self):
        self.balance.apply_transaction(Transaction(self.amount, TransactionCategory.INCOME))  # Undoing an expense is like adding income

class CommandManager():
    def __init__(self):
        self.history = []
        self.redo_history = []

    def execute(self, command: ICommand):
        command.execute()
        self.history.append(command)
        self.redo_history.clear()  # Clear redo stack on new command

    def undo(self):
        if len(self.history) > 0:
            last_command = self.history.pop()
            last_command.undo()
            self.redo_history.append(last_command)

    def redo(self):
        if len(self.redo_history) > 0:
            next_command = self.redo_history.pop()
            next_command.execute()
            self.history.append(next_command)