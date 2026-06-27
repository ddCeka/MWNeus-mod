screen tree_spell:         
    vpgrid:
        cols 1
        spacing 30  
        ypos -10
        ysize 550        
        allow_underfull True  
        scrollbars "vertical"
        draggable True
        mousewheel True
        for i in range(0,len(tree)):
            vbox:
                xsize 635 
                spacing 20  
                label _('{color=#FFFFFF}Level [i]') xalign 0.5  
                hbox: 
                    spacing 20
                    xalign 0.5                    
                    for j in range(0,len(tree[i])):                        
                        if tree[i][j].is_active:
                            imagebutton:
                                idle tree[i][j].image % 'active'
                                hover tree[i][j].image % 'hover'
                                selected_idle tree[i][j].image % 'hover'
                                insensitive "btn_lock_idle"
                                sensitive i <=relationship_level
                                action SetVariable("select_spell",tree[i][j])                                                                                                           
                        else:
                            imagebutton:
                                auto tree[i][j].image                                    
                                selected_idle tree[i][j].image % 'hover' 
                                insensitive "btn_lock_idle"
                                sensitive i <=relationship_level and tree[i][j].start              
                                action SetVariable("select_spell", tree[i][j])                           
    use modal_confirmation
    
screen modal_confirmation:
    vbox:        
        xsize 630 
        spacing 5
        text _("[select_spell.name!tq]") xalign 0.5
        text str(select_spell.description):
            xalign 0.5
            size 35
          
        if select_spell.is_active:
            pass
            # text _("{size=+10}learned") xalign 0.5
        else:     
            textbutton _("{size=+15}{b}Learn"):
                text_color "#cc0066"
                text_hover_color "#fff"
                ypos -10
                xalign 0.5
                action [
                    SetField(select_spell, "is_active", True),
                    If(select_spell.quest != "", [
                        SetField(select_spell.quest, "completion", True),
                        Function(quest_screen_spells),
                        Function(is_quest_change, True),
                        Function(is_quest_change_screen, True),
                        Call("notify_personalized", _("Side Quest updated"))
                    ])
                ]
                at text_animation_alpha
