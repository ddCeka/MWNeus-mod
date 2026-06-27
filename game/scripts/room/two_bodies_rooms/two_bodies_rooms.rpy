default two_bodies_is_change_quest=True
default two_bodies_is_change_phase=True
default two_bodies_select_room="mc"
default two_bodies_time=0
default two_bodies_times_of_day = [_('Morning'), _('Noon'), _('Evening'), _('Night')]
default tb_is_pregnancy_stages=True
default is_tb_pregnant_start=False
default is_tb_pregnant=False
default is_tb_pregnant_trimester=1
default is_tb_pregnant_day_count_stage_change=0
default is_tb_pregnant_day_count=0
default is_tb_pregnant_trimester_name ='First trimester'
default two_bodies_outfit_is_active_outfit=False
default tb_outfit_photo_count=0

label two_bodies_rooms: 
    $ phase_selected = "two_bodies"
    $ renpy.music.set_volume(1.0,channel='music')
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    stop music3 fadeout 1.0
    hide screen spell_screen
    if two_bodies_time < 3:
        play ambience morning_sounds fadeout 1.0 fadein 1.0 if_changed volume 1.0
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_day.webp'
    if two_bodies_time >= 3:
        play ambience night_ambience fadeout 1.0 fadein 1.0 if_changed volume 0.1
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_night.webp'
    call screen two_bodies_ui

screen  two_bodies_ui:   
    $ time_name = two_bodies_times_of_day[two_bodies_time]           
    hbox:
        xpos 5
        ypos 5
        spacing 5        
        imagebutton: 
            auto 'btn_gear_%s'
            action ShowMenu() 
            tooltip _("Settings")    
        imagebutton: 
            auto 'btn_backpack_%s'
            action Show("backpack")
            tooltip _("Backpack")    
        vbox:
            spacing -48
            imagebutton:
                auto 'btn_neus_two_%s'
                action SetVariable("two_bodies_is_change_quest",False),Jump("two_bodies_is_tree_spell_stats_quests")   
                tooltip _("Quests")
                               
            if two_bodies_is_change_quest: 
                text "{icon=icon-info}":
                        color "#fff"
                        size 48 
                        outlines [ (3,gui.accent_color) ] 
                        xalign 0.5
                        ypos 16                                                        
                        at text_animation_alpha
        vbox:
            spacing -48
            imagebutton:
                auto 'btn_phase_change_%s'
                action SetVariable("two_bodies_is_change_phase",False),Jump("two_bodies_phase_change")   
                tooltip _("Phase change")
                               
            if two_bodies_is_change_phase: 
                text "{icon=icon-info}":
                        color "#fff"
                        size 48 
                        outlines [ (3,gui.accent_color) ] 
                        xalign 0.5
                        ypos 16                                                        
                        at text_animation_alpha    
        if is_tb_pregnant:
            vbox:
                spacing -48
                imagebutton:
                    auto 'btn_pregnancy_stages_%s'
                    action SetVariable("tb_is_pregnancy_stages",False),Jump("tb_pregnancy_stages_ui")   
                    tooltip _("Pregnancy stages")
                                
                if tb_is_pregnancy_stages: 
                    text "{icon=icon-info}":
                            color "#fff"
                            size 48 
                            outlines [ (3,gui.accent_color) ] 
                            xalign 0.5
                            ypos 16                                                        
                            at text_animation_alpha 
        imagebutton: 
            auto 'btn_clock_%s'                                    
            action If(two_bodies_time <3, Jump("two_bodies_time_advances"),
                    Show("confirm",None,_("Do you want to sleep? {color=#cc0066}(forward one day)"),
                    [Hide("confirm"),Jump("two_bodies_sleeping_event")],Hide("confirm")))
            tooltip _("Advance time")
    use two_bodies_house_room
    text _("{size=60}{color=#cc0066}[time_name!t]{/size}")  xalign 0.99 outlines [ (3,"#000") ]
    use two_bodies_house_room
    use screen_tooltip
screen two_bodies_house_room(): 
    use expression "two_bodies_%s_room_quest"%two_bodies_select_room    
    if  two_bodies_time<2:
        hbox:
            xalign 0.5
            ypos 830
            spacing 7
            imagebutton:
                auto "icon_two_bodies_mc_room_%s"                   
                selected_idle "icon_two_bodies_mc_room_hover"
                tooltip _("My room") 
                action SetVariable(
                                name='two_bodies_select_room', 
                                value="mc"
                                    ),Jump("two_bodies_rooms") 
            if  two_bodies_time==0:                                                                           
                imagebutton:
                    auto "icon_two_bodies_kitchen_room_%s"                   
                    selected_idle "icon_two_bodies_kitchen_room_hover"
                    tooltip _("Kitchen")
                    action SetVariable(
                                name='two_bodies_select_room', 
                                value="kitchen"
                                    ),Jump("two_bodies_rooms")
            if  two_bodies_time==1:                                                                           
                imagebutton:
                    auto "icon_two_bodies_bath_room_%s"                   
                    selected_idle "icon_two_bodies_bath_room_hover"
                    tooltip _("Bath") 
                    action SetVariable(
                                name='two_bodies_select_room', 
                                value="bath"
                                    ),Jump("two_bodies_rooms")        
label two_bodies_sleeping_event:
    if not(probability_of_pregnancy==0) and not(probability_of_pregnancy==100):
        $ probability_of_pregnancy_init_random= random.randint(20,60)
        $ probability_of_pregnancy=probability_of_pregnancy_init_random
    if is_tb_pregnant_start and not(is_tb_pregnant):
        play ambience morning_sounds if_changed
        scene two_bodies_mc_night0_36 with dissolve
        if incest_story:
            neus "Good morning, brother."
        else:
            neus "Good morning."
        scene two_bodies_mc_night0_37 with dissolve
        neus_lyra "Guess what?"
        scene two_bodies_mc_night0_38 with dissolve
        neus "You're going to be a dad."
        mc "That's great!"
        scene two_bodies_mc_night0_39 with dissolve
        neus_lyra "Hehe, I knew you'd love it."
        scene two_bodies_mc_night0_40 with dissolve
        neus_lyra "Ugh, I need to go to the bathroom—I'm feeling nauseous."
        scene two_bodies_mc_night0_41 with dissolve
        neus "Mmmm, I'm craving something, I think I’ll head to the kitchen and see what I can find."
        scene black with dissolve
        ""
        $ is_tb_pregnant=True        
    $ two_bodies_time=0
    $ is_view_tb_chess=False
    if is_tb_pregnant:
        if is_tb_pregnant_day_count>=4 and is_tb_pregnant_trimester<3:
            $ is_tb_pregnant_trimester+=1
            $ is_tb_pregnant_day_count=0
            scene black with dissolve
            if is_tb_pregnant_trimester==2:                
                centered "{size=+60}Second trimester{/size}"
                scene tb_pregnant_first_trimester_second with dissolve
                ""
            if is_tb_pregnant_trimester==3:                
                centered "{size=+60}Third trimester{/size}"
                scene tb_pregnant_second_trimester_third with dissolve
                ""
        if is_tb_pregnant_trimester<3:
            $ is_tb_pregnant_day_count+=1   
    jump two_bodies_rooms
label two_bodies_sleeping_event_call(auxtime=0):
    if not(probability_of_pregnancy==0) and not(probability_of_pregnancy==100):
        $ probability_of_pregnancy_init_random= random.randint(20,60)
        $ probability_of_pregnancy=probability_of_pregnancy_init_random
    $ two_bodies_time=auxtime
    $ is_view_tb_chess=False
    if is_tb_pregnant:
        if is_tb_pregnant_day_count>=4 and is_tb_pregnant_trimester<3:
            $ is_tb_pregnant_trimester+=1
            $ is_tb_pregnant_day_count=0
            scene black with dissolve
            if is_tb_pregnant_trimester==2:                
                centered "{size=+60}Second trimester{/size}"
                scene tb_pregnant_first_trimester_second with dissolve
                ""
            if is_tb_pregnant_trimester==3:                
                centered "{size=+60}Third trimester{/size}"
                scene tb_pregnant_second_trimester_third with dissolve
                ""
        if is_tb_pregnant_trimester<3:
            $ is_tb_pregnant_day_count+=1   
    return

label two_bodies_phase_change:
    if two_bodies_time < 3:         
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_day.webp'
    if two_bodies_time >= 3:        
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_night.webp'
    call screen two_bodies_phase_change
screen two_bodies_phase_change(): 
    imagebutton:
        idle "gui/overlay/confirm.png"
        action Jump("two_bodies_rooms")  
    vbox:
        spacing 50 
        xalign 0.5
        yalign 0.5
        vbox:
            label _('{color=#cc0066}{size=+40}{b}Phase change{/b}'):
                text_outlines [(2,"#fff")]
                xalign 0.5 
            text _("Here you can {color=#cc0066}switch{/color} between the different {color=#cc0066}phases or stages{/color} of the game.")
            text _("{b}Current Phase:{/b} {color=#cc0066}Two bodies")
        hbox:
            xalign 0.5 
            spacing 50
            vbox:               
                imagebutton:
                    auto 'btn_normal_phase_%s'                    
                    action Jump("rooms")              
                text _("{size=+40}{b}Normal{/b}"): 
                    outlines [ (2,"#000") ]                   
                    xalign 0.5                     
                    ypos -100
            if unlock_milf: 
                vbox:
                    imagebutton:
                        auto 'btn_milf_phase_%s' 
                        action Jump("milf_rooms")        
                    text _("{size=+40}{b}MILF{/b}"):
                        outlines [ (2,"#000") ] 
                        xalign 0.5 
                        ypos -100
            else:
                vbox:
                    imagebutton:
                        auto 'btn_lock_phase_%s' 
                        action Jump("level3_0_div") 
                    text _("{size=+40}{b}Unlock{/b}"):
                        outlines [ (2,"#000") ]
                        xalign 0.5 
                        ypos -100
            if unlock_nym: 
                vbox:
                    imagebutton:
                        auto 'btn_nym_phase_%s' 
                        action Jump("nym_rooms")        
                    text _("{size=+40}{b}Nymphomania{/b}"):
                        outlines [ (2,"#000") ] 
                        xalign 0.5 
                        ypos -100
            else:
                vbox:
                    imagebutton:
                        auto 'btn_lock_phase_%s' 
                        action Jump("two_bodies_personality3") 
                    text _("{size=+40}{b}Unlock{/b}"):
                        outlines [ (2,"#000") ]
                        xalign 0.5 
                        ypos -100
    textbutton _("{size=+80}Back"):
        text_outlines [ (2,"#000") ]
        xalign 1.0
        at text_animation_alpha action Jump("two_bodies_rooms")  
label two_bodies_time_advances:
    if(two_bodies_time<3):
        $ two_bodies_time+= 1  
    $ two_bodies_select_room="mc" 
    jump two_bodies_rooms

label two_bodies_is_tree_spell_stats_quests:
    if two_bodies_time < 3:         
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_day.webp'
    if two_bodies_time >= 3:        
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_night.webp'
    call screen two_bodies_is_tree_spell_stats_quests

screen two_bodies_is_tree_spell_stats_quests():    
    default select_option = quest_screen
    if is_tb_pregnant:
        default outfit_sprite_two=  "outfit_sprite_two%s"%(is_tb_pregnant_trimester-1)
    else:
        default outfit_sprite_two=  "outfit_sprite_two0"    
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
                spacing 15                                                                         
                imagebutton:
                    auto 'btn_quest_%s'                   
                    selected_idle 'btn_quest_hover'
                    action SetScreenVariable(
                                name='select_option', 
                                value="quests"
                                ) 
                vbox:
                    spacing -76   
                    if quest_v2:  
                        imagebutton:                         
                            auto 'btn_tree_spell_%s'                        
                            selected_idle 'btn_tree_spell_hover'
                            insensitive "btn_lock_idle"
                            sensitive questSide_v2_1.completion
                            action SetScreenVariable(
                                    name='select_option', 
                                    value="tree_spell"
                                    )      
                    else:                  
                        imagebutton:                         
                            auto 'btn_tree_spell_%s'                        
                            selected_idle 'btn_tree_spell_hover'
                            insensitive "btn_lock_idle"
                            sensitive questSide_1.completion
                            action SetScreenVariable(
                                    name='select_option', 
                                    value="tree_spell"
                                    )                   
                imagebutton:                         
                    auto 'btn_config_%s'                        
                    selected_idle 'btn_config_hover'
                    insensitive "btn_lock_idle"                    
                    action SetScreenVariable(
                            name='select_option', 
                            value="confi"
                            )
                                        
                imagebutton:
                    xpos 259
                    auto 'btn_close_%s'                                      
                    action [Function(quest_screen_quests), Jump("two_bodies_rooms")]
                key "K_ESCAPE" action [Function(quest_screen_quests), Jump("two_bodies_rooms")]

            if select_option=="tree_spell":                    
                use tree_spell                                   
            elif select_option=="quests":
                use two_bodies_quests_all   
            elif select_option=="confi":
                use two_bodies_config_screen                          
        # middle  
        vbox: 
            xpos 60             
            xsize 600                                                                       
            add outfit_sprite_two ypos 40                            
        #Left             
        use two_bodies_neus_stats        
    
    #outfit back
    imagebutton: 
        xpos 1750 
        ypos 930                            
        auto 'btn_turn_around_%s'        
        selected_idle 'btn_turn_around_hover'
        action SetScreenVariable(
                name='outfit_sprite_two', 
                value=If(isback, outfit_sprite_two.replace('_back',''),
                '%s_back' % outfit_sprite_two)),SetScreenVariable(
                name='isback', 
                value=If(isback, False, True)) 
    if not(is_tb_pregnant):
        imagebutton:
            idle 'icon_chance_pregnancy'                                      
            action NullAction()
            xalign 0.85
            yalign 0.92
        hbox:  
            xsize 150         
            xalign 0.86
            yalign 0.795                    
            text _("%s%%")%(probability_of_pregnancy):
                outlines [ (4, gui.accent_color) ]
                xalign 0.5
screen two_bodies_neus_stats:
    vbox:                  
        yalign 0.5
        spacing 30
        if isback:
            vbox:                    
                xsize 470           
                label _('{color=#FFFFFF}P Points')                    
                text _("{b}Love:{/b}{color=#B2FFFF} [neus_love_hide]")
                text _("{b}Lust:{/b}{color=#B2FFFF} [neus_lust]")                
                text _("{b}[neus_obsession_name!t]{/b}{color=#B2FFFF} [neus_obsession]")                                      
        else:
            vbox:
                xpos 10
                xsize 470 
                label _('{color=#FFFFFF}Description:')                
                text _("{color=#B2FFFF}In a failed attempt to contain her obsession, she developed a second personality."):
                    justify True                   
                text _("{b}Age:{/b}{color=#B2FFFF} [neus_age]")          
                text _("{b}Title:{/b}{color=#B2FFFF} [neus_title!t]")
                text _("{b}Relationship level:{/b}{color=#B2FFFF} 4")
                if is_tb_pregnant:
                    text _("{b}Status:{/b}{color=#B2FFFF} Pregnant")
                else:
                    text _("{b}Status:{/b}{color=#B2FFFF} Normal")             

screen two_bodies_config_screen:
    vpgrid:
        cols 1
        spacing 30  
        ysize 545        
        allow_underfull True  
        scrollbars "vertical"
        draggable True
        mousewheel True
        vbox:  
            spacing 30
            ysize 545          
            vbox:
                xsize 640
                label _('{color=#cc0066}{b}Change names{/b}') 
                hbox:
                    textbutton "MC" action [Function(quest_screen_config), Jump("two_bodies_name_mc")]
                    textbutton "Neus" action [Function(quest_screen_config), Jump("two_bodies_name_neus")]
                    textbutton "Lyra" action [Function(quest_screen_config), Jump("two_bodies_name_lyra")]
                    
            vbox:
                xsize 640
                label _('{color=#cc0066}{b}Pregnancy{/b}') 
                hbox:
                    textbutton _("Activate") action SetVariable("set_active_pregnancy", True)
                    textbutton _("Deactivate") action SetVariable("set_active_pregnancy", False)               
                
            vbox:
                xsize 640            
                label _('{color=#cc0066}{b}Probability of pregnancy{/b}') 
                hbox:
                    textbutton _("100%"):
                        sensitive spell_3_1.is_active
                        action SetVariable("probability_of_pregnancy", 100)
                    textbutton _("[probability_of_pregnancy_init_random]%"):
                        action SetVariable("probability_of_pregnancy", probability_of_pregnancy_init_random)
                    textbutton _("0%"):
                        sensitive spell_3_1.is_active
                        action SetVariable("probability_of_pregnancy", 0)                
screen two_bodies_quests_all:   
    default auxSide=0
    vbox:        
        spacing 30
        ysize 545
        vbox:
            xsize 640
            label _('{color=#cc0066}{size=+10}{b}Main quests{/b}')            
            text _("Enjoy the events or start the {color=#cc0066}Ending{/color} for this {color=#cc0066}phase{/color}.") 
        vbox:
            xsize 640
            label _('{color=#0b2ecb}{size=+10}{b}Side quests{/b}')
            if not(tb_side_quests1):
                text _("In {color=#cc0066}your room{/color}, select the option ''Another personality, again?''")
            else:
                text _("All the side quests have been completed for this phase.")
    vbox:
        xsize 640
        spacing 10        
        text _('{b}Outfit photo:{/b} {color=#cc0066}[tb_outfit_photo_count]{/color}/1')   
        text "{b}Endings Obtained:{/b} {color=#cc0066}[endings_obtained_count]{/color}/[total_endings]"    
label tb_pregnancy_stages_ui:
    if two_bodies_time < 3:         
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_day.webp'
    if two_bodies_time >= 3:        
        scene expression 'bg/bg_two_bodies_[two_bodies_select_room]_room_night.webp'
    $ is_tb_pregnant_day_count_stage_change = 4-is_tb_pregnant_day_count
    $ is_tb_pregnant_trimester_name = [_('First trimester'), _('Second trimester'), _('Third trimester')][is_tb_pregnant_trimester-1]
    call screen tb_pregnancy_stages_ui
screen tb_pregnancy_stages_ui():
    imagebutton:
        idle "gui/overlay/confirm.png"
        action Jump("two_bodies_rooms")  
    vbox:         
        xalign 0.5
        spacing 20
        vbox:
            xalign 0.5
            label _('{color=#cc0066}{size=+40}{b}Pregnancy stages{/b}'):
                text_outlines [ (2,"#fff") ]
                xalign 0.5
            hbox:
                spacing 20
                text _("{b}Current stage:{/b} {color=#cc0066}[is_tb_pregnant_trimester_name!t]")
                if is_tb_pregnant_trimester<3:                
                    text _("{b}Stage change:{/b}  in {color=#cc0066}[is_tb_pregnant_day_count_stage_change] days")
                else:
                    text _("{b}Stage change:{/b}  {color=#cc0066}This stage will not conclude")
                    
                         
        hbox:
            spacing 50
            xalign 0.5 
            vbox:        
                xmaximum 500  
                vbox:              
                    if is_tb_pregnant_trimester==1:              
                        imagebutton:
                            idle 'tb_pregnant_first_trimester_active'                                      
                            action NullAction()   
                    else:
                        imagebutton:
                            idle 'tb_pregnant_first_trimester_idle'                
                            action NullAction()  
                    text _("{size=+15}{b}First trimester{/b}"):                        
                        xalign 0.5 
                        ypos -75
                text _("{b}Change in events:{/b} {color=#cc0066}Dialogue"):
                    ypos -50              
            vbox: 
                xmaximum 500             
                vbox: 
                    if is_tb_pregnant_trimester==2:              
                        imagebutton:
                            idle 'tb_pregnant_second_trimester_active'                
                            action NullAction()   
                    else:
                        imagebutton:
                            idle 'tb_pregnant_second_trimester_idle'                
                            action NullAction()  
                    text _("{size=+15}{b}Second trimester{/b}"):                        
                        xalign 0.5 
                        ypos -75  
                text _("{b}Change in events:{/b} {color=#cc0066}All"):
                    ypos -50         
            vbox: 
                xmaximum 500                
                vbox:
                    if is_tb_pregnant_trimester==3:              
                        imagebutton:
                            idle 'tb_pregnant_third_trimester_active'                
                            action NullAction()   
                    else:
                        imagebutton:
                            idle 'tb_pregnant_third_trimester_idle'                
                            action NullAction()  
                    text _("{size=+15}{b}Third trimester{/b}"):                        
                        xalign 0.5 
                        ypos -75   
                text _("{b}Change in events:{/b} {color=#cc0066}All"):
                    ypos -50       
    if is_tb_pregnant_trimester <3:
        textbutton _("{size=+60}Advance stage"):  
            text_outlines [ (2,"#000") ]   
            xalign 0.5 
            yalign 0.9                        
            action Jump("tb_pregnancy_stages_advance")
    if is_tb_pregnant_trimester==3:
        textbutton _("{size=+60}Reset every stage"):  
            text_outlines [ (2,"#000") ]
            xalign 0.5
            yalign 0.9          
            action Jump("tb_pregnancy_stages_reset")
    textbutton _("{size=+60}Back"):
        text_outlines [ (2,"#000") ]
        xalign 1.0
        at text_animation_alpha action Jump("two_bodies_rooms")
label tb_pregnancy_stages_advance:
    $ two_bodies_select_room="mc"
    $ is_tb_pregnant_trimester+=1
    $ is_tb_pregnant_day_count=0
    $ two_bodies_time=0
    scene black with dissolve
    if is_tb_pregnant_trimester==2:        
        centered "{size=+60}Second trimester{/size}"
        scene tb_pregnant_first_trimester_second with dissolve
        ""
    if is_tb_pregnant_trimester==3:        
        centered "{size=+60}Third trimester{/size}"
        scene tb_pregnant_second_trimester_third with dissolve
        ""
    jump two_bodies_rooms
label tb_pregnancy_stages_reset:
    scene black with dissolve
    if incest_story:
        $ menu_text = "your sister"
    else:
        $ menu_text = neusname
    menu(screen="custom_choice_long"):
        "This will remove [menu_text]'s pregnancy status, are you sure?"
        "Yes":
            $ is_tb_pregnant_trimester=1
            $ is_tb_pregnant_day_count=0
            $ two_bodies_time=0
            $ is_tb_pregnant=False
            $ is_tb_pregnant_start=False
            jump two_bodies_rooms
        "No":
            jump tb_pregnancy_stages_ui 
label two_bodies_name_mc:
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
    jump two_bodies_is_tree_spell_stats_quests
label two_bodies_name_neus:
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
    jump two_bodies_is_tree_spell_stats_quests
label two_bodies_name_lyra:
    scene lyra_name with dissolve
    if persistent.gallery_lyra != "Lyra":
        $ neusname_lyra = renpy.input(_("What is the name of your [friend_sister]'s second personality? (Default: Lyra)"), default=persistent.gallery_lyra, exclude='\\[{')
    else:
        $ neusname_lyra = renpy.input(_("What is the name of your [friend_sister]'s second personality? (Default: Lyra)"), exclude='\\[{') 
    $ neusname_lyra = neusname_lyra.title()
    $ neusname_lyra = neusname_lyra.strip()
    if neusname_lyra == "":
        $ neusname_lyra = "Lyra" 
    $ persistent.gallery_lyra = neusname_lyra
    jump two_bodies_is_tree_spell_stats_quests

label two_bodies_outfit_unluck: 

    if selected_mode != "None":
        show  old_photo_s at left

        if selected_mode != "Fifteen": 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start    
                    $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(4, puzzle_grid_sizes["Normal"][0])       
                    $ chosen_img = "rooms/tb/mc/two_bodies_outfit_cat_photo.webp"                        
                    call puzzle
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump two_bodies_rooms
        else:
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start    
                    $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(4, fifteen_grid_sizes["Normal"][0])       
                    $ chosen_img = "rooms/tb/mc/two_bodies_outfit_cat_photo.webp"                        
                    call fifteen_game
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump two_bodies_rooms
        hide old_photo_s 

    $ two_bodies_outfit_is_active_outfit = True
    scene two_bodies_outfit_cat_photo with dissolve
    if incest_story:
        centered "{size=+30}A new outfit has been unlocked for your sister"
    else:
        centered "{size=+30}A new outfit has been unlocked for [neusname] and [neus_lyra]"
    $ tb_outfit_photo_count+=1
    jump two_bodies_rooms