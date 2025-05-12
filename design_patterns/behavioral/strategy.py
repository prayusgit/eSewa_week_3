from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, cart: 'ShoppingCart', amount):
        cart.reset_cart()
        print(f"Paying {amount} using card number ****-****-*{self.card_number[-3:]}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, cart: 'ShoppingCart', amount):
        cart.reset_cart()
        print(f"Paying {amount} using PayPal of {self.email}")

class CryptoPayment(PaymentStrategy):
    def pay(self, cart: 'ShoppingCart', amount):
        cart.reset_cart()
        print(f"Paying {amount} using crypto")

# Context class
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
        self.payment_strategy = None

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def reset_cart(self):
        self.items = []
        self.total = 0
        self.payment_strategy = None

    def add_item(self, name, price):
        self.items.append(name)
        self.total += price

    def checkout(self):
        print(f"Total Amount: {self.total}")
        if self.payment_strategy:
            self.payment_strategy.pay(self, self.total)
        else:
            print("No payment strategy selected.")


# Usage
shopping_cart = ShoppingCart()

shopping_cart.add_item('Coke', 10)
shopping_cart.add_item('Detergent', 118)

shopping_cart.set_payment_strategy(PayPalPayment('hari@gmail.comj'))
shopping_cart.checkout()

shopping_cart.add_item('Soap', 19)
shopping_cart.set_payment_strategy(CreditCardPayment('123456789012'))
shopping_cart.checkout()