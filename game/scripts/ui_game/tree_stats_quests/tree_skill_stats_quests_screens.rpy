label is_tree_spell_stats_quests:
    if time < 4:         
        scene expression 'bg/bg_[select_room]_room_day.webp'
    if time >= 4:        
        scene expression 'bg/bg_[select_room]_room_night.webp'
    call screen is_tree_spell_stats_quests
    jump is_tree_spell_stats_quests


init python:
    def btn_tree_spell():
        renpy.store.is_change_tree_skill = False
    def is_quest_change(value):
        renpy.store.is_change_quest = value
    def is_quest_change_screen(value):
        renpy.store.is_change_quest_screen = value
    def quest_screen_quests():
        renpy.store.quest_screen = "quests"
    def quest_screen_spells():
        renpy.store.quest_screen = "tree_spell"
    def quest_screen_config():
        renpy.store.quest_screen = "confi"

screen is_tree_spell_stats_quests():

    default select_option = quest_screen

    if relationship_level==2:
        default outfit_sprite=  "neus_casual%s_%s"%(relationship_level,N_state)
    else: 
        default outfit_sprite=  "neus_casual%s_0"%relationship_level
    default isback = False          
    add "images/treespell/tree_spell_stats_quests_back.png"  
    add particles_sprite                 
    hbox:
        spacing 50                       
        vbox:
            xsize 680                                
            xpos 70
            ypos 15
            spacing 20
            hbox:                     
                spacing 10    
                vbox:       
                    spacing -86                                                                   
                    imagebutton:
                        auto 'btn_quest_%s'                   
                        selected_idle 'btn_quest_hover'
                        action [SetScreenVariable(
                                    name='select_option', 
                                    value="quests"
                                    ), Function(is_quest_change_screen, False), Function(is_quest_change, False)] 
                    if quest_v2:
                        if is_change_quest_screen and questSide_v2_2.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                    else:
                        if is_change_quest_screen and questSide_2.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                vbox:
                    spacing -83      
                    if quest_v2:
                        imagebutton:                         
                            auto 'btn_tree_spell_%s'                        
                            selected_idle 'btn_tree_spell_hover'
                            insensitive "btn_lock_idle"
                            sensitive questSide_v2_1.completion
                            action [SetScreenVariable(
                                    name='select_option', 
                                    value="tree_spell"
                                    ),Function(btn_tree_spell)]
                    else:               
                        imagebutton:                         
                            auto 'btn_tree_spell_%s'                        
                            selected_idle 'btn_tree_spell_hover'
                            insensitive "btn_lock_idle"
                            sensitive questSide_1.completion
                            action [SetScreenVariable(
                                    name='select_option', 
                                    value="tree_spell"
                                    ),Function(btn_tree_spell)]
                    if quest_v2:
                        if is_change_tree_skill and questSide_v2_1.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                    else:
                        if is_change_tree_skill and questSide_1.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                imagebutton:                         
                    auto 'btn_config_%s'                        
                    selected_idle 'btn_config_hover'
                    insensitive "btn_lock_idle"                    
                    action SetScreenVariable(
                            name='select_option', 
                            value="confi"
                            )
                                        
                imagebutton:
                    xpos 254
                    auto 'btn_close_%s'                                      
                    action [Function(quest_screen_quests), Jump("rooms")]
                key "K_ESCAPE" action [Function(quest_screen_quests), Jump("rooms")]
            if select_option=="tree_spell":                    
                use tree_spell                                   
            elif select_option=="quests":
                use quests_all   
            elif select_option=="confi":
                use config_screen
                          
        # middle  
        vbox:              
            xsize 600                                                                       
            add outfit_sprite ypos 40                            
        #Left             
        use neus_stats        
    
    #outfit back
    imagebutton: 
        xpos 1750 
        ypos 930                            
        auto 'btn_turn_around_%s'        
        selected_idle 'btn_turn_around_hover'
        action SetScreenVariable(
                name='outfit_sprite', 
                value=If(isback, outfit_sprite.replace('_back',''),
                '%s_back' % outfit_sprite)),SetScreenVariable(
                name='isback', 
                value=If(isback, False, True)) 
                                  
                
screen neus_stats:
    default statename=neus_states[N_state]
    vbox: 
        xpos -50          
        yalign 0.5
        spacing 30
        if isback:
            vbox:                    
                xsize 530           
                label _('{color=#FFFFFF}P Points')                    
                text _("{b}Love:{/b}{color=#B2FFFF} [neus_love_hide]")
                text _("{b}[neus_obsession_name!t]{/b}{color=#B2FFFF} [neus_obsession]")  
                text _("{b}Spanking Level:{/b}{color=#B2FFFF} [spanking_level]/2")                             
        else:
            vbox:
                xsize 530 
                label _('{color=#FFFFFF}Description:')        
                if incest_story:
                    text _("{color=#B2FFFF}From the moment she was born, [neusname]'s world has revolved around [firstname], her older brother. Though they occasionally bicker, they share a deep bond. With her brother’s home conveniently near her university, moving in with him was the perfect option.")
                else:        
                    text _("{color=#B2FFFF}She's known [firstname] since age 12. They have occasional fights, but generally, they get along well. Her family is middle class. To save on rent money, she moved in with [firstname] when she entered university."):
                        justify True                     
                text _("{b}Age:{/b}{color=#B2FFFF} [neus_age]")          
                text _("{b}Title:{/b}{color=#B2FFFF} [neus_title!t]")
                text _("{b}Relationship level:{/b}{color=#B2FFFF} [relationship_level]/?") 
                text _("{b}Lust:{/b}{color=#B2FFFF} [neus_lust]")               
                if relationship_level>=2:
                    text _("{b}State:{/b}{color=#B2FFFF} [statename!t]")

screen config_screen:
    vpgrid:
        cols 1
        spacing 30                
        allow_underfull True        
        draggable True
        mousewheel True
        vbox:  
            spacing 30                     
            vbox:
                xsize 640
                label _('{color=#cc0066}{b}Change names{/b}') 
                hbox:
                    textbutton _("MC") action [Function(quest_screen_config), Jump("name_mc")]
                    textbutton _("Neus") action [Function(quest_screen_config), Jump("name_neus")]
                    
            vbox:
                xsize 640
                label _('{color=#cc0066}{b}Pregnancy Content{/b}') 
                hbox:
                    if set_active_pregnancy:
                        textbutton _("Enabled") action SetVariable("set_active_pregnancy", not set_active_pregnancy)
                    else:
                        textbutton _("Disabled") action SetVariable("set_active_pregnancy", not set_active_pregnancy)
label name_mc:
    scene black
    if persistent.gallery_firstname != "Neron":
        $ firstname = renpy.input(_("What is your name? (Default: Neron)"), default=persistent.gallery_firstname, exclude='\\[{') 
    else:
        $ firstname = renpy.input(_("What is your name? (Default: Neron)"), exclude='\\[{') 
    $ firstname = firstname.title()
    $ firstname = firstname.strip()   
    if firstname == "":
        $ firstname = "Neron" 
    $ persistent.gallery_firstname = firstname
    jump is_tree_spell_stats_quests
label name_neus:
    scene neus_name with dissolve
    if persistent.gallery_neusname != "Neus":
        $ neusname = renpy.input(_("What is your [friend_sister]'s name? (Default: Neus)"), default=persistent.gallery_neusname, exclude='\\[{') 
    else:
        $ neusname = renpy.input(_("What is your [friend_sister]'s name? (Default: Neus)"), exclude='\\[{') 
    $ neusname = neusname.title()
    $ neusname = neusname.strip()
    if neusname == "":
        $ neusname = "Neus" 
    $ persistent.gallery_neusname = neusname
    jump is_tree_spell_stats_quests
        