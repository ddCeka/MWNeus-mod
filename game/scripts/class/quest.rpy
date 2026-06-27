init python:
    class Quest:
        def __init__(self,description="",level=0,place="",time_event=0,label_event="",completion=False,start=True):              
            self.description = description 
            self.level = level
            self.place = place 
            self.time_event = time_event  
            self.label_event=label_event                       
            self.completion = completion  
            self.start = start 
               
           
        