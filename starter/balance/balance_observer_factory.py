from balance.balance_observer import PrintObserver, LowBalanceAlertObserver

class BalanceObserverFactory:
    """Factory to create observers based on type."""
    @staticmethod
    def create_observer(observer_type, **kwargs):
        if observer_type == "print":
            return PrintObserver()
        elif observer_type == "low_balance_alert":
            threshold = kwargs.get("threshold", 100)
            return LowBalanceAlertObserver(threshold=threshold)
        else:
            raise ValueError(f"Unknown observer type: {observer_type}")