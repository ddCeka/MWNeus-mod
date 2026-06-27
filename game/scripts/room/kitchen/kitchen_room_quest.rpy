image kitchen0_1 = DynamicAnimation(
["rooms/kitchen/lvl0/kitchen0_1_0.webp",
"rooms/kitchen/lvl0/kitchen0_1_1.webp", 
"rooms/kitchen/lvl0/kitchen0_1_2.webp"])
image kitchen0_4 = DynamicAnimation(
["rooms/kitchen/lvl0/kitchen0_4_0.webp",
"rooms/kitchen/lvl0/kitchen0_4_1.webp", 
"rooms/kitchen/lvl0/kitchen0_4_2.webp"],0.2,0.2,2.0,1.0)
image kitchen1_1= DynamicAnimation(
["rooms/kitchen/lvl1/kitchen1_1_0.webp",
"rooms/kitchen/lvl1/kitchen1_1_1.webp",
"rooms/kitchen/lvl1/kitchen1_1_2.webp"])
image kitchen2_1_0= DynamicAnimation(
["rooms/kitchen/lvl2/kitchen2_1_0_0.webp",
"rooms/kitchen/lvl2/kitchen2_1_0_1.webp",
"rooms/kitchen/lvl2/kitchen2_1_0_2.webp"])
image kitchen3_1_0= DynamicAnimation(
["rooms/kitchen/lvl3/kitchen3_1_0_0.webp",
"rooms/kitchen/lvl3/kitchen3_1_0_1.webp",
"rooms/kitchen/lvl3/kitchen3_1_0_2.webp"])
image kitchen3_out1_1= DynamicAnimation(
["rooms/kitchen/lvl3/kitchen3_out1_1_0.webp",
"rooms/kitchen/lvl3/kitchen3_out1_1_1.webp",
"rooms/kitchen/lvl3/kitchen3_out1_1_2.webp"])
image kitchen3_out2_6= DynamicAnimation(
["rooms/kitchen/lvl3/kitchen3_out2_6_0.webp",
"rooms/kitchen/lvl3/kitchen3_out2_6_1.webp",
"rooms/kitchen/lvl3/kitchen3_out2_6_2.webp"])

screen kitchen_room_quest:
    if quest_v2:
        if not(time==questMain_v2_select.time_event) or not(select_room==neus_routine[time]) or questMain_v2_select.place=="":
            use expression "kitchen%s"%kitchen_event_lvl
    else:
        if not(time==questMain_select.time_event) or not(select_room==neus_routine[time]) or questMain_select.place=="":
            use expression "kitchen%s"%kitchen_event_lvl
    if time<=3 and not(neus_routine[time]=="kitchen"):        
        imagebutton:
            auto "btn_food_event_%s" 
            pos   1000, 550        
            tooltip _("Food")
            action Jump("food_event%s"%kitchen_event_lvl)
    if relationship_level>=1 and not(key_room_neus.is_view):  
        if time < 4:
            imagebutton:
                auto "btn_key_neus_%s"            
                focus_mask True
                tooltip _("Key")
                action Jump("key_neus")
        else:
            imagebutton:
                auto "btn_night_key_neus_%s"            
                focus_mask True
                tooltip _("Key")
                action Jump("key_neus")
    if relationship_level>=3 and not(kitchen3_is_active_outfit):
        if time < 4:
            imagebutton:
                auto "btn_old_photo_s_%s"     
                action Jump("kitchen3_minigame")
                tooltip _("Special photo")
                pos 350,730
        else:
            imagebutton:
                auto "btn_night_old_photo_s_%s"     
                action Jump("kitchen3_minigame")
                tooltip _("Special photo")
                pos 350,730
            
#----------------------------Level 0---------------------------------
screen kitchen0:
    if neus_routine[time]=="kitchen":         
        imagebutton:
            auto "rooms/kitchen/lvl0/kitchen0_0_%s.png"            
            focus_mask True            
            action Jump("kitchen0")
            tooltip "%s"%neusname     
            
label kitchen0:
    call rooms_music
    scene kitchen0_1
    show screen kitchen_spell
    menu:   
        "Talk":           
            jump kitchen0_talk
        "Kiss" ((not quest_v2 and questMain_2.completion) or (quest_v2 and questMain_v2_5.completion)):
            jump kitchen0_action
        "Hang out":
            hide screen kitchen_spell
            scene kitchen0_9 with dissolve
            ""
            jump time_advances                
        "Leave":           
            jump rooms

label kitchen0_talk: 
    call rooms_music
    scene kitchen0_1
    hide screen spell_screen   
    menu:
        "What do you want to talk about?"        
        "Amusement park":
            scene level0_0_10 at gray_scale with dissolve
            neus "The amusement park was so cool."
            neus "Would you like to go to the amusement park again sometime?"            
            mc "Sure, I would love to go on another date with you."  
            scene kitchen0_2 with dissolve
            neus "Hmm, I think I can live without going to the amusement park."    
            neus "Once is enough for me (I'm strong)"  
            mc "Are you sure? They just opened a new attraction." 
            scene kitchen0_3 with dissolve
            neus "Yes, I'm sure (how strong I am...)"               
        "Breakfast": 
            scene kitchen0_4 with dissolve           
            mc "What are you having for breakfast?"     
            neus "Coffee" 
            mc "Coffee?{w} You've always had milk for breakfast."  
            neus "It was a waste of time (I drank it every day for 10 years without any change)"                  
        "Back":
            jump kitchen0   
    jump kitchen0_talk 

label kitchen0_action:    
    hide screen spell_screen
    if is_kiss>=1:
        scene kitchen0_12 with dissolve
        neus "No"
    else:        
        scene kitchen0_10 with dissolve
        neus "{sc=3}Ha!{/sc}"        
        scene kitchen0_11 with circlefx
        play char1 short_kiss
        pause  
        $ is_kiss+=1 
        if quest_v2:
            call addLust(1)
    jump kitchen0
label food_event0:
    scene kitchen0_16 with dissolve
    ""
    jump time_advances
#----------------------------Level 1---------------------------------
screen kitchen1:
    if neus_routine[time]=="kitchen":         
        imagebutton:
            auto "rooms/kitchen/lvl1/kitchen1_0_%s.png"            
            focus_mask True            
            action Jump("kitchen1")
            tooltip "%s"%neusname
label kitchen1:
    call rooms_music
    scene kitchen1_1
    show screen kitchen_spell
    menu:   
        "Talk":           
            jump kitchen1_talk
        "Action":
            jump kitchen1_action
        "Hang out":
            hide screen kitchen_spell
            scene kitchen1_12 with dissolve
            ""
            jump time_advances                
        "Leave":           
            jump rooms
label kitchen1_talk: 
    call rooms_music
    scene kitchen1_1
    hide screen spell_screen   
    menu:
        "What do you want to talk about?"                  
        "Breakfast": 
            scene kitchen1_2 with dissolve           
            mc "What are you having for breakfast?"     
            neus "Coffee" 
            mc "Do you know there is a new milk that can help you?"
            scene kitchen1_3 with dissolve  
            neus "Mmm, not interested. (pervert)"                    
        "Back":
            jump kitchen1   
    jump kitchen1_talk
label kitchen1_action:   
    call rooms_music
    scene kitchen1_1
    hide screen spell_screen
    menu:
        "What do you want to do?"        
        "Kiss":
            if is_kiss>=1:
                scene kitchen1_5 with dissolve 
                play char1 short_kiss               
                ""
                scene kitchen1_6 with dissolve
                play char1 french01
                ""
                scene kitchen1_7 with dissolve
                neus "(I want {sc=3}{=lust_style}more{/sc}, but...)"
                if is_kiss<2:
                    if quest_v2:
                        call addLust(1)
                    $is_kiss+=1
            else:
                scene kitchen1_4 with dissolve
                neus "All right"            
                scene kitchen1_5 with dissolve 
                play char1 short_kiss               
                neus "(I think i might like this)"  
                if quest_v2:
                    call addLust(1)
                $ is_kiss+=1
        "Handjob":           
            scene kitchen1_8 with dissolve
            neus "No, I don't want to be covered in your cum again"
            scene kitchen1_9 with circlefx 
            neus "(How do I always end up accepting?)"
            scene kitchen1_10 with dissolve 
            neus "Hey, can you finish already?"
            call splash_message(_("Moments later")) from _call_splash_message_8
            play charM cum1
            scene kitchen1_11 with flash2 
            ""
            scene black with dissolve 
            "She cleans herself"
            if is_handjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_handjob+=1
        "Blowjob"((not quest_v2 and questMain_4.completion) or (quest_v2 and questMain_v2_9.completion)):
            scene kitchen1_23 with dissolve  
            neus "You better finish fast" 
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            scene kitchen1_24 with dissolve   
            neus "(It stinks)" 
            scene kitchen1_25 with dissolve 
            neus "(But if I do this quickly, it will be over faster)"
            scene kitchen1_26 with dissolve 
            play char3 suck2      
            menu:
                "Inside"((not quest_v2 and questMain_5.completion) or (quest_v2 and questMain_v2_11.completion)):
                    stop char3
                    play charM cum1
                    scene kitchen1_27 with flash2
                    neus "{sc=3}Hmm{/sc}"
                    scene kitchen1_28 with dissolve
                    neus "(I can't get used to the taste)"
                "Outside":
                    stop char3
                    play charM cum1
                    scene kitchen1_29 with flash2                
                    ""
            $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
            scene black with dissolve 
            "She cleans herself"
            if is_blowjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob+=1
        "Back":
            jump kitchen1
    jump kitchen1_action
label food_event1:
    scene kitchen1_21 with dissolve
    ""
    jump time_advances
#----------------------------Level 2---------------------------------
default is_view_kitchen2=False
screen kitchen2:
    if neus_routine[time]=="kitchen":  
        if is_sexpussy>=1:       
            imagebutton:
                auto "rooms/kitchen/lvl2/kitchen2_0_1_%s.png"            
                focus_mask True            
                action Jump("kitchen2_intro")
                tooltip "%s"%neusname
        else:
            imagebutton:
                auto "rooms/kitchen/lvl2/kitchen2_0_0_%s.png"            
                focus_mask True            
                action Jump("kitchen2_intro")
                tooltip "%s"%neusname
label kitchen2_intro:
    if neus_is_evading:
        scene black with dissolve
        if incest_story:
            "Your sister notices your presence and quickly leaves the room."
        else:
            "She notices your presence and quickly leaves the room."
        jump time_advances  
    if N_state==1:
        jump kitchen2     
    $choice_kitchen=renpy.random.choice([0,1])
    if choice_kitchen==1 or not(is_view_kitchen2):
        $ is_view_kitchen2=True
        scene kitchen2_1_intro1 with dissolve  
        if incest_story:
            $ menu_text = "Your sister"
        else: 
            $ menu_text = neusname
        menu:
            "[menu_text] doesn't notice your presence."
            "Spank":
                scene kitchen2_1_intro2 with dissolve
                play charM slap1 volume 2.0
                play char1 groan_normal1
                neus "Hmm"
                scene kitchen2_1_intro3 with dissolve
                neus "Can you remove your hand from my ass?"
                menu:
                    "Sex":     
                        $ renpy.music.set_volume(0.5, delay=2.0, channel='music')         
                        scene kitchen2_1_intro5 with dissolve
                        if incest_story:
                            neus "Uhhh brother, what are you doing?"
                            scene kitchen2_1_intro6 with dissolve
                            mc "Providing my little sister with the nutrients she needs."
                        else:
                            neus "Uhhh Hey, what are you doing?"
                            scene kitchen2_1_intro6 with dissolve
                            mc "Providing you with the nutrients you need."
                        scene kitchen2_1_intro7 with dissolve
                        neus "What the hell are you saying?"
                        scene kitchen2_1_intro8 with dissolve
                        mc "Relax, you don't need to be defensive, just leave it to me."
                        if incest_story:
                            neus "Ahh brother"
                        else:
                            neus "Ahh"
                        play char3 sex2
                        scene kitchen2_1_intro9 with dissolve
                        menu:
                            "Inside":  
                                stop char3
                                play charM cum1                              
                                scene kitchen2_1_intro10 with flash2
                                neus "Uhhh"
                                neus "Next time, cum outside."
                                mc "Next time?"
                                neus "Die."
                            "Outside":
                                stop char3
                                play charM cum1  
                                scene kitchen2_1_intro11 with flash2
                                neus "Uhhh"
                                neus "Thank you for not cumming inside."
                        $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
                        scene black
                        "She cleans herself"
                        if is_sex_intro<1:
                            if quest_v2:
                                call addLust(3)
                            $ is_sex_intro+=1
                    "Leave":
                        scene kitchen2_1_intro4 with dissolve
                        if incest_story:
                            neus "Please don't do that again brother! (It feels weird)"     
                        else:
                            neus "Please don't do that again! (It feels weird)"                                
            "Don't spank":
                pass
    jump kitchen2
label kitchen2:  
    if N_state==1:     
        stop music fadeout 0.5   
        if is_sexpussy>=1:
            play char3 breathing2 volume 0.3 fadeout 1.0
            scene kitchen2_1_1_1
        else:
            play char3 breathing1 fadeout 1.0
            scene kitchen2_1_1_0
    else:
        call rooms_music
        scene kitchen2_1_0
    show screen kitchen_spell
    menu:       
        "More"((not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion)) if N_state==1:
            hide screen kitchen_spell
            if is_sexpussy>=1:
                scene black with dissolve
                if incest_story:
                    "Your sister is so tired that she offers no resistance."
                else:
                    "[neusname] is so tired that she offers no resistance."
                play char3 sex2
                scene kitchen2_43 with dissolve                
                neus "Haaa Haaa Haaa"
                scene kitchen2_44 with dissolve
                neus "Mmmm!{w=1.0}{nw}"                
                stop char3
                play charM cum1 
                scene kitchen2_45 with flash2
                neus "Ohhh"           
                scene black with dissolve
                if incest_story:
                    "You notice that she can't take anymore, so you let her go."  
                else:
                    "You notice that [neusname] can't take anymore, so you let her go."  
                $ neus_left_room = True
                if is_sex_more<2:
                    if quest_v2:
                        call addLust(3)
                    $is_sex_more+=1
                jump time_advances
            else:
                scene kitchen2_34 with dissolve
                neus "?"
                stop char3 fadeout 1.0
                scene kitchen2_35 with dissolve
                neus "Seriously, you still have energy?"
                scene kitchen2_36
                if incest_story:
                    neus "Brother no more, please."
                    scene kitchen2_37 with dissolve
                    mc "Relax sis, I'll go gentle as always. When you're more accustomed, I'll go harder."
                else:
                    neus "No more, please."
                    scene kitchen2_37 with dissolve
                    mc "Relax, I'll go gentle as always. When you're more accustomed, I'll go harder."
                neus "N-No{w=0.3}{nw}"
                scene kitchen2_38 with dissolve
                play char1 penetration2
                neus "Haaa"
                play char3 sex2
                scene kitchen2_39 with dissolve
                neus "Haaa haaa haaa"
                scene kitchen2_40 with dissolve
                neus "Ohhh!{w=1.0}{nw}"                
                stop char3
                play charM cum1                
                scene kitchen2_41 with flash2
                play char1 climax1
                neus "Uhhhh"
                scene kitchen2_42 with dissolve
                ""      
                $is_sexpussy+=1          
                if is_sex_more<1:
                    if quest_v2:
                        call addLust(3)
                    $is_sex_more+=1
            jump kitchen2 
        "Talk"if N_state==0:           
            jump kitchen2_talk
        "Action" if N_state==0:
            jump kitchen2_action
        "Hang out" if N_state==0:
            hide screen kitchen_spell 
            scene kitchen2_26 with dissolve
            ""                      
            jump time_advances                
        "Leave":           
            jump rooms
label kitchen2_talk:
    call rooms_music
    scene kitchen2_1_0
    hide screen spell_screen   
    menu:
        "What do you want to talk about?"                  
        "Breakfast": 
            mc "You know, there's a new type of milk that can make them grow." 
            scene kitchen2_2 with dissolve  
            neus "You're disgusting." 
            call splash_message(_("Moments later")) from _call_splash_message_14  
            scene kitchen2_3 with dissolve
            neus "(I hope it works.)"
        "Back":
            jump kitchen2   
    jump kitchen2_talk
label kitchen2_action:
    call rooms_music
    scene kitchen2_1_0
    hide screen spell_screen
    menu:
        "What do you want to do?"        
        "Kiss":
            scene kitchen2_4 with dissolve
            play char1 french01 
            ""
            scene kitchen2_5 with dissolve
            if incest_story:
                neus "Hey brother, can I have a little more?"  
            else:
                neus "Hey, can I have a little more?"  
            mc "A little more of what?"
            scene kitchen2_6 with dissolve  
            neus "Nothing"    
            if is_kiss<1:
                if quest_v2:
                    call addLust(1)
                $ is_kiss+=1
        "Blowjob":
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            scene kitchen2_7 with dissolve
            neus "Make it quick."
            scene kitchen2_8 with dissolve
            play char3 suck2
            menu: 
                "Cum":
                    stop char3
                    play charM cum1
            scene kitchen2_9 with flash2 
            neus "Umm"
            scene kitchen2_10 with dissolve
            menu: 
                "Take a photo":                    
                    scene kitchen2_11 with dissolve 
                    neus "What are you doing?"
                    if incest_story:
                        mc "Relax sis, I'll censor the photo."
                    else:
                        mc "Relax, I'll censor the photo."
                    scene kitchen2_12 with dissolve 
                    neus "Hey, why are you putting your dick on my face?"
                    mc "Say cheese!"
                    play sound camera_flash
                    scene kitchen2_13 with dissolve                     
                    ""
                    scene kitchen2_14 with dissolve 
                    neus "You better not show that to anyone."
                    mc "This photo is for my personal use only. Do you want me to send it to you?"
                    scene kitchen2_15 with dissolve 
                    neus "No"
                "Leave":
                    pass
            $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
            scene black
            "She cleans herself"
            if is_blowjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_blowjob+=1
        "Titjob":                            
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            scene kitchen2_21 with dissolve 
            neus "?"
            scene kitchen2_22 with dissolve
            neus "Can you finish fast? (Do my boobs make him feel good?)"
            play char1 cum1
            scene kitchen2_23 with dissolve
            neus "You got your cum all over me."
            scene kitchen2_24 with dissolve
            if incest_story:
                neus "Are you satisfied now? I have to clean myself up. (My tits made my big brother cum hehehe)"
            else:
                neus "Are you satisfied now? I have to clean myself up. (My tits made him cum hehehe)"
            $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
            scene black
            "She cleans herself"
            if is_titjob<1:
                if quest_v2:
                    call addLust(2)
                $ is_titjob+=1
        "Sex":
            $ renpy.music.set_volume(0.5, delay=2.0, channel='music')
            scene kitchen2_27 with dissolve
            if incest_story:
                neus "Uhhh, no brother!"    
            else:
                neus "Uhhh, No!"            
            scene kitchen2_28 with dissolve  
            if incest_story:
                mc "Let's go, we've already done it before, doesn't it feel good sis?"
            else:                  
                mc "Let's go, we've already done it before, doesn't it feel good?"
            neus "N-No"
            call splash_message(_("Moments later")) from _call_splash_message_21
            play char3 sex2
            scene kitchen2_29 with dissolve
            neus "(How did we end up doing this?)"
            neus "Ahh (It's so big.)"
            neus "Haa Haaa Haaa"
            mc "I'm about to cum."
            if incest_story:
                neus "Please, cum outside brother."
            else:
                neus "Please, cum outside."
            menu:
                "Inside":  
                    stop char3
                    play charM cum1                              
                    scene kitchen2_30 with flash2
                    play char1 climax3
                    neus "Uhhh"
                    neus "(It's hot.)"
                    neus "(I will have to take a morning-after pill.)"
                "Outside":
                    stop char3
                    play charM cum1  
                    scene kitchen2_31 with flash2
                    play char1 climax3
                    neus "Uhh"
                    scene kitchen2_32 with dissolve
                    neus "Thank you for not cumming inside."               
            menu:
                "More"((not quest_v2 and questMain_7.completion) or (quest_v2 and questMain_v2_13.completion)):  
                    scene black with dissolve                  
                    neus "Mmmm?"
                    play char3 sex2
                    scene kitchen2_33 with dissolve
                    neus "Haa Haaa Haaa"
                    stop char3
                    $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
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
                    jump kitchen2 
                "Leave": 
                    $ renpy.music.set_volume(1.0, delay=2.0, channel='music')
                    scene black with dissolve                   
                    "She cleans herself"
                    if is_sex<1:
                        if quest_v2:
                            call addLust(3)
                        $ is_sex+=1          
        "Back":
            jump kitchen2
    jump kitchen2_action
label food_event2:
    scene kitchen2_25 with dissolve
    ""
    jump time_advances
#----------------------------Level 3---------------------------------
default kitchen3_outfit_type=0
default kitchen3_is_view_outfit_intro=False
default kitchen3_is_view_outfit_intro2=False
default kitchen3_is_active_outfit=False
default is_view_kitchen3_outfit1=False
default is_view_kitchen3_outfit2=False
screen kitchen3:
    if neus_routine[time]=="kitchen":
        if kitchen3_outfit_type==0:
            imagebutton:
                auto "rooms/kitchen/lvl3/kitchen3_0_0_%s.png"            
                focus_mask True            
                action Jump("kitchen3")
                tooltip "%s"%neusname
        if kitchen3_outfit_type==1:
            imagebutton:
                auto "rooms/kitchen/lvl3/kitchen3_out1_0_%s.png"            
                focus_mask True            
                action Jump("kitchen3_outfit1_pre")
                tooltip "%s"%neusname
        if kitchen3_outfit_type==2:
            imagebutton:
                auto "rooms/kitchen/lvl3/kitchen3_out2_0_%s.png"            
                focus_mask True            
                action Jump("kitchen3_outfit2_pre")
                tooltip "%s"%neusname
label kitchen3:          
    scene kitchen3_1_0
    show screen kitchen_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    menu:   
        "Talk":           
            jump kitchen3_talk
        "Action":
            jump kitchen3_action
        "Outfit":
            if not(kitchen3_is_view_outfit_intro):
                menu:                
                    "Requirements: Object creation: {color=#cc0066}[spell_2_2.is_active]{/color} and outfit photo: {color=#cc0066}[kitchen3_is_active_outfit]{/color}"
                    "Give outfit"((kitchen3_is_active_outfit and spell_2_2.is_active)):     
                        hide screen spell_screen                              
                        jump kitchen3_outfit1_intro1            
                    "Back":
                        jump kitchen3    
            else:
                menu:                
                    "Outfit 1"((kitchen3_is_active_outfit and spell_2_2.is_active)) if kitchen3_is_view_outfit_intro:
                        hide screen spell_screen 
                        scene kitchen3_b_6 with dissolve
                        neus "Alright."
                        $kitchen3_outfit_type=1 
                        jump kitchen3_outfit1   
                    "Outfit 2"((neus_lust>=100)) if (kitchen3_is_view_outfit_intro2):
                        hide screen spell_screen 
                        scene kitchen3_b_6 with dissolve
                        neus "A-Alright."
                        $ kitchen3_outfit_type=2
                        jump kitchen3_outfit2
                    "Outfit 1 intro"((kitchen3_is_active_outfit and spell_2_2.is_active)) if kitchen3_is_view_outfit_intro: 
                        hide screen spell_screen                                   
                        jump kitchen3_outfit1_intro1            
                    "Back":
                        jump kitchen3                  
        "Leave":           
            jump rooms
label kitchen3_talk:
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    scene kitchen3_1_0
    hide screen spell_screen   
    $ xsize_value = 650
    $ neus_lust_label_location = "kitchen_movie"
    call neus_lust_label
    menu(screen="custom_choice_enhanced"):
        "What do you want to talk about?"                  
        "Boobs": 
            mc "Are you still worried about your small tits?"
            play music DarkestSoul_Schmidt fadeout 0.5 volume 0.5
            scene kitchen3_t_0 with dissolve
            neus "Are you looking to start a fight?"
            neus "We may be a couple, and I may have agreed to let you do certain things to me-"
            neus "But if you're going to bother me, I won't tolerate it."
            scene kitchen3_t_1 with dissolve
            mc "You know I prefer your big butt, but I've heard that if you give them massages, they grow."
            scene kitchen3_t_2 with dissolve
            stop music fadeout 0.5
            neus "Really?"
            play music Trance_Steele volume 0.3 fadeout 1.0
            if incest_story:
                mc "Yes, let me help you little sister."
            else:
                mc "Yes, let me help you."
            scene kitchen3_t_3 with dissolve
            neus "W-Wait, wait, why are you getting closer?"
            scene kitchen3_t_4 with fadesex            
            neus "Haa Haa Haa"     
            if incest_story:
                neus "Be careful brother, my breasts are very sensitive... haa haa ooh!"
            else:      
                neus "Be careful, my breasts are very sensitive... haa haa ooh!"
            scene kitchen3_t_5 
            neus "And don't put your hand there."           
            mc "You know, I also heard that if you drink a special milk, they grow faster."
            scene kitchen3_t_6 with dissolve
            neus "Really? Although it's probably a scam... I've tried a many things, and none of them work."
            mc "Well, I think this one will actually work."
            scene kitchen3_t_7 with dissolve
            neus "Huh!?"  
            call splash_message(_("Moments later")) from _call_splash_message_37
            scene kitchen3_t_8 with dissolve
            neus "{bt=2}{=lust_style}Uhhh.{/bt}"(multiple=2) 
            mc "If you drink it every day, they might grow."(multiple=2) 
            if incest_story:
                mc "Since you're my little sister, I'm willing to provide it to you for free."
            else:
                mc "I'm willing to provide it to you for free."
            scene kitchen3_t_9 with dissolve
            neus "Mmm... I don't think it works like that... (He just wants me to drink his semen every day...)"
            stop music fadeout 1.0
            scene black
            "She cleans herself"
            if is_boobs<1:
                call addLust(2)
                $ is_boobs+=1
        "Movie plans[neus_lust_label]" (neus_lust>=100):
            $ kitchen_room3_is_view_talk_movie = True
            scene kitchen3_t_10 with dissolve
            neus "There's a new movie premiering today."
            neus "Wanna come watch it with me?"
            scene kitchen3_t_11 with dissolve
            mc "You mean the one that got terrible reviews?"
            mc "What about that movie from last week? I still haven’t seen it."
            scene kitchen3_t_10 with dissolve
            neus "Oh yes, that one was so good, especially when..."
            mc "No spoilers."
            scene kitchen3_t_12 with dissolve
            neus "And that plot twist totally caught me off guard."
            mc "That's straight-up manipulation."
            scene kitchen3_t_13 with dissolve
            neus "Just like the magazine thing... and making me your girlfriend."
            mc "Looks like we’ve got a date for tonight."
            scene kitchen3_t_14 with dissolve
            neus "Well, actually the movie starts in 3 hours."           
            mc "Alright, I’ll be ready."
            stop music fadeout 0.5
            play ambience people fadein 1.0 volume 0.2
            scene kitchen3_t_15 with storyfx            
            swoman "Here is your order."
            scene kitchen3_t_16 with dissolve
            "You reach into your pocket and notice something is missing."
            scene kitchen3_t_17 with dissolve
            neus "I'll pay."
            scene kitchen3_t_18 with dissolve
            if incest_story:
                mc "I'll pay you back later, sis."
            else:
                mc "I'll pay you back later."
            scene kitchen3_t_19 with dissolve
            neus "Don't worry about it, after all, I'm the one who invited you to the movies."
            scene kitchen3_t_20 with dissolve
            neus "I can't wait for the movie to start."
            stop ambience fadeout 1.0
            scene kitchen3_t_21 with storyfx
            neus "*Murmuring*{size=-15} 10 [firstname], 11 [firstname], 12 [firstname]..."
            mc "*Sarcastic tone* Wow, this movie sure is fascinating."
            scene kitchen3_t_22 with dissolve
            neus "Oh, absolutely. So thrilling."
            mc "Especially that part earlier."
            scene kitchen3_t_23 with dissolve
            neus "Seriously, I missed it."
            mc "..."
            scene kitchen3_t_24 with dissolve
            neus "..."
            scene kitchen3_t_25 with fade
            if incest_story:
                mc "Hey little sister, what if we try another type of entertainment?"
                scene kitchen3_t_26 with dissolve
                neus "*whispers* Hey, hey, brother, there are people around."
            else:
                mc "Hey, what if we try another type of entertainment?"
                scene kitchen3_t_26 with dissolve
                neus "Hey, hey, there are people around."
            scene kitchen3_t_27 with dissolve
            rcouples "Oh yes, right there! That's the spot {e_heartbt=FF0000}"(multiple=2)
            mc "I don't think the few people who have come to see this movie will even notice us. I think they are too busy with their own... activities."(multiple=2)
            scene kitchen3_t_28 with dissolve
            play char1 penetration3
            neus "Uh."
            scene kitchen3_t_29 with dissolve
            play char3 sex6
            if incest_story:
                neus "{bt=1}{=lust_style}Ha ha ha ha brother!{/bt} {e_heartbt=FF0000}"
                mc "Hey, sis, even if there aren't many people, you should still lower your voice."
            else:
                neus "{bt=1}{=lust_style}Ha ha ha ha{/bt}"
                mc "Hey, even if there aren't many people, you should lower your voice."
            neus "Shut up, it's your fault, you're going too fast... it's hard for me to contain my voice."
            neus "This is so intense."
            neus "If you keep touching that spot, I..."
            scene kitchen3_t_29_1 with dissolve
            if incest_story:
                neus "{bt=2}I'm cumming brother{/bt} {e_heartbt=FF0000}"
            else:
                neus "{bt=2}I'm cumming {e_heartbt=FF0000}{/bt}"
            stop char3
            play charM cum1
            scene kitchen3_t_29_2 with dissolve   
            play char1 climax1      
            neus "Uh!"
            scene kitchen3_t_30 with dissolve
            neus "Oh, it's spilling."
            menu:
                "''Help her''(Butt Plug)":
                    scene kitchen3_t_31 with dissolve
                    mc "I have something for situations like this"
                    scene kitchen3_t_31_1 with dissolve
                    play char1 penetration3
                    neus "Uh"
                    scene kitchen3_t_32 with storyfx
                    if incest_story:
                        neus "Hey brother, can we go back home?"
                    else:
                        neus "Hey, can we go back home?"
                    scene kitchen3_t_33 with dissolve
                    neus "It's embarrassing walking around like this"
                    if incest_story:
                        mc "Let's take a short walk and then we'll head back, okay sis?"
                    else:
                        mc "Let's take a short walk and then we'll head back, okay?"
                    scene kitchen3_t_34 with dissolve
                    neus "Well, if it's just a short walk, I guess that's fine."
                    play ambience night_ambience volume 0.1
                    scene kitchen3_t_35 with dissolve
                    neus "(I feel so hot and bothered, we walked around the entire city, it was so embarrassing.)"
                    scene kitchen3_t_36 with dissolve
                    mc "That was a good walk, but it's time to go home."(multiple=2)
                    neus "(I can't take it any more...)"(multiple=2)
                    scene kitchen3_t_37 with dissolve
                    ""
                    scene kitchen3_t_38 with dissolve
                    neus "Hey, what are you waiting for? Take me to a hotel."
                    mc "Oh, that would be great"
                    mc "But you know, I forgot my wallet at home, so you'll have to wait until we get back"
                    scene kitchen3_t_39 with dissolve
                    neus "I'll pay"
                    stop ambience fadeout 1.0
                    scene kitchen3_t_40 with dissolve
                    recep "Which room would you like?"
                    mc "Hmm... let me see"
                    scene kitchen3_t_40_1 with dissolve
                    if incest_story:
                        mc "Have you got any preferences... *whispers* little sister?"
                    else:
                        mc "Have you got any preferences, [neusname]?"
                    scene kitchen3_t_41 with dissolve
                    neus "Which is the room farthest from the others and where if someone screamed a lot, it wouldn't be heard?"
                    recep "That would be room 69"
                    scene kitchen3_t_42 with dissolve
                    neus "Come on, let's go"
                    scene kitchen3_t_43 with dissolve
                    if incest_story:
                        mc "*Mocking tone* I didn't expect you to take charge little sister, do you really want it that badly?"
                    else:
                        mc "*Mocking tone* I didn't expect you to take charge, do you really want it that badly?"
                    play sound door_kick
                    scene kitchen3_t_43_1 with dissolve
                    "" with vpunch
                    play music funk_funkadelic_funkstorm volume 0.4
                    scene kitchen3_t_44 with dissolve
                    neus "(Maybe spending the entire day under the sun, with a butt plug in my ass has fried my brain)"
                    scene kitchen3_t_45 with dissolve
                    neus "(But at the moment, I don't really care, all I care about is having sex)"
                    $ renpy.music.set_volume(0.2, delay=3.0, channel='music')
                    scene kitchen3_t_45_1 with dissolve
                    play char1 penetration3
                    neus "{sc=2}UH!{/sc}"
                    scene kitchen3_t_45_2 with dissolve
                    neus "(I'm cumming just by inserting his cock.)"
                    neus "(But...)"
                    scene kitchen3_t_46 with dissolve
                    play char3 sex2
                    neus "{bt=2}{=lust_style}oh oh oh{/bt}"
                    if incest_story:
                        neus "Brother, I want more, give it to me harder"
                    else:
                        neus "I want more, give it to me harder"
                    neus "Fill me with lots of your cum"
                    scene black with dissolve
                    neus "I want more, more, more"
                    stop char3
                    scene kitchen3_t_47 with dissolve
                    mc "(She's speaking unconsciously)"
                    mc "(I guess her brain malfunctioned)"  
                    scene kitchen3_t_48 with dissolve                  
                    menu:
                        "She starts moving her ass from side to side, as if trying to provoke you"
                        "Continue":
                            scene kitchen3_t_49 with dissolve
                            neus "Yes.. yes.. satisfy my tight ass again"
                            scene kitchen3_t_49_1 with dissolve
                            if incest_story:
                                neus "Yes.. put it all the way in brother"
                            else:
                                neus "Yes.. put it all the way in"
                            scene kitchen3_t_50 with dissolve
                            play char1 penetration2
                            neus "{bt=2}Uh!{/bt}"
                            scene kitchen3_t_51 with dissolve
                            play char3 sex4
                            neus "{bt=2}{=lust_style}oh oh oh{/bt}"
                            if incest_story:
                                neus "Yes.. yes.. give lots of love to your little sister's ass..."
                            else:
                                neus "Yes.. yes.. give lots of love to your girlfriend's ass..."
                            neus "Make my ass become addicted to your dick..."
                            neus "Make my ass your dick's girlfriend..."
                            neus "Make my ass crave your dick..."
                            scene kitchen3_t_52 with fade
                            play char3 kissing1 fadein 0.5
                            neus "*kiss kiss*"
                            scene kitchen3_t_52_1 with dissolve
                            if incest_story:
                                neus "Your little sister longs for more kisses, and as your girlfriend, I demand them."
                            else:
                                neus "I long for more kisses, I demand more kisses as your girlfriend."
                            stop char3 fadeout 0.5
                            stop music fadeout 0.5
                            play ambience morning_sounds fadein 1.0
                            scene kitchen3_t_53 with dissolve
                            neus "(My body aches, and I can't quite remember everything that happened yesterday.)"
                            neus "(The last thing I remember is us taking a walk around the city.)"
                            scene kitchen3_t_54 with dissolve
                            mc "You were amazing last night."
                            scene kitchen3_t_55 with dissolve
                            neus "I don't remember what happened... but please forget it."
                            mc "You were very honest, I loved it, and I can't forget it. We should do it again sometime"
                            scene kitchen3_t_56 with dissolve
                            neus "I said forget it, and... can we head home now please?"
                            stop ambience fadeout 1.0
                            scene black with dissolve
                            if incest_story:
                                "After a short trip, you return home with your sister"
                            else:
                                "After a short trip, you return home with [neusname]"
                            $ renpy.music.set_volume(1.0, channel='music')
                            jump next_day
                        "Let her rest":     
                            stop music fadeout 1.0
                            scene black with dissolve           
                            if incest_story:
                                "After resting, you return home with your sister"
                            else:        
                                "After resting, you return home with [neusname]"
                            $ renpy.music.set_volume(1.0, channel='music')
                            jump next_day
                "No":
                    scene black with dissolve
                    if incest_story:
                        "After a short trip, you return home with your sister"
                    else:
                        "After a short trip, you return home with [neusname]"
                    jump time_advances
        "Back":
            jump kitchen3   
    jump kitchen3_talk
label kitchen3_action:
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed
    scene kitchen3_1_0
    hide screen spell_screen
    menu:
        "What do you want to do?"
        "Kiss":
            scene kitchen3_ki_0 with dissolve            
            neus "Okay"
            scene kitchen3_ki_1 with dissolve
            play char1 short_kiss
            if incest_story:
                "Your little sister kisses you"
            else:
                "She kisses you"
            "After a few minutes, she pulls away"
            scene kitchen3_ki_2 with fade
            neus "Can I have a little more?"
            menu:
                "Tease her":
                    mc "What do you mean?"
                    scene kitchen3_ki_3 with dissolve
                    if incest_story:
                        neus "Brother, I know you like teasing me."
                    else:
                        neus "I know you like teasing me."
                    scene kitchen3_ki_4 with dissolve
                    neus "But there's nothing wrong with wanting to kiss my boyfriend, right?"
                    scene kitchen3_ki_5 with dissolve
                    neus "It's not like I'm asking for something perverted."
                    scene kitchen3_ki_6 with dissolve
                    neus "Now be quiet and let me kiss you."
                    scene kitchen3_ki_7 with dissolve
                    play char1 french02
                    if incest_story:
                        "Your sister jumps into your arms and kisses you."
                    else:
                        "She jumps into your arms and kisses you."
                    neus "Chu {e_heartbt=FF0000}"
                    scene kitchen3_ki_8 with fade
                    neus "(That felt good... but if I ask for more, he'll probably tease me again)"
                "Sure":
                    scene kitchen3_ki_1 with dissolve
                    play char1 french02               
                    neus "(I think I'm becoming addicted to his kisses)"
                    neus "Chu {e_heartbt=FF0000}"
                    scene kitchen3_ki_8 with fade
                    neus "Thank you."
            if is_kiss<1:
                call addLust(1)
                $ is_kiss+=1
        "Blowjob":
            mc "Hey, can you give me a blowjob?"
            play music Trance_Steele fadeout 0.5 volume 0.3
            scene kitchen3_b_0 with dissolve
            if incest_story:
                neus "So, you want your little sister, to use her lips and lick your thing?"
            else:
                neus "So, you want me to use my lips and lick your thing?"
            scene kitchen3_b_1 with dissolve
            neus "(It's so big...)"
            scene kitchen3_b_2 with dissolve
            neus "Hehe, I guess I can't avoid it, after all, I'm your girlfriend."
            neus "Besides, it would be bad if you walked around with that erection, you could get arrested."
            scene kitchen3_b_3 with dissolve
            neus "Come here." 
            menu:
                "Never mind, I changed my mind":
                    stop music fadeout 0.5
                    scene kitchen3_b_4 with dissolve
                    neus "Eh! Why?"
                    scene kitchen3_b_5 with dissolve
                    mc "Hmm... I guess I lost interest."
                    scene kitchen3_b_4 with dissolve
                    neus "?"
                    scene kitchen3_b_5 with dissolve
                    play music Trance_Steele fadeout 0.5 volume 0.3
                    mc "But if you really want to give me a blowjob, I could make an exception."
                    scene kitchen3_b_6 with dissolve
                    if incest_story:
                        neus "Saying that I want to suck my brother's dick would be too vulgar, even if I am your girlfriend-"
                    else:
                        neus "Saying that I want to suck you would be too vulgar, even if I'm your girlfriend-"
                    mc "I understand, let's leave it then."
                    scene kitchen3_b_7 with dissolve
                    neus "W-Wait, I want to suck your p-penis."                    
                    mc "Penis?"
                    scene kitchen3_b_8 with dissolve
                    neus "I-I want to suck your d-dick."
                "Continue":
                    pass     
            $ renpy.music.set_volume(0.3, delay=2.0, channel='music')
            scene kitchen3_b_9 with fadesex
            play char3 suck3
            neus "*lick, lick, lick*"
            neus "*suck, suck* (It's so delicious... It's so tasty...)"
            neus "(but I can't say that, I have to try to maintain some decency)"
            if incest_story:
                neus "(I don't want my brother to think I'm some kind of slut who only wants to do sexual things)"
            else:
                neus "(I don't want him to think I'm some kind of slut who only wants to do sexual things)"
            scene kitchen3_b_10 with fadesex
            neus "(It's so big, it's touching my throat.)"
            neus "(It's amazing that my little throat can suck this entire thing.)" 
            if incest_story:
                neus "(Having my big brother fuck my throat is really exciting...)"   
            else:
                neus "(Having him fuck my throat is really exciting...)"           
            menu:
                "Inside":  
                    stop char3
                    play charM cum1 
                    scene kitchen3_b_11 with flash2 
                    play char1 groan1    
                    neus "Uhh!" 
                    scene kitchen3_b_12 with dissolve     
                    neus "(Although I've tried it before, I still can't get used to the taste)"
                    scene kitchen3_b_13 with dissolve 
                    neus "(But if I keep drinking his fluids, I'm afraid I'll become addicted)"
                    play char1 gulp1    
                    scene kitchen3_b_14 with dissolve                                    
                    neus "(I have to avoid swallowing it next time)"
                "Outside":
                    stop char3
                    play charM cum1  
                    scene kitchen3_b_15 with flash2
                    neus "Ah, you got your cum all over my face."
                    neus "(Maybe, having him cum inside my mouth...)"
                    scene kitchen3_b_16 with dissolve
                    neus "(No, that wouldn't be good either.)"     
            stop music fadeout 1.0       
            scene black with dissolve
            "She cleans herself"
            if is_blowjob<1:
                call addLust(2) from _call_addLust_3
                $ is_blowjob+=1
            $ renpy.music.set_volume(1.0, channel='music')
        "Sex":
            scene kitchen3_2 with dissolve
            neus "Mmm... I guess I can't avoid it"
            stop music fadeout 1.0
            scene kitchen3_3 with fadesex
            play char3 sex2
            neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
            if incest_story:
                mc "You're very tight little sister, are you trying to squeeze me?"
            else:
                mc "You're very tight, are you trying to squeeze me?"
            neus "That's just your imagination"
            if incest_story:
                neus "As if I want to be filled with my brother's viscous and hot..."
            else:
                neus "As if I want to be filled with your viscous and hot..."
            neus "..."
            neus "Forget it and cum already"        
            menu:
                neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                "Inside":
                    stop char3
                    play charM cum1
                    scene kitchen3_4 with flash2
                    play char1 climax1
                    neus "Uh"
                    scene kitchen3_5 with dissolve
                    neus "(So hot)"
                "Outside":
                    stop char3
                    play charM cum1
                    scene kitchen3_6 with flash2
                    play char1 climax1
                    neus "Ohh"                  
            scene black with dissolve
            "After a while, she recovers and cleans herself."
            if is_sex<1:
                call addLust(3) from _call_addLust_12
                $ is_sex+=1
        "Anal": 
            scene kitchen3_7 with dissolve
            neus "Actually, I have something to do."
            scene kitchen3_8 with dissolve
            neus "See you later."
            stop music fadeout 1.0
            scene black with dissolve
            if incest_story:
                "Before your little sister escapes, you grab her and put her on the table."
                scene kitchen3_9 with dissolve
                neus "Okay, but just this once brother."
            else:
                "Before she escapes, you grab her and put her on the table."
                scene kitchen3_9 with dissolve
                neus "Okay, but just this once."
            scene kitchen3_10 with dissolve
            play char1 penetration3 volume 0.75
            neus "Uh."
            mc "Does having anal sex bother you that much?"
            neus "(It's not that I don't like it, in fact, it feels somewhat good.)"
            scene kitchen3_11 with dissolve
            play char3 sex2
            neus "{bt=2}{=lust_style}ah ah ah ah{/bt} (But I don't want to become addicted to anal sex.)"
            mc "You know, I love your tight ass."
            mc "It's impressive how you can take my entire cock."
            mc "I always feel like making love to your cute little ass."
            neus "(What the hell is he saying, as if that shit makes me happy? {e_heartbt=FF0000})"
            scene kitchen3_12 with fadesex
            mc "Is it just me or has your ass become tighter."
            neus "It's just your imagination."
            scene kitchen3_13 with dissolve
            neus "I'm {sc=2}cumming!{/sc}"
            scene kitchen3_12 with fade
            menu:                
                "Inside":
                    stop char3
                    play charM cum1
                    scene kitchen3_14 with dissolve
                    play char1 climax1                     
                    neus "Uhhh."
                    scene kitchen3_15 with dissolve
                    if incest_story:
                        mc "Did that feel good little sister?"
                    else:
                        mc "Did that feel good?"
                    scene kitchen3_16 with dissolve
                    neus "It might have felt somewhat good, for now."
                    scene black with dissolve
                    "She moves away from you and cleans herself."
                "Outside":
                    stop char3
                    play charM cum1
                    scene kitchen3_17 with dissolve
                    play char1 climax1                    
                    neus "Ahhh."
                    scene black with dissolve
                    "After a while, she recovers and cleans herself."
            if is_sexanal<1:
                call addLust(3) from _call_addLust_13 
                $ is_sexanal+=1             
        "Back":
            jump kitchen3
    jump kitchen3_action
#-----------------outfit1-----------------
label kitchen3_outfit1_pre:
    $choice_kitchen=renpy.random.choice([0,1])
    if choice_kitchen==1 or not(is_view_kitchen3_outfit1):
        $ is_view_kitchen3_outfit1=True 
        jump kitchen3_outfit1_intro2
    jump kitchen3_outfit1
label kitchen3_outfit1:    
    scene kitchen3_out1_1
    show screen kitchen_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed 
    $ xsize_value = 650
    $ neus_lust_label_location = "kitchen_outfit"
    call neus_lust_label
    menu:       
        "Change outfit":
            menu(screen="custom_choice_enhanced"):
                "Normal":
                    hide screen spell_screen
                    scene kitchen3_out1_2 with dissolve
                    neus "Okay"
                    $kitchen3_outfit_type=0
                    jump kitchen3  
                "Outfit 2[neus_lust_label]"((neus_lust>=100)) if not(kitchen3_is_view_outfit_intro2):
                    hide screen spell_screen
                    jump kitchen3_outfit2_intro2
                "Outfit 2"((neus_lust>=100)) if (kitchen3_is_view_outfit_intro2):
                    hide screen spell_screen 
                    scene kitchen3_out2_5 with dissolve
                    neus "A-Alright."
                    $ kitchen3_outfit_type=2
                    jump kitchen3_outfit2
                "Outfit 2 intro"((neus_lust>=100)) if (kitchen3_is_view_outfit_intro2):
                    hide screen spell_screen
                    jump kitchen3_outfit2_intro2
                "Back":
                    jump kitchen3_outfit1   
        "Blowjob":
            hide screen spell_screen     
            mc "Have you had breakfast? If you want, I can provide you with some nutrients."
            scene kitchen3_out1_3 with dissolve
            if incest_story:
                neus "... uh huh, you know, if you want your little sister to give you a blowjob, all you need to do is ask, right?"
            else:
                neus "... uh huh, you know, if you want me to give you a blowjob, all you need to do is ask, right?"
            mc "?... I just wanted to give you some ''nutrients''."
            stop music fadeout 1.0
            scene kitchen3_out1_4 with fade
            neus "Yeah, yeah, sure, you're fooling no one. Now give me your ''nutrients''."
            scene kitchen3_out1_5 with dissolve
            play char3 suck2
            neus "*suck suck*gulp"
            if incest_story:
                neus "(... I've realized that I don't mind having my brother's thing in my mouth, in fact, I think I like it)"
            else:
                neus "(... I've realized that I don't mind having his thing in my mouth, in fact, I think I like it)"
            neus "*suck suck*..."
            scene kitchen3_out1_6 with flash2
            stop char3
            play charM cum1
            neus "Mmm"
            scene kitchen3_out1_7 with dissolve
            play char1 gulp1
            neus "*sarcastically* Thanks for the ''nutrients''."
            if incest_story:
                mc "You're welcome little sister."
            else:
                mc "You're welcome."
            scene kitchen3_out1_8 with dissolve
            neus "Mmmm"
            scene black with dissolve
            "She cleans herself"
            if is_blowjob_outfit<1:
                call addLust(3) from _call_addLust_24
                $ is_blowjob_outfit+=1
        "Sex":
            hide screen spell_screen
            mc "Hey, you know, I really feel like some freshly baked bread."
            scene kitchen3_out1_9 with dissolve
            neus "?"
            mc "I wanted to know if you'd allow me to use your oven to bake some ''bread''."
            scene kitchen3_out1_10 with dissolve
            neus "Mmm... (That's a new way of saying he wants to impregnate me.)"
            scene kitchen3_out1_11 with dissolve
            neus "No, the ''oven'' isn't available and won't be for a long time."
            scene kitchen3_out1_12 with dissolve
            mc "Are you sure? Wouldn't it be nice to make sure the oven is in perfect condition?"
            mc "Baking our first loaf of bread."
            scene kitchen3_out1_11 with dissolve
            neus "The oven is in perfect condition, and there's no need to check it."
            stop music fadeout 1.0
            play sound clothes
            scene kitchen3_out1_13 with fade
            if incest_story:
                mc "Come on sis, just a little test to make sure it bakes good bread."
            else:
                mc "Come on, just a little test to make sure it bakes good bread."           
            scene kitchen3_out1_14 with dissolve            
            neus "..."
            mc "I suppose I'll put some dough in the oven."
            scene kitchen3_out1_15 with dissolve
            play char1 penetration3
            neus "Ah."
            mc "The oven has a good temperature, and it's very snug."
            mc "I'd say this oven is ready to bake its first loaf of bread."
            scene kitchen3_out1_16 with fadesex
            play char3 sex2
            neus "Impossible {bt=2}{=lust_style}Ha{/bt} , I'm {bt=2}{=lust_style}Ha{/bt} not {bt=2}{=lust_style}Ha{/bt} rea-"
            neus "{bt=2}{=lust_style}Ha ha ha.{/bt}"
            neus "(His dough feels so good inside my oven.)"            
            neus "(If this keeps up, my uterus will want to bake many loaves of bread)"
            neus "{bt=2}{=lust_style}Please{/bt} put a lot of dough in my ove-... (I don't have to maintain composure)"
            scene kitchen3_out1_17 with dissolve
            neus "I'm cumming {e_heartbt=FF0000}"
            scene kitchen3_out1_18 with dissolve
            stop char3
            play charM cum1
            neus "Uh (There's a lot of dough in my oven)."
            scene kitchen3_out1_19 with dissolve
            if incest_story:
                neus "(I have to remember to take the pill, or my brother's loaf of bread will be baking in my uterus)."
            else:
                neus "(I have to remember to take the pill, or there will be a loaf of bread baking in my uterus)."
            scene black with dissolve
            "She cleans herself"
            if is_sex_outfit<1:
                call addLust(4) from _call_addLust_25
                $is_sex_outfit+=1
        "Leave":           
            jump rooms
    jump kitchen3_outfit1
label kitchen3_outfit1_intro1:
    $kitchen3_is_view_outfit_intro=True
    $kitchen3_outfit_type=1
    mc "I have something for you."
    scene kitchen3_ci1_0 with dissolve
    neus "Uh, new clothes, great."
    scene kitchen3_ci1_1 with fade
    neus "Mmm... just an apron (I’ve definitely seen this in certain... videos.)."
    scene kitchen3_ci1_2 with dissolve
    neus "(I think women use it as an invitation for sex)."
    scene kitchen3_ci1_3 with dissolve
    neus "I appreciate the gift, but I'll pass."
    mc "Oh, come on. Scared?"
    scene kitchen3_ci1_4 with dissolve
    neus "Huh?"
    mc "Let's play rock-paper-scissors, and if I win, you wear it, and if you win, I'll give you anything you ask for."
    scene kitchen3_ci1_5 with dissolve
    neus "Do you really think I'll fall for that?"
    mc "Scaredy-cat"
    scene kitchen3_ci1_6 with dissolve
    neus "Let's do it. You better prepare some treats."
    mc "You'll end up with diabetes if you keep going like this, but okay."    
    scene kitchen3_ci1_7 with fade
    neus "(How the hell did he win every game? It's supposed to be a game of luck.)"
    mc "You can turn around now."
    scene kitchen3_ci1_8 with dissolve
    mc "I think those panties are unnecessary."
    scene kitchen3_ci1_9 with dissolve
    neus "We never bet that I had to wear just the apron, hehe."
    mc "I get it. Let's play another round."
    scene kitchen3_ci1_10 with dissolve
    neus "No way, I won't play with cheaters."
    mc "Your moves are easy to predict, so I wouldn't call it cheating, just that you're bad at the game."
    scene kitchen3_ci1_11 with dissolve
    neus "Silence... I'm not going to play."
    scene kitchen3_ci1_12 with dissolve     
    neus "Moreover, wearing this is a bit embarrassing."
    mc "You know, I have another one, but it's little smaller."
    scene kitchen3_ci1_13 with dissolve
    neus "Forget it."  
    scene black with dissolve  
    call addLust(1)
    jump kitchen3_outfit1
label kitchen3_outfit1_intro2:
    scene kitchen3_out1_in_0  
    if incest_story:  
        $ menu_text = "Your sister"
    else:
        $ menu_text = neusname
    menu:
        "[menu_text] doesn't notice your presence."
        "Give a good morning greeting":
            play music Trance_Steele fadeout 0.5 volume 0.3
            scene kitchen3_out1_in_1 with dissolve
            if incest_story:
                mc "Good morning little sister"
            else:
                mc "Good morning"
            scene kitchen3_out1_in_2 with dissolve
            neus "Hey, I'm busy!"
            if incest_story:
                mc "Come on, let have some fun."
            else:
                mc "Come on, there's nothing wrong with this."
            scene kitchen3_out1_in_3 with dissolve
            neus "S-Stop. {size=-10}This is dangerous."
            scene kitchen3_out1_in_4 with dissolve
            mc "Don't be boring."
            scene kitchen3_out1_in_5 with dissolve
            play char1 penetration4
            neus "{=lust_style}Huh?"
            $ renpy.music.set_volume(0.3, delay=2.0, channel='music')
            mc "I'm going to start moving."
            scene kitchen3_out1_in_6 with dissolve
            play char3 sex2
            neus "{=lust_style}Ohh Ohh Ohh"
            neus "(I should stop him, but it feels...)"
            if incest_story:
                mc "How does my greeting feel sister?"
            else:
                mc "How does my greeting feel?"
            scene kitchen3_out1_in_7 with dissolve
            neus "{size=-15}Not bad!"
            scene kitchen3_out1_in_8 with dissolve
            stop char3
            play char1 penetration3
            mc "I can't hear you."
            neus "Oh, it feels {bt=1}{=lust_style}good{/bt}"
            scene kitchen3_out1_in_9 with dissolve
            play char3 sex3
            mc "I'm glad you're starting to be more honest."
            mc "If you're always honest with me, I promise to always give you love."
            neus "{bt=1}{=lust_style}Ahh ahh ahh{/bt}"
            scene kitchen3_out1_in_10 with dissolve
            neus "I'm cumming... I'm cumming"
            stop char3
            play charM cum1
            scene kitchen3_out1_in_11 with flash2              
            play char1 climax1
            neus "Oh!"
            scene kitchen3_out1_in_12 with dissolve
            neus "(My body feels so horny, I want more...)"
            scene kitchen3_out1_in_13 with dissolve
            stop music fadeout 0.5
            neus "... Damn it, my breakfast is burnt."
            scene kitchen3_out1_in_14 with dissolve
            neus "Hey, because of you, my breakfast is burnt. You have to pay."
            mc "What do you want me to do?"
            scene kitchen3_out1_in_15 with dissolve
            neus "Well... if you help me in the kitchen (I hate to admit it, but he's good at cooking)"
            mc "Okay"
            scene black with dissolve
            if incest_story:
                neus "Hey, I didn't mean this kind of help brother, oh... {e_heartbt=FF0000}"
            else:
                neus "Hey, I didn't mean this kind of help, oh... {e_heartbt=FF0000}"
            scene kitchen3_out1_in_16 with dissolve
            neus "(Damn it, because of him, it took us 2 hours to make breakfast.)"
            scene kitchen3_out1_in_17 with dissolve
            neus "(And I almost fainted, it's dangerous to engage in that kind of activity without breakfast.)"
            scene kitchen3_out1_in_16 with dissolve
            neus "(Even though his food is very delicious, it's risky to cook together)"
            $ renpy.music.set_volume(1.0, channel='music')
            call addLust(4) from _call_addLust_4
            jump time_advances
        "No":
            pass
    jump kitchen3_outfit1
#-----------------outfit2-----------------
label kitchen3_outfit2_intro2:
    $ kitchen3_is_view_outfit_intro2=True    
    if incest_story:
        mc "Hey sister, I have another gift for you."
    else:                                            
        mc "Hey, I have another gift for you."
    scene kitchen3_out2_1 with dissolve
    neus "Really, let me see it."
    scene kitchen3_out2_2 with dissolve
    neus "Mmm..."
    neus "(I guess I was expecting this, but it looks kinda nice)."
    scene kitchen3_out2_3 with dissolve
    neus "..."
    scene kitchen3_out2_4 with fadesex
    if incest_story:
        mc "It looks great on you sis."
    else:
        mc "It looks great on you."
    neus "(Damn, I shouldn't have put it on, but I was curious to see how it would look on me)."
    jump kitchen3_outfit2

label kitchen3_outfit2_pre:
    $choice_kitchen=renpy.random.choice([0,1])
    if choice_kitchen==1 or not(is_view_kitchen3_outfit2):
        $ is_view_kitchen3_outfit2=True 
        jump kitchen3_outfit2_intro1
    jump kitchen3_outfit2
label kitchen3_outfit2:
    scene kitchen3_out2_6
    show screen kitchen_spell
    play music talk_and_walk volume 0.05 fadeout 1.0 if_changed    
    menu:       
        "Change outfit":            
            menu:
                "Normal":
                    hide screen spell_screen
                    scene kitchen3_out2_33 with dissolve
                    neus "Okay"
                    $kitchen3_outfit_type=0
                    jump kitchen3
                "Outfit 1":
                    hide screen spell_screen
                    scene kitchen3_out2_33 with dissolve
                    if incest_story:
                        neus "O-Okay brother"
                    else:
                        neus "O-Okay"
                    $kitchen3_outfit_type=1
                    jump kitchen3_outfit1
                "Back":
                    jump kitchen3_outfit2 
        "Kiss":
            hide screen spell_screen
            scene kitchen3_out2_20 with dissolve
            if incest_story:
                "Your sister sticks the knife into the table."
            else:
                "She sticks the knife into the table."
            scene kitchen3_out2_21 with dissolve
            "And without saying anything, she pounces on you."
            play char1 mmm1
            scene kitchen3_out2_22 with dissolve
            "She kisses you affectionately."
            play char1 mmm2 fadeout 2.0
            neus "*murmuring* {size=-10}A little more."
            scene kitchen3_out2_23 with dissolve
            play char1 french03 fadeout 2.0
            "She hugs you tightly and doesn't let go until she is satisfied."
            scene kitchen3_out2_24 with dissolve
            neus "Satisfied."
            scene kitchen3_out2_25 with dissolve
            neus "(I love kisses, but I have to keep my composure a bit)."
        "Blowjob":
            hide screen spell_screen
            scene kitchen3_out2_26 with dissolve
            neus "So you want to supply me with smelly and sticky nutrients."
            mc "If you don't want to, it's okay."
            mc "I think I can throw them somewhere else."
            scene kitchen3_out2_27 with dissolve
            neus "That's a waste."
            neus "Although I don't like it much, it's better to not let it go to waste."
            stop music fadeout 1.0
            scene kitchen3_out2_28 with fade
            neus "So I'll take these nutrients."
            scene kitchen3_out2_29 with dissolve
            neus "(delicious)"
            scene kitchen3_out2_30 with fadesex
            play char3 suck4
            neus "*sucking* lick lick"
            neus "*Suck suck*"
            stop char3
            play charM cum1
            scene kitchen3_out2_31 with dissolve
            neus "Uh"
            neus "My stomach is being filled with lots of nutrients"
            play char1 gulp1
            scene kitchen3_out2_32 with dissolve
            neus "Ahhh!"             
            scene black with dissolve
            "She cleans herself"    
        "Sex":  
            play music Trance_Steele fadeout 0.5 volume 0.2
            hide screen spell_screen
            scene kitchen3_out2_34 with dissolve
            if incest_story:
                "Without saying anything, your little sister climbs onto the table and positions herself."
            else:
                "Without saying anything, she climbs onto the table and positions herself."
            scene kitchen3_out2_35 with dissolve
            neus "..."
            mc "When did you become so assertive."
            scene kitchen3_out2_36 with dissolve
            neus "Shut up and do it quickly."
            menu:
                "Tease her":
                    mc "Mmm... I think I just want to enjoy the view."
                    scene kitchen3_out2_37 with dissolve
                    neus "And what is this, liar?"
                    mc "Well, I think that's enough. Thanks for the beautiful scenery."
                    scene kitchen3_out2_38 with dissolve
                    if incest_story:
                        neus "Just fuck me, okay? Please brother."
                    else:
                        neus "Just fuck me, okay? Please."
                    mc "Alright, I love your honesty."
                "Continue":
                    mc "Well, well."
            $ renpy.music.set_volume(0.3, delay=2.0, channel='music')
            scene kitchen3_out2_39 with dissolve
            play char1 penetration3 volume 0.5
            neus "Uh"
            scene kitchen3_out2_40 with fadesex
            play char3 sex6
            mc "As always, your oven is the best."
            neus "{bt=2}{=lust_style}Ha ha ha ha{/bt}"
            neus "I'm going to cum... I'm going to..."
            stop char3
            play charM cum1 
            scene kitchen3_out2_41 with dissolve
            play char1 climax1
            neus "Uh"
            stop music fadeout 1.0
            neus "(My oven is overflowing with so much dough)"
            scene kitchen3_out2_42 with dissolve
            neus "(If I didn't take my pills, I would have already baked dozens of loaves)"
            scene black with dissolve
            "After recovering, she cleans herself."
            $ renpy.music.set_volume(1.0, channel='music')
        "Leave":           
            jump rooms
    jump kitchen3_outfit2
label kitchen3_outfit2_intro1:
    scene kitchen3_out2_7 with dissolve
    menu:
        neus "*Humming* {e_musical2=FFF}"
        "Accept offer":
            play music Trance_Steele fadeout 0.5 volume 0.2
            scene kitchen3_out2_8 with dissolve
            mc "Good morning, and thank you for the breakfast you offer me"
            scene kitchen3_out2_9 with dissolve
            neus "It's not the right time, I'm not in the mood"
            scene kitchen3_out2_10 with dissolve
            mc "That's not what I interpret from someone who isn't wearing panties"
            mc "That's a clear invitation that you want to be my breakfast"
            scene kitchen3_out2_11 with dissolve
            $ renpy.music.set_volume(0.3, delay=2.0, channel='music')
            mc "Therefore, I claim this delicious breakfast"
            scene kitchen3_out2_12 with dissolve
            play char1 penetration3 volume 0.5
            neus "Uhh!"
            mc "I love this pancake so crispy and delicious"
            scene kitchen3_out2_13 with dissolve
            play char3 sex6
            if incest_story:
                neus "Stop {bt=2}{=lust_style}Ha{/bt} saying {bt=2}{=lust_style}Ha{/bt} weird things {bt=2}{=lust_style}Ha{/bt} brother {bt=2}{=lust_style}Ha{/bt}"
            else:
                neus "Stop {bt=2}{=lust_style}Ha{/bt} saying {bt=2}{=lust_style}Ha{/bt} weird things {bt=2}{=lust_style}Ha{/bt}"
            neus "{bt=2}{=lust_style}oh oh oh oh{/bt}"
            mc "Well, this mouth down here disagrees"
            neus "{bt=2}{=lust_style}oh oh oh oh{/bt}"
            scene kitchen3_out2_14 with dissolve
            neus "I'm cumming"
            stop char3
            play charM cum1
            scene kitchen3_out2_15 with dissolve
            play char1 climax1
            neus "Uh"
            scene kitchen3_out2_16 with dissolve
            mc "Hey, can I have some more of this delicious pancake?"
            scene kitchen3_out2_17 with dissolve
            neus "I guess I can allow you to have a little more"
            scene kitchen3_out2_18 with fadesex
            play char3 breathing1
            neus "{bt=2}{=lust_style}I shaid jhust a lhittle mhore, you ahte all my panchakes{/bt}\n(I said just a little more, you ate all my pancakes)"
            scene kitchen3_out2_19 with dissolve
            neus "There's nothing left"
            if incest_story:
                mc "Thank you sis, they were delicious"
            else:
                mc "Thank you, they were delicious"
            stop char3
            stop music fadeout 1.0
            scene black with dissolve
            "After making new pancakes, she let you go"
            $ renpy.music.set_volume(1.0, channel='music')
            jump kitchen3_outfit2
        "No":
            jump kitchen3_outfit2

label food_event3:
    scene kitchen2_25 with dissolve
    ""
    jump time_advances
#----------------------------Object---------------------------------
label key_neus:
    scene kitchen1_22    
    "You found the key to [neusname]'s room."
    $ inventory.add_item(key_room_neus)
    if quest_v2:
        $ questSide_v2_4.completion = True
    else:
        $ questSide_3.completion = True
    $ is_change_quest = True
    call notify_personalized(_("Side Quest updated")) from _call_notify_personalized_33
    jump rooms        
