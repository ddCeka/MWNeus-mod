init python:
    import math
    class Item:
        def __init__(self, name="", image="", description="",event_image="",is_view=False,level=0):
            self.name = name           
            self.image = image
            self.description = description   
            self.event_image = event_image
            self.is_view = is_view 
            self.level = level
    class Inventory:
        def __init__(self):
            self.items = []
        def add_item(self, item):
            if item not in self.items:
                item.is_view = True
                self.items.append(item)


    