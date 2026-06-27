screen bath_spell:
    default statename=neus_states[N_state]
    tag spell_screen    
    vbox:
        xpos 10
        text _("Level: [bath_event_lvl]"):
            outlines [ (4, gui.accent_color) ]
            size 100  
        if bath_event_lvl>=2:          
            text _("{b}State:{/b} [statename!t]"):
                outlines [ (2, "#000") ]
                size 50    
    hbox:
        xalign 0.95
        yalign 0.95            
        spacing 10        
        imagebutton:
            auto "btn_level_down_%s"
            insensitive "btn_lock_skil_idle"
            sensitive bath_event_lvl>0 and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level down")
            action Show("confirm",None,_("Are you sure you want to level down?"),
                [Hide("confirm"), Call("adjust_room_levels", change=-1)],Hide("confirm"))
                
        imagebutton:
            auto "btn_level_up_%s"
            insensitive "btn_lock_skil_idle"
            sensitive bath_event_lvl<relationship_level and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level up")
            action Show("confirm",None,_("Are you sure you want to level up?"),
                [Hide("confirm"), Call("adjust_room_levels", change=+1)],Hide("confirm"))