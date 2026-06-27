image living0_1 = DynamicAnimation(
["rooms/living/lvl0/living0_1_0.webp",
"rooms/living/lvl0/living0_1_1.webp", 
"rooms/living/lvl0/living0_1_2.webp"])
image living1_1= DynamicAnimation(
["rooms/living/lvl1/living1_1_0.webp",
"rooms/living/lvl1/living1_1_1.webp",
"rooms/living/lvl1/living1_1_2.webp"])
image living2_1_0= DynamicAnimation(
["rooms/living/lvl2/living2_1_0_0.webp",
"rooms/living/lvl2/living2_1_0_1.webp",
"rooms/living/lvl2/living2_1_0_2.webp"])
image living3_1_0= DynamicAnimation(
["rooms/living/lvl3/living3_1_0_0.webp",
"rooms/living/lvl3/living3_1_0_1.webp",
"rooms/living/lvl3/living3_1_0_2.webp"])
image living_room3_out1_1= DynamicAnimation(
["rooms/living/lvl3/living_room3_out1_1_0.webp",
"rooms/living/lvl3/living_room3_out1_1_1.webp",
"rooms/living/lvl3/living_room3_out1_1_2.webp"])
image living_room3_out2_4= DynamicAnimation(
["rooms/living/lvl3/living_room3_out2_4_0.webp",
"rooms/living/lvl3/living_room3_out2_4_1.webp",
"rooms/living/lvl3/living_room3_out2_4_2.webp"])

screen living_room_quest:
    if quest_v2:
        if not(time==questMain_v2_select.time_event) or not(select_room==neus_routine[time]) or questMain_v2_select.place=="":
            use expression "living%s"%living_event_lvl 
    else:
        if not(time==questMain_select.time_event) or not(select_room==neus_routine[time]) or questMain_select.place=="":
            use expression "living%s"%living_event_lvl   
    if time<=3 and not(neus_routine[time]=="living"):        
        imagebutton:
            auto "btn_tv_event_%s" 
            pos   850, 400        
            tooltip _("Tv")
            action Jump("tv_event%s"%living_event_lvl)
    if quest_v2:
        if questMain_v2_9.completion and not(key_room_attic.is_view):  
            if time < 4:    
                imagebutton:
                    auto "btn_key_attic_%s"            
                    focus_mask True
                    tooltip _("Book?")
                    action Jump("key_attic")
                    at event_animation_page  
            else:
                imagebutton:
                    auto "btn_night_key_attic_%s"            
                    focus_mask True
                    tooltip _("Book?")
                    action Jump("key_attic")
                    at event_animation_page  
    else:
        if questMain_4.completion and not(key_room_attic.is_view):      
            if time < 4:
                imagebutton:
                    auto "btn_key_attic_%s"            
                    focus_mask True
                    tooltip _("Book?")
                    action Jump("key_attic")
                    at event_animation_page  
            else:
                imagebutton:
                    auto "btn_night_key_attic_%s"            
                    focus_mask True
                    tooltip _("Book?")
                    action Jump("key_attic")
                    at event_animation_page  
    if relationship_level>=3 and not(living_room3_is_active_outfit):
        if time < 4:
            imagebutton:
                auto "btn_old_photo_s_%s"     
                action Jump("living_room3_minigame")
                tooltip _("Special photo")
                pos 230,700
        else:
            imagebutton:
                auto "btn_night_old_photo_s_%s"     
                action Jump("living_room3_minigame")
                tooltip _("Special photo")
                pos 230,700

#----------------------------Level 0---------------------------------    
screen living0:
    if neus_routine[time]=="living":      
        imagebutton:
            auto "rooms/living/lvl0/living0_0_%s.png"            
            focus_mask True
            tooltip "%s"%neusname
            action Jump("living0")

label living0:     
    call rooms_music
    scene living0_1
    show screen living_spell
    menu:       
        "Talk":            
            jump living0_talk
        "Kiss" ((not quest_v2 and questMain_2.completion) or (quest_v2 and questMain_v2_5.completion)):
            jump living0_action       
        "Hang out":
            hide screen spell_screen
            scene living0_9 
            if incest_story:
                "You spend time with your sister"
            else:
                "You spend time with [neusname]"
            jump time_advances
        "Leave":               
            jump rooms    


label living0_talk:
    scene living0_1
    hide screen spell_screen    
    menu:
        "What do you want to talk about?"        
        "Series":           
            mc "What series are you watching?"
            scene living0_2 with dissolve
            neus "It's a new series, I'm seeing if it's any good."   
            menu:
                "Stay":
                    scene living0_3 with dissolve
                    neus "Can you make me popcorn?"
                    mc "Sure! If you help me."
                    scene living0_4 with dissolve
                    if incest_story:
                        "You spend time with your sister, but nothing has changed."
                    else:
                        "You spend time with [neusname], but nothing has changed."
                    jump time_advances
                "Leave":
                    jump living0
        "Back":
            jump living0
    jump living0_talk                  
label living0_action:
    hide screen spell_screen
    if is_kiss>=1:
        scene living0_11 with dissolve
        neus "No"
    else:        
        scene living0_10 with dissolve
        neus "{sc=3}Mmm{/sc}"        
        scene living0_12 with ccirclefx
        play char1 short_kiss
        pause 
        $ is_kiss+=1   
        if quest_v2:
            call addLust(1)
    jump living0
label tv_event0:          
    scene living0_16 with dissolve        
    ""
    jump time_advances
#----------------------------Level 1---------------------------------
screen living1:
    if neus_routine[time]=="living":      
        imagebutton:
            auto "rooms/living/lvl1/living1_0_%s.png"            
            focus_mask True
            tooltip "%s"%neusname
            action Jump("living1")
label living1: 
    call rooms_music
    scene living1_1
    show screen living_spell
    $ xsize_value = 650
    menu(screen="custom_choice_enhanced"):       
        "Talk":            
            jump living1_talk
        "Action":
            jump living1_action 
        "Spanking (Level:[spanking_level]/2)":
            hide screen spell_screen
            if not(is_view_spanking):
                scene black with dissolve
                if incest_story:
                    neus "Brother, what are you doing?"
                else:
                    neus "Hey, what are you doing?"
                "You place her over your lap."
                $is_view_spanking=True
            # if not(spell_0_1.is_active):   
            #     menu:             
            #         "To pass the next level, you need {color=#cc0066}''Touch''{/color}. Do you want to activate it?"
            #         "Yes":
            #             $ questSide_2.completion = True
            #             $ spell_0_1.is_active = True 
            #             $is_change_quest = True 
            #             call notify_personalized(_("Side Quest updated"))                       
            #         "No":
            #             pass
            $outfit_spanking=0
            $spanking_count=0
            jump spanking_start      
        "Hang out":
            hide screen spell_screen
            scene living1_13
            if incest_story:
                "You spend time with your sister"
            else:
                "You spend time with [neusname]"
            jump time_advances
        "Leave":               
            jump rooms
            
label living1_talk:
    scene living1_1
    hide screen spell_screen    
    menu:
        "What do you want to talk about?"        
        "Tv": 
            scene living1_2 with dissolve
            neus "There is a new series, do you want to watch it with me?"
            mc "Sure!"
            scene living1_3 with dissolve
            ""  
            jump time_advances                     
        "Back":
            jump living1
    jump living1_talk 

label living1_action:
    call rooms_music
    scene living1_1
    hide screen spell_screen 
    menu:
        "What do you want to do?"        
        "Kiss":           
            if is_kiss>=1:
                scene living1_5 with dissolve 
                play char1 short_kiss               
                ""
                scene living1_6 with dissolve
                play char1 french01
                ""
                scene living1_7 with dissolve
                neus "(I want {sc=3}{=lust_style}more{/sc}, but I have to resist)"
                if is_kiss<2:
                    if quest_v2:
                        call addLust(1)
                    $is_kiss+=1
            else:
                scene living1_4 with dissolve
                neus "Hmm"            
                scene living1_5 with dissolve 
                play char1 short_kiss               
                ""                
                if quest_v2:
                    call addLust(1)
                $ is_kiss+=1
        "Footjob":          
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            scene living1_8 with dissolve
            neus "You better finish fast" 
            scene living1_9 with dissolve 
            if incest_story:
                neus "Can you finish already brother?"   
            else:
                neus "Hey, can you finish already?"            
            scene living1_10 with dissolve
            play char3 handjob2  fadeout 1.0  
            menu:
                "Cum":
                    stop char3
                    play charM cum1                    
                    scene living1_11 with flash2
                    ""
                    scene living1_12 with dissolve 
                    "..."
                    $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
                    scene black with dissolve 
                    "She cleans herself"
                    if is_footjob<1:
                        if quest_v2:
                            call addLust(2)
                        $ is_footjob+=1
        "Blowjob"((not quest_v2 and questMain_4.completion) or (quest_v2 and questMain_v2_9.completion)):
            scene living1_22 with dissolve 
            neus "Ugh... fine"
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            scene living1_23 with dissolve
            if incest_story:
                neus "Why are you such a pervert, brother?" 
            else:
                neus "Why are you such a pervert?" 
            scene living1_24 with dissolve  
            neus "(It's so big, it barely fits in my mouth.)"
            scene living1_25 with dissolve          
            play char3 suck2 
            menu:
                "Inside"((not quest_v2 and questMain_5.completion) or (quest_v2 and questMain_v2_11.completion)):
                    stop char3
                    play charM cum1
                    scene living1_26 with flash2 
                    neus "{sc=3}Hmm{/sc}"
                    scene living1_27 with dissolve 
                    ""
                "Outside":
                    stop char3
                    play charM cum1
                    scene living1_28 with flash2
                    ""             
            $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
            scene black with dissolve 
            "She cleans herself"
            if is_blowjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob+=1
        "Back":
            jump living1
    jump living1_action
label tv_event1:        
    scene living0_16 with dissolve        
    ""   
    jump time_advances
#----------------------------Level 2---------------------------------
screen living2:
    if neus_routine[time]=="living": 
        if is_sexpussy>=1:     
            imagebutton:
                auto "rooms/living/lvl2/living2_0_1_%s.png"            
                focus_mask True
                tooltip "%s"%neusname
                action Jump("living2")
        else:
            imagebutton:
                auto "rooms/living/lvl2/living2_0_0_%s.png"            
                focus_mask True
                tooltip "%s"%neusname
                action Jump("living2")
label living2: 
    if neus_is_evading:
        scene black with dissolve
        if incest_story:
            "Your sister notices your presence and quickly leaves the room."
        else:
            "She notices your presence and quickly leaves the room."
        jump time_advances    
    if N_state==1:     
        stop music fadeout 1.0   
        if is_sexpussy>=1:
            play char3 breathing2 volume 0.3 fadeout 1.0
            scene living2_1_1_1
        else:
            play char3 breathing1 fadeout 1.0
            scene living2_1_1_0
    else:
        call rooms_music
        scene living2_1_0    
    show screen living_spell
    $ xsize_value = 650
    menu(screen="custom_choice_enhanced"):   
        "More"((not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion)) if N_state==1:
            hide screen living_spell
            if is_sexpussy>=1:
                scene black with dissolve
                if incest_story:
                    "Your sister is so tired that she offers no resistance."
                else:
                    "[neusname] is so tired that she offers no resistance."
                play char3 sex2
                scene living2_42 with dissolve
                neus "Haaa Haaa Haaa"                
                scene living2_43 with dissolve
                neus "Mmm!{w=1.0}{nw}"
                stop char3
                play charM cum1 
                scene living2_44 with flash2
                neus "Ohhh"                
                scene black with dissolve      
                if incest_story:
                    "You notice that she can't take anymore, so you let her go."
                else:          
                    "You notice that [neusname] can't take anymore, so you let her go."
                $ neus_left_room = True
                if quest_v2:
                    call addLust(3)
                jump time_advances
            else:
                scene living2_33 with dissolve
                neus "Mmmm"
                scene living2_34 with dissolve    
                neus "No more, please."
                scene living2_35 with dissolve
                mc "Relax, I'll go gentle as always"
                scene living2_36 with dissolve
                if incest_story:
                    neus "Brother, you only recently took my virginity, if you do this to me every day, I could become addicted.{w=4.0}{nw}"
                else:
                    neus "You only recently took my virginity, if you do this to me every day, I could become addicted.{w=5.0}{nw}"
                stop char3 fadeout 1.0
                scene living2_37 with dissolve
                play char1 penetration3
                neus "Haaa"
                if incest_story:
                    mc "That's the idea little sister."
                else:
                    mc "That's the idea."
                play char3 sex2
                scene living2_38 with dissolve
                neus "Haaa haaa haaa"               
                scene living2_39 with dissolve
                neus "Ahhh!{w=1.0}{nw}"                
                stop char3
                play charM cum1                
                scene living2_40 with flash2
                neus "Uhhhh"
                scene living2_41 with dissolve
                ""                
                $is_sexpussy+=1
                if is_sex_more<1:
                    if quest_v2:
                        call addLust(3)
                    $ is_sex_more+=1
            jump living2     
        "Talk"if N_state==0:            
            jump living2_talk
        "Action"if N_state==0:
            jump living2_action 
        "Spanking (Level:[spanking_level]/2)" if N_state==0:
            hide screen spell_screen
            if not(is_view_spanking):
                scene black with dissolve
                if incest_story:
                    neus "Brother, what are you doing?"
                else:
                    neus "Hey, what are you doing?"
                "You place her over your lap."
                $is_view_spanking=True
            # if not(spell_0_1.is_active):   
            #     menu:             
            #         "To pass the next level, you need {color=#cc0066}''Touch''{/color}. Do you want to activate it?"
            #         "Yes":
            #             $ questSide_2.completion = True
            #             $ spell_0_1.is_active = True       
            #             $is_change_quest = True 
            #             call notify_personalized(_("Side Quest updated"))                 
            #         "No":
            #             pass
            # if not(spell_2_1.is_active):   
            #     menu:             
            #         "To pass the next level, you need {color=#cc0066}''Pain is pleasure''{/color}. Do you want to activate it?"
            #         "Yes":                        
            #             $ spell_2_1.is_active = True                        
            #         "No":
            #             pass 
            $outfit_spanking=1
            $spanking_count=0
            jump spanking_start          
        "Leave":               
            jump rooms
            
label living2_talk:
    scene living2_1_0
    hide screen spell_screen    
    menu:
        "What do you want to talk about?"        
        "Tv": 
            scene living2_2 with dissolve            
            neus "A new episode just came out. Do you want to watch it together?" 
            mc "Sure!"  
            scene living2_3 with dissolve
            menu:
                "Put your own episode on the TV.":
                    $tv_talk_choice= renpy.random.choice([0,1,2,3])
                    scene expression "living2_4_%s"%tv_talk_choice with dissolve
                    if incest_story:
                        neus "Brother, what is this?"
                    else:
                        neus "What is this?"
                    play charM slap1 volume 2.0
                    scene living2_5 with dissolve
                    play char1 groan_normal1
                    mc "Some beautiful memories."                    
                    scene living2_6 with dissolve               
                    neus "(This is so embarrassing.)" 
                    scene black with dissolve
                    if incest_story:
                        "You enjoy watching your little sister's expressions of embarrassment."
                    else:
                        "You enjoy watching [neusname]'s expressions of embarrassment."
                    if quest_v2:
                        call addLust(1)
                "Leave":
                    scene black with dissolve
                    if incest_story:
                        "You spend some quality time with your little sister."
                    else:
                        "You spend some quality time with [neusname]."
            jump time_advances                   
        "Back":
            jump living2
    jump living2_talk 

label living2_action:
    call rooms_music
    scene living2_1_0
    hide screen spell_screen 
    menu:
        "What do you want to do?"        
        "Kiss": 
            scene living2_7 with dissolve 
            play char1 french01 
            "" 
            scene living2_8 with dissolve
            play char1 groan1
            neus "Uhmm"
            scene living2_9 with dissolve
            neus "(I want {sc=3}{=lust_style}more{/sc}.)"
            if is_kiss<1:
                if quest_v2:
                    call addLust(1)
                $ is_kiss+=1
        "Blowjob":           
            neus "..."  
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')       
            scene living2_10 with dissolve
            play char3 suck2 
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene living2_11 with flash2 
                    neus "{sc=3}Hmm{/sc}"
                    scene living2_12 with dissolve 
                    ""
                "Outside":
                    stop char3
                    play charM cum1
                    scene living2_13 with flash2
                    ""            
            $ renpy.music.set_volume(1.0, delay=2.0, channel='music') 
            scene black with dissolve 
            "She cleans herself"
            if is_blowjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob+=1
        "Sex":                     
            stop music fadeout 1.0
            scene living2_19 with dissolve  
            neus "Mmmm"
            scene living2_20 with dissolve
            neus "H-Hey"
            scene living2_21 with dissolve
            if incest_story:
                neus "You are such a perverted brother"
            else:
                neus "You are a fucking perverted monkey"
            scene living2_22 with dissolve
            mc "Does it bother you that much?"            
            neus "Y-Yes. Ahhh."
            scene living2_23 with dissolve
            neus "(I can't get used to how big it is.)"
            play char3 sex2
            scene living2_24 with dissolve
            if incest_story:
                mc "Does it feel good little sister?"
            else:
                mc "Does it feel good?"
            neus "...(I don't feel any pain like the first time, in fact, it feels...)"
            mc "I'll take that as a yes."
            scene living2_25 with dissolve
            neus "Die"
            mc "If that’s how you feel, why not just kill me while I’m asleep?"
            scene living2_26 with dissolve
            neus "You're so annoying, finish quickly."
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene living2_27 with flash2 
                    neus "{sc=3}Hmm{/sc}"
                    scene living2_28 with dissolve 
                    neus "Why did you cum inside, what happens if I get pregnant?"
                    if incest_story:
                        mc "That's what I want sis, don't worry I will take responsibility."
                    else:
                        mc "That's what I want, don't worry I will take responsibility."
                    scene living2_29 with dissolve 
                    neus "..."
                "Outside":
                    stop char3
                    play charM cum1
                    scene living2_30 with flash2
                    neus "{sc=3}Hmm{/sc}"
                    scene living2_31 with dissolve
                    neus "Thank you for not cumming inside."                
            menu:
                "More"((not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion)):
                    scene black with dissolve
                    if incest_story:
                        neus "Brother, what are you doing?"
                    else:
                        neus "Hey, what are you doing?"
                    play char3 sex2
                    scene living2_32 with dissolve
                    neus "Haa Haaa Haaa Haaa"
                    stop char3
                    scene black with dissolve
                    "You cum two more times."
                    "She manages to clean herself."
                    $N_state=1
                    if is_sex<1:
                        if quest_v2:
                            call addLust(4)
                        $ is_sex+=1 
                    if incest_story:
                        "Your sister is very tired. (You can use {color=#1f8a09}''Touch''{/color} to give her energy)"  
                    else:
                        "[neusname] is very tired. (You can use {color=#1f8a09}''Touch''{/color} to give her energy)"  
                    jump living2 
                "Leave": 
                    scene black with dissolve                   
                    "She cleans herself"     
            if is_sex<1:
                if quest_v2:
                    call addLust(3)
                $ is_sex+=1
        "Back":
            jump living2
    jump living2_action
label tv_event2:           
    scene living0_16 with dissolve        
    ""  
    jump time_advances
#----------------------------Level 3--------------------------------- 
default living_room3_outfit_type=0
default living_room3_is_view_outfit_intro=False
default living_room3_is_view_outfit_intro2=False
default living_room3_is_active_outfit = False
screen living3:
    if neus_routine[time]=="living": 
        if living_room3_outfit_type==0:         
            imagebutton:
                auto "rooms/living/lvl3/living3_0_0_%s.png"            
                focus_mask True
                tooltip "%s"%neusname
                action Jump("living3")
        if living_room3_outfit_type==1:
            imagebutton:
                auto "rooms/living/lvl3/living_room3_out1_0_%s.png"            
                focus_mask True            
                action Jump("living_room3_outfit1")
                tooltip "%s"%neusname
        if living_room3_outfit_type==2:
            imagebutton:
                auto "rooms/living/lvl3/living_room3_out2_0_%s.png"            
                focus_mask True            
                action Jump("living_room3_outfit2")
                tooltip "%s"%neusname
label living3:
    scene living3_1_0
    show screen living_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    $ xsize_value = 650
    menu(screen="custom_choice_enhanced"):   
        "Talk":           
            jump living3_talk
        "Action":
            jump living3_action
        "Outfit":
            if not(living_room3_is_view_outfit_intro):
                menu:                
                    "Requirements: Object creation: {color=#cc0066}[spell_2_2.is_active]{/color} and outfit photo: {color=#cc0066}[living_room3_is_active_outfit]{/color}"
                    "Give outfit"((living_room3_is_active_outfit and spell_2_2.is_active)):
                        hide screen spell_screen
                        jump living_room3_outfit1_intro1                                         
                    "Back":
                        jump living3
            else:
                menu:
                    "Outfit 1"((living_room3_is_active_outfit and spell_2_2.is_active)):
                        hide screen spell_screen
                        scene living3_2 with dissolve
                        neus "A-Alright."
                        $ living_room3_outfit_type=1 
                        jump living_room3_outfit1
                    "Outfit 2"((neus_lust>=100)) if (living_room3_is_view_outfit_intro2):
                        hide screen spell_screen
                        scene living3_2 with dissolve                
                        neus "A-Alright."
                        $ living_room3_outfit_type=2                                          
                        jump living_room3_outfit2
                    "Outfit 1 intro"((living_room3_is_active_outfit and spell_2_2.is_active)):
                        hide screen spell_screen                            
                        jump living_room3_outfit1_intro1                                         
                    "Back":
                        jump living3
        "Spanking (Level:[spanking_level]/2)":
            hide screen spell_screen
            if not(is_view_spanking):
                scene black with dissolve
                neus "Hey, what are you doing?"
                if incest_story:
                    "You place your little sister over your lap."
                else:
                    "You sit her on your lap."
                $is_view_spanking=True
            # if not(spell_0_1.is_active):   
            #     menu:             
            #         "To pass the next level, you need {color=#cc0066}''Touch''{/color}. Do you want to activate it?"
            #         "Yes":
            #             $ questSide_2.completion = True
            #             $ spell_0_1.is_active = True      
            #             $is_change_quest = True 
            #             call notify_personalized(_("Side Quest updated"))                  
            #         "No":
            #             pass
            # if not(spell_2_1.is_active):   
            #     menu:             
            #         "To pass the next level, you need {color=#cc0066}''Pain is pleasure''{/color}. Do you want to activate it?"
            #         "Yes":                        
            #             $ spell_2_1.is_active = True                        
            #         "No":
            #             pass
            $outfit_spanking=2
            $spanking_count=0
            jump spanking_start               
        "Leave":           
            jump rooms

label living3_talk:
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    scene living3_1_0
    hide screen spell_screen    
    menu:
        "What do you want to talk about?"        
        "Watch a movie": 
            scene living3_t_0 with dissolve      
            menu:                
                neus "What movie do you want to watch?"
                "A scary one (Level:[lvl_event_fear]/2)": 
                    if lvl_event_fear==0:
                        jump fear_level1
                    elif lvl_event_fear==1:
                        jump fear_level2
                    else:
                        menu:
                            "Event 1":
                                jump fear_level1
                            "Event 2":
                                jump fear_level2
                            "Leave":
                                jump living3_talk                    
                "An erotic one": 
                    scene living3_t_8 with dissolve                    
                    neus "Seriously? You want to watch that kind of movie?"
                    mc "Why not?"
                    scene living3_t_9 with dissolve 
                    neus "..."
                    stop music fadeout 0.5
                    scene living3_t_10 with fade 
                    play music TheGirlFromBrasil_Hauser volume 0.5
                    neus "Hey, what is this?"
                    mc "Well, I wanted us to watch the good moments we've shared together."
                    scene living3_t_11 with dissolve 
                    neus "Not again. And why do you have that recorded?"
                    scene living3_t_12 with dissolve 
                    mc "I wanted a way to preserve our memories, and I love the expressions you show."
                    scene living3_t_13 with dissolve
                    neus "Turn it off."
                    mc "Don't you like yourself?"
                    scene living3_t_14 with dissolve
                    neus "I-I don't like you."
                    scene living3_t_15 with dissolve
                    neus "Haa Haa"
                    neus "(This is embarrassing.)"                                      
                    menu:
                        neus "(Seeing myself making those expressions.)" 
                        "Sex":
                            play music PoolParty_Christensen volume 0.1
                            scene living3_t_16 with fadesex
                            neus "Mmm"(multiple=2)
                            mc "I want to see you moan in first person."(multiple=2)
                            scene living3_t_17 with dissolve
                            play char1 penetration1
                            neus "Haaa"
                            scene living3_t_18 with dissolve
                            if incest_story:
                                neus "Mmm... {size=-15}brother, you can't just stick your thing in whenever you want."
                            else:
                                neus "Mmm... {size=-15}hey, you can't just stick your thing in whenever you want."
                            mc "Your expressions don't match what you're trying to say, and you're speaking very softly."
                            scene living3_t_19 with dissolve
                            neus "{size=-15}Well... maybe this time, I'll allow it."                           
                            mc "?"
                            scene living3_t_20 with dissolve
                            neus "Never mind."
                            mc "I'm going to start moving."
                            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
                            scene living3_t_21 with dissolve
                            play char3 sex2
                            neus "{bt=2}{=lust_style}Haa Haa Haa{/bt}"
                            neus "(This feels really good... I guess doing it so many times helps.)"
                            neus "(That means I'm becoming addicted to this...)"
                            neus "(I don't want to be called a nymphomaniac. Last time, I was too excited and said very embarrassing things.)"
                            neus "(I have to maintain my composure.)"
                            neus "{bt=2}{=lust_style}Haa Haa Haa{/bt}"
                            scene living3_t_22 with dissolve
                            neus "{sc=2}{=lust_style}Ohhh, I'm cumming.{/sc}"
                            menu:
                                "Inside":
                                    stop music fadeout 1.0
                                    stop char3
                                    play charM cum1
                                    scene living3_t_23 with flash2
                                    play char1 climax1
                                    neus "{color=#cc0066}Ohhh"
                                    scene living3_t_24 with dissolve
                                    if incest_story:
                                        neus "(My brother came inside me again.)"
                                    else:
                                        neus "(He came inside me again.)"
                                    scene living3_t_25 with dissolve
                                    neus "(I can feel his fluids filling my uterus.)"
                                    neus "(With the sole intention of fertilizing my eggs.)"
                                    neus "(And turning me into a mother.)"                                   
                                    scene living3_t_26 with dissolve                                    
                                    neus "(Huh!? What am I thinking? I'm definitely not ready to be a mother.)"
                                    neus "(I mustn't forget to take the pill.)"
                                "Outside":
                                    stop music fadeout 1.0
                                    stop char3
                                    play charM cum1
                                    scene living3_t_27 with flash2
                                    play char1 climax1
                                    neus "{color=#cc0066}Ohhh"
                                    scene living3_t_28 with dissolve
                                    if incest_story:
                                        neus "Thank you brother."
                                    else:
                                        neus "Thank you."
                            $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
                            scene black with dissolve
                            "She leaves the room to clean up."  
                            call addLust(4) from _call_addLust_5
                            jump time_advances
                        "Leave":
                            pass                                            
        "Back":
            jump living3
    jump living3_talk 
label living3_action:
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    scene living3_1_0
    hide screen living_spell
    menu:
        "What do you want to do?"        
        "Kiss": 
            scene living3_3 with dissolve
            neus "Oh, great! *clearing throat* Okay!"
            scene living3_4 with dissolve
            play char1 short_kiss
            neus "Chuuuuu"
            scene living3_5 with dissolve
            play char1 french01
            if incest_story:
                "Your little sister puts her tongue in your mouth."
            else:
                "She puts her tongue in your mouth."
            scene living3_6 with dissolve
            neus "{bt=2}{=lust_style}More{/bt}"
            scene living3_7 with fade
            if incest_story:
                neus "(I think I've become addicted to kissing my brother, I have to stop)"
            else:
                neus "(I think I've become addicted to kissing him, I have to stop)"
            scene living3_8 with dissolve
            play char1 french02
            neus "(but just a little more won't hurt)"
            scene living3_9 with dissolve
            neus "{size=-10}Alright, that's enough!"
            if is_kiss<1:
                call addLust(1)
                $ is_kiss+=1
        "Blowjob": 
            scene  living3_3 with dissolve  
            if incest_story:
                neus "Okay brother!"
            else:         
                neus "Okay!"
            stop music fadeout 1.0
            scene living3_10 with fade
            neus "I'm going to start."
            scene living3_11 with dissolve
            play char3 suck2
            neus "Uhm... AHMU!"
            neus "Suck, suck"
            neus "HMMM UUHN (His penis is throbbing)"
            menu:
                "Cum":
                    pass
            scene living3_12 with flash2
            stop char3
            play charM cum1
            neus "BUUAH... HMMM UUAHN!"
            scene living3_13 with dissolve
            if incest_story:
                neus "UGH...(My brother's semen is so thick that it's stuck in my throat and hard to swallow)"
            else:
                neus "UGH...(His semen is so thick that it's stuck in my throat and hard to swallow)"
            scene living3_14 with dissolve
            play char1 gulp1
            if incest_story:
                neus "Are you satisfied now big brother?"
            else:
                neus "Are you satisfied now?"
            mc "Yes, thank you."
            scene black with dissolve
            "She cleans herself"
            if is_blowjob<1:
                call addLust(2) from _call_addLust_14
                $ is_blowjob+=1
        "Sex":
            scene living3_15 with dissolve
            neus "I've noticed you're always horny lately."
            neus "Are you sure you’re not suffering from some kind of sex addiction?"
            scene living3_16 with dissolve
            neus "*serious tone* I think you should seek help-"
            mc "Hmm, maybe... but it only happens when I see you, so I think you should take responsibility."
            scene living3_17 with dissolve
            neus "Hmm..?"
            stop music fadeout 1.0
            scene black with dissolve
            if incest_story:
                neus "Hey, hey, brother what are you doing?"
            else:
                neus "Hey, hey, what are you doing?"
            scene living3_18 with dissolve
            neus "This position is weird."
            mc "I like it, I can appreciate your beauty."
            neus "You mean my ass, right?"
            scene living3_18_1 with dissolve
            mc "Yes, I like your ass."
            mc "Well, enough games, let's get to the action."
            scene living3_19 with dissolve
            play char1 penetration3 volume 0.5
            neus "Uh!"
            mc "As always, it feels really good to be inside you."
            scene living3_20 with dissolve
            play char3 sex2
            neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
            if incest_story:
                neus "Can you be a bit more gentle brother, please."
            else:
                neus "Can you be a bit more gentle, please."
            mc "Doesn't it feel good?"
            neus "It's not that, it's just a bit intense."
            neus "(And if he keeps going like this, I'm going to blank out.)"
            scene living3_21 with dissolve
            neus "I'm {sc=2}cumming!{/sc}"
            scene living3_20 with dissolve
            menu:                
                "Inside":
                    stop char3
                    play charM cum1
                    scene living3_22 with dissolve
                    play char1 climax1
                    neus "Uh."
                    if incest_story:
                        neus "(My uterus is filled with my brother's semen.)"
                    else:
                        neus "(My uterus is filled with his semen.)"
                    scene living3_23 with dissolve
                    neus "(I'm sure my eggs are drowning.)"
                    neus "(If I didn't take the pill, I'm absolutely certain I would get pregnant.)"                    
                "Outside":
                    stop char3
                    play charM cum1
                    scene living3_24 with dissolve
                    play char1 climax1
                    neus "Uh."
                    neus "Thank you for cumming outside." 
            scene black with dissolve
            "After a while, she recovers and cleans herself."
            if is_sex<1:
                call addLust(3) from _call_addLust_15
                $ is_sex+=1
        "Anal":     
            mc "Hey, lets have some fun!"
            scene living3_25 with dissolve
            neus "Mmm... I'll pass."
            stop music fadeout 1.0
            scene living3_26 with fadesex
            neus "How the hell did I end up in this situation?"
            if incest_story:
                mc "Come on sis, don't be a sore loser."
            else:
                mc "Come on, don't be a sore loser."
            scene living3_27 with dissolve
            neus "(I shouldn't have bet again, I should know by now that he always has some trick up his sleeve)."
            neus "(Although for now, it's best to finish this quickly)."
            play char1 penetration3
            scene living3_28 with dissolve            
            neus "(It's so big. It's incredible that I can fit it in my tight ass)."
            scene living3_29 with dissolve
            play char3 sex2
            neus "ahh ahh ahh ahh."
            if incest_story:
                mc "This feels amazing, I love how tight your ass is little sister."
            else:
                mc "This feels amazing, I love how tight your ass is."
            mc "It's like it's trying to strangle my cock."
            neus "(Damn, this is so intense, I'm going to cum from an anal orgasm)."
            scene living3_30 with dissolve
            neus "I'm {sc=2}cumming!{/sc}"
            menu:                
                "Inside":
                    stop char3
                    play charM cum1
                    scene living3_31 with dissolve
                    play char1 climax1
                    neus "uhhh!"
                    neus "(My stomach feels so hot)."
                    scene living3_32 with dissolve
                    neus "Satisfied, I've fulfilled the deal we made."
                    if incest_story:
                        mc "Yes, thank you, you're an awesome sister."
                    else:
                        mc "Yes, thank you, you're awesome."
                    scene living3_33 with dissolve
                    neus "Yeah, yeah, as if I needed that kind of praise. {e_heartbt=FF0000}"
                    scene black with dissolve
                    "She gets up and cleans herself."
                "Outside":
                    stop char3
                    play charM cum1
                    scene living3_34 with dissolve
                    play char1 climax1
                    neus "Ohh!"
                    if incest_story:
                        mc "You're the best sister ever, that felt so good."
                        scene living3_35 with dissolve
                        neus "Shut up brother and stop flattering me for this. {e_heartbt=FF0000}"
                    else:
                        mc "You're the best, that felt so good."
                        scene living3_35 with dissolve
                        neus "Shut up and stop flattering me for this. {e_heartbt=FF0000}"
                    scene black with dissolve
                    "She walks away from you in embarrassment and cleans herself."
            if is_sexanal<1:
                call addLust(3) from _call_addLust_16
                $ is_sexanal+=1
        "Back":
            jump living3
    jump living3_action
    
label fear_level1:
    scene living3_t_1 with dissolve                   
    neus "Horror movies really freaked me out when I was younger."
    scene living3_t_2 with dissolve
    neus "But these days, I’ve seen so many that they don’t scare me anymore."
    neus "I hope this one isn't just another cliché."
    mc "Don't worry, I’ve got the perfect movie for you. It’s... unique."
    stop music fadeout 1.0
    call splash_message(_("Moments later")) from _call_splash_message_39
    scene living3_t_3 with dissolve
    neus "(What the hell is going on in this movie? The only characters getting killed have small breasts...)"                   
    neus "(Mmm, like the killer is called 'The Small-Breasted Killer'.)"
    scene living3_t_4 with dissolve
    neus "(What happened to the good old tradition of killing off the ones with more boobs than brains first?)"
    scene living3_t_5 with fade
    neus "(Ha, and of course, the only characters who survived are the ones with big breasts.)"                    
    neus "(And to top it off, the killer was defeated after being crushed by some giant breasts.)"
    scene living3_t_6 with dissolve
    neus "{sc=3}!?{/sc}"(multiple=2)
    mc "So, did you like it? Did it scare you?"(multiple=2)
    scene living3_t_7 with dissolve
    neus "Hmph... What a ridiculous movie... Th-that was not scary at all."                        
    $lvl_event_fear_aux=1
    scene black with dissolve
    "She leaves the room."
    "{color=#cc0066}She might visit you when you go to sleep."
    jump time_advances
label fear_level2:
    stop music fadeout 1.0
    scene living3_t_5 with fade
    neus "(How many movies like this does he have?)"   
    scene living3_t_6 with dissolve
    neus "{sc=3}!?{/sc}"(multiple=2)
    mc "So... did this one scare you?"(multiple=2)
    scene living3_t_7 with dissolve
    neus "N-No"
    $lvl_event_fear_aux=2
    scene black with dissolve
    "She leaves the room."
    "{color=#cc0066}She might visit you when you go to sleep."
    jump time_advances

label living_room3_outfit1_intro1:
    $ living_room3_is_view_outfit_intro=True
    $ living_room3_outfit_type=1    
    mc "I have something for you"
    scene living_room3_oi1_0 with dissolve
    neus "?"
    scene living_room3_oi1_1 with fade
    neus "I suppose this was to be expected."
    scene living_room3_oi1_2 with dissolve
    neus "(Well, it's nice)"
    scene living_room3_oi1_3 with dissolve
    if incest_story:
        neus "So, I guess you want your little sister to do a role play, like!"
    else:
        neus "So, I guess you want me to do a role play, like!"
    scene living_room3_oi1_4 with dissolve
    neus "''I, your humble servant-girlfriend, offer my mouth to clean your saber''"
    scene living_room3_oi1_5 with dissolve
    neus "or ''I've been a very naughty maid and need to be punished by my master''"
    scene living_room3_oi1_6 with dissolve
    if incest_story:
        neus "You want me to do that, right brother?"
    else:
        neus "You want me to do that, right?"
    neus "Well, it's not going to happen."
    scene living_room3_oi1_7 with dissolve
    mc "Well, honestly when I saw that outfit, I just thought it would look good on you."
    mc "But now that you mention it, that would be really hot."
    scene living_room3_oi1_8 with dissolve
    mc "Let's do it!"
    scene living_room3_oi1_9 with dissolve
    neus "(Damn it, me and my big mouth.)"
    scene living_room3_oi1_10 with fade
    mc "Well, let's begin."
    scene living_room3_oi1_11 with dissolve
    neus "W-Would master like to use the mouth of his servant-girlfriend."
    scene living_room3_oi1_12 with dissolve
    neus "Or perhaps you prefer to use my two holes."
    scene living_room3_oi1_13 with dissolve
    neus "That was..."
    scene black with dissolve
    call addLust(1)
    jump living_room3_outfit1
label living_room3_outfit1:
    scene living_room3_out1_1
    show screen living_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    menu:       
        "Change outfit":
            $ xsize_value = 650
            $ neus_lust_label_location = "living_outfit"
            call neus_lust_label
            menu(screen="custom_choice_enhanced"):
                "Normal":
                    hide screen spell_screen
                    scene living_room3_out1_2 with dissolve
                    neus "Thank you m-, I can finally take off this clothing."
                    scene living_room3_out1_3 with dissolve
                    neus "And don't think I'll forgot about this. You'll have to make it up to me for all those embarrassing words you made me say."
                    $living_room3_outfit_type=0
                    jump living3  
                "Outfit 2[neus_lust_label]"((neus_lust>=100)) if not(living_room3_is_view_outfit_intro2):
                    hide screen spell_screen
                    jump living_room3_outfit2_intro1
                "Outfit 2"((neus_lust>=100)) if (living_room3_is_view_outfit_intro2):
                    hide screen spell_screen
                    scene living_room3_out1_2 with dissolve                      
                    neus "A-Alright."
                    $ living_room3_outfit_type=2                                          
                    jump living_room3_outfit2
                "Outfit 2 intro"((neus_lust>=100)) if (living_room3_is_view_outfit_intro2):
                    hide screen spell_screen
                    jump living_room3_outfit2_intro1
                "Back":
                    jump living_room3_outfit1   
        "Blowjob":
            hide screen spell_screen
            mc "I think I'll choose the first service."
            stop music fadeout 1.0
            scene living_room3_out1_4 with dissolve
            neus "Y-Your humble maid-girlfriend will proceed to clean your blade, Master!"
            scene living_room3_out1_5 with dissolve
            neus "Aaaaah"
            scene living_room3_out1_6 with dissolve
            play char3 suck2
            neus "Suck suck"
            neus "(It's so embarrassing to play the role of a maid)"
            if incest_story:
                neus "(Although I think I'm doing a good job, it seems like my brother is really enjoying it)"
            else:
                neus "(Although I think I'm doing a good job, it seems like he is really enjoying it)"
            neus "(I guess all the practice I've had with this blade served a purpose)"
            menu:
                "Cum":
                    pass
            scene living_room3_out1_7 with flash2
            stop char3
            play charM cum1
            neus "Ahh, it's so hot."
            scene living_room3_out1_8 with dissolve
            neus "(There's more semen than usual, I suppose my roleplay was pleasing...)"
            play char1 gulp1
            scene living_room3_out1_9 with dissolve           
            neus "H-How did my service feel, ''master''?"
            scene living_room3_out1_10 with dissolve            
            mc "Thank you very much, I loved it."
            scene living_room3_out1_11 with dissolve
            neus "(I like his head pat, but it was embarrassing to say all those words)"
            scene black
            "She cleans herself"
            if is_blowjob_outfit<1:
                call addLust(3) from _call_addLust_6
                $ is_blowjob_outfit+=1
        "Sex":
            hide screen spell_screen 
            stop music fadeout 1.0
            scene living_room3_out1_12 with dissolve
            neus "So, ''master'' wants me to clean his sword?"
            scene living_room3_out1_13 with dissolve
            neus "With my e-exclusive sheath, meant only for his sword."
            mc "Sheath, huh?"
            scene living_room3_out1_14 with dissolve
            neus "Quiet, ''master'' and let me do my job."
            mc "I didn't know my servant would be so eager to do their jo-"
            play char1 penetration3
            scene living_room3_out1_15 with dissolve
            neus "Uh"
            scene living_room3_out1_16 with dissolve
            neus "How does it feel, having your sword in my exclusive sheath?"
            mc "Very good, I want to use it every day."
            scene living_room3_out1_17 with dissolve
            play char3 sex2
            neus "Thank you, but it's not available for daily use."
            mc "Well, it feels very wet and tight to me."
            mc "As if it's trying to tell me it wants to be my exclusive sheath everyday and forever."
            neus "Those are just your own fantasies, ''master.''"
            neus "And please hurry, my sheath is getting tired."
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene living_room3_out1_18 with flash2
            neus "Uh."
            neus "How did my service feel, m-master? (What am I even saying?)"
            mc "Very good."
            scene living_room3_out1_19 with dissolve
            neus "Great, but just to clarify, everything I said was just part of my maid roleplay. Don't let it get to your head."
            if incest_story:
                mc "Of course little sister, I understand. It was all part of the ''roleplay''." 
            else:
                mc "Of course, I understand. It was all part of the ''roleplay''." 
            scene living_room3_out1_20 with dissolve
            neus "..."
            scene black
            "She cleans herself"     
            if is_sex_outfit<1:       
                call addLust(4) from _call_addLust_17  
                $ is_sex_outfit+=1    
        "Leave":           
            jump rooms
    jump living_room3_outfit1
label living_room3_outfit2_intro1:
    $ living_room3_is_view_outfit_intro2=True
    mc "Hey, I have a new gift for you."
    scene living_room3_out1_3 with dissolve
    neus "Mmm... Let me see, give it to me. Let's see what kind of unpleasant thing you've got me this time."
    scene living_room3_out2_1 with fadesex
    if incest_story:
        neus "Brother, this one is even smaller. I might as well be naked at this point."
    else:
        neus "This one is even smaller. I might as well be naked at this point."
    mc "That's not a bad idea, but you look really good in this bride-maiden outfit."
    scene living_room3_out2_2 with dissolve
    if incest_story:
        neus "Uh-huh, uh-huh. Yeah, yeah, whatever you say brother. I expect proper compensation afterwards."
    else:
        neus "Uh-huh, uh-huh. Yeah, yeah, whatever you say. I expect proper compensation afterwards."
    mc "It might be my idea, but you’re not exactly resisting."
    scene living_room3_out2_3 with dissolve
    neus "I always end up doing what you want anyway. It's a waste of time to resist, so I give in."
    jump living_room3_outfit2
label living_room3_outfit2:
    scene living_room3_out2_4 with dissolve
    show screen living_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    menu:       
        "Change outfit":
            menu:
                "Normal":
                    hide screen spell_screen
                    scene living_room3_out2_5 with dissolve
                    neus "Okay"
                    $living_room3_outfit_type=0
                    jump living3
                "Outfit 1":
                    hide screen spell_screen
                    scene living_room3_out2_5 with dissolve
                    if incest_story:
                        neus "O-Okay brother"
                    else:
                        neus "O-Okay"
                    $living_room3_outfit_type=1
                    jump living_room3_outfit1
                "Back":
                    jump living_room3_outfit2 
        "Blowjob":
            hide screen spell_screen
            scene living_room3_out2_15 with dissolve
            neus "Okay 'Master'"
            stop music fadeout 1.0
            scene living_room3_out2_16 with dissolve
            neus "lick"
            scene living_room3_out2_17 with dissolve
            neus "ha"
            play char3 deep_suck1
            scene living_room3_out2_18 with dissolve
            neus "Suck suck suck"
            menu:
                "Faster":
                    pass
            scene living_room3_out2_19 with dissolve
            neus "Suck suck suck lick"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene living_room3_out2_20 with dissolve
            neus "Uh!"
            scene living_room3_out2_21 with dissolve
            ""
            play char1 gulp1
            scene living_room3_out2_22 with dissolve
            neus "Glup"
        "Sex":
            hide screen spell_screen
            scene living_room3_out2_6 with dissolve
            neus "Well, I guess I'll have to do my job"
            stop music fadeout 1.0
            scene living_room3_out2_7 with fade
            neus "So, how do you want me to serve you?"
            scene living_room3_out2_8 with dissolve
            neus "Dear ''master''"
            neus "I suppose you want to put your sword in my e-exclusive sheath"
            scene living_room3_out2_9 with dissolve
            play char1 penetration2
            neus "Uh"
            neus "How does it feel? Does it feel wet and warm?"
            neus "I'm going to start moving"
            scene living_room3_out2_10 with dissolve
            play char3 sex2
            neus "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"
            neus "Your sword is very big, and I feel like you're going to break me"
            neus "It's touching so deep, it reaches my womb"
            scene living_room3_out2_11 with dissolve
            neus "I'm going to cum, I'm going to cum"            
            stop char3
            play charM cum1
            scene living_room3_out2_12 with dissolve
            play char1 climax1
            neus "Uh"
            if incest_story:
                neus "(My brother's sperm is drowning my eggs)"
            else:
                neus "(His sperm is drowning my eggs)"
            scene living_room3_out2_13 with dissolve
            neus "Did using me as your exclusive sheath make you happy, m-master"
            mc "Yes, I loved it"
            scene living_room3_out2_14 with dissolve
            neus "Great, but I can't allow you to keep using my s-sheath, it's very tired"
            scene black with dissolve
            "After a few minutes, she recovers and cleans herself"
        "Leave":           
            jump rooms
    jump living_room3_outfit2
label tv_event3:    
    scene living0_16 with dissolve        
    ""   
    jump time_advances
#----------------------------Object---------------------------------
label key_attic:
    scene living1_21
    if quest_v2:
        $questSide_v2_5.completion = True
    else:
        $questSide_4.completion = True
    "You found the key to the attic."
    $ is_change_quest = True
    call notify_personalized(_("Side Quest updated")) from _call_notify_personalized_34
    $ inventory.add_item(key_room_attic)
    jump rooms
label newspaper_living:
    scene living0_18
    "The newspaper headline says, ''Tribute is paid to those who fell in the war between humans and wizards 2 years ago.''"
    $ inventory.add_item(item_newspaper_living)
    jump rooms

