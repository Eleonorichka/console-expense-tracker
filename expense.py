class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        } 
    @classmethod
    def from_dict(cls, data):
        return cls(
            amount = data["amount"],
            category = data["category"],
            date = data["date"],
            description = data.get("description", "")
        )
    
    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"