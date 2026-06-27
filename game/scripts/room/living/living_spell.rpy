screen living_spell:
    default statename=neus_states[N_state]
    tag spell_screen
    vbox:
        xpos 10
        text _("Level: [living_event_lvl]"):
            outlines [ (4, gui.accent_color) ]
            size 100  
        if living_event_lvl>=2:          
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
            sensitive living_event_lvl>0 and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level down")
            action Show("confirm",None,_("Are you sure you want to level down?"),
                [Hide("confirm"), Call("adjust_room_levels", change=-1)],Hide("confirm"))
                
        imagebutton:
            auto "btn_level_up_%s"
            insensitive "btn_lock_skil_idle"
            sensitive living_event_lvl<relationship_level and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level up")
            action Show("confirm",None,_("Are you sure you want to level up?"),
                [Hide("confirm"), Call("adjust_room_levels", change=+1)],Hide("confirm")) 
    if  living_event_lvl<=2:   
        vbox:
            xpos 10
            yalign 0.5       
            xmaximum 138
            spacing 30
            for spell in spells_action:
                if spell.level<=living_event_lvl:
                    imagebutton:
                        auto spell.image at zoom_1_5
                        insensitive "btn_lock_idle"
                        sensitive spell.is_active
                        tooltip spell.name
                        action [Hide("spell_screen"),Jump("living_touch%s"%living_event_lvl)]
    use screen_tooltip 
#----------------------------Level 0---------------------------------
label living_touch0:    
    if is_touch>0:
        scene living0_13 with dissolve
        neus "Don't come close (My heart can't take it again)"
    else:
        scene living0_5 with spellfx
        neus "Mmm" 
        scene living0_6 with dissolve
        if incest_story:
            neus "What do you want brother?"
        else:
            neus "What do you want?"
        scene living0_7   
        neus "Hey, let me go."
        play sound magical1 volume 0.3       
        scene living0_8 with dissolve        
        neus "(I {sc=2}{=lust_style}feel{/sc} strange)"
        if (not quest_v2 and questMain_2.completion) or (quest_v2 and questMain_v2_5.completion):   
            scene living0_14 with dissolve
            neus "{sc=2}{=lust_style}Mmm{/sc}"
            scene living0_15 with dissolve
            play char1 short_kiss
            ""            
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
    jump living0
#----------------------------Level 1---------------------------------
label living_touch1:    
    if is_touch>0:
        scene living1_19 with dissolve
        neus "Stay away"
    else:
        scene living1_14 with spellfx
        neus "Hmm" 
        scene living1_15 with dissolve
        if incest_story:
            neus "Hey! Brother, what are you doing?"  
        else:
            neus "Hey! What are you doing?"        
        play sound magical1 volume 0.3       
        scene living1_16 with dissolve        
        neus "(I {sc=2}{=lust_style}feel{/sc} strange)"
        scene living1_17 with dissolve        
        neus "{sc=3}Haa{/sc}"
        scene living1_18 with dissolve
        play char1 french02 
        neus "{sc=3}Guuuuuh{/sc}"       
        scene black with dissolve     
        "After a while, she escapes your touch" 
        $is_touch+=1    
        if quest_v2:
            call addLust(2)
    jump living1
#----------------------------Level 2---------------------------------
label living_touch2: 
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
        scene living2_14 with dissolve
        neus "(Here we go again.)"
        play sound magical1 volume 0.3
        scene living2_15 with spellfx
        play char1 short_kiss
        neus "Uhmm"    
        scene living2_16 with dissolve
        play char1 french01
        neus "More ..."
        scene living2_17 with dissolve
        neus "More ..."    
        scene living2_18 with dissolve
        neus "(Is it over already?)"    
        if is_touch<1:
            if quest_v2:
                call addLust(2)
            $is_touch+=1 
    jump living2

    