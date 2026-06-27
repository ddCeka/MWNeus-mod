image level1_0_0:
    "story/level1/level1_0_0_0.webp" with dissolve           
    1.0
    "story/level1/level1_0_0_1.webp" with dissolve 
    0.5
    "story/level1/level1_0_0_2.webp" with dissolve
    1.0
    "story/level1/level1_0_0_3.webp" with dissolve 
image level1_2_0:
    "story/level1/level1_2_0_0.webp"  with dissolve
    0.5
    "story/level1/level1_2_0_1.webp"  with dissolve
image level1_3_19:
    "story/level1/level1_3_19_1.webp" with dissolve           
    Brightness0_2_a       
    Brightness0_a 
    Brightness0_2_a       
    Brightness0_a   
image level1_3_23:
    "story/level1/level1_3_23_0.webp" with dissolve           
    0.1    
    "story/level1/level1_3_23_1.webp" with dissolve
    0.1 
    "story/level1/level1_3_23_2.webp" with dissolve
default level1_3_active = False
    
label level1_0:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene level1_0_0 with storyfx
    pause 1.9
    if incest_story:
        neus "Hey, brother"
    else:
        neus "Hey, [firstname]"
    scene level1_0_1 with dissolve
    neus "I have a reservation at a restaurant today."
    mc "Nice, let's go."
    scene level1_0_2 with dissolve
    neus "And my friends are busy, so if you want, you can..."
    scene level1_0_3 with dissolve
    ""
    scene black with dissolve
    stop music fadeout 0.5
    scene level1_0_4 with storyfx
    mc "Foods rich in phytoestrogens."
    play ambience people volume 0.2
    scene level1_0_5 with dissolve
    neus "Could I have number three from the menu, please?"
    scene level1_0_6 with dissolve
    mc "I doubt eating food like this will make much of a difference.\nThe amount of phytoestrogens in them is very small."
    mc "If anything, surgery would be much more effective."
    scene level1_0_7 with dissolve
    neus "{sc=3}Cough, cough...{/sc}"
    mc "Besides, I actually like small breasts. You don't have to force them to grow."
    scene level1_0_8 with dissolve        
    neus "That's not true."  
    neus "Also, I wanted to ask why you've been bothering me lately, by pushing us to do things."
    if incest_story:
        neus "*whispering* You're my big brother... don't you think that's wrong"
    menu:
        neus "What do you want from me?"
        "A child":
            scene level1_0_9 with dissolve
            neus "Huh?! what the hell are you saying?"
            if incest_story:
                neus "*whispering* You can't have a child with me, I'm your sister."
            scene level1_0_10 with dissolve
            neus "Why don't you consider surrogacy or adoption?"
            menu:
                "I want one with you":
                    scene level1_0_11 with dissolve
                    neus "Mmm, {sc=3}more{/sc} food, please"                
        "Your love":
            scene level1_0_12 with dissolve
            neus "....{w=1.0}{nw}"
            scene level1_0_13 with dissolve 
            neus "{sc=3}More{/sc} food, please"
    stop ambience fadeout 2.0
    scene black with dissolve
    if quest_v2 and not _in_replay:
        call addLust(1,27)
    scene level1_0_14 with storyfx
    mc "Thank you for the invitation."
    scene level1_0_15 with dissolve
    neus "You're welcome. (I hope they grow.)"
    scene black with dissolve
    "You go to your room"
    $renpy.end_replay()
    jump level1_1   

label level1_1: 
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene mc_room_sleep_close with dissolve
    scene black with eyeclose
    play sound door_knock
    ""    
    scene mc_room_sleep_close with eyeopen     
    scene level1_1_0 with storyfx   
    if incest_story:
        neus "Hey brother, have you seen the key to the attic?"   
    else:
        neus "Hey, have you seen the key to the attic?"    
    mc "No"
    scene level1_1_1 with dissolve
    neus "Hmm, okay. (Maybe it's in the living room.)"
    mc "Since you're here, you can help me with something."
    scene level1_1_2 with dissolve
    "{w=1.5}{nw}"    
    call splash_message(_("Minutes later")) from _call_splash_message_13
    play music PoolParty_Christensen volume 0.1
    scene level1_1_3 with storyfx
    neus "Seriously, again?"
    scene level1_1_4 with dissolve
    neus "Can you at least cum quickly, I've got stuff to do?"
    mc "Well, if you're in a hurry, you should put in a little more effort."
    scene level1_1_5 with dissolve
    neus "Hmm?"
    mc "Maybe use those lips of yours?"
    scene level1_1_6 with dissolve
    neus "No way-"
    scene level1_1_7 with dissolve
    neus "(Although if I want to go look for the key, I should probably hurry this along...)"
    scene level1_1_8 with dissolve
    if incest_story:
        neus "(But having my lips touching my brothers thing is...)"
    else:
        neus "(But having my lips touching this thing is a bit...)"
    scene level1_1_9 with dissolve
    if sleep_blowjob:
        neus "(It has a strange yet familiar taste, very salty.)"
    else:
        neus "(It has a strange taste, very salty.)"
    if incest_story:
        neus "(I can't believe that I'm about to give my brother a blowjob)."
        mc "You seem very focused, little sister."
    else:
        neus "(I can't believe that I'm about to give a blowjob)."
        mc "You seem very focused."
    scene level1_1_10 with dissolve
    neus "Uhhh, shut up."
    scene level1_1_10_1 with dissolve
    neus "And cum quickly."
    scene level1_1_11 with dissolve
    play char3 suck1 fadeout 1.0
    neus "(I'm only doing this because I want to leave quickly.)"
    if incest_story:
        neus "(It's not like I actually want to give my brother a blowjob.)"
    else:
        neus "(It's not like I actually want to give him a blowjob.)"
    neus "(It has a weird texture, I didn't know it would feel like this.)"
    scene level1_1_12 with dissolve
    play char3 suck2 fadeout 1.0
    neus "(Please, cum quickly)."
    if incest_story:
        mc "That feels good sis, you're doing great."
    else:
        mc "That feels good, you're doing great."
    neus "(Obviously, my lips are touching your cock)"
    scene level1_1_13 with fadesex
    neus "(It's a good thing that I watched those videos. For educational purposes, obviously)."
    neus "(Although, someone inexperienced like me wouldn't be able to give a blowjob like they do in some of those videos.)"
    scene level1_1_12 with fadesex
    neus "(Even a professional would struggle to handle such a big tool)."
    if incest_story:
        neus "(I can't believe that just a few days ago I gave my brother my first kiss and now I'm sucking his cock)."   
    else:
        neus "(I can't believe that just a few days ago I gave him my first kiss and now I'm sucking his cock)."                      
    menu:
        neus "Are you going to cum soon? I'm getting tired."
        "Cum":                    
            pass      
    stop char3  
    play charM cum1
    scene level1_1_14 with flash2
    neus "{sc=3}{=lust_style}Ahh{/sc}"
    scene level1_1_15 with dissolve
    stop music fadeout 3.0
    neus "Seriously?! You covered me in your cum again."
    mc "I'm sorry, next time-{w=1.5}{nw}"
    scene level1_1_16 with storyfx
    neus "I’m leaving, I have things to do."
    scene level1_1_17 with dissolve
    play char1 lick01
    neus "(It tastes strange.)"
    scene black with dissolve
    if not quest_v2:
        mc "Hmm, I think it's time to take the next step."   
    $renpy.end_replay()    
    if quest_v2:
        call addLust(3,30)
        $ questMain_v2_9.completion = True
        $ questMain_v2_select = questMain_v2_10
        $questSide_v2_5.start = True
    else:
        $neus_lust=15 
        call splash_message(_("Lust {color=cc0066}+10")) from _call_splash_message_46
        $questMain_4.completion = True
        $questMain_select=questMain_5
        $questSide_4.start = True
    $days_to_final_obsession=0
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_4
    $is_change_quest = True
    $ select_room="mc"
    jump time_advances     

label level1_2:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene level1_2_0 with storyfx
    neus "What a useless book"
    scene level1_2_1 with dissolve
    if incest_story:
        mc "Hey sis, do you want to go on another date?"
    else:
        mc "Hey, do you want to go on another date?"
    scene level1_2_2 with dissolve
    neus "No.  (That would just make things worse, especially since that book isn’t helping me anymore.)"
    scene level1_2_3 with dissolve
    mc "I already have a reservation. It would be a shame to not go."
    scene level1_2_4 with dissolve
    neus "Hmm"
    play music night_ambience fadeout 0.5 volume 0.1
    scene level1_2_5 with storyfx
    neus "That food was really good." 
    stop music fadeout 0.5    
    scene level1_2_6 with circlefx
    neus "Why are we here?"
    play sound clothes
    scene level1_2_7 with dissolve
    neus "Hey, why are you taking off your clothes?"
    play music PoolParty_Christensen volume 0.1 fadeout 1.0
    scene level1_2_8 with dissolve
    mc "It's time to take our relationship to the next level."
    scene level1_2_9 with dissolve
    if incest_story:
        neus "W-Wait, wait! We can't do that, It's wrong..."
    else:
        neus "W-Wait, wait! You’re going too fast—I’m not ready yet!"
    scene level1_2_10 with dissolve
    mc "Don't worry, I'll take care of everything."
    scene level1_2_11 with dissolve
    if incest_story:
        mc "Thanks to inheriting our parents' business, I have enough money and resources to have more than 20 children."
        mc "Not to mention, I'm sure our auntie would love to take care of the kids from time to time."
        scene level1_2_12 with dissolve
        neus "{sc=3}HA!{/sc} I don't think I can have that many and I very much doubt she would be okay with... this."
        scene level1_2_13 with dissolve
        neus "Brother, let go of me!"
    else:
        mc "I have enough money and resources to have about 20 children."
        scene level1_2_12 with dissolve
        neus "{sc=3}HA!{/sc} I don't think I can have that many."
        scene level1_2_13 with dissolve
        neus "Hey, let go of me!"
    scene level1_2_14 with dissolve
    ""
    scene level1_2_15 with circlefx
    if incest_story:
        neus "Why are you such a pervert brother?"
    else:
        neus "Why are you such a pervert?"
    scene level1_2_16 with dissolve
    neus "(Maybe if he cums, he'll calm down)"
    play char3 suck2 fadeout 1.0
    scene level1_2_17 with dissolve
    menu:
        "Cum":
            pass
    stop char3 
    play charM cum1     
    scene level1_2_18 with flash2
    stop music fadeout 2.0
    neus "There, now will you calm down already?"
    play music PoolParty_Christensen volume 0.1 fadeout 1.0
    scene level1_2_19 with circlefx
    neus "W-Wait... Wait! I-I'm not ready to have children!"
    scene level1_2_20 with dissolve
    mc "Calm down, I've got this."
    scene level1_2_21 with dissolve
    neus "{sc=4}A-alright{/sc}, but... please, not now... C-Can we leave it for another {sc=4}time?{/sc}"
    scene level1_2_22 with dissolve
    stop music fadeout 2.5
    mc "Okay."
    scene level1_2_23 with dissolve
    neus "Eh, you stopped that easily?"
    mc "Don't tell me you wanted me to continue?"
    scene level1_2_24 with dissolve
    mc "In that case-"
    scene level1_2_25 with dissolve
    neus "Don't even think about it."
    mc "(I've been waiting a long time for this, so waiting a little longer until she feels ready isn't a bad thing.)"
    scene black with dissolve  
    mc "Do you want to stop by the candy store?"
    neus "That's the least I expect as compensation for what you put me through."
    if incest_story:
        "After enjoying some candy, you return home with your sister."
    else:
        "After enjoying some candy, you return home with [neusname]."
    scene mc_room_sleep_close with dissolve
    scene black with eyeclose  
    if quest_v2 and not _in_replay:
        call addLust(3,41)
    elif not quest_v2 and not _in_replay:
        $neus_lust=25 
        call splash_message(_("Lust {color=cc0066}+10")) from _call_splash_message_47
    scene bg_hypnosis with dissolve  
    play sound magical1 volume 0.1
    play char1 whisper volume 0.3
    pause 0.5
    centered "{size=+40}Using a condom doesn't make a baby. Using a condom doesn't make a baby. Using a condom doesn't make a baby. Using a condom doesn't make a baby. Using a condom doesn't make a baby ...{w=8.0}{nw}"
    scene black with dissolve
    stop char1 fadeout 1.0
    pause 1.0 
    scene mc_room_sleep_open with eyeopen 
    $renpy.end_replay()
    if quest_v2:
        $ questMain_v2_11.completion = True
        $ questMain_v2_select = questMain_v2_12
    else:
        $questMain_5.completion = True
        $questMain_select=questMain_6
    $days_to_final_obsession=0
    if incest_story:
        call page_4_2_incest from _call_page_4_2_incest 
    else:
        call page_4_2 from _call_page_4_2   
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_5     
    $is_change_quest = True
    $ select_room="mc"    
    jump next_day

label level1_3:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene level1_3_0 with storyfx
    if incest_story:
        mc "Hey sis"
    else:
        mc "Hey"
    scene level1_3_1 with dissolve
    neus "Hum?"
    scene level1_3_2 with dissolve 
    mc "Shall we continue where we left off?"
    scene level1_3_3_0 with dissolve
    if incest_story:
        neus "Actually... I’ve been thinking. Maybe we should slow down. I mean, we’re siblings... shouldn’t we take some time to think this through? Maybe go on a few dates or something first."
    else:
        neus "Actually, I wanted to talk about that. I think we should take things slower, maybe go on a few dates and see where it leads."
    mc "Okay"    
    scene level1_3_3_1 with dissolve
    neus "Great? (I didn’t think he’d agree so easily...)"
    play music Cipher volume 0.5 fadeout 1.0
    call splash_message(_("One week later")) from _call_splash_message_30     
    scene level1_3_dates_0 with dissolve 
    ""    
    scene level1_3_dates_6  with dissolve
    ""
    scene level1_3_dates_3 with dissolve
    ""
    scene level1_3_dates_3_kiss  with dissolve
    ""
    if quest_v2 and not _in_replay:
        call addLust(1,42)
    call splash_message(_("Two weeks later")) from _call_splash_message_31    
    scene level1_3_dates_9 with dissolve 
    ""
    show level1_3_dates_8  at rotate_15 with dissolve
    ""
    show level1_3_dates_7  at rotate_15_degrees with dissolve
    ""
    show level1_3_dates_9_kiss  at rotate_15 with dissolve
    ""
    if quest_v2 and not _in_replay:
        call addLust(1,43)
    hide level1_3_dates_7
    hide level1_3_dates_8
    call splash_message(_("One month later.")) from _call_splash_message_32    
    scene level1_3_dates_4  with dissolve
    ""      
    scene level1_3_dates_5  with dissolve 
    "{w=0.5}{nw}"    
    scene level1_3_dates_2  with dissolve
    "" 
    scene level1_3_dates_1 with dissolve
    ""     
    scene level1_3_dates_1_kiss with dissolve
    ""   
    if quest_v2 and not _in_replay:
        call addLust(2,45)
    call splash_message(_("Two months later.")) from _call_splash_message_33          
    scene level1_3_dates_0 with dissolve
    ""  
    scene level1_3_dates_3 with dissolve
    ""
    play music Lobby_Time volume 0.3 fadeout 1.0
    scene level1_3_4 with storyfx
    neus "Why have you brought me here again?"    
    play sound clothes
    scene level1_3_5 with dissolve
    mc "I think we've had enough dates now."
    scene level1_3_6 with dissolve
    neus "Well, I think we've had too few dates."
    scene level1_3_7 with dissolve
    mc  "We've had twenty dates in the last two months."
    scene level1_3_8 with dissolve
    neus "..."
    play music PoolParty_Christensen volume 0.08 fadeout 1.0
    scene level1_3_9 with circlefx
    neus "Hey!"   
    scene level1_3_10 with dissolve
    mc "Don't worry, I'll be gentle."
    scene level1_3_11 with dissolve
    neus "Haaa Haaaa Haaaa"
    mc  "You're very wet"
    mc "It feels good when I use my fingers, doesn't it?"
    neus "{bt=3}No{/bt}{w=1.5}{nw}"
    neus "{sc=2}{=lust_style}I'm cumming!{/sc}{w=1.0}{nw}"    
    scene level1_3_12 with dissolve
    play char1 climax1
    neus "{sc=3}{=lust_style}Ohhh{/sc}"
    scene level1_3_13 with circlefx    
    if incest_story:
        neus "(I shouldn't let this go any further.)"
        neus "C-Can we stop? We shouldn't be doing this, we're siblings."
        mc "If that's what you want, just give me a kick."
        mc "I know very well that it's hard for you to express what you really want though, little sister."
    else:
        neus "Can we stop?"
        mc "If that's what you want, just give me a kick."
        mc "I know very well that it's hard for you to express what you really want though."
    scene level1_3_13_1 with dissolve
    mc "If you want it to really stop, a kick is enough."
    mc "I want actions, not words."    
    scene level1_3_13_2 with dissolve    
    stop music fadeout 2.0
    neus "(Damn it, my body isn't obeying me.)"
    neus "(It's like a part of me really wants this.)"
    neus "(And it's as if that part of me is the one controlling my body...)"
    if incest_story:
        neus "(I can't believe I'm about to let my brother fuck me...)"
    scene level1_3_14 with snow1
    play music CocktailHour_Hauser volume 0.05 fadeout 1.0
    if incest_story:
        neus "Please do it slowly big brother." 
    else:
        neus "Please do it slowly." 
    scene level1_3_14_1 with dissolve
    neus "It's my first time..."   
    mc "Don't worry, leave it to me."
    scene level1_3_15  
    play char1 penetration4    
    neus "{sc=3}It hurts{/sc}"
    stop char1
    scene level1_3_16 with dissolve
    neus "Hmm, why aren't you using a condom?"    
    mc "I'm going to start moving now."
    scene level1_3_16_1 with dissolve
    neus "Wait a moment, I'm not ready yet.{w=1.0}{nw}"
    scene level1_3_17 with dissolve
    play char3 sex1    
    neus "Haa Haa Haa"  
    mc "How does it feel?"
    if incest_story:
        neus "It feels weird... (having my brother inside me.)"
    else:
        neus "It feels weird."
    mc "You'll get used to it. From now on, we'll do it every day."
    neus "Every day?"
    mc "I'm going to increase the speed."
    neus "?!{w=1.5}{nw}"
    scene level1_3_18 with dissolve
    neus "Haa Haa Haa"
    mc "This feels much better."
    mc "You're very tight."
    neus "Haa Haa Haa"    
    mc "I'm going to cum."
    if incest_story:
        neus "Brother, please cum outside... {w=1.5}{nw}"
    else:
        neus "Please, cum outside... {w=1.5}{nw}"
    stop char3 
    play charM cum1
    scene level1_3_19 with dissolve
    play char1 climax1
    "{sc=3}{=lust_style}Ahhhh{/sc}"
    scene level1_3_20 with dissolve
    stop music fadeout 2.0
    if incest_story:
        neus "I asked you not to cum inside me." 
        neus  "I'm your sister, what happens if I get pregnant?" 
    else:
        neus "Why did you cum inside?" 
        neus  "What happens if I get pregnant?"   
    scene level1_3_21 with dissolve
    mc "That would be great."
    neus "..."
    scene level1_3_22 with dissolve
    if incest_story:
        neus "I'm going to take a shower (it hurts)."
        neus "(I can't let my brother get me pregnant, I need to buy some contraceptive pills.)"
    else:
        neus "I'm going to take a shower (it hurts, I need to buy some contraceptive pills)."
    scene level1_3_23 with dissolve
    play charM slap1 volume 2.0
    play char1 groan_normal1 
    neus "Hmm!?"    
    menu:       
        "More":
            $level1_3_active = True
            play sound dark1 volume 0.3
            scene level1_3_24 at red_zoom1 
            mc "We need to keep practicing so you can get used to it."  
            stop sound fadeout 2.0
            call splash_message(_("2 hours later")) from _call_splash_message_16                                 
            scene level1_3_25 at zoom_moven1
            play char3 breathing1
            ""                    
            scene black 
            stop char3 fadeout 1.0
            "You let her rest and then return home together."
        "Leave":
            scene black 
            "You take a shower and go home with her."
    $renpy.end_replay()
    if quest_v2:
        call addLust(5,50)
        $ questMain_v2_12.completion = True
        $ questMain_v2_select = questMain_v2_13
    else:
        $neus_lust=45 
        call splash_message(_("Lust {color=cc0066}+20")) from _call_splash_message_48  
        $questMain_6.completion = True
        $questMain_select=questMain_7  
    if incest_story:
        call page_4_3_incest from _call_page_4_3_incest
    else:
        call page_4_3 from _call_page_4_3
    call splash_message(_("Relationship level {color=cc0066}+1"),2.0) from _call_splash_message_17  
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_31
    $days_to_final_obsession=0  
    if incest_story:
        $neus_title=_("Sister/Girlfriend?")
    else:
        $neus_title=_("Girlfriend?")
    $is_change_quest = True
    $ select_room="mc"
    call level_up(2) from _call_level_up_1
    $night_1=True
    jump expression "sleeping_event%s"%mc_event_lvl
