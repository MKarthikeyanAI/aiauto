class ShoppingAssistant:
    def __init__(self):
        self.user_preferences = []
        self.wallet_balance = 0.0
        self.product_catalog = {
            "electronics": {"Smartphone": 699.99, "Laptop": 999.99, "Headphones": 199.99},
            "fashion": {"T-shirt": 19.99, "Jeans": 49.99, "Sneakers": 79.99},
            "books": {"Fiction Novel": 14.99, "Science Book": 29.99, "Biography": 24.99}
        }

    def get_user_preferences(self):
        print("Enter your shopping preferences. Type 'done' when you are finished:")
        while True:
            preference = input("Enter a shopping category (e.g., electronics, fashion, books, etc.): ")
            if preference.lower() == 'done':
                break
            self.user_preferences.append(preference)
        print(f"Your preferences: {self.user_preferences}")

    def recommend_products(self):
        recommendations = []
        for category in self.user_preferences:
            if category in self.product_catalog:
                recommendations.extend(self.product_catalog[category].keys())
            else:
                print(f"No recommendations available for category: {category}")

        if recommendations:
            print("Recommended products for you:")
            for product in recommendations:
                print(f"- {product}")
        else:
            print("No products to recommend based on your preferences.")

    def add_funds(self, amount):
        if amount > 0:
            self.wallet_balance += amount
            print(f"${amount:.2f} has been added to your wallet. Current balance: ${self.wallet_balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def check_balance(self):
        print(f"Your current wallet balance is: ${self.wallet_balance:.2f}")

    def process_payment(self, product_name):
        for category in self.product_catalog:
            if product_name in self.product_catalog[category]:
                product_price = self.product_catalog[category][product_name]
                if product_price <= self.wallet_balance:
                    self.wallet_balance -= product_price
                    print(f"Payment of ${product_price:.2f} for {product_name} processed successfully. Remaining balance: ${self.wallet_balance:.2f}")
                else:
                    print("Insufficient balance. Please add more funds to your wallet.")
                return
        print(f"Product '{product_name}' not found.")

    def buy_product(self):
        while True:
            product_name = input("Enter the product name you want to buy: ")
            if product_name.lower() == "done":
                break
            self.process_payment(product_name)

# Example of using the ShoppingAssistant class with M-Wallet system
assistant = ShoppingAssistant()
assistant.get_user_preferences()
assistant.recommend_products()

# M-Wallet functionality
assistant.add_funds(1000.0)
assistant.check_balance()
assistant.buy_product()
assistant.check_balance()