screen kitchen_spell:
    default statename=neus_states[N_state]
    tag spell_screen    
    vbox:
        xpos 10
        text _("Level: [kitchen_event_lvl]"):
            outlines [ (4, gui.accent_color) ]
            size 100  
        if kitchen_event_lvl>=2:          
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
            sensitive kitchen_event_lvl>0 and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level down")
            action Show("confirm",None,_("Are you sure you want to level down?"),
                [Hide("confirm"), Call("adjust_room_levels", change=-1)],Hide("confirm"))
                
        imagebutton:
            auto "btn_level_up_%s"
            insensitive "btn_lock_skil_idle"
            sensitive kitchen_event_lvl<relationship_level and item_book_magic.is_view and spell_1_1.is_active
            tooltip _("Level up")
            action Show("confirm",None,_("Are you sure you want to level up?"),
                [Hide("confirm"), Call("adjust_room_levels", change=+1)],Hide("confirm"))
    if kitchen_event_lvl<=2:
        vbox:
            xpos 10
            yalign 0.5       
            xmaximum 144
            spacing 30
            for spell in spells_action:
                if spell.level<=kitchen_event_lvl:
                    imagebutton:
                        auto spell.image at zoom_1_5
                        insensitive "btn_lock_idle"
                        sensitive spell.is_active
                        tooltip spell.name
                        action [Hide("spell_screen"),Jump("kitchen_touch%s"%kitchen_event_lvl)]
    use screen_tooltip


#----------------------------Level 0---------------------------------
label kitchen_touch0:
    if is_touch>0:
        scene kitchen0_13 with dissolve
        neus "Don't come any closer (My heart can't take it again)"
    else:
        scene kitchen0_5 with spellfx       
        if incest_story:
            neus "Brother, why are you getting so close?"
        else:
            neus "Why are you getting so close?"
        scene kitchen0_6 with dissolve
        neus "That's sexual harassment"
        play sound magical1 volume 0.3
        scene kitchen0_7 with dissolve
        neus "{sc=2}{b}{=lust_style}Hey....{/sc} (I feel strange)"
        if not quest_v2:
            menu:
                neus "Let me go."
                "Continue":
                    scene kitchen0_8 with dissolve
                    neus "(My heart is beating faster than normal and I feel weird down there)"
                    if (not quest_v2 and questMain_2.completion) or (quest_v2 and questMain_v2_5.completion):   
                        scene kitchen0_14 with dissolve
                        neus "{sc=2}{=lust_style}Mmh..{/sc}"
                        scene kitchen0_15 with dissolve
                        play char1 short_kiss
                        if incest_story:
                            "Your sister kisses you on the lips"  
                        else:
                            "[neusname] kisses you on the lips"                                   
                    scene black with dissolve
                    "After a while, she escapes your touch"
                "Leave":
                    neus "T-Thank you"
        else:
            scene kitchen0_8 with dissolve
            neus "(My heart is beating faster than normal and I feel weird down there)"
            if (not quest_v2 and questMain_2.completion) or (quest_v2 and questMain_v2_5.completion):   
                scene kitchen0_14 with dissolve
                neus "{sc=2}{=lust_style}Mmh..{/sc}"
                scene kitchen0_15 with dissolve
                play char1 short_kiss
                if incest_story:
                    "Your sister kisses you on the lips"  
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
    jump kitchen0

#----------------------------Level 1---------------------------------  
label kitchen_touch1:
    if is_touch>0:
        scene kitchen1_20 with dissolve
        neus "Get away (I feel weird when he touches me)"
    else:
        scene kitchen1_13 with spellfx       
        neus "?"
        scene kitchen1_14 with dissolve
        if incest_story:
            neus "Why do you like touching me...? I'm your sister."
        else:
            neus "Why do you like touching me...?"
        play sound magical1 volume 0.3
        scene kitchen1_15
        neus "{sc=2}{b}{=lust_style}Hmm....{/sc} (I feel a tingle)"
        if not quest_v2:
            menu:
                neus "Hey!"
                "Continue":
                    scene kitchen1_16 with dissolve
                    neus "(I can't resist)" 
                    scene kitchen1_17 with ccirclefx 
                    play char1 french01
                    neus "Guu{sc=3}{icon=icon-heart}{/sc}"
                    scene kitchen1_18 with dissolve
                    play char1 french02
                    neus "{sc=3}More{/sc} kisses"
                    scene kitchen1_19 with dissolve
                    ""
                    scene black with dissolve
                    "After a while, she escapes your touch"
                "Leave":
                    neus "Thank you"
        else:
            scene kitchen1_16 with dissolve
            neus "(I can't resist)" 
            scene kitchen1_17 with ccirclefx 
            play char1 french01
            neus "Guu{sc=3}{icon=icon-heart}{/sc}"
            scene kitchen1_18 with dissolve
            play char1 french02
            neus "{sc=3}More{/sc} kisses"
            scene kitchen1_19 with dissolve
            ""
            scene black with dissolve
            "After a while, she escapes your touch"
        $is_touch+=1 
        if quest_v2:
            call addLust(2)
    jump kitchen1
#----------------------------Level 2---------------------------------  
label kitchen_touch2:
    if N_state==1:
        stop char3 fadeout 1.0
        scene black with dissolve
        if incest_story:
            neus "Brother, what are you doing?{w=1.0}{nw}"
        else:
            neus "Hey, what are you doing?{w=1.0}{nw}"
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
        if is_touch>0:
            scene kitchen2_16 with dissolve
            neus "(Yesss)" 
        else:
            scene kitchen2_17 with dissolve
            neus "(Here we go again.)"
        play sound magical1 volume 0.3   
        scene kitchen2_18 with spellfx       
        neus "It feels so {sc=2}{b}{=lust_style}good{/sc}..."
        call splash_message(_("Moments later")) from _call_splash_message_15
        scene kitchen2_19 with dissolve
        neus "More... (more please)" 
        mc "?"
        scene kitchen2_20 with dissolve 
        neus "Nothing (You know what I said, don't play dumb)"
        if is_touch<1:
            if quest_v2:
                call addLust(2)
            $is_touch+=1 
    jump kitchen2

    
