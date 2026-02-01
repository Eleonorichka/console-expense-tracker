from expense import Expense
from category import Category
import os
import json

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.categories = Category()
        self.load()
        
    def add_expense(self, amount, category, date, description):
        if amount <= 0:
            print ("Amount must be greater than 0")
            return
        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        if category not in self.categories.get_categories():
            self.categories.add_category(category)
        self.save()
        
    def remove_expense(self,index):
        if index < 0  or index >= len(self.expenses):
            print ("Error: Invalid index")
            return
        self.expenses.pop(index)
        self.save()
    
    def get_all_expenses(self):
        return self.expenses
    
    def get_expenses_by_category(self, category):
        result = []
        for expense in self.expenses:
            if category == expense.category:
                result.append(expense)
        return result
    
    def get_expenses_by_date(self, date):
        result = []
        for expense in self.expenses:
            if date == expense.date:
                result.append(expense)
        return result
    
    def get_total_for_day(self, date):
        total = 0
        for expense in self.expenses:
            if expense.date == date:
                total += expense.amount
        return total
        
    def get_total_for_month(self, month, year):
        total = 0
        for expense in self.expenses:
            year_str, month_str, _ = expense.date.split("-")
            if int(year_str) == year and int(month_str) == month:
                total += expense.amount
        return total
    
    def add_category(self, name):
        self.categories.add_category(name)
        self.save()
    
    def save(self):
        data = {
            "expenses": [exp.to_dict() for exp in self.expenses],
            "categories": self.categories.get_categories()
        }
        with open("expenses.json", "w") as f:
            json.dump(data, f, indent = 4)
        
    
    def load(self):
        file_name = "expenses.json"
        if not os.path.exists("expenses.json"):
            return
        with open(file_name, "r") as f:
            data = json.load(f)
        self.expenses = [Expense.from_dict(item) for item in data.get("expenses", [])]
        self.categories = Category(data.get("categories", []))