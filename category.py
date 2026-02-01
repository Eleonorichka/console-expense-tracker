class Category:
    def __init__(self, categories = None):
        if categories is None:
            self.categories = set()
        else:
            self.categories = set(categories)
        
    def add_category(self, name):
        self.categories.add(name)
            
    def get_categories(self):
        return list(self.categories)