# Console Expense Tracker (Python)

## Description
A simple console-based Expense Tracker written in Python.  
The project was created as a learning exercise to practice object-oriented programming (OOP), application structure, and data persistence using JSON.

## Features
- Add new expenses with amount, category, date, and description  
- Remove existing expenses  
- View all expenses  
- Filter expenses by category  
- Filter expenses by date  
- Show total expenses for a specific day  
- Show total expenses for a specific month  
- Automatically save and load data from a JSON file  

## Technologies Used
- Python 3  
- Object-Oriented Programming (OOP)  
- Lists, loops, and conditional statements  
- JSON file handling  
- Console input/output  

## Data Storage
Expenses and categories are stored locally in a JSON file (`expenses.json`).  
All changes are automatically saved, and data is restored on program start.

## Project Structure
expense-tracker/
├── expense.py           # Expense model
├── category.py          # Category model
├── expense_manager.py   # Business logic and data handling
├── main.py              # Application entry point
├── expenses.json        # Local data storage
└── README.md            # Project documentation

## How to Run
1. Clone the repository:
```bash
 git clone https://github.com/Eleonorichka/console-expense-tracker.git
2. Navigate to the project folder: 
cd console-expense-tracker
3. Run the application: python 
main.py

### Note: Dates must be entered in the format YYYY-MM-DD.

## Purpose of the Project
The main goal of this project was to strengthen Python fundamentals, practice OOP principles in a real-world scenario, understand how to structure a small application, learn to separate logic into multiple files, and prepare projects for a GitHub portfolio.

## Author
Eleonora Topal