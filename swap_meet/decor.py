from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = None, condition = None, age = None):
        super().__init__(category, condition, age)
        self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."
