default nym_is_change_quest=True
default nym_is_change_phase=True
default nym_time=0
default nym_times_of_day = [_('Day'),_('Night')]
default nym_outfit_is_active_outfit=False
default nym_outfit_photo_count=0
default is_view_intro_nym_outfit=False
default is_nym_outfit=False
default nym_tired=False
label nym_rooms: 
    $ phase_selected = "nym"
    $ renpy.music.set_volume(1.0,channel='music')
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    stop music3 fadeout 1.0
    hide screen spell_screen
    if nym_time < 1:
        play ambience morning_sounds fadeout 1.0 fadein 1.0 if_changed volume 1.0 
        scene expression 'bg/bg_nym_mc_room_day.webp'
    if nym_time >= 1:
        play ambience night_ambience fadeout 1.0 fadein 1.0 if_changed volume 0.1
        scene expression 'bg/bg_nym_mc_room_night.webp'      
    call screen nym_ui

screen  nym_ui:   
    $ time_name = nym_times_of_day[nym_time]    
    use nym_house_room       
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
                auto 'btn_neus_nym_%s'
                action SetVariable("nym_is_change_quest",False),Jump("nym_is_tree_spell_stats_quests")   
                tooltip _("Quests")
                               
            if nym_is_change_quest: 
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
                action SetVariable("nym_is_change_phase",False),Jump("nym_phase_change")   
                tooltip _("Phase change")
                               
            if nym_is_change_phase: 
                text "{icon=icon-info}":
                        color "#fff"
                        size 48 
                        outlines [ (3,gui.accent_color) ] 
                        xalign 0.5
                        ypos 16                                                        
                        at text_animation_alpha     
        imagebutton: 
            auto 'btn_clock_%s'                                    
            action If(nym_time <1, Jump("nym_time_advances"),
                    Show("confirm",None,_("Do you want to sleep? {color=#cc0066}(forward one day)"),
                    [Hide("confirm"),Jump("nym_sleeping_event")],Hide("confirm")))
            tooltip _("Advance time")
    
    text _("{size=60}{color=#cc0066}[time_name!t]{/size}")  xalign 0.99 outlines [ (3,"#000") ]
    use screen_tooltip
screen nym_house_room(): 
    if not(nym_outfit_is_active_outfit):
        imagebutton:
            auto "btn_old_photo_s_%s"     
            action Jump("nym_outfit_unluck")
            tooltip _("Special photo")
            pos 600,620
    imagebutton:
        auto "btn_event_%s"                   
        tooltip _("Ending") 
        xpos 0
        ypos 140      
        action Jump("menu_nym_ending")
        at event_animation_ending 
    if nym_time==0:
        if not(is_nym_outfit) and not(nym_tired):
            imagebutton:
                auto "nym_day_0_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("nym_event_day_control") 
        if not(is_nym_outfit) and nym_tired:
            imagebutton:
                auto "nym_day_126_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("nym_event_day_control_tired") 
        if is_nym_outfit and not(nym_tired):
            imagebutton:
                auto "nym_day_78_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("nym_event_day_control_outfit")
        if is_nym_outfit and nym_tired:
            imagebutton:
                auto "nym_day_127_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("nym_event_day_control_outfit_tired")
    if nym_time==1:
        if not(nym_tired):
            imagebutton:
                auto "nym_night_0_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("nym_event_night_control") 
        else:
            imagebutton:
                auto "nym_night_1_%s"   
                focus_mask True        
                tooltip "%s"%neusname 
                action Jump("nym_event_night_control_tired") 

label nym_phase_change:
    if nym_time < 1:         
        scene expression 'bg/bg_nym_mc_room_day.webp'
    if nym_time >= 1:        
        scene expression 'bg/bg_nym_mc_room_night.webp'
    call screen nym_phase_change
screen nym_phase_change(): 
    imagebutton:
        idle "gui/overlay/confirm.png"
        action Jump("nym_rooms")  
    vbox:
        spacing 50 
        xalign 0.5
        yalign 0.5
        vbox:
            label _('{color=#cc0066}{size=+40}{b}Phase change{/b}'):
                text_outlines [(2,"#fff")]
                xalign 0.5 
            text _("Here you can {color=#cc0066}switch{/color} between the different {color=#cc0066}phases or stages{/color} of the game.")
            text _("{b}Current Phase:{/b} {color=#cc0066}Nymphomania")
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
            vbox:
                imagebutton:
                    auto 'btn_two_bodies_phase_%s' 
                    action Jump("two_bodies_rooms")        
                text _("{size=+40}{b}Two bodies{/b}"): 
                    xalign 0.5 
                    ypos -100
    textbutton _("{size=+80}Back"):
        text_outlines [ (2,"#000") ]
        xalign 1.0
        at text_animation_alpha action Jump("nym_rooms")  
label nym_time_advances:
    if(nym_time<1):
        $ nym_time+= 1   
    jump nym_rooms

label nym_is_tree_spell_stats_quests:
    if time < 4:         
        scene expression 'bg/bg_nym_mc_room_day.webp'
    if time >= 4:        
        scene expression 'bg/bg_nym_mc_room_night.webp'
    call screen nym_is_tree_spell_stats_quests

screen nym_is_tree_spell_stats_quests():   
    add "images/treespell/tree_spell_stats_quests_back.png"  
    default select_option = quest_screen
    default outfit_sprite_nym=  "neus_nym"
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
                    action [Function(quest_screen_quests), Jump("nym_rooms")]
                key "K_ESCAPE" action [Function(quest_screen_quests), Jump("nym_rooms")]
             
            if select_option=="quests":
                use nym_quests_all   
            if select_option=="confi":
                use nym_config_screen                    
        # middle  
        vbox:              
            xsize 1000 
            xalign 0.5
            add outfit_sprite_nym ypos 40 xpos 100
    imagebutton: 
        xpos 1750 
        ypos 930                            
        auto 'btn_turn_around_%s'        
        selected_idle 'btn_turn_around_hover'
        action SetScreenVariable(
                name='outfit_sprite_nym', 
                value=If(isback, outfit_sprite_nym.replace('_back',''),
                '%s_back' % outfit_sprite_nym)),SetScreenVariable(
                name='isback', 
                value=If(isback, False, True))
screen nym_quests_all:
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
        text _('{b}Outfit photo:{/b} {color=#cc0066}[nym_outfit_photo_count]{/color}/1') 
        text "{b}Endings Obtained:{/b} {color=#cc0066}[endings_obtained_count]{/color}/[total_endings]"
screen nym_config_screen:
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
                    textbutton "MC" action [Function(quest_screen_config), Jump("nym_name_mc")]
                    textbutton "Neus" action [Function(quest_screen_config), Jump("nym_name_neus")]
                    textbutton "Lyra" action [Function(quest_screen_config), Jump("nym_name_lyra")]
                    textbutton "Sylvia" action [Function(quest_screen_config), Jump("nym_name_sylvia")]             
            vbox:
                xsize 640
                label _('{color=#cc0066}{b}Pregnancy{/b}') 
                hbox:
                    textbutton _("Activate") action SetVariable("set_active_pregnancy", True)
                    textbutton _("Deactivate") action SetVariable("set_active_pregnancy", False)    
label nym_name_mc:
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
    jump nym_is_tree_spell_stats_quests
label nym_name_neus:
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
    jump nym_is_tree_spell_stats_quests
label nym_name_lyra:
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
    jump nym_is_tree_spell_stats_quests
label nym_name_sylvia:
    scene sylvia_name with dissolve
    if persistent.gallery_sylvia != "Sylvia":
        $ neusname_sylvia = renpy.input(_("What is the name of your [friend_sister]'s third personality? (Default: Sylvia)"), default=persistent.gallery_sylvia, exclude='\\[{') 
    else:
        $ neusname_sylvia = renpy.input(_("What is the name of your [friend_sister]'s third personality? (Default: Sylvia)"), exclude='\\[{') 
    $ neusname_sylvia = neusname_sylvia.title()
    $ neusname_sylvia = neusname_sylvia.strip()
    if neusname_sylvia == "":
        $ neusname_sylvia = "Sylvia" 
    $ persistent.gallery_sylvia = neusname_sylvia
    jump nym_is_tree_spell_stats_quests
label nym_sleeping_event:
    $ nym_time=0
    $ nym_tired=False
    jump nym_rooms

label nym_outfit_unluck: 

    if selected_mode != "None":
        show  old_photo_s at left

        if selected_mode != "Fifteen": 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start    
                    $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(4, puzzle_grid_sizes["Normal"][0])       
                    $ chosen_img = "rooms/nym/nym_outfit_photo.webp"                        
                    call puzzle
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump nym_rooms
        else: 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start    
                    $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(4, fifteen_grid_sizes["Normal"][0])    
                    $ chosen_img = "rooms/nym/nym_outfit_photo.webp"                        
                    call fifteen_game
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump nym_rooms
        hide old_photo_s 

    $ nym_outfit_is_active_outfit = True
    scene nym_outfit_photo with dissolve
    if incest_story:
        centered "{size=+30}New outfits have been unlocked for your sister"
    else:
        centered "{size=+30}New outfits have been unlocked for [neusname], [neus_lyra] and [neus_sylvia]"
    $ nym_outfit_photo_count+=1
    jump nym_rooms