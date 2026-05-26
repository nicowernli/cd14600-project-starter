# balance_observer.py

class IBalanceObserver:
    def update(self, balance, transaction):
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    def update(self, balance, transaction):
        """Print balance update message."""
        print(f"Balance updated to ${balance:.2f}")


class LowBalanceAlertObserver(IBalanceObserver):
    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance, transaction):
        """Alert if balance drops below threshold."""
        if balance < self.threshold and not self.alert_triggered:
            print(f"Alert: Balance is below threshold of ${self.threshold:.2f} after transaction {transaction}")
            self.alert_triggered = True
        elif balance >= self.threshold and self.alert_triggered:
            print(f"Balance has recovered above threshold of ${self.threshold:.2f} after transaction {transaction}")
            self.alert_triggered = False
