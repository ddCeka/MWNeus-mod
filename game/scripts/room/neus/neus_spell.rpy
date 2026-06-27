screen neus_spell:
    default statename=neus_states[N_state]
    tag spell_screen    
    vbox:
        xpos 10
        text _("Level: [neus_event_lvl]"):
            outlines [ (4, gui.accent_color) ]
            size 100  
        if neus_event_lvl>=2:          
            text _("{b}State:{/b} [statename!t]"):
                outlines [ (2, "#000") ]    
    hbox:
        xalign 0.95
        yalign 0.95            
        spacing 10        
        imagebutton:
            auto "btn_level_down_%s"
            insensitive "btn_lock_skil_idle"
            sensitive neus_event_lvl>0 and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level down")
            action Show("confirm",None,_("Are you sure you want to level down?"),
                [Hide("confirm"), Call("adjust_room_levels", change=-1)],Hide("confirm"))
                
        imagebutton:
            auto "btn_level_up_%s"
            insensitive "btn_lock_skil_idle"
            sensitive neus_event_lvl<relationship_level and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level up")
            action Show("confirm",None,_("Are you sure you want to level up?"),
                [Hide("confirm"), Call("adjust_room_levels", change=+1)],Hide("confirm"))
    if  neus_event_lvl<=2 and time < 4:
        vbox:
            xpos 10
            yalign 0.5       
            xmaximum 144
            spacing 30
            for spell in spells_action:
                if spell.level<=neus_event_lvl:
                    imagebutton:
                        auto spell.image at zoom_1_5
                        insensitive "btn_lock_idle"
                        sensitive spell.is_active
                        tooltip spell.name
                        action [Hide("spell_screen"),Jump("neus_touch%s"%neus_event_lvl)]
    use screen_tooltip
#----------------------------Level 0---------------------------------
label neus_touch0:    
    if is_touch>0:
        scene neus0_10
        neus "Don't come any closer (My heart can't take it again)"
    else:
        scene neus0_2 with spellfx
        if incest_story:
            neus "Brother, why are you getting so close?"
        else:
            neus "Why are you getting so close?"
        scene neus0_3 with dissolve
        neus "Stop it!"
        play sound magical1 volume 0.3
        scene neus0_4 with dissolve        
        neus "(why does it {sc=2}{=lust_style}feel{/sc} good?)"
        if (not quest_v2 and questMain_2.completion) or (quest_v2 and questMain_v2_5.completion):            
            scene neus0_5 with dissolve
            neus "(I can't take it anymore I want to {sc=2}{=lust_style}kiss{/sc} him)"
            scene neus0_6 with dissolve
            play char1 short_kiss
            if incest_story:
                "your little sister kisses you on the lips"
            else:
                "[neusname] kisses you on the lips"
        scene black with dissolve     
        "After a while, she escapes your touch"             
        $is_touch+=1
        if quest_v2:
            if questMain_v2_5.completion:
                call addLust(2)
            else:
                call addLust(1)
            if not questSide_v2_3.completion:
                $ questSide_v2_3.completion = True
                $is_change_quest = True   
                call notify_personalized(_("Side Quest updated"))
    jump neus0
#----------------------------Level 1---------------------------------    
label neus_touch1:    
    if is_touch>1:
        scene neus1_24
        neus "Stay away (enough for today)"
    else:
        scene neus1_19 with spellfx
        neus "..."
        scene neus1_20 with dissolve
        neus "Hey!"
        play sound magical1 volume 0.3
        scene neus1_21 with dissolve        
        neus "(This {sc=2}{=lust_style}feels{/sc}...)" 
        scene neus1_22 with dissolve
        ""  
        scene neus1_23 with dissolve 
        play char1 french02 
        neus "Guuuu"   
        scene black with dissolve     
        "After a while, she escapes your touch"             
        $is_touch+=1
        if quest_v2:
            call addLust(2)
    jump neus1  
#----------------------------Level 2---------------------------------  
label neus_touch2: 
    if N_state==1:
        stop char3 fadeout 1.0
        scene black with dissolve
        if incest_story:
            neus "Brother, what are you doing?{w=0.5}{nw}"
        else:
            neus "Hey, what are you doing?{w=0.5}{nw}"
        play sound magical1 volume 0.3
        $N_state=0
        if incest_story:
            "You give your sister energy."
        else:
            "You give [neusname] energy."
        if is_sexpussy>=1:
            "She uses some of that energy to clean herself."
            $is_sexpussy=0
    else:   
        play sound magical1 volume 0.3
        scene neus2_21 with dissolve        
        neus "This {sc=2}{=lust_style}feels{/sc} good" 
        scene neus2_22 with dissolve
        play char1 french02 
        neus "Guuuu"     
        scene neus2_23 with dissolve 
        neus "More ..."     
        if is_touch<1:
            if quest_v2:
                call addLust(2)
            $is_touch+=1 
    jump neus2 

    