label rooms: 
    call neus_quest_routine
    $ phase_selected = "normal"
    stop ambience fadeout 1.0
    stop music2 fadeout 1.0
    stop music3 fadeout 1.0
    hide screen spell_screen    
    if quest_v2 and questMain_v2_select.place==select_room and time==questMain_v2_select.time_event:     
        jump expression questMain_v2_select.label_event   
    elif not quest_v2 and questMain_select.place==select_room and time==questMain_select.time_event:
        jump expression questMain_select.label_event
    if select_room == "neus" and neus_routine[time] == "neus" and ((neus_event_lvl <= 0) or (neus_event_lvl == 1 and not neus_room_unlocked)):
        jump neus_hallway
    if select_room=="bath"and neus_routine[time]=="bath" and bath_event_lvl<2:
        if quest_v2:
            if not(time==questMain_v2_select.time_event) or not(select_room==neus_routine[time]):
                jump bath_hallway
        else:
            if not(time==questMain_select.time_event) or not(select_room==neus_routine[time]):
                jump bath_hallway

    call rooms_background

    call rooms_music
    
    if neus_event_lvl == 1 and time == 3 and select_room=="neus"and neus_routine[time]=="neus" and neus_room_unlocked and not(is_view_key_room_neus):
        show neus1_0_idle
        pause 1.0
        jump neus1

    call screen ui

label rooms_background:
    if time < 4:
        scene expression 'bg/bg_[select_room]_room_day.webp'
    elif time >= 4:
        scene expression 'bg/bg_[select_room]_room_night.webp' 
    return

label rooms_music:
    stop char3 fadeout 1.0
    if time < 4:
        play music [Lobby_Time,Cipher] fadeout 1.0 fadein 1.0 if_changed volume 0.1 
    elif time >= 4 and ((select_room != "neus") or (select_room == "neus" and neus_routine[time] != "neus")):
        play music lazy_night fadeout 1.0 fadein 1.0 if_changed volume 0.2
    elif time >= 4 and select_room == "neus" and neus_routine[time] == "neus":
        stop music fadeout 1.0
    return

label neus_quest_routine:
    if not quest_v2:
        if questMain_9.completion:
            $ neus_routine = ["kitchen","living","bath","neus","neus"]
        else:
            if not questMain_1.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_1.completion and not questMain_2.completion:
                $ neus_routine = ["neus","living","bath","neus","neus"]
            elif questMain_2.completion and not questMain_3.completion:
                $ neus_routine = ["neus","living","bath","neus","neus"]
            elif questMain_3.completion and not questMain_4.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_4.completion and not questMain_5.completion:
                $ neus_routine = ["kitchen","living","neus","neus","neus"]
            elif questMain_5.completion and not questMain_6.completion:
                $ neus_routine = ["kitchen","living","neus","neus","neus"]
            elif questMain_6.completion and not questMain_7.completion:
                $ neus_routine = ["kitchen","neus","bath","neus","neus"]
            elif questMain_7.completion and not questMain_8.completion:
                $ neus_routine = ["neus","living","bath","neus","neus"]
            elif questMain_8.completion and not questMain_9.completion:
                $ neus_routine = ["kitchen","living","bath","kitchen","neus"]
    elif quest_v2:
        if questMain_v2_16.completion:
            $ neus_routine = ["kitchen","living","bath","neus","neus"]
        else:
            if not questMain_v2_1.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_1.completion and not questMain_v2_2.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_2.completion and not questMain_v2_3.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_3.completion and not questMain_v2_4.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_4.completion and not questMain_v2_5.completion:
                $ neus_routine = ["neus","living","bath","neus","neus"]
            elif questMain_v2_5.completion and not questMain_v2_6.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_6.completion and not questMain_v2_7.completion:
                $ neus_routine = ["neus","living","bath","neus","neus"]
            elif questMain_v2_7.completion and not questMain_v2_8.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_8.completion and not questMain_v2_9.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_9.completion and not questMain_v2_10.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_10.completion and not questMain_v2_11.completion:
                $ neus_routine = ["kitchen","living","neus","neus","neus"]
            elif questMain_v2_11.completion and not questMain_v2_12.completion:
                $ neus_routine = ["kitchen","living","neus","neus","neus"]
            elif questMain_v2_12.completion and not questMain_v2_13.completion:
                $ neus_routine = ["kitchen","neus","bath","neus","neus"]
            elif questMain_v2_13.completion and not questMain_v2_14.completion:
                $ neus_routine = ["kitchen","living","bath","neus","neus"]
            elif questMain_v2_14.completion and not questMain_v2_15.completion:
                $ neus_routine = ["neus","living","bath","neus","neus"]
            elif questMain_v2_15.completion and not questMain_v2_16.completion:
                $ neus_routine = ["kitchen","living","bath","kitchen","neus"]
                
    return

label neus_lust_label:
    if neus_lust >= 100 and (
        (neus_lust_label_location == "kitchen_movie" and kitchen_room3_is_view_talk_movie) or 
        (neus_lust_label_location == "kitchen_outfit" and kitchen3_is_view_outfit_intro2) or 
        (neus_lust_label_location == "living_outfit" and living_room3_is_view_outfit_intro2) or 
        (neus_lust_label_location == "neus_outfit" and neus3_is_view_outfit_intro2)):
        $ neus_lust_label = ""
    else:
        $ neus_lust_label = " (Lust " + str(neus_lust) + "/100)"
    return

label time_advances:
    if(time<4):
        $ time+= 1 
    $ is_peek = 0    
    $ is_touch = 0
    $ is_kiss = 0   
    $ is_handjob = 0
    $ is_footjob = 0
    $ is_blowjob_more = 0
    $ is_blowjob = 0
    $ is_blowjob_outfit = 0
    $ is_boobs = 0
    $ is_sex_intro = 0
    $ is_sex_more = 0
    $ is_sex = 0
    $ is_sex_outfit = 0
    $ is_sexpussy = 0
    $ is_sexanal = 0
    $ spanking_count=0
    $ is_view_trigger_wake_up_neus_yandere = 0
    $ is_view_wake_up_neus_yandere = False
    $ sleep_action = False
    $ neus_left_room = False
    $ neus_room_unlocked = False
    jump rooms

label next_day:
    $ time = 0   
    $ is_peek = 0    
    $ is_touch = 0
    $ is_kiss = 0   
    $ is_handjob = 0
    $ is_footjob = 0
    $ is_blowjob_more = 0
    $ is_blowjob = 0
    $ is_blowjob_outfit = 0
    $ is_boobs = 0
    $ is_sex_intro = 0
    $ is_sex_more = 0
    $ is_sex = 0
    $ is_sex_outfit = 0
    $ is_sexpussy = 0
    $ is_sexanal = 0
    $ select_room="mc"
    $ spanking_count=0   
    $ is_view_trigger_wake_up_neus_yandere = 0
    $ is_view_wake_up_neus_yandere = False
    $ sleep_action = False
    $ neus_left_room = False
    $ neus_room_unlocked = False
    jump rooms
label next_day_neus:
    $ time = 0   
    $ is_peek = 0    
    $ is_touch = 0
    $ is_kiss = 0   
    $ is_handjob = 0
    $ is_footjob = 0
    $ is_blowjob_more = 0
    $ is_blowjob = 0
    $ is_blowjob_outfit = 0
    $ is_boobs = 0
    $ is_sex_intro = 0
    $ is_sex_more = 0
    $ is_sex = 0
    $ is_sex_outfit = 0
    $ is_sexpussy = 0
    $ is_sexanal = 0    
    $ spanking_count=0   
    $ is_view_trigger_wake_up_neus_yandere = 0
    $ sleep_action = False
    $ neus_left_room = False
    $ neus_room_unlocked = False
    jump rooms

label level_up(level_re=1):    
    $ relationship_level=level_re
    $ kitchen_event_lvl=level_re
    $ bath_event_lvl=level_re 
    $ living_event_lvl=level_re 
    $ neus_event_lvl=level_re
    $ mc_event_lvl=level_re   
    $ is_change_tree_skill=True           
    return

label adjust_room_levels(change):
    $ kitchen_event_lvl += change
    $ bath_event_lvl += change
    $ living_event_lvl += change
    $ neus_event_lvl += change
    $ mc_event_lvl += change
    jump rooms

label addLust(lust_add=1,lust_max=0):
    if quest_v2:
        if not questMain_v2_16.completion:
            if questMain_v2_1.completion and not questMain_v2_2.completion:
                $ lust_max = 3
            elif questMain_v2_3.completion and not questMain_v2_4.completion:
                $ lust_max = 8
            elif questMain_v2_5.completion and not questMain_v2_6.completion:
                $ lust_max = 16
            elif questMain_v2_7.completion and not questMain_v2_8.completion:
                $ lust_max = 26
            elif questMain_v2_9.completion and not questMain_v2_10.completion:
                $ lust_max = 38
            elif questMain_v2_13.completion and not questMain_v2_14.completion:
                $ lust_max = 64
            elif questMain_v2_14.completion and not questMain_v2_15.completion:
                $ lust_max = 64
        elif questMain_v2_16.completion:
            $ lust_max = 100
        if (neus_event_lvl==0 and not neus_lust>=20) or (neus_event_lvl==1 and not neus_lust>=50) or (neus_event_lvl==2 and not neus_lust>=69) or (neus_event_lvl==3):
            if neus_lust < lust_max:  # Only proceed if current lust is below the maximum
                scene black with dissolve 
                
                # Step 1: Calculate the actual amount of lust to add
                $ actual_add = min(lust_add, lust_max - neus_lust)
                
                # Step 2: Display the actual amount of lust added
                centered "{size=+60}Lust {color=cc0066}+[actual_add]"
                
                # Step 3: Update `neus_lust`
                $ neus_lust += actual_add
                
                # Step 4: Display "Lust at maximum" message only when `neus_lust` is 100
                if neus_lust == 100:  
                    centered "{size=+60}Lust at maximum"
        if neus_lust == lust_max:
            if lust_max == 3:
                call completeQuest(2)
            elif lust_max == 8:
                call completeQuest(4)
            elif lust_max == 16:
                call completeQuest(6)
            elif lust_max == 26:
                call completeQuest(8)
            elif lust_max == 38:
                call completeQuest(10)
            elif lust_max == 64 and not questMain_v2_14.completion:
                call completeQuest(14)
            elif lust_max == 64 and questMain_v2_14.completion:
                call completeQuest(15)

    else:
        if not(neus_lust>=100):
            scene black with dissolve        
            centered "{size=+60}Lust {color=cc0066}+[lust_add]"
            if (neus_lust+lust_add)>=100:            
                centered "{size=+60}Lust at maximum"
                $neus_lust=100
            else:                
                $neus_lust+=lust_add
    return
            
label completeQuest(quest_number=1):
    scene black with dissolve 

    if quest_number == 2:
        $ questMain_v2_2.completion = True
    elif quest_number == 4:
        $ questMain_v2_4.completion = True
    elif quest_number == 6:
        $ questMain_v2_6.completion = True
    elif quest_number == 8:
        $ questMain_v2_8.completion = True
    elif quest_number == 10:
        $ questMain_v2_10.completion = True
    elif quest_number == 14:
        $ questMain_v2_14.completion = True
        
    if not neus_left_room:
        if N_state<1:
            if bath_event_lvl == 0 and select_room=="bath":
                pass
            elif neus_event_lvl == 0 and select_room=="neus":
                "Overwhelmed, she quickly kicks you out of her room, her face flushed with emotion."
            elif neus_event_lvl == 0 and not select_room=="neus":
                "Overwhelmed, she quickly leaves the room, her face flushed with emotion."
            elif neus_event_lvl == 1 and select_room=="neus":
                "She asks you to leave her room, clearly overwhelmed by her emotions."
            elif neus_event_lvl == 1 and not select_room=="neus":
                "She leaves the room, clearly overwhelmed by her emotions."
            elif neus_event_lvl == 2 and select_room=="neus":
                "She asks you to leave her room, clearly struggling with her emotions."
            elif neus_event_lvl == 2 and not select_room=="neus":
                "She leaves the room, clearly struggling with her emotions."
        elif N_state>=1:
            if neus_event_lvl == 2 and select_room=="neus":
                "You notice that [neusname] can't take much more, so you let her rest."
            elif neus_event_lvl == 2 and not select_room=="neus":
                "You notice that [neusname] can't take much more, so you let her go."
    if not questMain_v2_13.completion:
        mc "(I think she's ready to be pushed further.)"

    if quest_number == 15:
        pass
    else:
        if quest_number == 2:
            $ questMain_v2_select = questMain_v2_3
        elif quest_number == 4:
            $ questMain_v2_select = questMain_v2_5
        elif quest_number == 6:
            $ questMain_v2_select = questMain_v2_7
        elif quest_number == 8:
            $ questMain_v2_select = questMain_v2_9
        elif quest_number == 10:
            $ questMain_v2_select = questMain_v2_11
        elif quest_number == 14:
            $ questMain_v2_select = questMain_v2_15
        
        $ is_change_quest = True
        call notify_personalized(_("Main Quest updated"))
    
    if select_room=="neus":
        $ select_room="mc" 

    jump time_advances
