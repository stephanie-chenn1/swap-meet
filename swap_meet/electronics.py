from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = None, condition = None, age = None):
        super().__init__(category, condition, age)
        self.category = "Electronics"

    def __str__(self):
        return "A gadget full of buttons and secrets."
