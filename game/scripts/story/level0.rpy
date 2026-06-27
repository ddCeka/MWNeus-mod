image level0_2_20:
    "animation/start_image/level0_2_17.webp" with dissolve           
    Brightness0_2_a 
    "story/level0/level0_2_20_0.webp" with dissolve     
    Brightness0_a       
    Brightness0_2_a      
    Brightness0_a 
    Brightness0_2_a       
    Brightness0_a
    "story/level0/level0_2_20_1.webp" with dissolve

label level0_0a:
    scene level0_0_0 with storyfx
    mc "Hey, good morning"
    neus "Mmm ..." 
    if not date_ask:
        mc "Drinking milk won't make them grow"
        play music DarkestSoul_Schmidt volume 0.5 fadeout 0.5           
        scene level0_0_1 with dissolve
        neus "What did you say?"
        mc "They haven't grown in the 10 years you've been drinking it."
        mc "(I think all that milk went somewhere else)"
        scene level0_0_2 with dissolve
        neus "Do you want a fight?"   
        play music [Lobby_Time,Cipher] fadeout 1.0 fadein 1.0 if_changed volume 0.1   
        mc "No, I just don't think you need to worry about it, you're perfect the way you are."     
        scene level0_0_3 with dissolve  
        neus "That's not true. (Hmmm, he must want something, probably chores again.)"
        scene level0_0_4 with dissolve    
        neus "Anyway, I've got stuff to do."
        menu:
            "Propose a date":
                mc "Hey, you said you wanted a boyfriend the other day, right?"   
                mc "So, how about we go on a date tonight?"
                scene level0_0_5 with dissolve
                neus "A date?! With me?!"
                neus "(Wait, no... Be strong.)"
                scene level0_0_6 with dissolve
                if incest_story:
                    neus "We... we can’t go on a date! You’re my brother... that’s wrong!"
                else:
                    neus "I... I can't tonight, sorry."
        scene black with dissolve
        "She quickly leaves the room."
        mc "(Hmm, that didn't go well.)"
        mc "(Perhaps if I increase her lust towards me, she'll find it harder to say no.)"
        call addLust(1,1)
        $ date_ask = True
        $ is_change_quest = True
        $ questMain_v2_1.completion = True
        $ questMain_v2_select = questMain_v2_2
        call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_9 
    else:
        menu:
            "Propose a date":
                mc "(She already turned me down once... pushing might only make things worse.)" 
                mc "(I should increase her lust before trying again.)" 
        
    jump time_advances 

label level0_0:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene level0_0_0 with storyfx
    mc "Hey, good morning"
    neus "Mmm ..."
    if quest_v2:
        play music [Lobby_Time,Cipher] fadeout 1.0 fadein 1.0 if_changed volume 0.1        
        mc "I have tickets to an amusement park for today."
    else:
        menu:                    
            "Drinking milk won't make them grow": 
                play music DarkestSoul_Schmidt volume 0.5 fadeout 0.5           
                scene level0_0_1 with dissolve
                neus "What did you say?"
                mc "They haven't grown in the 10 years you've been drinking it."
                mc "(I think all that milk went somewhere else)"
                scene level0_0_2 with dissolve
                neus "Do you want a fight?"            
            "Propose a date":
                pass
        play music [Lobby_Time,Cipher] fadeout 1.0 fadein 1.0 if_changed volume 0.1        
        mc "Hey, I have tickets to an amusement park for today."   
    scene level0_0_3 with dissolve  
    neus "The one they recently built?"
    mc "Yes, that's the one."
    scene level0_0_4 with dissolve
    neus "I just need to change clothes and then we'll go."
    mc "Great, I'm looking forward to the date."
    scene level0_0_5 with dissolve
    neus "Date?!"
    mc "I take it you're not interested, I guess I won't be needing these tickets."
    scene level0_0_6 with dissolve
    neus "Are you really going to tear them up?"
    neus "W-Wait, it's fine. I-I'll go."
    play music Kazuchi_2_23_am volume 0.5 fadeout 1.0
    call splash_message(_("At the amusement park")) from _call_splash_message_4     
    scene level0_0_7 with dissolve
    "{w=1.5}{nw}"
    show level0_0_8 at rotate_15 with dissolve
    "{w=1.5}{nw}"
    show level0_0_9 at rotate_15_degrees with dissolve
    "{w=1.5}{nw}"     
    scene level0_0_10 with dissolve
    hide level0_0_8   
    hide level0_0_9
    neus "That was really fun. Hehe."
    scene level0_0_10_1 with slidele
    stop music fadeout 2.0
    neus "Mmm!"(multiple=2)
    if incest_story:
        mc "Hey, before we go home, there's something I want to talk to you about, sis."(multiple=2) with hpunch
        mc "I know you always avoid having this conversation with me because we're siblings."
    else:
        mc "Hey, before we go home, there's something I want to talk to you about, [neusname]."(multiple=2) with hpunch
        mc "I know you always avoid having this conversation with me."
    mc "But I want us to talk about our feelings and move our relationship forwa-"
    scene level0_0_10_2 with dissolve
    neus "*nervously* L-Look at how late it is."
    scene level0_0_10_3 with dissolve
    neus "W-We better hurry home."
    scene level0_0_10_4 with dissolve
    mc "..."    
    call splash_message(_("In your bedroom")) from _call_splash_message_5   
    scene bg_mc_room_night with dissolve   
    mc "(I guess I should've seen that coming.)"
    if quest_v2:
        mc "(I've already tried the direct approach, and it didn’t work.)"    
    else:
        mc "(I've tried that approach before, and it didn’t work.)"    
    mc "(Perhaps I need to rethink my strategy.)" 
    mc "(*Yawning* But I'll leave that for tomorrow.)"
    scene mc_room_sleep_close with dissolve
    scene black with eyeclose   
    if quest_v2 and not _in_replay:
        call addLust(2,5)
    play ambience morning_sounds fadein 1.0
    scene mc_room_sleep_open with eyeopen    
    scene level0_0_11 with dissolve
    mc "(Something's missing...)"
    scene bg_hentai_magazine at gray_blur5 with dissolve
    mc "(My collection. Hmm...)"
    scene level0_0_11 with dissolve
    mc "(This could be the perfect excuse to move things forward.)"
    mc "(Although with my usual approach, I will probably fail.)"
    scene level0_0_12 with dissolve
    "''How to deal with your Tsundere''"(multiple=2)
    mc "(Maybe I should try following the advice in that magazine.)"
    scene bg_mc_room_day with dissolve
    if quest_v2: 
        if incest_story:
            "You grab the magazine and begin absorbing its contents, using it to plan your next move with your sister." 
        else:
            "You grab the magazine and begin absorbing its contents, using it to plan your next move with [neusname]." 
    stop ambience fadeout 1.0 
    $renpy.end_replay()   
    if quest_v2:
        $questMain_v2_3.completion = True
        $questMain_v2_select=questMain_v2_4
        $ is_stundere_magazine = True   
        $ inventory.add_item(item_tsundere_magazine)    
    else:
        $questMain_1.completion = True
        $questMain_select=questMain_2
    $days_to_final_obsession=0
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_2 
    $is_change_quest = True  
    jump next_day
 
label level0_1:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    stop music fadeout 1.0
    scene level0_1_0 with storyfx
    mc "Hey, have you seen my collection?"
    scene level0_1_1 with dissolve
    neus "Are you referring to those porn magazines?"
    neus "No, I haven't seen them."    
    if incest_story:
        mc "Well, it's just the two of us living here sis. So, who else could've taken them?"
    else:
        mc "Well, it's just the two of us living here. So, who else could've taken them?"
    scene level0_1_2 with dissolve
    neus "Isn't it better this way? This helps you get over your addiction. Besides, all those girls were ..."    
    mc "*Acting* Those physical copies are hard to come by, they need proper care."
    mc "*Acting* Without my valuable collection to relieve stress, I might resort to... illegal activities."    
    scene level0_1_3 with dissolve
    neus "Th-That's an exaggeration."
    mc "*Acting* The criminal must take responsibility for the harm they have caused me."
    scene level0_1_4 with dissolve
    neus "And what should that criminal do to be forgiven?"
    mc "A single kiss would be enough."
    scene level0_1_5 with dissolve
    if incest_story:
        neus "Eh! You're my brother, I cant do that..."
    else:
        neus "Eh!"
    mc "The more time passes, the more I may want."
    scene level0_1_6 with dissolve
    neus "{sc=4}Fine!{/sc}"
    scene level0_1_10 with dissolve
    "She kisses you on the right cheek."
    scene level0_1_7 with dissolve
    mc "That brought back memories from when we were kids, but I meant a kiss on the lips."
    scene level0_1_8 with dissolve
    neus "{sc=3}Eh! ...{/sc}"
    stop music
    scene level0_1_9 with dissolve
    play char1 short_kiss
    "She quickly gives you a kiss on the lips."
    menu: 
        "I want more":
            scene level0_1_11 with dissolve
            "She kicks you out of her room."
        "Leave":
            scene black with dissolve
            "You leave the room"
            pass 
    scene black with dissolve
    mc "(Well, that was progress, not as much as I would have liked, but it's better than nothing.)"
    if quest_v2:
        mc "(I should probably get her comfortable with kissing me, before pushing her any further.)"
    $renpy.end_replay()  
    if quest_v2:
        call addLust(2,10)
        $questMain_v2_5.completion = True
        $questMain_v2_select=questMain_v2_6
    else:
        $questMain_2.completion = True
        $questMain_select=questMain_3
    $days_to_final_obsession=0
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_3
    $is_change_quest = True
    $ select_room="mc"
    jump time_advances

label level0_2:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene level0_2_0 with storyfx
    if incest_story:
        mc "Hey, sis"
        scene level0_2_1 with dissolve
        neus "Hey, brother (Where is that key?)"
    else:
        mc "Hey, [neusname]"
        scene level0_2_1 with dissolve
        neus "Hey, [firstname] (Where is that key?)"
    scene level0_2_2 with dissolve
    mc "I need a little more help, since I don't have my collection to rely on anymore."
    play music DarkestSoul_Schmidt volume 0.5
    scene level0_2_3 with dissolve
    if incest_story:
        neus "Are you seriously going to keep this up? I'm your sister, I shouldn't be kissing you like that. You don't even know if it was me who took them!"
    else:
        neus "Are you seriously going to keep this up? You don't even know if it was me who took them!"
    scene level0_2_4 with dissolve
    neus "..."(multiple=2)
    mc "Then what is this?"(multiple=2)
    play music Lobby_Time fadeout 0.5 volume 0.1
    scene level0_2_5 with dissolve
    neus "A kiss is enough, right?"
    scene level0_2_6 with dissolve
    play char1 short_kiss
    neus "*kiss*"
    scene level0_2_7 with dissolve
    neus "Alright, now get out of my room."    
    mc "(If I stop here, she'll probably pretend like nothing happened afterwards.)"
    mc "Hey, can you help me with something else?"
    scene level0_2_8 with dissolve
    play sound clothes
    neus "Why are you undressing?"
    mc "Isn't it obvious?"
    scene level0_2_9 with dissolve
    if incest_story:
        neus "Hey! I only just gave you my first kiss recently."
        scene level0_2_10 with dissolve
        neus "And... Uhm... I'm your sister, I can't give you my first time."
    else:
        neus "Hey! You're going too fast. I only just gave you my first kiss recently."
        scene level0_2_10 with dissolve
        neus "It's too soon to give you my first time."
    mc "Don't worry, that's not happening today. I have another time and place in mind for that."
    scene level0_2_11 with dissolve
    neus "What the hell are you saying?"
    scene level0_2_12 with dissolve
    play sound zipper_unzip volume 0.5
    neus "(Why is it so big? I don't remember it being that size.)"
    scene level0_2_13 with dissolve
    neus "Damn it, I let my guard down."(multiple=2)
    mc "Come here."(multiple=2)   
    stop music fadeout 1.0
    call splash_message(_("10 minutes later")) from _call_splash_message_6
    play music PoolParty_Christensen volume 0.1 fadeout 1.0
    scene level0_2_14 with dissolve
    neus "How the hell did we end up in this situation?"
    scene level0_2_15 with dissolve
    neus "(Yeah, it's definitely bigger than the last time I saw it.)"
    neus "(I don't think this can fit inside me.)"
    neus "(It would surely split me in two.)"
    scene level0_2_16 with dissolve
    if incest_story:
        neus "(What is wrong with me? I shouldn’t be thinking about my brother like this.)"
    else:
        neus "(What am I thinking? I sound like a pervert.)"
    mc "What's wrong?"              
    label menu0_2:
        play char3 handjob1 fadeout 1.0 if_changed                
        scene level0_2_17
        menu:        
            neus "Nothing! Can you finish already? I don't want to keep {size=-15}touching this thing..."
            "I want a kiss":
                stop char3
                play char1 short_kiss
                scene level0_2_18 with dissolve
                ""
                jump menu0_2
            "Continue": 
                play char3 handjob2  fadeout 1.0                             
                scene level0_2_19
                ""
                menu:                   
                    "Cum":
                        stop char3
                        play charM cum1
                        scene level0_2_20 with dissolve
                        neus "Ah!"
                        scene level0_2_20_1 with dissolve
                        stop music fadeout 3.0
                        neus "Why didn't you warn me you were going to finish? Now I'm covered in your cum."
                        mc "I will be counting on you to help me with this, from now on."
                        scene level0_2_21 with dissolve 
                        if incest_story:
                            neus "Mmm... (What else will my perverted brother make me do?)"
                        else:
                            neus "Mmm... (What else will this pervert make me do?)"
                        scene black with dissolve
                        neus "Now get out of my room, I want to clean myself up."
                        if quest_v2:
                            mc "That was progress, but she’ll probably need to get used to doing similar favours for me, before she’ll do anything more."
                        $renpy.end_replay()               
                        if quest_v2:
                            call addLust(4,20)
                            $ questMain_v2_7.completion = True
                            $ questMain_v2_select = questMain_v2_8
                            $ questSide_v2_4.start = True
                        else:            
                            $questMain_3.completion = True
                            $ questSide_3.start = True
                            $questMain_select=questMain_4 
                        $is_change_quest = True 
                        if not quest_v2:
                            $neus_lust=5  
                            call splash_message(_("Lust {color=cc0066}+5")) from _call_splash_message_45 
                        call splash_message(_("Relationship level {color=cc0066}+1"),2.0) from _call_splash_message_12   
                        call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_29        
                        $days_to_final_obsession=0                   
                        $ select_room="mc"
                        call level_up(1) from _call_level_up
                        jump time_advances
        
    