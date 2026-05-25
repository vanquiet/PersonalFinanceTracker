from models import Income, Expense
from storage import load_data, save_data
from manager import FinanceManager

def print_menu():
    print("PERSONAL FINANCE TRACKER")
    print("1. Add income")
    print("2. Add expense")
    print("3. Balance")
    print("4. Category breakdown")
    print("5. Monthly summary")
    print("6. Detect overspending")
    print("7. Statistics")
    print("8. Exit")

def ask_amount():
    amount = float(input("Enter amount: "))
    if amount < 0:
        raise ValueError
    return amount

def ask_date():
    date = input("Enter date (YYYY-MM-DD): ")
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        raise ValueError
    return date

def show_dict(data):
    if len(data) == 0:
        print("No data")
    else:
        for category in data:
            print(f"{category}: {data[category]}")

def main():
    data = load_data()

    while True:
        manager = FinanceManager(data)
        print_menu()
        choice = input("Choose option: ")

        if choice == "1":
            try:
                amount = ask_amount()
                date = ask_date()
                income = Income(amount, date)
                data.append(income.to_dict())
                save_data(data)
                print("Saved")
            except ValueError:
                print("Error. Use YYYY-MM-DD format")

        elif choice == "2":
            try:
                amount = ask_amount()
                date = ask_date()
                category = input("Enter category: ")
                if category == "":
                    category = "other"
                expense = Expense(amount, date, category)
                data.append(expense.to_dict())
                save_data(data)
                print("Saved")
            except ValueError:
                print("Error. Use YYYY-MM-DD format")

        elif choice =="3":
            balance = manager.calculate_balance()
            print(f"Balance: {balance}")

        elif choice =="4":
            summary = manager.category_breakdown()
            print(f"Category breakdown:")
            show_dict(summary)
            print("Categories: ", manager.get_all_categories())

        elif choice =="5":
            month = input("Enter month (YYYY-MM): ")
            result = manager.monthly_summary(month)
            show_dict(result)

        elif choice =="6":
            if manager.detect_overspending():
                print("Overspending")
            else:
                print("No overspending")
        elif choice =="7":
            stats = manager.get_statistics()
            show_dict(stats)

        elif choice =="8":
            print("Exit")
            break

        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
