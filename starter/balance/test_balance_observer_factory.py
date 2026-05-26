from balance.balance_observer import PrintObserver, LowBalanceAlertObserver
from balance.balance import Balance
from balance.balance_observer_factory import BalanceObserverFactory

class TestBalanceObserverFactory:
    def test_observer_factory(self):
        BalanceObserverFactory.create_observer("print")
        BalanceObserverFactory.create_observer("low_balance_alert", threshold=100)
        balance = Balance.get_instance()
        
        print_observer = PrintObserver()
        low_balance_observer = LowBalanceAlertObserver(threshold=100)
        
        balance.register_observer(print_observer)
        balance.register_observer(low_balance_observer)
        
        # Add transactions to trigger observers
        balance.add_transaction(150, 'income')  # Should trigger print observer
        balance.add_transaction(60, 'expense')  # Should trigger print observer and low balance alert

    def test_invalid_observer_type(self):
        try:
            BalanceObserverFactory.create_observer("unknown")
        except ValueError as e:
            assert str(e) == "Unknown observer type: unknown"