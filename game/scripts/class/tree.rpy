init python:
    class spell:
        def __init__(self, name,description="", image="",cost=0,level=0,quest="",is_active=False,start=True):
            self.name = name 
            self.description = description          
            self.image = image                             
            self.cost=cost           
            self.level = level
            self.quest = quest
            self.is_active =  is_active
            self.start = start
            
    