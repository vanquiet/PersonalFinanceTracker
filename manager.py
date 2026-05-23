class FinanceManager:
    def __init__(self, transactions):
        self.transactions = transactions

    def calculate_balance(self):
        income = 0
        expense = 0
        for item in self.transactions:
            if item["type"] == "income":
                income = income + item["amount"]
            elif item["type"] == "expense":
                expense = expense + item["amount"]
        return income - expense

    def detect_overspending(self):
        balance = self.calculate_balance()
        if balance < 0:
            return True
        return False

    def category_breakdown(self):
        summary = {}
        for item in self.transactions:
            if item["type"] == "expense":
                category = item.get("category", "other")
                amount = item["amount"]

                if category in summary:
                    summary[category] = summary[category] + amount
                else:
                    summary[category] = amount
        return summary

    def monthly_summary(self, month):
        income = 0
        expense = 0
        for item in self.transactions:
            if item["date"][:7] == month:
                if item["type"] == "income":
                    income = income + item["amount"]
                elif item["type"] == "expense":
                    expense = expense + item["amount"]

        return {
            "month": month,
            "income": income,
            "expense": expense,
            "balance": income - expense
        }

    def get_statistics(self):
        incomes = []
        expenses = []
        for item in self.transactions:
            if item["type"] == "income":
                incomes.append(item["amount"])
            elif item["type"] == "expense":
                expenses.append(item["amount"])

        total_income = sum(incomes)
        total_expense = sum(expenses)

        if len(expenses) > 0:
            biggest_expense = max(expenses)
            average_expense = total_expense / len(expenses)
        else:
            biggest_expense = 0
            average_expense = 0

        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": total_income - total_expense,
            "biggest_expense": biggest_expense,
            "average_expense": average_expense,
            "number_of_transactions": len(self.transactions)
        }

    def get_all_categories(self):
        categories = set()
        for item in self.transactions:
            if item["type"] == "expense":
                categories.add(item.get("category", "other"))

        return categories


