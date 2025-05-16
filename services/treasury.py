class TreasuryService:
    def __init__(self):
        self.treasury_balance = 1000000  # Example starting balance

    def execute_transaction(self, amount, recipient):
        """Processes a treasury transaction."""
        if amount <= self.treasury_balance:
            self.treasury_balance -= amount
            return True  # Successful transaction
        return False  # Failed due to insufficient funds

    def get_treasury_balance(self):
        """Returns current treasury balance."""
        return self.treasury_balance
