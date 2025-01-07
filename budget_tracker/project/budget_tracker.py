import json
from datetime import datetime
from pathlib import Path


class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.categories = ['Food', 'Transport',
                           'Entertainment', 'Housing', 'Utilities', 'Other']
        self.load_data()

    def add_income(self, description, amount, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        transaction = {
            'type': 'income',
            'description': description,
            'amount': float(amount),
            'date': date,
            'category': 'Income'
        }
        self.transactions.append(transaction)
        self.save_data()
        print(f"Income added: {description} - ${amount}")

    def add_expense(self, description, amount, category, date=None):
        if category not in self.categories:
            print(
                f"Invalid category. Please choose from: {', '.join(self.categories)}")
            return

        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        transaction = {
            'type': 'expense',
            'description': description,
            'amount': float(amount),
            'date': date,
            'category': category
        }
        self.transactions.append(transaction)
        self.save_data()
        print(f"Expense added: {description} - ${amount} ({category})")

    def get_balance(self):
        total_income = sum(t['amount']
                           for t in self.transactions if t['type'] == 'income')
        total_expenses = sum(t['amount']
                             for t in self.transactions if t['type'] == 'expense')
        return total_income - total_expenses

    def get_monthly_summary(self, year, month):
        monthly_transactions = [
            t for t in self.transactions
            if datetime.strptime(t['date'], '%Y-%m-%d').year == year
            and datetime.strptime(t['date'], '%Y-%m-%d').month == month
        ]

        summary = {
            'income': 0,
            'expenses': {},
            'total_expenses': 0
        }

        for transaction in monthly_transactions:
            if transaction['type'] == 'income':
                summary['income'] += transaction['amount']
            else:
                category = transaction['category']
                if category not in summary['expenses']:
                    summary['expenses'][category] = 0
                summary['expenses'][category] += transaction['amount']
                summary['total_expenses'] += transaction['amount']

        return summary

    def save_data(self):
        with open('budget_data.json', 'w') as f:
            json.dump(self.transactions, f, indent=2)

    def load_data(self):
        try:
            with open('budget_data.json', 'r') as f:
                self.transactions = json.load(f)
        except FileNotFoundError:
            self.transactions = []


def print_menu():
    print("\n=== Personal Budget Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Monthly Summary")
    print("5. Exit")


def main():
    tracker = BudgetTracker()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            description = input("Enter income description: ")
            amount = float(input("Enter amount: $"))
            tracker.add_income(description, amount)

        elif choice == '2':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: $"))
            print("\nCategories:", ', '.join(tracker.categories))
            category = input("Enter category: ")
            tracker.add_expense(description, amount, category)

        elif choice == '3':
            balance = tracker.get_balance()
            print(f"\nCurrent Balance: ${balance:.2f}")

        elif choice == '4':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            summary = tracker.get_monthly_summary(year, month)

            print(f"\n=== Monthly Summary ({month}/{year}) ===")
            print(f"Total Income: ${summary['income']:.2f}")
            print("\nExpenses by Category:")
            for category, amount in summary['expenses'].items():
                print(f"{category}: ${amount:.2f}")
            print(f"\nTotal Expenses: ${summary['total_expenses']:.2f}")
            print(
                f"Net Savings: ${(summary['income'] - summary['total_expenses']):.2f}")

        elif choice == '5':
            print("Thank you for using my personal budget tracker, view the budget_data.json file to see all the data :)")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
