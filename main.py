from expense_manager import ExpenseManager
def main():
    manager = ExpenseManager()
    while True:
        print("\n1 - Add_expense")
        print("2 - Remove_expense")
        print("3 - Show all expenses")
        print("4 - Show by category")
        print("5 - Show expenses by date")
        print("6 - Show total for day")
        print("7 - Show total for month")
        print("0 - Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount")
                continue
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description: ")
            manager.add_expense(amount, category, date, description)
            
        elif choice == "2":
            try:
                index = int(input("Index: "))
                manager.remove_expense(index)
            except ValueError:
                print("Invalid index")
            
        elif choice == "3":
            expenses = manager.get_all_expenses()
            if not expenses:
                print("No expenses found")
            else:
                for idx, exp in enumerate(expenses):
                    print(f"{idx} - {exp}")
        
        elif choice == "4":
            print("Available categories:", manager.categories.get_categories())
            category = input("Choose category: ")
            for exp in manager.get_expenses_by_category(category):
                print(exp)
        
        elif choice == "5":
            date = input("Date (YYYY-MM-DD): ")
            for exp in manager.get_expenses_by_date(date):
                print(exp)
            
        elif choice == "6":
            date = input("Date (YYYY-MM-DD): ")
            total = manager.get_total_for_day(date)
            print(f"Total: {total}")
            
        elif choice == "7":
            try:
                month = int(input("Month: "))
                year = int(input("Year: "))
                total = manager.get_total_for_month(month, year)
                print(f"Total: {total}")
            except ValueError:
                print("Invalid input")
                continue
            
        elif choice == "0":
            manager.save()
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
        