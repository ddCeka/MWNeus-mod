screen item_desc(Item):    
    text "[Item.name!t][Item.description!ti]" xpos 450 ypos 820 xsize 1050
              
screen item_event_image(Item):
    imagebutton:
        idle  Item.event_image
        action Hide("item_event_image")  
         
style backpack_grid:
    spacing 50
    xalign 0.5
    yalign 0.5
 

screen backpack():
    style_prefix "backpack"
    tag menu 
    imagebutton:
        idle "gui/overlay/confirm.png"
        action [Hide("backpack"),Hide("item_desc")]
    key "K_ESCAPE" action [Hide("backpack"), Hide("item_desc")]
    add "inventory/backpack.png"
    default page = 0
    default gridSize = 8      
    grid 4 2:
        allow_underfull True
        for i in range(page*gridSize,(page+1)*gridSize):
            if i < len(inventory.items):               
                imagebutton:
                    auto inventory.items[i].image                  
                    xalign 0.5
                    yalign 0.5
                    action If(inventory.items[i].event_image =="",
                        Show("item_desc", Item = inventory.items[i]),
                        Show("item_event_image", Item = inventory.items[i]) )                                                  
            
    if len(inventory.items) > (page+1)*gridSize:
        textbutton "{size=250}{icon=icon-arrow-right-circle}{/size}" action SetScreenVariable("page", page+1) xpos 1520 yalign .5            
    if page > 0:
        textbutton "{size=250}{icon=icon-arrow-left-circle}{/size}" action SetScreenVariable("page", page-1) xpos 150 yalign .5