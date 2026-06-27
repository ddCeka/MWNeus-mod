default is_view_bath2 = False
default is_view_bath3 = False
screen bath_room_quest:
    if quest_v2:
        if not(time==questMain_v2_select.time_event) or not(select_room==neus_routine[time]):
            use expression "bath%s"%bath_event_lvl 
    else:
        if not(time==questMain_select.time_event) or not(select_room==neus_routine[time]):
            use expression "bath%s"%bath_event_lvl 
    if time<=3 and not(neus_routine[time]=="bath"):        
        imagebutton:
            auto "btn_shower_event_%s" 
            pos   765, 350        
            tooltip _("Shower")
            action Jump("shower_event%s"%bath_event_lvl)
#----------------------------Level 0---------------------------------
screen bath0:
    pass 
label shower_event0:
    play ambience shower2 volume 0.5
    scene bath0_0 with dissolve
    ""
    jump time_advances
#----------------------------Level 1---------------------------------
screen bath1:
    pass 
label shower_event1:
    play ambience shower2 volume 0.5
    scene bath1_0 with dissolve
    ""
    jump time_advances
#----------------------------Level 2---------------------------------
screen bath2:
    if neus_routine[time]=="bath":
        imagebutton:
                auto "rooms/bath/lvl2/bath2_0_%s.png"            
                focus_mask True
                tooltip "%s"%neusname
                action Jump("bath2")
label bath2:
    if neus_is_evading:
        scene black with dissolve
        if incest_story:
            "Your sister notices your presence and quickly leaves the room."
        else:
            "She notices your presence and quickly leaves the room."
        jump time_advances
    scene bath2_1
    show screen bath_spell
    stop music fadeout 0.5
    play ambience shower2 volume 0.5 
    menu:       
        "Surprise Her":
            hide screen spell_screen
            if not(is_view_bath2):
                scene bath2_2 with dissolve
                neus "Hey, how did you get in?"  
                mc "The door was open."  
                scene bath2_3 with dissolve
                neus "(I could've sworn I closed it.)" 
                if incest_story:
                    mc "There's no need to feel ashamed little sister." 
                else:
                    mc "There's no need to feel ashamed." 
                $is_view_bath2 = True
            jump bath2_action
        "Leave":                          
            jump rooms

label bath2_action:
    play ambience shower2 volume 0.5 if_changed
    scene expression "bath2_4_%s"%spanking_count
    menu:
        neus "Hmm"
        "Spank her":
            scene  bath2_5 with dissolve
            play charM slap1 volume 2.0
            play char1 groan_normal1 
            neus "Hey"
            $spanking_count = 1            
        "Shower together":
            scene bath2_6 with dissolve
            neus "Ugh, alright" 
            scene black with dissolve  
            if incest_story:
                "You shower with your little sister"
            else:         
                "You shower with [neusname]"
            jump time_advances
        "Blowjob":
            neus "Ugh"
            scene bath2_7 with dissolve
            play char3 suck2 
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene bath2_8 with flash2 
                    neus "{sc=3}Hmm{/sc}"
                    scene bath2_9 with dissolve 
                    neus "Are you satisfied?"
                "Outside":
                    stop char3
                    play charM cum1
                    scene bath2_10 with flash2
                    ""             
            scene black with dissolve 
            "The water cleans her"
            if is_blowjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob+=1      
        "Sex":
            scene expression "bath2_11_%s"%spanking_count with dissolve
            neus "?"
            scene expression "bath2_12_%s"%spanking_count with dissolve
            neus "{sc=2}H-Hey{/sc}"
            scene expression "bath2_13_%s"%spanking_count with dissolve
            play char1 penetration2
            neus "Ahhh"
            play char3 sex1
            scene expression "bath2_14_%s"%spanking_count with dissolve
            if incest_story:
                neus "Why are you always so horny brother?"
                mc "Your ass is responsible, now be a good little sister and take responsibility."
            else:
                neus "Why do you always act like a horny monkey?"
                mc "Your ass is responsible, now be a good girl and take responsibility."
            neus "Hmmm..."
            if incest_story:
                $ menu_text = "Brother can"
            else:
                $ menu_text = "Can"
            menu:
                neus "[menu_text] you cum outside, please."
                "Inside":  
                    stop char3
                    play charM cum1
                    play char1 climax1             
                    scene expression "bath2_15_%s"%spanking_count with flash2
                    neus "{sc=2}Uhhh{/sc}"
                    neus "Next time, listen to me and cum outside."
                    scene expression "bath2_16_%s"%spanking_count with dissolve
                    neus "(I will have to take a morning-after pill.)"                    
                "Outside":
                    stop char3
                    play charM cum1
                    play char1 climax1
                    scene expression "bath2_17_%s"%spanking_count with flash2
                    neus "{sc=2}Uhhh{/sc}"
                    neus "Thank you for not cumming inside."              
            scene black with dissolve
            "She cleans herself"    
            if is_sex<1:
                if quest_v2:
                    call addLust(3)
                $ is_sex+=1              
        "Leave":
            jump rooms
    jump bath2_action

label shower_event2:
    play ambience shower2 volume 0.5
    scene bath1_0 with dissolve
    ""
    jump time_advances
#----------------------------Level 3--------------------------------- 
screen bath3:
    if neus_routine[time]=="bath":
        imagebutton:
                auto "rooms/bath/lvl2/bath2_0_%s.png"            
                focus_mask True
                tooltip "%s"%neusname
                action Jump("bath3")
label bath3:    
    scene bath3_1
    show screen bath_spell
    stop music fadeout 0.5
    play ambience shower2 volume 0.5 if_changed
    menu:       
        "Take a Shower":   
            hide screen spell_screen             
            if not(is_view_bath3):
                scene bath3_2 with dissolve
                if incest_story:
                    mc "Hey sis, can I take a shower with you?"
                else:
                    mc "Hey, can I take a shower with you?"
                scene bath3_3 with dissolve
                neus "... fine!"
                scene bath3_4 with dissolve
                if incest_story:
                    neus "Mah! Hey! Brother!"
                else:
                    neus "Mah! Hey!"                
                mc "Can't I?"
                scene bath3_5 with dissolve
                neus "You just caught me by surprise, let me know in advance next time."
                $is_view_bath3 = True
            jump bath3_action
        "Leave":                          
            jump rooms
label bath3_action:
    scene bath3_6 with dissolve
    play ambience shower2 volume 0.5 if_changed
    menu:
        "What do you want to do?"
        "Blowjob":
            scene bath3_7 with dissolve
            if incest_story:
                neus "It seems you really like my mouth big brother."
            else:
                neus "It seems you really like my mouth."
            scene bath3_8 with dissolve
            neus "Aaa"
            scene bath3_9 with dissolve
            play char3 suck2
            neus "*sucking* lick lick"
            neus "*Suck suck*"
            menu:
                "Deeper":
                    pass           
            scene bath3_10 with dissolve
            stop char3
            neus "Mmm"
            scene bath3_11 with dissolve
            play char3 suck2            
            neus "(Soo rough)"  
            neus "(He's using my mouth like a toy)"
            neus "(That's a bit...)"
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene bath3_12 with flash2                    
                    neus "Ugh!"
                    scene bath3_13 with dissolve
                    ""
                    play char1 gulp1
                    scene bath3_14 with dissolve                    
                    neus "Gulp"
                    scene bath3_15 with dissolve
                    neus "(I think I'm getting used to doing this...{e_heartbt=FF0000})"
                    scene bath3_15_1 with dissolve
                    neus "(N-No...)"
                "Outside":
                    stop char3
                    play charM cum1
                    scene bath3_16 with flash2                    
                    neus "Aaa"                    
            scene black with dissolve
            "She cleans herself"
            if is_blowjob<1:
                call addLust(2) from _call_addLust
                $ is_blowjob+=1
        "Sex":
            scene bath3_17 with dissolve
            if incest_story:
                neus "Brother, do we have to do it again?"
                mc "Does it bother you little sister?"
            else:
                neus "Do we have to do it again?"
                mc "Does it bother you?"
            scene bath3_18 with dissolve
            neus "..."
            scene bath3_19 with fadesex
            if incest_story:
                neus "Go easy on me, okay brother?"
            else:
                neus "Go easy on me, okay?"
            scene bath3_20 with dissolve
            play char1 penetration3
            neus "Oh"
            neus "(It's so deep)"
            scene bath3_21 with dissolve
            play char3 sex2
            neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
            neus "(With each thrust, it's like his thing is giving kisses to my {bt=2}{=lust_style}uterus{/bt})"
            neus "(As if I'm trying to convince him to let me be {bt=2}{=lust_style}fertilized{/bt})"
            scene bath3_22 with dissolve
            neus "{sc=2}{=lust_style}ohhH Guhhohh{/sc}"
            scene bath3_22_1 with dissolve
            play char1 climax1
            neus "I'm cumming {e_heartbt=FF0000}"
            stop char3
            menu:
                "Inside":
                    play charM cum1
                    scene bath3_23 with flash2                    
                    neus "EEEKK! (So hot)"
                    scene bath3_24 with dissolve
                    if incest_story:
                        neus "(My {bt=2}{=lust_style}stomach{/bt} is all warm with my brother's cum)"
                    else:
                        neus "(My {bt=2}{=lust_style}stomach{/bt} is all warm with his cum)"
                    neus "(I must not forget to take the pill)"
                "Outside":
                    play charM cum1
                    scene bath3_25 with flash2    
                    if incest_story:
                        neus "Thank you brother (Hot)"   
                    else:                
                        neus "Thank you (Hot)"            
            scene black with dissolve
            "She cleans herself"
            if is_sex<1:
                call addLust(3) from _call_addLust_1
                $ is_sex+=1
        "Anal ":
            scene bath3_26 with dissolve  
            if incest_story:
                neus "Uh... brother... I'd prefer if we had regular sex, I don't feel very comfortable doing it in my backside."
            else:         
                neus "Uh... I'd prefer if we had regular sex, I don't feel very comfortable doing it in my backside."
            mc "More reason to do it, so you can get used to it."
            scene bath3_27 with dissolve
            neus "W-Wait, wait."
            scene bath3_28 with dissolve
            neus "Do it gently, okay?"
            scene bath3_29 with dissolve
            play char1 penetration2
            neus "Ah!"
            mc "I'm going to start moving now."            
            scene bath3_30 with dissolve
            play char3 sex2
            neus "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"
            neus "(This feels weird.)"
            neus "(My {sc=2}{=lust_style}backside{/sc} feels hot.)"
            menu:
                "Deeper":
                    pass  
            stop char3
            scene bath3_31 with dissolve 
            play char1 penetration2              
            neus "Ha"
            scene bath3_32 with dissolve
            play char3 sex3
            neus "{bt=4}{=lust_style}Ah ah ah ah.{/bt}"
            if incest_story:
                neus "Brother, can you go slower?"
            else:
                neus "Can you go slower?"
            mc "Your butt is so tight."
            scene bath3_32_1 with dissolve
            neus "Uhhh."
            scene bath3_32 with dissolve
            neus "I'm cumming, I'm cumming!"
            menu:
                "Inside":
                    stop char3
                    play charM cum1
                    scene bath3_33 with flash2 
                    play char1 climax1                     
                    neus "Uhhh."
                "Outside":
                    stop char3
                    play charM cum1
                    scene bath3_34 with flash2
                    play char1 climax1                    
                    neus "Ahhh."                  
            neus "(I just came from having anal sex...)"
            neus "(Am I that kind of person? No way, I don't want to become addicted to this kind of sex.)"
            mc "So you liked it?"
            neus "N-No..."
            scene bath3_35 with dissolve
            mc "Your face tells a different story."
            mc "I love those lewd expressions."
            scene bath3_36 with dissolve
            mc "We will keep doing it until you get used to it and your backside takes the shape of my dick."
            mc "I'm going to give you a lot of love."
            neus "{bt=2}...{/bt} {e_musical=FFF}"
            scene black with dissolve
            "After a while, she recovers and cleans herself."
            if is_sexanal<1:
                call addLust(3) from _call_addLust_2
                $ is_sexanal+=1
        "Leave":
            jump rooms
    jump bath3_action


label shower_event3:
    play ambience shower2 volume 0.5
    scene bath1_0 with dissolve
    ""
    jump time_advances

