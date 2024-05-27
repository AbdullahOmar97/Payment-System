
from abc import ABC, abstractmethod


#Define the Strategy Interface

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#Define Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_expiry, card_cvv):
        self.card_number = card_number
        self.card_expiry = card_expiry
        self.card_cvv = card_cvv

    def pay(self, amount):
        return f"Paid {amount} using Credit Card ending with {self.card_number[-4:]}."

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} using PayPal account {self.email}."

class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Paid {amount} using Cryptocurrency to wallet {self.wallet_address}."


# Define the Context

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        return self._strategy.pay(amount)

# Use the Strategy Pattern

if __name__ == "__main__":
    # Using Credit Card payment
    credit_card_payment = CreditCardPayment("1234567890123456", "12/25", "123")
    context = PaymentContext(credit_card_payment)
    print(context.execute_payment(100))

    # Switching strategy to PayPal
    paypal_payment = PayPalPayment("user@example.com")
    context.set_strategy(paypal_payment)
    print(context.execute_payment(200))

    # Switching strategy to Cryptocurrency
    crypto_payment = CryptoPayment("1A2b3C4d5E6f7G8h9I0j")
    context.set_strategy(crypto_payment)
    print(context.execute_payment(300))
