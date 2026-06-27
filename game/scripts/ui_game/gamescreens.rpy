default times_of_day = [_('Morning'), _('Noon'), _('Afternoon'), _('Evening'), _('Night')]
default is_change_phase=True
screen ui:   
    $ time_name = times_of_day[time]         
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
                auto 'btn_neus_%s'
                action SetVariable("is_change_quest",False), Function(is_quest_change_screen, False), Jump("is_tree_spell_stats_quests")   
                tooltip _("Quests")
                               
            if is_change_quest: 
                text _("{icon=icon-info}"):
                        color "#fff"
                        size 48 
                        outlines [ (3,gui.accent_color) ] 
                        xalign 0.5
                        ypos 16                                                        
                        at text_animation_alpha 
        if quest_v2:
            if (questSide_v2_8.completion) or (questSide_v2_8.description=="''Don't split''") or (questSide_v2_8.description=="''Split personalities''"):
                vbox:
                    spacing -48
                    imagebutton:
                        auto 'btn_phase_change_%s'
                        action SetVariable("is_change_phase",False),Jump("phase_change")   
                        tooltip _("Phase change")
                                    
                    if is_change_phase: 
                        text _("{icon=icon-info}"):
                                color "#fff"
                                size 48 
                                outlines [ (3,gui.accent_color) ] 
                                xalign 0.5
                                ypos 16                                                        
                                at text_animation_alpha  
        else: 
            if (questSide_7.completion) or (questSide_7.description == "''Split personalities''") or (questSide_7.description == "''Don't split''"):
                vbox:
                    spacing -48
                    imagebutton:
                        auto 'btn_phase_change_%s'
                        action SetVariable("is_change_phase",False),Jump("phase_change")   
                        tooltip _("Phase change")
                                    
                    if is_change_phase: 
                        text _("{icon=icon-info}"):
                                color "#fff"
                                size 48 
                                outlines [ (3,gui.accent_color) ] 
                                xalign 0.5
                                ypos 16                                                        
                                at text_animation_alpha     
        imagebutton: 
            auto 'btn_clock_%s'                                    
            action If(time <4, Jump("time_advances"),
                    Show("confirm",None,_("Do you want to sleep? {color=#cc0066}(forward one day)"),
                    [Hide("confirm"),Jump("sleeping_event%s"%mc_event_lvl)],Hide("confirm")))
            tooltip _("Advance time")

    use house_room   
    text _("{size=60}{color=#cc0066}[time_name!t]{/size}")  xalign 0.99 outlines [ (3,"#000") ]
    use screen_tooltip
    
    
screen house_room(): 
    use expression "%s_room_quest"%select_room 
    use expression "%s_photo"%select_room  
    hbox:
        xalign 0.5
        ypos 830
        spacing 15
        for i in xrange(0,len(house)): 
            vbox:
                spacing -96                
                hbox:
                    spacing -64                                                                  
                    imagebutton:
                            auto house[i].icon                    
                            selected_idle house[i].icon % 'hover'
                            tooltip house[i].tooltip 
                            action SetVariable(
                                name='select_room', 
                                value=house[i].name
                                    ),Jump("rooms")
                    if house[i].name==neus_routine[time]:
                        if quest_v2:
                            if not(time==questMain_v2_select.time_event) or questMain_v2_select.place=="":
                                imagebutton:
                                    idle "icon_neus_routine"
                                    yalign 1.0
                        else:
                            if not(time==questMain_select.time_event) or questMain_select.place=="":
                                imagebutton:
                                    idle "icon_neus_routine"
                                    yalign 1.0
                if quest_v2 and questMain_v2_select.place== house[i].name and time==questMain_v2_select.time_event:
                    text _("{icon=icon-info}"):
                        color "#fff"
                        size 96 
                        outlines [ (2,gui.accent_color) ] 
                        xalign 0.5
                        ypos -48
                        at text_animation_alpha
                elif not quest_v2 and questMain_select.place== house[i].name and time==questMain_select.time_event:
                    text _("{icon=icon-info}"):
                        color "#fff"
                        size 96 
                        outlines [ (2,gui.accent_color) ] 
                        xalign 0.5
                        ypos -48
                        at text_animation_alpha
screen screen_tooltip:
    $ tooltip = GetTooltip()
    if tooltip:            
            text str(tooltip):
                xalign 0.5
                size 60
                outlines [ (2,"#000") ]     

label phase_change:
    if time < 4:         
        scene expression 'bg/bg_[select_room]_room_day.webp'
    if time >= 4:        
        scene expression 'bg/bg_[select_room]_room_night.webp'
    call screen phase_change

screen phase_change(): 
    imagebutton:
        idle "gui/overlay/confirm.png"
        action Jump("rooms") 
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
            text _("{b}Current Phase:{/b} {color=#cc0066}Normal")
        hbox:
            spacing 50
            xalign 0.5 
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
            if unlock_two_bodies:
                vbox:
                    imagebutton:
                        auto 'btn_two_bodies_phase_%s' 
                        action Jump("two_bodies_rooms")        
                    text _("{size=+40}{b}Two bodies{/b}"):
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
            at text_animation_alpha action Jump("rooms")  


  
      




        

