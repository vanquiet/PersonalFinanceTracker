class Transaction:
    def __init__(self, amount, date):
        self._amount = amount
        self.date = date

    def get_amount(self):
        return self._amount


    def to_dict(self):
        return {
            "type": "transaction",
            "amount": self._amount,
            "date": self.date
        }


class Income(Transaction):
    def __init__(self, amount, date):
        super().__init__(amount, date)
        self.type = "income"


    def to_dict(self):
        return {
            "type": self.type,
            "amount": self._amount,
            "date": self.date
        }


class Expense(Transaction):
    def __init__(self, amount, date, category):
        super().__init__(amount, date)
        self.type = "expense"
        self.category = category


    def to_dict(self):
        return {
            "type": self.type,
            "amount": self._amount,
            "date": self.date,
            "category": self.category
        }
