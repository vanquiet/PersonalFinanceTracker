from manager import FinanceManager
from models import Income, Expense

def run_tests():
    data = [
        {"type": "income", "amount": 1000, "date": "2026-05-01"},
        {"type": "expense", "amount": 200, "date": "2026-05-02", "category": "food"},
        {"type": "expense", "amount": 100, "date": "2026-05-03", "category": "games"},
        {"type": "income", "amount": 500, "date": "2026-06-01"}
    ]

    manager = FinanceManager(data)

    assert manager.calculate_balance() == 1200
    assert manager.detect_overspending() == False

    summary = manager.category_breakdown()
    assert summary["food"] == 200
    assert summary["games"] == 100

    may = manager.monthly_summary("2026-05")
    assert may["income"] == 1000
    assert may["expense"] == 300
    assert may["balance"] == 700

    stats = manager.get_statistics()
    assert stats["total_income"] == 1500
    assert stats["total_expense"] == 300
    assert stats["biggest_expense"] == 200

    categories = manager.get_all_categories()
    assert "food" in categories
    assert "games" in categories
    expenses = [t for t in manager.transactions if t["type"] == "expense"]
    assert len(expenses) == 2

    income = Income(100, "2026-05-01")
    expense = Expense(50, "2026-05-01", "food")
    assert income.to_dict()["type"] == "income"
    assert expense.to_dict()["category"] == "food"

    empty_manager = FinanceManager([])
    assert empty_manager.calculate_balance() == 0
    assert empty_manager.category_breakdown() == {}

    print("Success")

if __name__ == "__main__":
    run_tests()