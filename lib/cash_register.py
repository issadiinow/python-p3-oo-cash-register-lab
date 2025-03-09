class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  # Track last transaction for voiding

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item_name] * quantity)  # Track items added
        self.last_transaction_amount = price * quantity  # Store last transaction amount

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100))  # Ensure integer output
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount  # Subtract last transaction
        self.last_transaction_amount = 0  # Reset last transaction amount
