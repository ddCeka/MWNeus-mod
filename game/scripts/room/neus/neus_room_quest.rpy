image neus0_0 = DynamicAnimation(
["rooms/neus/lvl0/neus0_0_0.webp",
"rooms/neus/lvl0/neus0_0_1.webp", 
"rooms/neus/lvl0/neus0_0_2.webp"])
image neus1_2 = DynamicAnimation(
["rooms/neus/lvl1/neus1_2_0.webp",
"rooms/neus/lvl1/neus1_2_1.webp",
"rooms/neus/lvl1/neus1_2_2.webp",])
image neus2_2_0 = DynamicAnimation(
["rooms/neus/lvl2/neus2_2_0_0.webp",
"rooms/neus/lvl2/neus2_2_0_1.webp",
"rooms/neus/lvl2/neus2_2_0_2.webp",])
image neus3_2_0 = DynamicAnimation(
["rooms/neus/lvl3/neus3_2_0_0.webp",
"rooms/neus/lvl3/neus3_2_0_1.webp",
"rooms/neus/lvl3/neus3_2_0_2.webp",])
image neus3_out1_1 = DynamicAnimation(
["rooms/neus/lvl3/neus3_out1_1_0.webp",
"rooms/neus/lvl3/neus3_out1_1_1.webp",
"rooms/neus/lvl3/neus3_out1_1_2.webp",])
image neus3_out2_3 = DynamicAnimation(
["rooms/neus/lvl3/neus3_out2_3_0.webp",
"rooms/neus/lvl3/neus3_out2_3_1.webp",
"rooms/neus/lvl3/neus3_out2_3_2.webp",])
default is_view_key_room_neus = False
default allow_room_neus = False
default is_view_wake_up_neus=False
default is_view_personality=False
default is_view_trigger_wake_up_neus_yandere=0
default is_view_wake_up_neus_yandere=False

screen neus_room_quest:
    if quest_v2:
        if not(time==questMain_v2_select.time_event) or not(select_room==neus_routine[time]):
            use expression "neus%s"%neus_event_lvl
    else:
        if not(time==questMain_select.time_event) or not(select_room==neus_routine[time]):
            use expression "neus%s"%neus_event_lvl
    if not(neus_routine[time]=="neus"): 
        imagebutton:
            auto "btn_arrow_right_%s"        
            tooltip _("Attic")
            yalign .5
            xalign 1.0
            action  Jump("attic_room_entrance") 
    if quest_v2:
        if not(questMain_v2_11.completion) and not(neus_routine[time]=="neus"):
            imagebutton:
                auto "btn_book_neus_feel_%s" 
                focus_mask True           
                action Jump("book_neus_feel")
                tooltip _("Book")
    else:     
        if not(questMain_5.completion) and not(neus_routine[time]=="neus"):
            imagebutton:
                auto "btn_book_neus_feel_%s" 
                focus_mask True           
                action Jump("book_neus_feel")
                tooltip _("Book")
    if relationship_level>=2 and not(N_state==1):
        imagebutton:
            auto "btn_box_postday_%s" 
            focus_mask True           
            action Jump("box_postday")
            tooltip _("Box?")    
    if not(N_state==1):
        imagebutton:
            auto "btn_ring_neus_%s" 
            focus_mask True       
            tooltip _("Ring")       
            action  Jump("ring_neus")
    if (neus_event_lvl==2 and time<=3 and not(N_state==1) and not neus_is_evading) or (neus_event_lvl>=3 and time<=3):
        imagebutton:
            auto "btn_bed_event_%s"       
            action Jump ("neus_bed")
            tooltip _("Sleep")
            xpos 500
            ypos 500
    if not(neus_routine[time]=="neus"):
        imagebutton:
            auto "btn_newspaper_bistro_%s" 
            focus_mask True       
            tooltip _("Newspaper")       
            action  Jump("newspaper_bistro")
    if not(neus_routine[time]=="neus"):
        imagebutton:
            auto "btn_baseball_bat_%s" 
            focus_mask True       
            tooltip _("Baseball Bat")       
            action  Jump("baseball_bat")
    if not(neus_routine[time]=="neus"): 
        imagebutton:
            auto "btn_phone_neus_%s" 
            focus_mask True       
            tooltip _("[neusname]'s cell phone")       
            action  Jump("phone_neus")
    if relationship_level>=3  and time<=3: 
        imagebutton:
            auto "btn_event_%s"                   
            tooltip _("Endings") 
            xpos 0
            ypos 140      
            action Jump("menu_regular_ending")
            at event_animation_ending
    if relationship_level>=3 and not(neus3_is_active_outfit):
        if time < 4:
            imagebutton:
                auto "btn_old_photo_s_%s"     
                action Jump("neus3_minigame")
                tooltip _("Special photo")
                pos 350,730
        else:
            imagebutton:
                auto "btn_night_old_photo_s_%s"     
                action Jump("neus3_minigame")
                tooltip _("Special photo")
                pos 350,730

#----------------------------Level 0---------------------------------  
screen neus0:
    pass             
label neus0:
    call rooms_music
    scene neus0_0
    show screen neus_spell        
    menu:
        "Talk":
            jump neus0_talk
        "Kiss" ((not quest_v2 and questMain_2.completion) or (quest_v2 and questMain_v2_5.completion)):
            jump neus0_action
        "Leave":                                
            jump rooms
    jump neus0

label neus0_talk:
    call rooms_music
    scene neus0_0
    hide screen spell_screen    
    menu:
        "What do you want to talk about?"        
        "Book":
            scene neus0_11 with dissolve
            mc "So what is that book about?{w=1.5}{nw}"
            scene neus0_0 with dissolve
            pause 0.1
            scene neus0_1 with dissolve
            neus "Nothing that interests you"                
        "Back":
            jump neus0
    jump neus0_talk   
label neus0_action:
    hide screen spell_screen
    if is_kiss>=1:
        scene neus0_9 with dissolve
        neus "No"
    else:        
        scene neus0_7 with dissolve
        neus "{sc=3}Ha!{/sc}"
        call splash_message(_("Moments later")) from _call_splash_message
        scene neus0_8 with dissolve
        play char1 short_kiss
        pause
        $ is_kiss+=1  
        if quest_v2:
            call addLust(1)
    jump neus0
#----------------------------Level 1---------------------------------  
screen neus1:
    if neus_routine[time]=="neus" and time<=3:      
        imagebutton:
            auto "rooms/neus/lvl1/neus1_0_%s.png"            
            focus_mask True
            tooltip "%s"%neusname
            action Jump("neus1")
    if neus_routine[time]=="neus" and time>=4:      
        imagebutton:
            auto "rooms/neus/lvl1/neus1_1_%s.png"            
            focus_mask True
            tooltip "%s"%neusname
            action Jump("neus_sleep1")

label neus1:
    if neus_room_unlocked and not(is_view_key_room_neus):
        stop music fadeout 1.0
        scene neus1_3 with dissolve        
        neus "Hey, how did you get in?"
        scene neus1_4 with dissolve
        mc "I found the key. Do you want it?"
        scene neus1_5 with dissolve
        neus "Mmm no"
        $ unlock_enter = "Enter room"
        $is_view_key_room_neus=True
    call rooms_music
    scene neus1_2
    show screen neus_spell        
    menu:
        "Talk":
            jump neus1_talk
        "Action":
            jump neus1_action
        "Leave":                                
            jump rooms
    jump neus1

label neus1_talk:
    scene neus1_2
    hide screen spell_screen    
    menu:
        "What do you want to talk about?"        
        "Wake me up" if not(is_wake_up_neus):
            if is_view_wake_up_neus:
                scene neus1_6 with dissolve
                if incest_story:
                    neus "Hmm, okey brother"
                else:
                    neus "Hmm, okey"
            else:            
                scene neus1_6 with dissolve
                if incest_story:
                    neus "Hmm, okey brother"
                else:
                    neus "Hmm, okey"
                scene neus1_7 with dissolve 
                mc "Here's the key to my room"
                scene neus1_8 with dissolve
                neus "I don't need it"
                mc "..."
                $is_view_wake_up_neus=True
            $is_wake_up_neus=True
        "Don't wake me up" if is_wake_up_neus:          
            $is_wake_up_neus=False
        "Back":
            jump neus1
    jump neus1_talk
label neus1_action:
    call rooms_music
    scene neus1_2
    hide screen spell_screen  
    menu:
        "What do you want to do?"        
        "Kiss":
            scene neus1_9 with dissolve
            neus "Hmm"            
            scene neus1_10 with dissolve 
            play char1 short_kiss               
            "" 
            if is_kiss<1:
                if quest_v2:
                    call addLust(1)
                $ is_kiss+=1 
        "Handjob":           
            scene neus1_11 with dissolve
            neus "?"
            scene neus1_12 with circlefx 
            if incest_story:
                neus "(When did my brother get this big?)"
            else:
                neus "(When did he get this big?)"
            scene neus1_13 with dissolve 
            neus "Can you hurry up?"
            call splash_message(_("Moments later")) from _call_splash_message_9
            play charM cum1
            scene neus1_14 with flash2 
            ""
            scene black with dissolve 
            "She cleans herself"
            if is_handjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_handjob+=1
        "Blowjob" ((not quest_v2 and questMain_4.completion) or (quest_v2 and questMain_v2_9.completion)):  
            scene neus1_25 with dissolve 
            neus "How annoying... fine" 
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            scene neus1_26 with dissolve 
            neus "(It smells weird)"
            scene neus1_27 with dissolve 
            neus "(And tastes weird)"
            scene neus1_28 with dissolve
            play char3 suck2 
            menu:
                "Inside"((not quest_v2 and questMain_5.completion) or (quest_v2 and questMain_v2_11.completion)):
                    stop char3
                    play charM cum1                    
                    scene neus1_29 with flash2 
                    neus "{sc=3}Hmm{/sc}"
                    scene neus1_30 with dissolve 
                    ""
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus1_31 with flash2
                    ""        
            $ renpy.music.set_volume(1.0, delay=2.0, channel='music')  
            scene black with dissolve 
            "She cleans herself"
            if is_blowjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob+=1
        "Back":
            jump neus1    
    jump neus1_action

label neus_sleep1:
    #play music lazy_night fadeout 1.0 fadein 1.0 if_changed volume 0.15
    show screen neus_spell
    scene neus1_15 with dissolve    
    menu:
        "Try wake her up" if is_view_trigger_wake_up_neus_yandere==0:  
            hide screen spell_screen
            $ is_view_wake_up_neus_yandere = True
            $ is_view_trigger_wake_up_neus_yandere=1     
            if incest_story:
                "You try to wake your little sister, but she doesn't awaken; she seems to be in a deep sleep."
            else:     
                "You try to wake her up, but she doesn't awaken; she seems to be in a deep sleep."
        "Try wake her up again" if is_view_trigger_wake_up_neus_yandere==1:
            hide screen spell_screen
            $ is_view_trigger_wake_up_neus_yandere=2       
            if incest_story:
                "You try to wake up your little sister again, but she doesn't awaken; she seems to be in a deep sleep, {color=#cc0066}but something feels different.."
            else:   
                "You try to wake her up again, but she doesn't awaken; she seems to be in a deep sleep, {color=#cc0066}but something feels different.."
        "Blowjob" if is_view_wake_up_neus_yandere:
            hide screen spell_screen
            scene neus1_32 with dissolve 
            ""
            scene neus1_33 with dissolve 
            play char3 suck2 
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus1_34 with flash2
                    ""
                    scene neus1_35 with dissolve
                    ""                    
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus1_36 with flash2
                    "" 
            scene black with dissolve
            "You clean the scene." 
            $ sleep_action = True
            $ sleep_blowjob = True
        "Footjob" if is_view_wake_up_neus_yandere:
            hide screen spell_screen
            scene neus1_16 with dissolve
            ""
            play char3 handjob2  fadeout 1.0
            scene neus1_17 with dissolve
            ""
            stop char3
            play charM cum1
            scene neus1_18 with flash2
            ""
            scene black with dissolve
            "You clean the scene."  
            $ sleep_action = True    
        "Leave":
            hide screen spell_screen
            if is_view_trigger_wake_up_neus_yandere==2 and not sleep_action:
                play music the_truth_is_in_the_dark volume 0.5 fadeout 1.0
                scene neus2_24 with w21
                if incest_story:
                    neus_ny "Big brother, why are you leaving?"
                else:
                    neus_ny "Why are you leaving?"
                scene neus2_24_1 with dissolve
                neus_ny "I give you permission to have fun with my body"
                neus_ny "I don't think she would mind"
                $ sleep_action = True
                stop music fadeout 0.5
                jump neus_sleep1  
            jump rooms
    jump neus_sleep1
#----------------------------Level 2--------------------------------- 
screen neus2:
    if neus_routine[time]=="neus" and time<=3: 
        if N_state==1:  
            if is_sexpussy>=1:   
                imagebutton:
                    auto "rooms/neus/lvl2/neus2_0_2_%s.png"            
                    focus_mask True
                    tooltip "%s"%neusname
                    action Jump("neus2")
            else:
                imagebutton:
                    auto "rooms/neus/lvl2/neus2_0_1_%s.png"            
                    focus_mask True
                    tooltip "%s"%neusname
                    action Jump("neus2")
        else:
            imagebutton:
                auto "rooms/neus/lvl2/neus2_0_0_%s.png"            
                focus_mask True
                tooltip "%s"%neusname
                action Jump("neus2")
    
    if neus_routine[time]=="neus" and time>=4:      
        imagebutton:
            auto "rooms/neus/lvl2/neus2_1_%s.png"            
            focus_mask True
            tooltip "%s"%neusname
            action Jump("neus_sleep2")
label neus2: 
    if neus_is_evading:
        scene black
        if incest_story:
            "Your sister notices your presence and kicks you out of her room"
        else:
            "She notices your presence and kicks you out of her room"
        jump time_advances 
    if N_state==1:
        stop music fadeout 1.0
        if is_sexpussy>=1:
            play char3 breathing2 volume 0.3 fadeout 1.0
            scene neus2_2_1_1
        else:
            play char3 breathing1 fadeout 1.0
            scene neus2_2_1_0           
    else:
        call rooms_music
        scene neus2_2_0    
    show screen neus_spell        
    menu:
        "Blowjob"((not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion)) if (N_state==1 and is_sexpussy==0):
            stop char3 fadeout 1.0
            hide screen neus_spell
            scene black with dissolve 
            neus "?"
            play char3 suck2
            scene neus2_66 with dissolve
            ""
            stop char3
            play charM cum1
            scene neus2_67 with flash2
            neus "Mmm!"
            scene black with dissolve                   
            "She cleans herself"
            if is_blowjob_more<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob_more+=1
            jump neus2
        "More"((not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion)) if N_state==1:
            hide screen neus_spell
            stop char3 fadeout 1.0
            if is_sexpussy>=1:
                scene black with dissolve
                if incest_story:
                    "Your little sister is so tired that she offers no resistance."
                else:
                    "[neusname] is so tired that she offers no resistance."
                play char3 sex2
                scene neus2_64 with dissolve
                neus "Haaa Haaa Haaa"               
                stop char3
                play charM cum1 
                scene neus2_65 with flash2
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
                scene black with dissolve
                if incest_story:
                    neus "Mmmm brother?"
                else:
                    neus "Mmmm?"
                scene neus2_59 with dissolve                                               
                neus "No more, please."                
                play char3 sex2
                scene neus2_60 with dissolve
                neus "Haaa haaa haaa"               
                scene neus2_61 with dissolve
                neus "Mmm!{w=1.0}{nw}"                
                stop char3
                play charM cum1                
                scene neus2_62 with flash2
                neus "Uhhhh"
                scene neus2_63 with dissolve
                ""                
                $is_sexpussy+=1
                if is_sex_more<1:
                    if quest_v2:
                        call addLust(3)
                    $ is_sex_more+=1
            jump neus2
        "Talk"if N_state==0:
            jump neus2_talk
        "Action"if N_state==0:
            jump neus2_action
        "Leave":    
            stop char3 fadeout 1.0                            
            jump rooms
    jump neus2

label neus2_talk:
    scene neus2_2_0
    hide screen spell_screen    
    if incest_story:
        $ menu_text = "Hmm, okey brother"
    else:
        $ menu_text = "Hmm, okey"
    menu:
        "What do you want to talk about?"        
        "Wake me up" if not(is_wake_up_neus):
            scene neus2_3 with dissolve           
            neus "[menu_text]"            
            $is_view_wake_up_neus=True
            $is_wake_up_neus=True
        "Don't wake me up" if is_wake_up_neus:           
            $is_wake_up_neus=False
        "Propose a date":
            scene neus2_4 with dissolve
            neus "No, thanks"
            mc "There will be cakes"
            scene neus2_5 with dissolve
            neus "..."
            stop music fadeout 1.0
            play ambience people fadein 0.5 volume 0.2
            scene neus2_6 with circlefx
            neus "These are so good!"        
            stop ambience fadeout 1.0  
            call splash_message(_("Moments later")) from _call_splash_message_22
            play ambience morning_sounds fadein 0.5
            scene neus2_12 with dissolve
            neus "That food was so delicious."
            menu:
                "Go to a hotel":
                    stop ambience fadeout 1.0
                    play music Trance_Steele volume 0.1
                    scene neus2_53 with dissolve
                    neus "You can slow down a bit..."
                    scene neus2_54 with dissolve
                    neus "Haahh"
                    play char3 sex2
                    scene neus2_55 with dissolve
                    menu:
                        "Inside":
                            stop char3
                            play charM cum1
                            scene neus2_56 with flash2 
                            neus "{sc=3}Hmm{/sc}"                                            
                        "Outside":
                            stop char3
                            play charM cum1
                            scene neus2_57 with flash2
                            ""
                    scene black with dissolve
                    stop music fadeout 1.0
                    "Afterwards, we returned home."
                    $ neus_left_room = True
                    if quest_v2:
                        call addLust(3)
                "Go home.":
                    stop ambience fadeout 1.0
                    scene black with dissolve
                    "Afterwards, we returned home."
            jump expression "sleeping_event%s"%mc_event_lvl            
        "Back":
            jump neus2
    jump neus2_talk
label neus2_action:
    call rooms_music
    scene neus2_2_0
    hide screen spell_screen  
    menu:
        "What do you want to do?"                
        "Blowjob": 
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            neus "..."
            scene neus2_13 with dissolve
            play char3 suck2  
            neus "Uhhh"         
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus2_14 with flash2 
                    neus "{sc=3}Hmm!{/sc}"
                    scene neus2_15 with dissolve 
                    ""
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus2_16 with flash2
                    ""         
            $ renpy.music.set_volume(1.0, delay=2.0, channel='music')    
            scene black with dissolve 
            "She cleans herself"
            if is_blowjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob+=1
        "Sex":                  
            scene neus2_25 with dissolve
            neus "...(Here we go again.)" 
            stop music fadeout 1.0
            scene neus2_26 with fadesex
            if incest_story:
                neus "Be gentle, please brother."
            else:
                neus "Be gentle, please."
            scene neus2_27 with dissolve
            play char1 penetration2
            neus "{sc=3}Ahhh{/sc}"
            play char3 sex2
            scene neus2_28 with dissolve
            menu:
                neus "Can you cum outside, please."
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus2_29 with flash2 
                    neus "{sc=3}Hmm{/sc}"
                    scene neus2_30 with dissolve 
                    neus "Same thing again..."
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus2_31 with flash2
                    neus "{sc=2}Uhhh{/sc}"
                    neus "Thank you for not cumming inside."         
            menu:
                "More"((not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion)):
                    scene black with dissolve                    
                    neus "How are you not tired yet?"
                    play char3 sex2
                    scene neus2_58 with dissolve
                    neus "Haa Haaa Haaa Haaa"
                    stop char3
                    scene black with dissolve
                    "You cum a few more times"
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
                    jump neus2 
                "Leave": 
                    scene black with dissolve                   
                    "She cleans herself"  
            if is_sex<1:
                if quest_v2:
                    call addLust(3)
                $ is_sex+=1      
        "Back":
            jump neus2    
    jump neus2_action

label neus_sleep2:
    show screen neus_spell
    scene neus2_17 with dissolve    
    if incest_story:
        $ menu_text = "big brother"
    else:
        $ menu_text = firstname
    menu:
        neus "*Dream* Hmm, don't be so rude to me [menu_text] {e_heartbt=FF0000}"
        "Try wake her up" if is_view_trigger_wake_up_neus_yandere==0:
            hide screen spell_screen
            $ is_view_wake_up_neus_yandere = True
            $ is_view_trigger_wake_up_neus_yandere=1 
            scene neus2_32 with dissolve   
            if incest_story:
                "You try to wake up your little sister, but she doesn't awaken; she seems to be in a deep sleep."
            else:            
                "You try to wake her up, but she doesn't awaken; she seems to be in a deep sleep."
        "Try wake her up again" if is_view_trigger_wake_up_neus_yandere==1:
            hide screen spell_screen
            $ is_view_trigger_wake_up_neus_yandere=2
            scene neus2_32 with dissolve  
            if incest_story:
                "You try to wake up your little sister, but she doesn't awaken; she seems to be in a deep sleep, {color=#cc0066}but something feels different.."
            else:             
                "You try to wake her up, but she doesn't awaken; she seems to be in a deep sleep, {color=#cc0066}but something feels different.."
        "Sleep"((neus_is_evading==False)):
            hide screen spell_screen
            scene neus2_45 with dissolve
            ""      
            call splash_message(_("The next day")) from _call_splash_message_24     
            play ambience morning_sounds fadein 1.0         
            scene neus2_46 with dissolve  
            if incest_story:
                neus "*Yawning* I haven't had a sleep that relaxing since those times I slept with my brother when we were younger."
            else:
                neus "*Yawning* I haven't had a sleep that relaxing since that time I slept with [firstname] when we were younger."
            scene neus2_47 with dissolve
            neus "Uhhh?" 
            scene neus2_48 with dissolve     
            if incest_story:
                neus "H-hey, brother? What are you doing in my bed?"
                mc "Good morning little sister."
            else:
                neus "H-hey, what are you doing in my bed?"
                mc "Good morning."
            scene neus2_49 with dissolve
            neus "Don't avoid my question. Good morning"
            if (not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion):
                mc "Sleeping with my girlfriend."
                neus "..."
                menu:
                    "Sex":
                        scene neus2_50 with dissolve 
                        if incest_story:
                            neus "H-Hey, what are you doing brother?" 
                        else:
                            neus "H-Hey, what are you doing?" 
                        mc "Nothing like a good fucking to wake up"
                        scene neus2_51 with dissolve 
                        neus "uhhh"
                        call splash_message(_("Moments later")) from _call_splash_message_25
                        scene neus2_52 with dissolve 
                        ""
                        $N_state=1
                    "Leave":
                        $N_state=0
            else:
                if incest_story:
                    mc "I wanted to sleep with my little sister like when we were younger."
                else:
                    mc "I wanted to sleep with you."
                neus "..."
                scene black with dissolve
                "She quickly gets out of bed and leaves." 
                $N_state=0 
            jump next_day_neus
        "Blowjob" if is_view_wake_up_neus_yandere: 
            hide screen spell_screen
            scene neus2_18 with dissolve
            play char3 suck2
            neus "Mmm"
            neus "*While sleeping* (A little slower.)"               
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus2_19 with flash2 
                    neus "*While sleeping* Hmm"                    
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus2_20 with flash2
                    ""                 
            scene black with dissolve
            "You clean the scene." 
            $ sleep_action = True    
        "Sex" if is_view_wake_up_neus_yandere:  
            hide screen spell_screen
            $is_sexpussy=+1         
            scene neus2_33 with dissolve
            ""
            scene neus2_34 with dissolve
            ""
            play char3 sex2
            scene neus2_35 with dissolve
            menu:                
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus2_36 with flash2 
                    if incest_story:
                        neus "*While sleeping* Hmm, don't cum inside brother"  
                    else:
                        neus "*While sleeping* Hmm, don't cum inside"                    
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus2_37 with flash2
                    ""
            scene black with dissolve
            "You clean the scene."    
            $ sleep_action = True           
        "Leave": 
            hide screen spell_screen
            if is_sexpussy>=1:

                scene neus2_24 with w21
                "{w=.5}{nw}"
                call splash_message(_("Next day.")) from _call_splash_message_26
                $N_state=1
                jump next_day  
            elif is_view_trigger_wake_up_neus_yandere==2 and not sleep_action:
                play music the_truth_is_in_the_dark volume 0.3 fadeout 1.0
                scene neus2_24 with w21
                if incest_story:
                    neus_ny "Big brother, why are you leaving?"
                else:
                    neus_ny "Why are you leaving?"
                scene neus2_24_1 with dissolve
                neus_ny "I give you permission to have fun with my body"
                neus_ny "I don't think she would mind"
                stop music fadeout 0.5
                $ sleep_action = True
                jump neus_sleep2                                             
            jump rooms
    jump neus_sleep2
#----------------------------Level 3--------------------------------- 
default neus3_outfit_type=0
default neus3_is_view_outfit_intro=False
default neus3_is_view_outfit_intro2=False
default neus3_is_active_outfit=False
screen neus3:
    if neus_routine[time]=="neus" and time<=3:  
        if neus3_outfit_type==0:         
            imagebutton:
                auto "rooms/neus/lvl3/neus3_0_0_%s.png"            
                focus_mask True
                tooltip "%s"%neusname
                action Jump("neus3")
        if neus3_outfit_type==1:
            imagebutton:
                auto "rooms/neus/lvl3/neus3_out1_0_%s.png"            
                focus_mask True            
                action Jump("neus3_outfit1")
                tooltip "%s"%neusname
        if neus3_outfit_type==2:
            imagebutton:
                auto "rooms/neus/lvl3/neus3_out2_0_%s.png"            
                focus_mask True            
                action Jump("neus3_outfit2")
                tooltip "%s"%neusname
    if neus_routine[time]=="neus" and time>=4:      
        imagebutton:
            auto "rooms/neus/lvl3/neus3_1_%s.png"            
            focus_mask True
            tooltip "%s"%neusname
            action Jump("neus_sleep3")
label neus3:
    scene neus3_2_0
    show screen neus_spell  
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed      
    menu:
        "Talk":           
            jump neus3_talk
        "Action":
            jump neus3_action        
        "Outfit":
            if not(neus3_is_view_outfit_intro):
                menu:                
                    "Requirements: Object creation: {color=#cc0066}[spell_2_2.is_active]{/color} and outfit photo: {color=#cc0066}[neus3_is_active_outfit]{/color}"
                    "Outfit 1"((neus3_is_active_outfit and spell_2_2.is_active)): 
                            hide screen spell_screen                                 
                            jump neus3_outfit1_intro1                                      
                    "Back":
                        jump neus3  
            else:
                menu:      
                    "Outfit 1":
                        hide screen spell_screen       
                        scene neus3_4 with dissolve
                        neus "Alright."
                        $neus3_outfit_type=1 
                        jump neus3_outfit1   
                    "Outfit 2"((neus_lust>=100)) if (neus3_is_view_outfit_intro2):
                        hide screen spell_screen     
                        scene neus3_4 with dissolve              
                        neus "A-Alright."
                        $ neus3_outfit_type=2
                        jump neus3_outfit2
                    "Outfit 1 intro"((neus3_is_active_outfit and spell_2_2.is_active)): 
                        hide screen spell_screen                                     
                        jump neus3_outfit1_intro1    
                    "Back":
                        jump neus3       
        "Leave":                                
            jump rooms
    jump neus3
label neus3_talk:
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed    
    scene neus3_2_0
    hide screen spell_screen
    if not is_neus_sec_dis:
        $ xsize_value = 650
    else:
        $ xsize_value = 600
    menu(screen="custom_choice_enhanced"):
        "What do you want to talk about?"  
        "Propose a date":   
            scene neus3_4 with dissolve           
            menu:
                neus "Where do you want to go?"
                "Special Restaurant (Level:[lvl_event_date_sr]/2)": 
                    if lvl_event_date_sr==0:
                        jump special_restaurant1
                    elif lvl_event_date_sr==1:
                        jump special_restaurant2
                    else:
                        menu:
                            "Event 1":
                                jump special_restaurant1
                            "Event 2":
                                jump special_restaurant2
                            "Leave":
                                jump neus3_talk        
        "Wake me up" if not(is_wake_up_neus):            
            neus "Okey"            
            $is_wake_up_neus=True
        "Don't wake me up" if is_wake_up_neus:          
            $is_wake_up_neus=False
        "???\n(Requires: ''Confront'')"(False) if not(is_neus_sec_dis):
            pass
        "Talk to ''Her''" if is_neus_sec_dis: 
            hide screen neus_spell           
            mc "Hey, can I talk to her for a while?"
            scene neus3_pt_0 with dissolve
            neus "Wh-"
            play sound whoosh1
            scene neus3_pt_1 with pushle
            play music lazy_night volume 0.3 fadeout 1.0
            neus_yan "Tell me what you want to talk about."
            if incest_story:
                $ menu_text = "Our parents"
            else:
                $ menu_text = "Your parents"
            menu:                
                "What do we want to talk about?"                
                "[menu_text]":
                    if incest_story:
                        mc "Did our parents know about your condition?"
                        scene neus3_pt_2 with dissolve
                        neus_yan "No, I only recently emerged after failing to suppress my feelings for you."
                        neus_yan "Not that they would’ve noticed anyway. They were always too busy with work."
                        mc "Yeah, you’re probably right. We barely saw them with how busy they were."
                        mc "Running a business that big must’ve been exhausting."
                        mc "I guess I got a bit lucky in that sense. When they passed, most of their work got re-assigned."
                        mc "By the time I was old enough to step in, the workload had already been divided up, so there wasn’t nearly as much for me to deal with."
                        scene neus3_pt_3 with dissolve
                        neus_yan "Since we're on the topic, there are some things that feel... unclear to me."
                        neus_yan "There are moments I remember so vividly… the pain of losing them is one of them."
                        neus_yan "But everything else? It's blurred, like my mind didn’t want to hold onto anything but you."
                        neus_yan "Please brother, could you tell me how they died?"
                    else:
                        mc "Do my in-laws know about your condition?"
                        scene neus3_pt_2 with dissolve
                        neus_yan "No, I only recently emerged after failing to suppress my feelings for you."
                        neus_yan "Although I don't think they would have found out either way, they're always traveling."
                        mc "I suppose you're right. I rarely see them."
                        mc "It must be quite hectic being a landscape photographer and a flight attendant."
                        scene neus3_pt_3 with dissolve
                        neus_yan "Since we're on the topic, there's a certain type of information that's blurry to me."
                        neus_yan "Like that of your parents. If I had known, I wouldn't have manipulated you with something like that."
                        neus_yan "If you don't mind, could you tell me what happened to them?"
                    mc "Why the sudden politeness? I thought you harbored all their negative feelings."
                    scene neus3_pt_4 with dissolve
                    neus_yan "Noo, you're wrong. It’s not the negative feelings—it's the most intense ones that end up becoming repugnant."
                    scene neus3_pt_5 with dissolve
                    neus_yan "But... I guess you’re not entirely wrong. I’ll give you a point for that."
                    if incest_story:
                        mc "Mmm... at first, it was announced that our parents died in an accident."
                    else:
                        mc "Mmm... at first, it was announced that my parents died in an accident."
                    mc "But that wasn’t the truth—they were murdered."
                    mc "Although I've resolved that matter. I put the culprits underground."
                    mc "But before that, I made sure they suffered for what they did, whe-"
                    scene neus3_pt_6 with dissolve
                    neus_yan "You cut off each of their fingers, then sent them to their loved ones to demand a ransom."
                    scene neus3_pt_7 with dissolve
                    if incest_story:
                        neus_yan "And right when they were filled with hope of being set free, you killed their loved ones right in front of them, making them feel the same agony we endured."(multiple=2)
                    else:
                        neus_yan "And right when they were filled with hope of being set free, you killed their loved ones right in front of them, making them feel the same agony you endured."(multiple=2)
                    mc "Just kidding, they're in an underground prison. I haven't killed anyone."(multiple=2)
                    neus_yan "And to end their torment and set them free, you killed them."(multiple=2)
                    mc "(Where did she get that knife? Yandere powers?)"(multiple=2)
                    scene neus3_pt_8 with dissolve
                    if incest_story:
                        neus_yan "And then you assumed the leadership of our parents' organization, now controlling the fate of all humans, witches and wizards from the shadows."
                        mc "Not quite, the organization our parents led was more of an intermediary for trade agreements between both races."
                        mc "And recently, they removed me from my position. They weren't very happy with how much time I've been taking off to be with you."
                    else:
                        neus_yan "And then you assumed the leadership of your parents' organization, now controlling the fate of all humans, witches and wizards from the shadows."
                        mc "Not quite, the organization my parents led was more of an intermediary for trade agreements between both races."
                        mc "And recently, they removed me from my position. They weren't very happy with how much time I've been taking off to be with you."
                    scene neus3_pt_3 with dissolve
                    neus_yan "Oh, I got carried away, {size=-15}hehe."
                    neus_yan "And I'm sorry... it's my fault you're unemployed now."
                    mc "No problem. I saved plenty of money, with the intention of having many children with you. I believe it's enough for around 21 to 24 children."
                    mc "Plus, I still have the shares."
                    scene neus3_pt_9 with dissolve
                    neus_yan "Oh, that's good to hear."
                    scene neus3_pt_10 with dissolve
                    neus_yan "I will make my greatest effort to fulfill your dream."             
                    mc "It feels strange telling you this story for the second time. Are you sure you don't remember?"
                    scene neus3_pt_2 with dissolve
                    neus_yan "No, there's a certain class of information I don't have access to."
                    scene neus3_pt_11 with dissolve
                    neus_yan "Uh, we'll have to leave it here. She's about to wake up."
                    jump neus3
                "Leave":
                        jump neus3_talk
        "Back":
            jump neus3
    jump neus3_talk
label neus3_action:
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed  
    scene neus3_2_0
    hide screen neus_spell
    menu:
        "What do you want to do?"     
        "Blowjob":
            scene neus3_5 with dissolve                    
            neus "I guess it can't be helped."
            neus "Just let me get comfortable so you can use my mouth."
            stop music fadeout 1.0
            scene neus3_6 with fade    
            play sound ahegao2 volume 1.0
            neus "*opening her mouth* Haaaaaa"
            scene neus3_7 with dissolve 
            play char3 suck2
            neus "*sucking* lick lick"
            neus "*Suck suck*"
            menu:
                "Deeper":
                    pass
            scene neus3_8 with fadesex  
            neus "(So deep, my throat is a little sensitive.)"
            neus "(but it feels good...)"
            neus "*Suck suck*"
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus3_9 with flash2
                    neus "Ugh!"
                    if incest_story:
                        neus "(My stomach is being filled with lots of my brother's milk.)"
                    else:
                        neus "(My stomach is being filled with lots of milk.)"
                    scene neus3_10 with dissolve
                    play char1 gulp1
                    neus "Gulp"
                    neus "(It tastes pretty good... I think)"
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus3_11 with flash2                    
                    neus "Mmmm."
            scene black with dissolve
            "She cleans herself"
            if is_blowjob<1:
                call addLust(2) from _call_addLust_18
                $ is_blowjob+=1
        "Sex": 
            scene neus3_12 with dissolve  
            if incest_story:
                neus "O-Okay brother"
            else:        
                neus "O-Okay"
            stop music fadeout 1.0
            scene neus3_13 with fade
            neus "..."
            mc "I'm going to insert it now"
            scene neus3_14 with dissolve
            play char1 penetration3 volume 0.4
            neus "Oh"
            neus "So deep"
            scene neus3_15 with fadesex
            play char3 sex2
            neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
            neus "(This feels good)"
            if incest_story:
                neus "(It feels like my womb is kissing my brother's cock)"
            else:
                neus "(It feels like my womb is kissing his cock)"
            neus "(As if it's asking for his seed to fertilize my eggs)"
            neus "(It feels great)"
            neus "(But I must keep my composure)"
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus3_16 with flash2
                    play char1 climax1
                    if incest_story:
                        neus "UHhh (My womb is being filled with my brother's seed)"
                    else:
                        neus "UHhh (My womb is being filled with his seed)"
                    scene neus3_17 with dissolve
                    neus "Satisfied?"
                    if incest_story:
                        mc "Yes, it felt really good, although I would like a little more sis-"
                    else:
                        mc "Yes, it felt really good, although I would like a little more-"
                    scene neus3_18 with dissolve
                    neus "Don't even think about it."                    
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus3_19 with flash2
                    play char1 climax1
                    neus "{sc=2}{=lust_style}AhM{/sc}"
                    neus "That felt somewhat amazing."
            scene black with dissolve
            "She moves away from you and cleans herself up"
            if is_sex<1:
                call addLust(3) from _call_addLust_19
                $ is_sex+=1
        "Anal":
            scene neus3_20 with dissolve
            if incest_story:
                neus "Can't we just have regular sex brother?"
            else:
                neus "Can't we just have regular sex?"
            mc "Come on, just this once."
            scene neus3_21 with dissolve
            neus "Well... (It doesn't feel bad, but it does feel a little strange)."
            stop music fadeout 1.0
            scene neus3_22 with fadesex            
            mc "I'm going to put it in now"(multiple=2)
            neus "(Although I must be careful not to let this happen too often or I may become addicted to anal sex)"(multiple=2)
            scene neus3_23 with dissolve
            play char1 penetration3 volume 0.5
            neus "{sc=2}{=lust_style}Uh{/sc}"
            scene neus3_24 with dissolve
            play char3 sex2
            neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
            if incest_story:
                mc "Does it feel good little sister?"
            else:
                mc "Does it feel good?"
            neus "NO... {bt=2}{=lust_style}ha ha ha{/bt}"
            neus "Well, maybe a little"
            neus "(It's a weird feeling)"
            if incest_story:
                neus "(But it feels so good to have my brother's cock going in and out of my ass)"
            else:
                neus "(But it feels so good to have his cock going in and out of my ass)"
            neus "(No, no, that's wrong, if I continue like this, in the future my ass will feel lonely without his cock inside)"
            neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
            scene neus3_25 with dissolve
            play char1 climax1
            neus "I'm cumming"
            scene neus3_24 with dissolve
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene neus3_26 with flash2
                    play char1 climax1
                    neus "Mmm"
                    scene neus3_27 with dissolve
                    if incest_story:
                        neus "(My ass is so full and hot, and my brother's cum is spilling out of me)"
                    else:
                        neus "(My ass is so full and hot, and his cum is spilling out of me)"
                    neus "(What the hell am I thinking?)"
                "Outside":
                    stop char3
                    play charM cum1
                    scene neus3_28 with flash2
                    play char1 climax1
                    neus "Uh"
                    if incest_story:
                        neus "(My clothes are covered in my brother's cum again, but it's not as bad as him cumming inside me.)"
                    else:
                        neus "(My clothes are covered in his cum again, but it's not as bad as him cumming inside me.)"
                    scene neus3_29 with dissolve
                    neus "(Although it's not like he can get me pregnant by cumming in my ass and I would be spared from cleaning my clothes)"
                    scene neus3_30 with dissolve
                    neus "..."
            scene black with dissolve
            "She moves away from you and cleans herself up"
            if is_sexanal<1:
                call addLust(3) from _call_addLust_20
                $ is_sexanal+=1
        "Back":
            jump neus3
    jump neus3_action
label special_restaurant1:
    if lvl_event_date_sr<=0:
        $lvl_event_date_sr=1
    scene neus3_er_0 with dissolve
    neus "I accept, hmmm... what clothes should I wear?"
    scene neus3_er_1 with dissolve
    if incest_story:
        neus "Hey brother, what are you still doing here?"
    else:
        neus "Hey, what are you still doing here?"
    mc "?"
    scene neus3_er_2 with dissolve
    neus "I know you've seen almost everything of me, but I want my outfit to be a surprise."
    scene black with dissolve
    "You leave the room"
    if incest_story:
        neus "(Hehe, this one is very sexy; I'm sure my brother will love it, but...)"
    else:
        neus "(Hehe, this one is very sexy; I'm sure he'll love it, but...)"
    neus "(He'll probably stop halfway and take me to a hotel, leaving me unable to walk.)"
    neus "(I need something a bit more modest.)"
    neus "(This will do.)"
    stop music fadeout 1.0
    call splash_message(_("After three hours of travel")) from _call_splash_message_55
    play music TheGirlFromBrasil_Hauser volume 0.5
    scene neus3_er_3 with dissolve
    neus "That was indeed a long trip."
    scene neus3_er_4 with dissolve
    neus "By the way, you haven't said anything about my appearance, do I look bad with this makeup? Do I look like a clown?"
    mc "The makeup looks good on you, although it's not necessary since you are naturally beautiful."
    scene neus3_er_5 with dissolve
    neus "Thank you..."
    mc "Although I would have liked to see you in... never mind, you still look very lovely."        
    scene neus3_er_6 with dissolve    
    mc "Yes, we're here for the reservation for two."(multiple=2)
    neus "(Mmm... Next time, I'm going to wear that dress...)"(multiple=2)
    scene neus3_er_7 with fade
    neus "The food here is delicious"
    scene neus3_er_8 with dissolve
    waitress "What would you like to drink?"
    mc "Just a juice for me, please."
    scene neus3_er_9 with dissolve
    neus "I would like this wine here, please. "
    scene neus3_er_10 with fade
    if incest_story:
        neus "Brother, are you sure you don't want some?"
    else:
        neus "Are you sure you don't want some?"
    mc "The trip is very long, and besides, if I recall correctly, you don't handle alcohol well."
    scene neus3_er_11 with dissolve
    neus "That's in the past, I can handle myself."
    menu:
        "Drink with her":       
            stop music fadeout 0.5
            scene neus3_er_12 with fade
            neus "You are so boring, Mr. Mushroom, why don't you drink more wine?"
            scene neus3_er_13 with dissolve
            play music funk_funkadelic_funkstorm fadeout 0.5 volume 0.4  
            mc "..."(multiple=2)
            neus "Come on, Mr. Mushroom, have a drink with me, let's have fun."(multiple=2)
            if incest_story:
                mc "It's incredible that you're in this state just after two glasses sister... \nthat's 0 alcohol tolerance."
            else:
                mc "It's incredible that you're in this state just after two glasses... \nthat's 0 alcohol tolerance."
            scene neus3_er_14 with dissolve            
            neus "Shoes off"
            scene neus3_er_15 with dissolve
            if incest_story:
                neus "Hey, don't you want to have some fun with your little sister's body? I'll let you use any part you want."
            else:
                neus "Hey, don't you want to have some fun with your girlfriend's body? I'll let you use any part you want."
            scene neus3_er_16 with dissolve
            neus "*Sucking finger* \nMy mouth "
            scene neus3_er_17 with dissolve
            neus "My breasts ...{w=1.0}{nw}"
            scene neus3_er_18 with dissolve
            neus "Ugh, forget it."
            scene neus3_er_19 with dissolve
            neus "Oh, my ..."
            scene neus3_er_20 with dissolve
            if incest_story:
                $ menu_text = "What do you say big brother?"
            else:
                $ menu_text = "What do you say?"
            menu:
                neus "[menu_text]"
                "Accept offer":               
                    $ renpy.music.set_volume(0.2, delay=3.0, channel='music')
                    scene neus3_er_21 with fade             
                    neus "Yay, some fun, then..."
                    scene neus3_er_22 with dissolve
                    neus "Let's start with my mouth."
                    scene neus3_er_23 with dissolve
                    play char3 suck1
                    neus "Gulp gulp"
                    neus "Mmm"
                    scene neus3_er_24 with dissolve
                    stop char3
                    play charM cum1
                    neus "Mmm"
                    scene neus3_er_25 with dissolve
                    play char1 gulp1 
                    neus "Gulp"
                    scene neus3_er_26 with dissolve
                    neus "How was my blowjob, Mr. Little Mushroom?"
                    scene neus3_er_27 with dissolve
                    play charM slap1
                    neus "Ah!"(multiple=2)
                    mc "This is the third time."(multiple=2)
                    scene neus3_er_28 with dissolve
                    neus "Oh... Mr. Little Mushroom is angry, hahaha."
                    scene neus3_er_29 with fade
                    play char3 suck2
                    neus "(Very deep)"                    
                    neus "(It's touching my throat, it's so big {e_heartbt=FF0000})"                    
                    neus "Gulp gulp"
                    scene neus3_er_30 with dissolve
                    stop char3
                    play charM cum1
                    neus "{sc=3}Ugh{/sc}"
                    scene neus3_er_31 with dissolve
                    neus "That was intense..."
                    scene neus3_er_32 with dissolve
                    neus "You used my mouth as if it were a toy."
                    scene neus3_er_33 with fadesex                    
                    neus "More fun, let's go Mr.-"
                    scene neus3_er_34 with dissolve
                    play char1 penetration1
                    neus "Mmmu!"
                    scene neus3_er_35 with dissolve
                    play char3 sex3
                    neus "aah aah aah"
                    neus "Mmm"
                    neus "So intense!"                    
                    if incest_story:
                        neus "{bt=2}Give me more, more love, please brother.{/bt}"
                    else:
                        neus "{bt=2}Give me more, more love, please.{/bt}"
                    stop char3     
                    stop music fadeout 1.0             
                    scene neus3_er_36 with fadesex     
                    play ambience morning_sounds               
                    neus "(Uhh, my whole body hurts, I can't get up. I only remember having a little wine)."     
                    if incest_story:
                        mc "Do you want me to help you sis?"
                    else:               
                        mc "Do you want me to help you?"
                    scene neus3_er_37 with dissolve
                    neus "What happened yesterday? Please tell me I didn't say anything embarrassing."
                    mc "At first, you were a bit annoying, but then you were very honest and cute."
                    mc "I think you should start drinking to get rid of your tsundere tendencies."
                    mc "Though it would be bad if you became an alcoholic."
                    scene neus3_er_38 with dissolve
                    mc "Besides, you were very intense, and I have some bites as if you were trying to mark your territory, hahaha."     
                    if incest_story:
                        mc "Maybe I'll start doing the same to you little sister, obviously not as aggressively, just some love bites."
                        scene neus3_er_39 with dissolve
                        neus "I-I'm sorry brother!"
                        stop ambience fadeout 1.0
                        scene black with dissolve
                        "After resting, you return home with your sister."
                    else:              
                        mc "Maybe I'll start doing the same to you, obviously not as aggressively, just some love bites."
                        scene neus3_er_39 with dissolve
                        neus "I-I'm sorry!"
                        stop ambience fadeout 1.0
                        scene black with dissolve
                        "After resting, you return home with [neusname]."
                    $ renpy.music.set_volume(1.0, channel='music') 
                    call addLust(5) from _call_addLust_9
                "Let her rest":                    
                    scene neus3_er_40 with dissolve
                    neus "Booo, boring... Zzzz."
                    stop music fadeout 1.0
                    scene black with dissolve
                    if incest_story:
                        "The next day, you return home with your sister."
                    else:
                        "The next day, you return home with [neusname]."
        "No, don't allow it":
            scene neus3_er_41 with dissolve
            neus "Alright, then I'll stick with this juice."
            scene neus3_er_42 with dissolve
            neus "It tastes good."
            stop music fadeout 1.0
            scene black with dissolve
            "After a long journey back, we returned home."
            scene neus3_er_43 with dissolve
            if incest_story:
                neus "Thank you for the invitation brother, I had a great time."
            else:
                neus "Thank you for the invitation, I had a great time."
    jump next_day
label special_restaurant2:
    if lvl_event_date_sr<=1:
        $lvl_event_date_sr=2   
    scene neus3_er_2 with dissolve 
    if incest_story:
        neus "Ok, just let me change brother."
    else:
        neus "Ok, just let me change."
    stop music fadeout 1.0
    call splash_message(_("At a hotel...")) from _call_splash_message_56
    scene neus3_er2_0 with dissolve 
    play char3 suck2
    neus "Gulp, gulp."    
    neus "Mmm."    
    if incest_story:
        mc "Sister, your blowjobs are the best."
    else:
        mc "Your blowjobs are the best."
    scene neus3_er2_1 with dissolve 
    stop char3
    play charM cum1
    stop music fadeout 1.0
    neus "(Mmm... I don't like that compliment.)"
    scene neus3_er2_2 with dissolve
    neus "Why are we here? We're going to miss the dinner reservation."
    scene neus3_er2_3 with dissolve
    if incest_story:
        mc "Well, that outfit looks great on you sis, I couldn't resist." 
    else:
        mc "Well, that outfit looks great on you, I couldn't resist." 
    scene neus3_er2_4 with dissolve   
    neus "So it's my fault..."
    scene neus3_er2_5 with dissolve 
    mc "I'm calm now. Although I don't like leaving things unfinished, but if we don't, we'll lose the reservation."
    play char1 lick01
    scene neus3_er2_6 with dissolve   
    neus "Wait... I can't leave like this, my makeup is a mess."
    if incest_story:
        mc "We still have 2 hours of travel, you can fix yourself during the journey, unless you have another reason to stay little sister."
    else:
        mc "We still have 2 hours of travel, you can fix yourself during the journey, unless you have another reason to stay."
    scene neus3_er2_7 with dissolve
    neus "W-well, I guess it wouldn't hurt to miss the {size=-10}reservation."
    play music funk_funkadelic_funkstorm fadeout 0.5 volume 0.4   
    mc "Ok"
    scene neus3_er2_8 with dissolve
    mc "Well, I suppose we can continue where we left off."
    scene neus3_er2_9 with dissolve
    neus "Eh!..."
    mc "Didn't you want this?"
    scene neus3_er2_10 with dissolve
    neus "N-no, and besides, you accepted too easily, you were just teasing me, right?"
    mc "Could be... although if we had gone to the restaurant, I most likely would have taken you to the bathroom for some fun."
    scene neus3_er2_11 with dissolve
    neus "I knew it, you were just teasing me."
    scene neus3_er2_12 with dissolve
    play char1 penetration2
    neus "Ah!"(multiple=2)
    mc "We have a whole night to enjoy."(multiple=2)   
    stop music fadeout 1.0    
    play ambience morning_sounds fadein 2.0
    scene neus3_er2_13 with fadesex
    mc "(I might have gone too far this time as well.)"
    neus "..."
    scene neus3_er2_14 with dissolve
    mc "(I think I'll let her rest, then we'll go back home.)"
    stop ambience fadeout 1.0
    scene black with dissolve
    if incest_story:
        "After a few hours, your sister regains her wits, and you return home with her."
    else:
        "After a few hours, she regains her wits, and you return home with her."
    call addLust(5) from _call_addLust_10
    jump next_day
#----------------------------outfit1--------------------------------- 
label neus3_outfit1_intro1:  
    $neus3_is_view_outfit_intro=True
    $neus3_outfit_type=1    
    if incest_story:
        mc "Hey sister, I have something for you."
    else:
        mc "Hey, I have something for you."
    scene neus3_4 with dissolve
    neus "Hmm... great?"
    scene neus3_oi1_0 with fade
    neus "(I suppose this was to be expected.)"
    scene neus3_oi1_1 with dissolve
    if incest_story:
        neus "Thanks brother, but I'll have to decline."
        mc "Come on sis, why not?"
    else:
        neus "Thanks, but I'll have to decline."
        mc "Come on, why not?"
    scene neus3_oi1_2 with dissolve
    neus "Hmm... No!"
    neus "I know very well that you gave me this bunny suit because you want to do dirty things to me."
    neus "So forget it, it's not going to happen."
    scene neus3_oi1_3 with dissolve
    play sound magical1 volume 0.3
    neus "{sc=1}Eh!?{/sc}"(multiple=2) 
    mc "{font=fonts/Alkatra-Regular.ttf}Touch{/font}"(multiple=2)
    scene neus3_oi1_4 with fadesex
    neus "I-I'm a little bunny who's very hungry."
    scene neus3_oi1_5 with dissolve
    neus "F-For a good carrot."
    if is_view_personality:
        neus "(Damn it, that damn spell is making me say what I think.)"
    else:
        neus "(Damn it, why can’t I stop blurting out my thoughts?)"
    if incest_story:
        mc "How hungry are you little sister?"
    else:
        mc "How hungry are you?"
    scene neus3_oi1_6 with dissolve
    neus "V-Very hungry, I need a big and juicy carrot."
    neus "(I'm going to die of embarrassment, please, someone end my suffering.)"    
    if is_neus_sec_dis:
        scene neus3_oi1_7 with dissolve
        if is_view_personality:
            neus_yan "I love that spell {e_heartbt=FF0000}"(multiple=2)
            neus "(I hate that spell {e_heartbt=FF0000})"(multiple=2)    
        else:
            neus_yan "I love that spell {e_heartbt=FF0000}"(multiple=2)   
            neus "({e_heartbt=FF0000})"
    else:
        scene neus3_oi1_8 with dissolve
        if is_view_personality:
            neus "(I hate that spell {e_heartbt=FF0000})"
        else:
            neus "({e_heartbt=FF0000})"
    call addLust(1)
    jump neus3_outfit1
label neus3_outfit1:
    scene neus3_out1_1
    show screen neus_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    menu:       
        "Change outfit":
            $ xsize_value = 650
            $ neus_lust_label_location = "neus_outfit"
            call neus_lust_label
            menu(screen="custom_choice_enhanced"):
                "Normal":
                    hide screen spell_screen
                    scene neus3_out1_26 with dissolve           
                    neus "Phew, I can finally take this costume off."
                    $neus3_outfit_type=0
                    jump neus3            
                "Outfit 2[neus_lust_label]"((neus_lust>=100)) if not(neus3_is_view_outfit_intro2):  
                    hide screen spell_screen 
                    jump neus3_outfit2_intro1        
                "Outfit 2"((neus_lust>=100)) if (neus3_is_view_outfit_intro2):
                    hide screen spell_screen
                    scene neus3_out1_27 with dissolve                      
                    neus "A-Alright."
                    $ neus3_outfit_type=2
                    jump neus3_outfit2
                "Outfit 2 (intro)"((neus_lust>=100)) if (neus3_is_view_outfit_intro2):
                    hide screen spell_screen
                    jump neus3_outfit2_intro1
                "Back":
                    jump neus3_outfit1
        "Blowjob":
            hide screen spell_screen       
            stop music fadeout 1.0     
            scene neus3_out1_2 with dissolve
            neus "It's time to devour this big carrot."
            scene neus3_out1_3 with dissolve
            neus "Lick"
            scene neus3_out1_4 with dissolve
            neus "Ah."
            scene neus3_out1_5 with fadesex
            play char3 suck4
            neus "Suck suck"
            mc "It looks like you were very hungry."
            neus "Suck suck suck"
            if incest_story:
                mc "(It seems like my sister is so focused that she can't hear me.)"
            else:
                mc "(It seems like she's so focused that she can't hear me.)"
            mc "(Here comes her carrot juice.)"
            scene neus3_out1_6 with dissolve
            stop char3
            play charM cum1
            if incest_story:
                neus "(Mmm... my brother's carrot juice is so delicious.)"
            else:
                neus "(Mmm... this carrot juice is so delicious.)"
            scene neus3_out1_7 with dissolve
            play char1 gulp1
            ""
            scene neus3_out1_8 with dissolve
            play char1 ahegao3
            neus "Ahhhh"            
            scene neus3_out1_9 with dissolve
            if incest_story:
                neus "T-Thanks for the meal brother." 
            else:
                neus "T-Thanks for the meal."  
            scene black with dissolve                   
            "She cleans herself"          
            if is_blowjob_outfit<1:
                call addLust(3) from _call_addLust_21
                $ is_blowjob_outfit+=1
        "Anal([lvl_neus3_out_event_anal]/2)":
            hide screen spell_screen
            if lvl_neus3_out_event_anal==0:
                jump neus3_out_event_anal1
            elif lvl_neus3_out_event_anal==1:
                jump neus3_out_event_anal2
            else:
                menu:
                    "Event 1":
                        jump neus3_out_event_anal1
                    "Event 2":
                        jump neus3_out_event_anal2
                    "Leave":
                        jump neus3_outfit1            
        "Leave":           
            jump rooms
    jump neus3_outfit1
label neus3_out_event_anal1:
    if lvl_neus3_out_event_anal<=0:
        $lvl_neus3_out_event_anal=1
    scene neus3_out1_10 with dissolve
    neus "You know, this bunny lost her tail."
    neus "I need something to replace it, or I can't call myself a bunny."
    scene neus3_out1_11 with dissolve
    neus "But I see a big carrot that could do the trick."
    if is_view_personality:
        neus "(Damn spell making me say what I think without filters.)"
    else:
        neus "(Damn, why can’t I keep these thoughts to myself?)"
    scene neus3_out1_12 with dissolve
    if incest_story:
        neus "So, could you lend it to me brother?"
        mc "Of course little sister, I'm always willing to help a needy bunny."
    else:
        neus "So, could you lend it to me?"
        mc "Of course, I'm always willing to help a needy bunny."
    stop music fadeout 1.0
    scene neus3_out1_13 with fadesex
    neus "Then I'm going to eat this carrot with my bottom mouth."
    scene neus3_out1_14 with dissolve
    play char1 penetration3
    neus "Ah"
    neus "I finally have my tail back."
    neus "But I think I need to check if this carrot is the right one to be my new bunny tail."
    scene neus3_out1_15 with dissolve
    play char3 sex2
    neus "{bt=2}{=lust_style}Ah Ah Ah{/bt}"
    neus "This carrot is so big and delicious."
    neus "My butt is so happy."
    neus "I think my butt won't be able to live without having this tail inside."
    if incest_story:
        neus "Please be my tail forever brother."
    else:
        neus "Please be my tail forever."
    scene neus3_out1_16 with dissolve
    neus "I'm {sc=2}{=lust_style}cumming{/sc} from anal sex."
    scene neus3_out1_17 with dissolve
    stop char3
    play charM cum1
    play char1 climax1
    neus "Ah."
    scene neus3_out1_18 with dissolve
    if incest_story:
        neus "I'm so full of your carrot juice brother."   
    else:
        neus "I'm so full of carrot juice."          
    scene black with dissolve                   
    "She cleans herself"    
    if is_sexanal<1:
        call addLust(4) from _call_addLust_22  
        $ is_sexanal+=1
    jump neus3_outfit1
label neus3_out_event_anal2:
    if lvl_neus3_out_event_anal<=1:
        $lvl_neus3_out_event_anal=2
    scene neus3_out1_19 with dissolve
    ""
    stop music fadeout 1.0
    scene neus3_out1_20 with fadesex
    play char3 sex2
    neus "{bt=2}{=lust_style}Ah Ah Ah{/bt}"    
    neus "(Damn it, this is so addictive.)"
    if is_view_personality:
        neus "(That damn spell.)"
    neus "(But just a little more won't hurt, {sc=2}right?{/sc})"
    stop char3
    scene neus3_out1_21 with fadesex    
    play char3 breathing1
    neus "(Oh, my legs are trembling.)"
    mc "For you to do 2 hours of nothing but squats."
    mc "You must really like my carrot juice."
    if incest_story:
        neus "Yes, I love it brother."    
    else:
        neus "Yes, I love it."    
    scene neus3_out1_22 with dissolve
    neus "But I think my belly is already too full."
    if incest_story:
        mc "I didn't know you were so perverted, little sister."
    else:
        mc "I didn't know you were so perverted."
    if is_view_personality:
        mc "Did you know the ''Touch'' spell only lasts for 1 hour?"
        scene neus3_out1_23 with dissolve
        neus "That must be a lie, you probably used it on me again while I was distracted doing my squat routine."
        mc "Nope, I haven't used the spell."
    scene neus3_out1_24 with dissolve
    neus "..."
    scene neus3_out1_25 with dissolve
    ""
    stop char3    
    scene black with dissolve
    if incest_story:
        "With weak movements, your sister moves away from you. And acts as if nothing had happened."  
    else:
        "With weak movements, she moves away from you. And acts as if nothing had happened."  
    if is_sexanal<2:
        call addLust(5) from _call_addLust_23  
        $ is_sexanal+=1
    jump neus3_outfit1
#----------------------------outfit2--------------------------------- 
label neus3_outfit2_intro1:
    $ neus3_is_view_outfit_intro2=True   
    if incest_story:
        mc "Hey sister, can you put this on?"
    else:              
        mc "Hey, can you put this on?"
        scene neus3_out1_27 with dissolve
    if is_view_personality:
        neus "I would love to. (Damn it, I'm saying what I think without restrictions)."
    else:
        neus "I would love to. (Damn it, why do I keep saying my thoughts out loud?)"
    scene neus3_out2_1 with fadesex
    neus "This is even more provocative than before."
    mc "Do you like it?"
    scene neus3_out2_2 with dissolve
    if is_view_personality:
        if incest_story:
            neus "I love it, I want to be my big brother's naughty little bunny (Damn spell)."        
        else:
            neus "I love it, I want to be your naughty little bunny (Damn spell)."      
    else:    
        if incest_story:
            neus "I love it, I want to be my big brother's naughty little bunny."        
        else:
            neus "I love it, I want to be your naughty little bunny."  
    jump neus3_outfit2
label neus3_outfit2:
    scene neus3_out2_3 with dissolve
    show screen neus_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    menu:       
        "Change outfit":
            menu:
                "Normal":
                    hide screen spell_screen
                    scene neus3_out2_4 with dissolve
                    neus "Okay"
                    $neus3_outfit_type=0
                    jump neus3
                "Outfit 1":
                    hide screen spell_screen
                    scene neus3_out2_4 with dissolve
                    if incest_story:
                        neus "O-Okay brother"
                    else:
                        neus "O-Okay"
                    $neus3_outfit_type=1
                    jump neus3_outfit1
                "Back":
                    jump neus3_outfit2 
        "Blowjob":
            hide screen spell_screen  
            scene neus3_out2_5 with dissolve
            if incest_story:
                "Your sister shows a slight smile"
            else:
                "She shows a slight smile"
            stop music fadeout 1.0
            scene neus3_out2_6 with w9
            neus "*lick*"
            scene neus3_out2_7 with dissolve
            play char3 deep_suck1
            neus "*suck lick*"
            neus "(Give me your carrot juice)"
            "She sucks your dick as if it were something super delicious"
            if incest_story:
                mc "*mocking tone* Do you like my dick that much little sister?"
            else:
                mc "*mocking tone* Do you like my dick that much?"
            neus "*Suck lick*"
            "She is so focused that she doesn't hear you"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene neus3_out2_8 with dissolve
            neus "{sc=2}{=lust_style}Uh!{sc}"
            play char1 gulp1
            scene neus3_out2_9 with dissolve
            play char1 ahegao1 fadeout 0.2
            neus "{bt=2}{=lust_style}{=lust_style}Ahhhhh{/bt}"
            stop char1 fadeout 1.0
            scene neus3_out2_10 with dissolve
            if incest_story:
                neus "Thanks for the meal big brother"
            else:
                neus "Thanks for the meal"
            scene black with dissolve                   
            "She cleans herself" 
        "Anal":
            hide screen spell_screen  
            scene neus3_out2_11 with dissolve
            neus "Hehe"
            neus "{e_heartbt=FF0000}"
            stop music fadeout 1.0
            scene neus3_out2_12 with w9
            neus "This horny rabbit is going to eat your carrot"
            play char3 sex7
            scene neus3_out2_13 with dissolve            
            neus "{bt=2}{=lust_style}Ha ha ha ha{/bt}"
            neus "I'm going to devour this carrot fully"
            neus "I'm going to drink with my bottom mouth"
            neus "Your nutrient-rich carrot juice"
            stop char3
            play charM cum1
            scene neus3_out2_14 with dissolve
            play char1 climax1
            neus "{sc=2}{=lust_style}Uh!{sc}"
            if incest_story:
                neus "Yes, fill my belly with lots of juice brother"
            else:
                neus "Yes, fill my belly with lots of juice"
            neus "But, I need you to feed me a little more"
            play char3 sex7
            scene neus3_out2_15 with w21
            neus "{bt=2}{=lust_style}Ha ha ha ha{/bt}"  
            if incest_story:
                mc "Are you a really hungry bunny, little sister?"
                neus "Yes brother, I am desperate for your juice"
            else:          
                mc "Are you a really hungry bunny?"
                neus "Yes, I am desperate for your juice"
            mc "Well, here you go"
            stop char3
            play charM cum1
            scene neus3_out2_16 with dissolve  
            play char1 climax2         
            neus "{sc=2}{=lust_style}Uh!{sc}"
            scene neus3_out2_17 with dissolve  
            neus "My bunny tummy is very full."
            stop char1 fadeout 1.5
            scene black with dissolve                   
            "After a few moments, she recovers and cleans herself up." 
        "Leave":           
            jump rooms
    jump neus3_outfit2
#----------------------------night--------------------------------- 
default night_try=0
label neus_sleep3:
    show screen neus_spell
    scene neus3_night1 with dissolve    
    menu:        
        "Try wake her up":   
            hide screen spell_screen          
            if night_try==0:    
                scene neus3_night2 with dissolve   
                if incest_story:
                    "You try to wake up your little sister, but she doesn't respond."
                else:                   
                    "You try to wake up [neusname], but she doesn't respond."
                $ night_try=1
            elif night_try==1:
                scene neus3_night2 with dissolve
                if incest_story:
                    "You try to wake up your little sister for the second time, but it doesn't work."
                else:                   
                    "You try to wake up [neusname] for the second time, but it doesn't work."
                $ night_try=2
            else: 
                scene neus3_night3 with dissolve    
                if incest_story:
                    "You try to wake up your little sister, but-"
                else:                              
                    "You try to wake up [neusname], but-"
                if is_neus_sec_dis:
                    scene neus3_night4 with dissolve
                    if incest_story:
                        neus_yan "I'm sorry brother, but at this hour it's me who is in control."
                    else:
                        neus_yan "I'm sorry, but at this hour it's me who is in control."
                    scene neus3_night5 with dissolve
                    if night_try == 2:
                        neus_yan "But since you're so insistent..."
                    else:
                        neus_yan "But since you're here..."
                    scene black with dissolve
                    "She grabs you tightly, pushes you onto the bed, and rides you."
                    scene neus3_night6 with dissolve
                    if incest_story:
                        neus_yan "Well brother, how should I have fun with you?"
                    else:
                        neus_yan "Well, how should I have fun with you?"
                    scene neus3_night7 with dissolve
                    neus_yan "I guess I'll suck this delicious cock."
                    scene neus3_night8 with dissolve
                    play char1 penetration3
                    neus_yan "Delicious."
                    scene neus3_night9 with fadesex
                    play char3 sex2
                    neus_yan "I'm going to make sure to squeeze all your cum out of you."
                    neus_yan "Your cock is giving lots of kisses to my uterus."
                    if incest_story:
                        neus_yan "Are you trying to impregnate your little sister? Because I love it."
                        neus_yan "Please brother, cum inside me and get me pregnant."
                    else:
                        neus_yan "Are you trying to impregnate me? Because I love it."
                        neus_yan "Please, cum inside me and get me pregnant."
                    menu:                
                        "Inside":
                            stop char3
                            play charM cum1
                            scene neus3_night10 with flash
                            play char1 climax1
                            if incest_story:
                                neus_yan "Uh, yes brother, please, fill me up."
                            else:
                                neus_yan "Uh, yes, please, fill me up."
                            neus_yan "I can feel your cum drowning all my eggs."
                        "Outside":  
                            stop char3 
                            scene neus3_night11 with dissolve    
                            if incest_story:
                                neus_yan "No way brother, it's a waste to let it out."
                            else:                
                                neus_yan "No way, it's a waste to let it out."
                            neus_yan "Cum inside."                        
                            play charM cum1
                            scene neus3_night12 with flash
                            play char1 climax1
                            neus_yan "Uh."  
                    scene neus3_night13 with dissolve              
                    neus_yan "Well, that was great."
                    scene neus3_night14 with dissolve
                    neus_yan "But tonight, you're mine alone."
                    scene black with dissolve
                    if incest_story:
                        "You spend the whole night having sex with your little sister."
                    else:
                        "You spend the whole night having sex with [neusname]."
                    play ambience morning_sounds fadein 0.5
                    scene neus3_night15 with dissolve
                    neus "(I feel very tired, as if I didn't sleep at all.)"
                    neus "(and my hips hurt a lot)."
                    if incest_story:
                        mc "Good morning sister."
                    else:
                        mc "Good morning."
                    scene neus3_night16 with dissolve
                    neus "Good morning... hey, what are you doing here? Did you do this to me?"
                    mc "Last night you were really intense and assertive, you're the best."
                    scene neus3_night17 with dissolve
                    neus "What are you talking about? I didn't do anything."
                    scene neus3_night18 with dissolve
                    mc "Well, you left me a lot of hickies."
                    scene neus3_night19 with dissolve
                    neus "(I don't remember doing that, but what if I did it while I was unconscious?)"
                    neus "..."
                    scene neus3_night20 with dissolve
                    neus "Well, forget it, just leave my room for a while, I want to change."
                    stop ambience fadeout 1.0
                    scene black with dissolve
                    if incest_story:
                        "You leave your sister's room." 
                    else:
                        "You leave [neusname]'s room." 
                    $ night_try=3
                    jump next_day
                else:
                    scene neus3_night21 with dissolve
                    ""
                    jump next_day_neus
        "Sleep":
            hide screen spell_screen
            scene neus3_night22 with dissolve
            ""
            scene black with eyeclose
            ""
            play ambience morning_sounds fadein 1.0
            scene neus3_night23 with eyeopen
            neus "*yawning* What a good sleep I had"
            if incest_story:
                mc "Good morning little sister"
                scene neus3_night24 with dissolve
                neus "Good morning brother"
            else:
                mc "Good morning"
                scene neus3_night24 with dissolve
                neus "Good morning"
            scene neus3_night25 with dissolve
            neus "..."
            scene neus3_night26 with dissolve
            neus "Hey, what are you doing here?"
            mc "It's normal for a couple to sleep together"
            scene neus3_night27 with dissolve
            neus "I suppose couples sleep together, but I didn't give you permission."
            $ xsize_value = 650
            menu(screen="custom_choice_enhanced"):
                "Say ''Good morning''":
                    scene neus3_night28 with dissolve
                    if incest_story:
                        mc "Hey little sister, what if we have some morning fun?"  
                    else:
                        mc "Hey, what if we have some morning fun?"                    
                    scene neus3_night29 with fadesex
                    play char3 sex2
                    neus "Hey, don't do {bt=2}{=lust_style}Ha{/bt} it spontaneously {bt=2}{=lust_style}Ha{/bt}"
                    mc "I'm going to give you lots of good morning kisses to your uterus"
                    neus "So deep"
                    mc "You must be delighted with my good morning greeting, you're so tight"
                    neus "That's not true, ah ah ah"
                    scene neus3_night30 with dissolve
                    neus "I'm gonna cum.. I'm gonna .." 
                    stop char3
                    play charM cum1
                    scene neus3_night31 with dissolve  
                    play char1 climax1                 
                    neus "Ugh"
                    if incest_story:
                        neus "(My uterus is so full of my brother's semen)"
                    else:
                        neus "(My uterus is so full of his semen)"
                    scene neus3_night32 with dissolve
                    neus "(I'm sure many of my eggs are being fertilized already)"
                    stop ambience fadeout 1.0
                    scene black with dissolve
                    "You leave the room and let her rest" 
                    call addLust(4)
                "No":
                    stop ambience fadeout 1.0
                    scene black with dissolve
                    if incest_story:
                        "You leave your sister's room."
                    else:
                        "You leave [neusname]'s room."  
            jump next_day       
        "Leave":  
            hide screen spell_screen                                                                       
            jump rooms
    jump neus_sleep3
#----------------------------Level 2--------------------------------- 
label neus_bed:
    scene bg_neus_room_night    
    menu:        
        "Sleep":            
            jump expression "neus_sleeping_event%s"%neus_event_lvl
        "Back":
            jump rooms
label neus_sleeping_event2:    
    stop music fadeout 1.0
    scene neus2_38 with dissolve
    if incest_story:
        neus "H-Hey, what are you doing in my bed brother?"  
    else:   
        neus "H-Hey, what are you doing in my bed?"  
    scene neus2_39 with dissolve  
    mc "Sleeping."
    scene neus2_40 with dissolve
    neus "Mmm..."
    call splash_message(_("Moments later")) from _call_splash_message_27  
    scene black with dissolve  
    neus "Die, die, die, die, die, die, die."    
    mc "Seems like you have a lot of energy."
    neus "Sorry."
    menu:
        "Help her sleep":
            scene neus2_41 with dissolve
            neus "I'm sorry, I'm sorry, I'm really sorry"
            scene neus2_42 with dissolve
            neus "Ahhh"
            play char3 sex2
            scene neus2_43 with dissolve
            neus "No more"
            stop char3
            call splash_message(_("The next day")) from _call_splash_message_28   
            scene neus2_44 with dissolve           
            ""
            $N_state=1
            if quest_v2:
                call addLust(4)
        "Leave":
            $N_state=0      
    jump next_day_neus
#----------------------------Level 3--------------------------------- 
label neus_sleeping_event3: 
    stop music fadeout 0.5
    scene neus3_sleep0 with storyfx
    if incest_story:
        neus "Mmm... So my big brother wants to sleep in my bed tonight..."
        scene neus3_sleep1 with dissolve
        neus "That's fine, but only for tonight."
    else:
        neus "Mmm... So you want to sleep in my bed tonight..."
        scene neus3_sleep1 with dissolve
        neus "Fine, but only for tonight."
    play ambience night_ambience volume 0.1
    scene neus3_sleep2 with w33
    ""
    stop ambience fadeout 2.0
    scene black with eyeclose
    ""
    play ambience morning_sounds fadein 1.0
    scene neus3_sleep3 with eyeopen    
    neus "(It has been a long time since I slept that well... Although I feel a bit horny...)"
    scene neus3_sleep4 with dissolve
    neus "..."
    menu:
        "Sex":
            scene neus3_sleep5 with dissolve
            neus "(Technically I'm his girlfriend... He does it whenever he wants...)"
            neus "(So if I do the same, it would only be fair, right?)"
            scene black with fadesex
            play char3 sex7
            neus "{bt=2}{=lust_style}Oh oh oh{/bt}"
            scene neus3_sleep6 with dissolve     
            if incest_story:
                mc "Good morning sister"
                neus "{bt=2}{=lust_style}Ghood mhornhing bhrother{/bt} (Good morning brother.)"
            else:      
                mc "Good morning"
                neus "{bt=2}{=lust_style}Ghood mhornhing{/bt} (Good morning.)"
            scene neus3_sleep7 with dissolve
            play char1 groan1
            neus "{sc=3}{=lust_style}I'M CUMMING...{/sc}{w=1.0}{nw}"
            stop char3
            play charM cum1
            scene neus3_sleep8 with hpunch
            play char1 climax1
            neus "{sc=2}{=lust_style}Uh!{/sc}"
            stop char1 fadeout 2.0
            scene neus3_sleep9 with dissolve
            neus "Phew..." 
            scene neus3_sleep10 with w9          
            if incest_story:
                mc "*Mocking tone* What a good way to wake someone up... I wouldn't mind if you do that more often sister."
            else: 
                mc "*Mocking tone* What a good way to wake someone up... I wouldn't mind if you do that more often."
            scene neus3_sleep11 with dissolve
            neus "Ehhh... maybe... although now I want to have breakfast..."
            stop ambience fadeout 1.0   
            scene black with dissolve
            if incest_story:
                "Your sister leaves the room"
            else:
                "[neusname] leaves the room"
            call addLust(4)
        "Refrain":            
            neus "(It's better if I forget it and go make breakfast)"
            stop ambience fadeout 1.0   
            scene black with dissolve
            ""
    jump next_day_neus

label book_neus_feel:
    scene neus0_11 with dissolve
    "The title of the book says ''Manage your emotions''"
    jump rooms
label ring_neus:
    scene neus0_12 with dissolve
    "A simple ring with a small heart."
    jump rooms
label newspaper_bistro:
    scene newspaper_bistro0 with dissolve
    ""
    jump rooms
label box_postday:    
    scene neus_box_posday_0     
    "A box of morning-after pills."            
    jump rooms  
label baseball_bat:
    scene baseball_bat0 with dissolve
    mc "..."
    jump rooms
label phone_neus:
    scene phone_neus0 with dissolve   
    mc "I don't remember her taking this picture of me."
    mc "I suppose she took it when I wasn't paying attention."
    jump rooms
label menu_regular_ending:  
    $ xsize_value = 750
    menu(screen="custom_choice_enhanced"):
        "Choose your ending or..."
        "Normal Ending (Requires Lust: 100)"(neus_lust>=100) if quest_v2 and not neus_lust>=100:
            pass
        "Normal Ending" if neus_lust>=100 or not quest_v2:
            jump ending_normal1      
        "???\n(Requires ''Confront'')"(is_neus_sec_dis) if not is_neus_sec_dis:
            pass
        "Another personality (Requires spell: Personality)"(spell_3_2.is_active) if is_neus_sec_dis and not spell_3_2.is_active: 
            pass
        "Another personality (Requires Lust: 100)"(neus_lust>=100) if quest_v2 and is_neus_sec_dis and spell_3_2.is_active and not neus_lust>=100: 
            pass
        "Another personality" if is_neus_sec_dis and spell_3_2.is_active and ((quest_v2 and neus_lust>=100) or (not quest_v2)):   
            jump level3_0
        "Another personality intro" if is_view_personality: 
            $ is_replay_level3_0 = True
            jump level3_0
        "Leave": 
            jump rooms
