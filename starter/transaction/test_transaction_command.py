import unittest
from transaction.transaction_command import IncomeCommand, ExpenseCommand, CommandManager
from balance.balance import Balance

class TestTransactionCommand(unittest.TestCase):
    def setUp(self):
        self.balance = Balance()

    def test_command_execution(self):
        # This is a placeholder test. In a real implementation, you would create
        # a concrete command class that implements ICommand and test its execute method.
        command = IncomeCommand(self.balance, 100)  # Assuming IncomeCommand is a concrete implementation of ICommand
        command.execute()

        self.assertEqual(self.balance.get_balance(), 100)

    def test_command_execution_expense(self):
        command = ExpenseCommand(self.balance, 50)  # Assuming ExpenseCommand is a concrete implementation of ICommand
        command.execute()

        self.assertEqual(self.balance.get_balance(), -50)

    def test_command_execution_sequence(self):
        income_command = IncomeCommand(self.balance, 200)
        expense_command = ExpenseCommand(self.balance, 75)

        income_command.execute()
        expense_command.execute()

        self.assertEqual(self.balance.get_balance(), 125)

    def test_command_history_undo(self):
        manager = CommandManager()  # Assuming CommandManager is implemented to manage command history
        income_command = IncomeCommand(self.balance, 150)
        expense_command = ExpenseCommand(self.balance, 50)

        manager.execute(income_command)
        manager.execute(expense_command)

        self.assertEqual(self.balance.get_balance(), 100)

    def test_command_history_undo(self):
        manager = CommandManager()
        income_command = IncomeCommand(self.balance, 150)
        expense_command = ExpenseCommand(self.balance, 50)

        manager.execute(income_command)
        manager.execute(expense_command)

        manager.undo()  # Assuming undo will revert the last command

        self.assertEqual(self.balance.get_balance(), 150)

    def test_command_history_redo(self):
        manager = CommandManager()
        income_command = IncomeCommand(self.balance, 150)
        expense_command = ExpenseCommand(self.balance, 50)

        manager.execute(income_command)
        manager.execute(expense_command)

        manager.undo()
        manager.redo()

        self.assertEqual(self.balance.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()