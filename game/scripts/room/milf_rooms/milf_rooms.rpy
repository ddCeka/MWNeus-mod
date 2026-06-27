default milf_is_change_quest=True
default milf_is_change_phase=True
default milf_is_pregnancy_stages=True
default is_milf_pregnant=False
default is_milf_pregnant_trimester=1
default is_milf_pregnant_day_count_stage_change=0
default is_milf_pregnant_day_count=0
default milf_times_of_day = [_('Morning'), _('Afternoon'), _('Evening'), _('Night')]
default is_milf_pregnant_trimester_name ='First trimester'
default milf_outfit_is_active_outfit=False
default milf_outfit_photo_count=0

default milf_time=0
label milf_rooms: 
    $ phase_selected = "milf"
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    stop music3 fadeout 1.0
    hide screen spell_screen
    if milf_time < 3:
        play ambience morning_sounds fadeout 1.0 fadein 1.0 if_changed
        scene expression 'bg/bg_milf_mc_room_day.webp'
    if milf_time >= 3:
        play ambience night_ambience fadeout 1.0 fadein 1.0 if_changed volume 0.1
        scene expression 'bg/bg_milf_mc_room_night.webp'      
    call screen milf_ui
screen  milf_ui:   
    $ time_name = milf_times_of_day[milf_time]    
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
                auto 'btn_neus_milf_%s'
                action SetVariable("milf_is_change_quest",False),Jump("milf_is_tree_spell_stats_quests")   
                tooltip _("Quests")
                               
            if milf_is_change_quest: 
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
                action SetVariable("milf_is_change_phase",False),Jump("milf_phase_change")   
                tooltip _("Phase change")
                               
            if milf_is_change_phase: 
                text "{icon=icon-info}":
                        color "#fff"
                        size 48 
                        outlines [ (3,gui.accent_color) ] 
                        xalign 0.5
                        ypos 16                                                        
                        at text_animation_alpha  
        if is_milf_pregnant:
            vbox:
                spacing -48
                imagebutton:
                    auto 'btn_pregnancy_stages_%s'
                    action SetVariable("milf_is_pregnancy_stages",False),Jump("milf_pregnancy_stages_ui")   
                    tooltip _("Pregnancy stages")
                                
                if milf_is_pregnancy_stages: 
                    text "{icon=icon-info}":
                            color "#fff"
                            size 48 
                            outlines [ (3,gui.accent_color) ] 
                            xalign 0.5
                            ypos 16                                                        
                            at text_animation_alpha   
        imagebutton: 
            auto 'btn_clock_%s'                                    
            action If(milf_time <3, Jump("milf_time_advances"),
                    Show("confirm",None,_("Do you want to sleep? {color=#cc0066}(forward one day)"),
                    [Hide("confirm"),Jump("milf_sleeping_event")],Hide("confirm")))
            tooltip _("Advance time")

    text _("{size=60}{color=#cc0066}[time_name!t]{/size}")  xalign 0.99 outlines [ (3,"#000") ]
    use milf_house_room
    use screen_tooltip
screen milf_house_room(): 
    if is_milf_pregnant_trimester==3 and is_milf_pregnant and not(milf_outfit_is_active_outfit):
        imagebutton:
            auto "btn_old_photo_s_%s"     
            action Jump("milf_outfit_unluck")
            tooltip _("Special photo")
            pos 420,780
    imagebutton:
        auto "btn_event_%s"                   
        tooltip _("Ending") 
        xpos 0
        ypos 140      
        action Jump("menu_milf_ending")
        at event_animation_ending  
    hbox:
        xalign 0.5
        ypos 830
        spacing 15  
        #-------------------kitchen-----------------
        if milf_time==0:  
            if is_milf_pregnant:
                if is_milf_pregnant_trimester==1:
                    hbox:
                        spacing -64                                                                            
                        imagebutton:
                            auto "icon_milf_kitchen_room_%s"                   
                            selected_idle "icon_milf_kitchen_room_hover"
                            tooltip _("Kitchen") 
                            action Jump("milf_event_kitchen_control")
                        text _("[milf_event_kitchen_count_normal]/2"):
                            color "#fff"
                            size 64 
                            outlines [ (2,gui.accent_color) ] 
                            yalign 1.0
                if is_milf_pregnant_trimester==2:
                    hbox:
                        spacing -64                                                                            
                        imagebutton:
                            auto "icon_milf_kitchen_room_%s"                   
                            selected_idle "icon_milf_kitchen_room_hover"
                            tooltip _("Kitchen") 
                            action Jump("milf_event_kitchen_pregnant2")
                        text _("[milf_event_kitchen_count_pregnant2]/1"):
                            color "#fff"
                            size 64 
                            outlines [ (2,gui.accent_color) ] 
                            yalign 1.0
                if is_milf_pregnant_trimester==3:
                    hbox:
                        spacing -64                                                                            
                        imagebutton:
                            auto "icon_milf_kitchen_room_%s"                   
                            selected_idle "icon_milf_kitchen_room_hover"
                            tooltip _("Kitchen") 
                            action Jump("milf_event_kitchen_pregnant3")
                        text _("[milf_event_kitchen_count_pregnant3]/1"):
                            color "#fff"
                            size 64 
                            outlines [ (2,gui.accent_color) ] 
                            yalign 1.0
            else:
                hbox:
                    spacing -64                                                                            
                    imagebutton:
                        auto "icon_milf_kitchen_room_%s"                   
                        selected_idle "icon_milf_kitchen_room_hover"
                        tooltip _("Kitchen") 
                        action Jump("milf_event_kitchen_control")
                    text _("[milf_event_kitchen_count_normal]/2"):
                        color "#fff"
                        size 64 
                        outlines [ (2,gui.accent_color) ] 
                        yalign 1.0  
        #-------------------bath-----------------          
        if milf_time==1:
            if is_milf_pregnant:
                if is_milf_pregnant_trimester==1:
                    hbox:
                        spacing -64 
                        imagebutton:
                            auto "icon_milf_bath_room_%s"                   
                            selected_idle "icon_milf_bath_room_hover"
                            tooltip _("Bath") 
                            action Jump("milf_event_bath_control")
                        text _("[milf_event_bath_count_normal]/2"):
                            color "#fff"
                            size 64 
                            outlines [ (2,gui.accent_color) ] 
                            yalign 1.0
                if is_milf_pregnant_trimester==2:
                    hbox:
                        spacing -64 
                        imagebutton:
                            auto "icon_milf_bath_room_%s"                   
                            selected_idle "icon_milf_bath_room_hover"
                            tooltip _("Bath") 
                            action Jump("milf_event_bath_pregnant2")
                        text _("[milf_event_bath_count_pregnant2]/1"):
                            color "#fff"
                            size 64 
                            outlines [ (2,gui.accent_color) ] 
                            yalign 1.0
                if is_milf_pregnant_trimester==3:
                    hbox:
                        spacing -64 
                        imagebutton:
                            auto "icon_milf_bath_room_%s"                   
                            selected_idle "icon_milf_bath_room_hover"
                            tooltip _("Bath") 
                            action Jump("milf_event_bath_pregnant3")
                        text _("[milf_event_bath_count_pregnant3]/1"):
                            color "#fff"
                            size 64 
                            outlines [ (2,gui.accent_color) ] 
                            yalign 1.0
            else:
                hbox:
                    spacing -64 
                    imagebutton:
                        auto "icon_milf_bath_room_%s"                   
                        selected_idle "icon_milf_bath_room_hover"
                        tooltip _("Bath") 
                        action Jump("milf_event_bath_control")
                    text _("[milf_event_bath_count_normal]/2"):
                        color "#fff"
                        size 64 
                        outlines [ (2,gui.accent_color) ] 
                        yalign 1.0
    #-------------------mc_evening-----------------
    if milf_time==2:
        if is_milf_pregnant:
            if is_milf_pregnant_trimester==1:  
                imagebutton:
                    auto "icon_milf_mc_eve_room_%s"   
                    focus_mask True        
                    tooltip "%s"%neusname  
                    action Jump("milf_event_mc_eve_control") 
            if is_milf_pregnant_trimester==2:  
                imagebutton:
                    auto "icon_milf_mc_eve2_room_%s"   
                    focus_mask True        
                    tooltip "%s"%neusname 
                    action Jump("milf_event_mc_eve_control_pregnant2") 
            if is_milf_pregnant_trimester==3 and is_milf_outfit_cow_nomal:  
                imagebutton:
                    auto "icon_milf_mc_eve3_room_%s"   
                    focus_mask True        
                    tooltip "%s"%neusname 
                    action Jump("milf_event_mc_eve_control_pregnant3") 
            if is_milf_pregnant_trimester==3 and not(is_milf_outfit_cow_nomal):  
                imagebutton:
                    auto "icon_milf_mc_eve3_room_outfit_cow_%s"   
                    focus_mask True        
                    tooltip "%s"%neusname  
                    action Jump("milf_event_mc_eve_control_pregnant3_outfit_cow") 
        else:          
            imagebutton:
                auto "icon_milf_mc_eve_room_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("milf_event_mc_eve_control")  
    #-------------------mc_ningt-----------------
    if milf_time==3: 
        if is_milf_pregnant:
            if is_milf_pregnant_trimester==1:
                imagebutton:
                    auto "icon_milf_mc_night_room_%s"   
                    focus_mask True        
                    tooltip "%s"%neusname 
                    action Jump("milf_event_mc_night_control") 
            if is_milf_pregnant_trimester==2:  
                imagebutton:
                    auto "icon_milf_mc_night2_room_%s"   
                    focus_mask True        
                    tooltip "%s"%neusname 
                    action Jump("milf_event_mc_night_control_pregnant2")
            if is_milf_pregnant_trimester==3:  
                imagebutton:
                    auto "icon_milf_mc_night3_room_%s"   
                    focus_mask True        
                    tooltip "%s"%neusname
                    action Jump("milf_event_mc_night_control_pregnant3")

        else:
            imagebutton:
                auto "icon_milf_mc_night_room_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("milf_event_mc_night_control")             
label milf_sleeping_event:
    $ milf_time= 0
    if is_milf_pregnant:
        if is_milf_pregnant_day_count>=4 and is_milf_pregnant_trimester<3:
            $ is_milf_pregnant_trimester+=1
            $ is_milf_pregnant_day_count=0
            scene black with dissolve
            if is_milf_pregnant_trimester==2:                
                centered "{size=+60}Second trimester{/size}"
                scene milf_pregnant_first_trimester_second with dissolve
                ""
            if is_milf_pregnant_trimester==3:                
                centered "{size=+60}Third trimester{/size}"
                scene milf_pregnant_second_trimester_third with dissolve
                ""
        if is_milf_pregnant_trimester<3:
            $ is_milf_pregnant_day_count+=1
    jump milf_rooms
label milf_phase_change:
    if milf_time < 3:         
        scene expression 'bg/bg_milf_mc_room_day.webp'
    if milf_time >= 3:        
        scene expression 'bg/bg_milf_mc_room_night.webp'
    call screen milf_phase_change
screen milf_phase_change():
    imagebutton:
        idle "gui/overlay/confirm.png"
        action Jump("milf_rooms") 
    vbox:
        spacing 50 
        xalign 0.5
        yalign 0.5
        vbox:
            label _('{color=#cc0066}{size=+40}{b}Phase change{/b}'):
                text_outlines [ (2,"#fff") ]
                xalign 0.5 
            text _("Here you can {color=#cc0066}switch{/color} between the different {color=#cc0066}phases or stages{/color} of the game."):
                outlines [ (1,"#000") ]
            text _("{b}Current Phase:{/b} {color=#cc0066}MILF")
        hbox:
            spacing 50
            xalign 0.5 
            vbox:               
                imagebutton:
                    auto 'btn_normal_phase_%s'                    
                    action Jump("rooms")              
                text _("{size=+40}{b}Normal{/b}"):                    
                    xalign 0.5                     
                    ypos -100
            if unlock_two_bodies:            
                vbox:
                    imagebutton:
                        auto 'btn_two_bodies_phase_%s' 
                        action Jump("two_bodies_rooms")        
                    text _("{size=+40}{b}Two bodies{/b}"): 
                        xalign 0.5 
                        ypos -100 
            else:
                vbox:
                    imagebutton:
                        auto 'btn_lock_phase_%s' 
                        action Jump("level3_0_div") 
                    text _("{size=+40}{b}Unlock{/b}"):
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
            elif unlock_two_bodies:
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
        at text_animation_alpha action Jump("milf_rooms")     

label milf_time_advances:
    if(milf_time<4):
        $ milf_time+= 1   
    jump milf_rooms

label milf_is_tree_spell_stats_quests:
    if milf_time < 3:         
        scene expression 'bg/bg_milf_mc_room_day.webp'
    if milf_time >= 3:        
        scene expression 'bg/bg_milf_mc_room_night.webp'
    call screen milf_is_tree_spell_stats_quests

screen milf_is_tree_spell_stats_quests():            
    add "images/treespell/tree_spell_stats_quests_back.png"  
    default select_option = quest_screen
    if is_milf_pregnant:
        default outfit_sprite_wife=  "neus_milf%s"%(is_milf_pregnant_trimester-1)
    else:
        default outfit_sprite_wife=  "neus_milf0"
    default isback = False
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
                imagebutton:                         
                    auto 'btn_config_%s'                        
                    selected_idle 'btn_config_hover'
                    insensitive "btn_lock_idle"                    
                    action SetScreenVariable(
                            name='select_option', 
                            value="confi"
                            )                               
                imagebutton:
                    xpos 349
                    auto 'btn_close_%s'                                      
                    action [Function(quest_screen_quests), Jump("milf_rooms")]   
                key "K_ESCAPE" action [Function(quest_screen_quests), Jump("milf_rooms")]                               
             
            if select_option=="quests":
                use milf_quests_all   
            if select_option=="confi":
                use milf_config_screen                    
        # middle  
        vbox:              
            xsize 600                                                                       
            add outfit_sprite_wife ypos 40                            
        #Left             
        use milf_neus_stats
        #outfit back
    imagebutton: 
        xpos 1750 
        ypos 930                            
        auto 'btn_turn_around_%s'        
        selected_idle 'btn_turn_around_hover'
        action SetScreenVariable(
                name='outfit_sprite_wife', 
                value=If(isback, outfit_sprite_wife.replace('_back',''),
                '%s_back' % outfit_sprite_wife)),SetScreenVariable(
                name='isback', 
                value=If(isback, False, True)) 
screen milf_quests_all:   
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
        spacing 10        
        text _('{b}Outfit photo:{/b} {color=#cc0066}[milf_outfit_photo_count]{/color}/1')  
        text "{b}Endings Obtained:{/b} {color=#cc0066}[endings_obtained_count]{/color}/[total_endings]"             
screen milf_neus_stats:
    vbox: 
        xpos -50          
        yalign 0.5               
        vbox:
            xsize 530 
            label _('{color=#FFFFFF}Description:')                
            if incest_story:
                text _("{color=#B2FFFF}After reconciling with herself, she developed heterochromia (different-colored eyes), and had 10 children with her brother, which caused her breast size to increase."):
                    justify True  
            else:
                text _("{color=#B2FFFF}After coming to terms with herself, she developed heterochromia (different-colored eyes), had 10 children with [firstname], which caused her breast size to increase."):
                    justify True                     
            text _("{b}Age:{/b}{color=#B2FFFF} 39")          
            text _("{b}Title:{/b}{color=#B2FFFF} Wife")  
            if is_milf_pregnant:
                text _("{b}Status:{/b}{color=#B2FFFF} Pregnant")
            else:
                text _("{b}Status:{/b}{color=#B2FFFF} Normal")
screen milf_config_screen:
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
                    textbutton "MC" action [Function(quest_screen_config), Jump("milf_name_mc")]
                    textbutton "Neus" action [Function(quest_screen_config), Jump("milf_name_neus")]            
            vbox:
                xsize 640
                label _('{color=#cc0066}{b}Pregnancy{/b}') 
                hbox:
                    textbutton _("Activate") action SetVariable("set_active_pregnancy", True)
                    textbutton _("Deactivate") action SetVariable("set_active_pregnancy", False)       
            
label milf_pregnancy_stages_ui:
    if milf_time < 3:         
        scene expression 'bg/bg_milf_mc_room_day.webp'
    if milf_time >= 3:        
        scene expression 'bg/bg_milf_mc_room_night.webp'
    $ is_milf_pregnant_day_count_stage_change = 4-is_milf_pregnant_day_count
    $ is_milf_pregnant_trimester_name = ['First trimester', 'Second trimester', 'Third trimester'][is_milf_pregnant_trimester-1]
    call screen milf_pregnancy_stages_ui
screen milf_pregnancy_stages_ui():
    imagebutton:
        idle "gui/overlay/confirm.png"
        action Jump("milf_rooms")  
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
                text _("{b}Current stage:{/b} {color=#cc0066}[is_milf_pregnant_trimester_name!t]")
                if is_milf_pregnant_trimester<3:                
                    text _("{b}Stage change:{/b}  in {color=#cc0066}[is_milf_pregnant_day_count_stage_change] days")
                else:
                    text _("{b}Stage change:{/b}  {color=#cc0066}This stage will not conclude")
                    
                         
        hbox:
            spacing 50
            xalign 0.5 
            vbox:        
                xmaximum 500  
                vbox:              
                    if is_milf_pregnant_trimester==1:              
                        imagebutton:
                            idle 'milf_pregnant_first_trimester_active'                                      
                            action NullAction()   
                    else:
                        imagebutton:
                            idle 'milf_pregnant_first_trimester_idle'                
                            action NullAction()  
                    text _("{size=+15}{b}First trimester{/b}"):                        
                        xalign 0.5 
                        ypos -75
                text _("{b}Change in events:{/b} {color=#cc0066}Dialogue"):
                    ypos -50              
            vbox: 
                xmaximum 500             
                vbox: 
                    if is_milf_pregnant_trimester==2:              
                        imagebutton:
                            idle 'milf_pregnant_second_trimester_active'                
                            action NullAction()   
                    else:
                        imagebutton:
                            idle 'milf_pregnant_second_trimester_idle'                
                            action NullAction()  
                    text _("{size=+15}{b}Second trimester{/b}"):                        
                        xalign 0.5 
                        ypos -75  
                text _("{b}Change in events:{/b} {color=#cc0066}All"):
                    ypos -50         
            vbox: 
                xmaximum 500                
                vbox:
                    if is_milf_pregnant_trimester==3:              
                        imagebutton:
                            idle 'milf_pregnant_third_trimester_active'                
                            action NullAction()   
                    else:
                        imagebutton:
                            idle 'milf_pregnant_third_trimester_idle'                
                            action NullAction()  
                    text _("{size=+15}{b}Third trimester{/b}"):                        
                        xalign 0.5 
                        ypos -75   
                text _("{b}Change in events:{/b} {color=#cc0066}All"):
                    ypos -50       
    if is_milf_pregnant_trimester <3:
        textbutton _("{size=+60}Advance stage"):  
            text_outlines [ (2,"#000") ]   
            xalign 0.5 
            yalign 0.9                        
            action Jump("milf_pregnancy_stages_advance")
    if is_milf_pregnant_trimester==3:
        textbutton _("{size=+60}Reset every stage"):  
            text_outlines [ (2,"#000") ]
            xalign 0.5
            yalign 0.9          
            action Jump("milf_pregnancy_stages_reset")
    textbutton _("{size=+60}Back"):
        text_outlines [ (2,"#000") ]
        xalign 1.0
        at text_animation_alpha action Jump("milf_rooms")   
label milf_pregnancy_stages_advance:
    $ is_milf_pregnant_trimester+=1
    $ is_milf_pregnant_day_count=0
    $ milf_time=0
    scene black with dissolve
    if is_milf_pregnant_trimester==2:        
        centered "{size=+60}Second trimester{/size}"
        scene milf_pregnant_first_trimester_second with dissolve
        ""
    if is_milf_pregnant_trimester==3:        
        centered "{size=+60}Third trimester{/size}"
        scene milf_pregnant_second_trimester_third with dissolve
        ""
    jump milf_rooms
label milf_pregnancy_stages_reset:
    scene black with dissolve
    if incest_story:
        $ menu_text = "your sister"
    else:
        $ menu_text = neusname
    menu(screen="custom_choice_long"):
        "This will remove [menu_text]'s pregnancy status, are you sure?"
        "Yes":
            $ is_milf_pregnant_trimester=1
            $ is_milf_pregnant_day_count=0
            $ milf_time=0
            $ is_milf_pregnant=False
            jump milf_rooms
        "No":
            jump milf_pregnancy_stages_ui 
label milf_name_mc:
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
    jump milf_is_tree_spell_stats_quests
label milf_name_neus:
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
    jump milf_is_tree_spell_stats_quests

label milf_outfit_unluck: 

    if selected_mode != "None":
        show  old_photo_s at left

        if selected_mode != "Fifteen": 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start    
                    $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(4, puzzle_grid_sizes["Normal"][0])       
                    $ chosen_img = "rooms/milf/milf_outfit_cow_photo.webp"                        
                    call puzzle
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump milf_rooms
        else:
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start    
                    $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(4, fifteen_grid_sizes["Normal"][0])        
                    $ chosen_img = "rooms/milf/milf_outfit_cow_photo.webp"                        
                    call fifteen_game
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump milf_rooms
        hide old_photo_s

    $ milf_outfit_is_active_outfit = True
    scene milf_outfit_cow_photo with dissolve
    if incest_story:
        centered "{size=+30}A new outfit has been unlocked for your sister"
    else:
        centered "{size=+30}A new outfit has been unlocked for [neusname]"
    $ milf_outfit_photo_count+=1
    jump milf_rooms