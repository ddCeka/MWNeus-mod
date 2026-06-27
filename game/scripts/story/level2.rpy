image level2_0_30:    
    "story/level2/level2_0_30_0.webp"  with dissolve
    0.5
    "story/level2/level2_0_30_1.webp"  with dissolve
image level2_1_0:
    "story/level2/level2_1_0_0.webp"  with dissolve
    0.5
    "story/level2/level2_1_0_1.webp"  with dissolve
    0.5
    "story/level2/level2_1_0_2.webp"  with dissolve
label level2_0:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene level2_0_0 with storyfx
    if incest_story:
        mc "Hey sis, How are you doing?"
    else:
        mc "Hey there, How are you doing?"
    scene level2_0_1 with dissolve
    neus "It still hurts, you were so rough."
    if level1_3_active:
        scene level2_0_2 with dissolve
        neus "Not to mention that you then made me do it for 2 hours"
    scene level2_0_3 with dissolve
    mc "I'm sorry, I'll be more careful today."
    scene level2_0_4 with dissolve
    neus "Today?"
    scene level2_0_5 with dissolve
    mc "Yeah, babies don't make themselves."
    scene level2_0_6 with dissolve
    mc "We need to do it every day."
    scene level2_0_7 with dissolve
    neus "I never agreed to have children."
    scene level2_0_8 with dissolve
    neus "Maybe we can talk about this in the future."    
    if incest_story:
        mc "I'm sorry little sister, I can't accept that. (I don't want to wait decades.)"
    else:
        mc "I'm sorry, I can't accept that. (I don't want to wait decades.)"
    scene level2_0_9 with dissolve
    mc "I want to have 11 children before your egg factory expires."
    scene level2_0_10 with dissolve
    if incest_story:
        neus "Mmmm... we're siblings, we shouldn’t even have one. Besides, I don’t think I can have that many."
    else:
        neus "Mmmm, I don't think I can have that many."
    scene level2_0_11 with dissolve
    mc "I believe in you..."
    scene level2_0_12 with dissolve
    neus "Hmm..."
    play music PoolParty_Christensen volume 0.1 fadeout 1.0
    scene level2_0_13 with storyfx
    if incest_story:
        neus "You're such a perverted brother, how do we always end up like this?"
        scene level2_0_14 with dissolve 
        mc "You are the cause sis, being so sexy. Besides, you're my girlfriend."
    else:
        neus "how do we always end up like this, you damn perverted monkey?"
        scene level2_0_14 with dissolve 
        mc "You are the cause, being so sexy. Besides, you're my girlfriend."
    scene level2_0_15 with dissolve
    neus "Girlfriend? I never agreed to that."
    scene level2_0_16 with dissolve
    play char1 penetration2
    neus "{sc=3}{=lust_style}Ahh{/sc}"
    scene level2_0_17 with dissolve
    mc "Oops, I forgot to ask. Will you be my girlfriend?"
    scene level2_0_18 with dissolve
    play char3 sex2
    if incest_story:
        neus "No. Not in a million {sc=2}{=lust_style}Haa{/sc} years would I be the {sc=2}{=lust_style}Haa{/sc} girlfriend of my perverted brother. I hate you {sc=2}{=lust_style}Haa{/sc} I hate you {sc=2}{=lust_style}Haa{/sc} I hate you {sc=2}{=lust_style}Haa{/sc} I hate you..."
    else:
        neus "No. Not in a million {sc=2}{=lust_style}Haa{/sc} years would I be the {sc=2}{=lust_style}Haa{/sc} girlfriend of a perverted monkey. I hate you {sc=2}{=lust_style}Haa{/sc} I hate you {sc=2}{=lust_style}Haa{/sc} I hate you {sc=2}{=lust_style}Haa{/sc} I hate you..."
    stop char3 fadeout 2.0
    #play music PoolParty_Christensen volume 0.1 fadeout 1.0
    scene level2_0_19 with fadesex
    mc "Maybe, I need to fuck you until you accept to be my girlfriend."
    play char3 sex2
    scene level2_0_20 with dissolve
    neus "N... Never {sc=2}{=lust_style}Ahh{/sc}"
    stop char3 fadeout 1.0
    #play music PoolParty_Christensen volume 0.1 fadeout 1.0
    scene level2_0_21 with dissolve
    mc "Come on, I know it's hard for you to admit your feelings, but if you tell me the truth, I'll give you much more love."
    scene level2_0_22 with dissolve 
    neus "..."
    scene level2_0_23 with dissolve 
    mc "You liked what I said, didn't you?"
    scene level2_0_24 with dissolve 
    neus "No!"
    scene level2_0_25 with dissolve 
    mc "Well, your other mouth doesn't seem to agree."
    scene level2_0_26 with dissolve 
    neus "..."
    stop music fadeout 1.0
    call splash_message(_("Several hours later")) from _call_splash_message_18
    scene level2_0_27 with dissolve
    play char3 breathing1
    if incest_story:
        neus "Brother, please, stop, I can't take it anymore."
    else:
        neus "[firstname], please, stop, I can't take it anymore."
    scene level2_0_28 with dissolve
    neus "(If I don't agree to be his girlfriend, I will most likely die.)"
    scene level2_0_29 with dissolve
    neus "I-I accept."
    menu:
        "Tease Her":
            scene level2_0_30 with dissolve
            play charM slap1 volume 2.0
            play char1 penetration4
            mc "What do you mean by ''accept''?" 
            scene level2_0_31 with dissolve
            neus "I accept to be your girlfriend (I hate you)."
        "Continue":
            pass 
    scene level2_0_32 with dissolve    
    mc "Great!"
    stop sound fadeout 0.5
    scene level2_0_33 with dissolve
    neus "I'm going to get some water from the kitchen. I need to hydrate."
    scene level2_0_34 with dissolve
    play charM slap1 volume 2.0
    play char1 penetration1 
    neus "Hmm!?"
    menu:
        "More":            
            mc "We’re not done yet—We have to keep going if we want to make a baby."             
            scene level2_0_35 
            if level1_3_active:                
                neus "Not again"
            else:
                ""
            stop char3 fadeout 1.0
            scene black 
            if incest_story:
                "One hour later, you let your sister get some water, and you head back to your room."
            else:
                "One hour later, you let [neusname] get some water, and you head back to your room."
        "Leave":
            stop char3 fadeout 1.0
            scene black 
            if incest_story:
                "You let your sister get some water, and you head back to your room."
            else:
                "You let her get some water, and you head back to your room."
    $renpy.end_replay()
    if incest_story:
        call page_4_4_incest from _call_page_4_4_incest
    else:
        call page_4_4 from _call_page_4_4 
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_6 
    if quest_v2:
        call addLust(4,54)
        $ questMain_v2_13.completion = True
        $ questMain_v2_select = questMain_v2_14
    else:    
        $neus_lust=50 
        call splash_message(_("Lust {color=cc0066}+5")) from _call_splash_message_49  
        $questMain_7.completion = True
        $questMain_select=questMain_8 
    $days_to_final_obsession=0   
    if incest_story:
        $neus_title=_("Sister/Girlfriend")
    else:
        $neus_title=_("Girlfriend")
    $is_change_quest = True
    $ select_room="mc"   
    $night_1=True
    jump expression "sleeping_event%s"%mc_event_lvl

label level2_1:    
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    scene level2_1_0 with storyfx
    if incest_story:
        neus "Hey brother, do you have some free time?"  
    else:
        neus "Hey, do you have some free time?"    
    neus "We need to talk."
    mc "Ohh, do you want us to start making our first child?"
    scene level2_1_1 with dissolve
    neus  "No!"
    scene level2_1_2 with dissolve
    neus "I want to talk about something that has been bothering me lately."
    neus "But I'd prefer to discuss it somewhere else."
    scene level2_1_3 with dissolve   
    neus "I was thinking the bistro we went to last time would be a good choice, plus they recently launched a new dessert."    
    mc "(Ah, so she just wants to eat something sweet.)"
    stop music fadeout 0.5
    play ambience people volume 0.2 fadein 0.2
    scene level2_1_4 with storyfx  
    neus "I'd like number three from the new menu, please."
    scene level2_1_5 with dissolve
    mc "So, what did you want to talk about?"
    scene level2_1_6 with dissolve
    if incest_story:
        neus "Well, as your little sister, I've known you my entire life, and recently, you've started acting very assertive... or should I say, very perverted."
    else:
        neus "Well, I've known you for 10 years, and recently you've been very assertive... or should I say, very perverted."
    scene level2_1_7 with dissolve 
    neus "What changed?"
    scene level2_1_8 with dissolve 
    mc "Well, I could say the same about you. In the past, you were always clinging to me and expressing your feelings of love intensely—sometimes it even came across as a little scary."
    scene level2_1_9 with dissolve
    neus "I don't remember any of that." 
    scene level2_1_10 with dissolve
    neus "And answer my question."    
    if incest_story:
        mc "Mmmm, after mom's call asking for a grandchild, I found the lost motivation."
        scene level2_1_11 with dissolve
        neus "Mom called you? (Mmm...)"    
        mc "Why do you care so much about this?"
    else:
        mc "Mmmm, after my mother's call asking for a grandchild, I found the lost motivation."
        scene level2_1_11 with dissolve
        neus "Your mother? (Mmm...)"
        mc "Why do you care so much about this? Does it bother you that we're a couple?"
    scene level2_1_12 with dissolve
    neus "(...){w=3.5}{nw}"
    if incest_story:
        mc "[neusname]? Is it really bothering you that we're siblings?"
    else:
        mc "Earth to [neusname]."
    scene level2_1_13 with dissolve
    neus "Well, it's not that... {w=1.5}{nw}"
    scene level2_1_14 with dissolve
    neus "I'd like item two, please."
    stop ambience fadeout 2.5
    scene black 
    "She avoids your question."
    "We enjoyed some more desserts before returning home."
    scene level2_1_15 with dissolve
    neus "Those desserts were delicious{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5} {size=-20}Thank you."   
    scene level2_1_16 with dissolve    
    neus "I'm sorry, I need to be alone.{w=2.5}{nw}"    
    play sound door_close
    scene level2_1_17 with dissolve    
    mc "..."
    $renpy.end_replay()   
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_7     
    if quest_v2:
        $ questMain_v2_15.completion = True
        $ questMain_v2_select = questMain_v2_16
    else:           
        $questMain_8.completion = True
        $questMain_select=questMain_9  
    $neus_is_evading=True
    $days_to_final_obsession=0   
    $is_change_quest = True
    call level_up(2) from _call_level_up_2
    $select_room="mc"    
    $night_1=True   
    jump expression "sleeping_event%s"%mc_event_lvl

label level2_2: 
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    stop music fadeout 0.5
    play ambience night_ambience volume 0.1     
    scene level2_2_0 with storyfx  
    mc"Hey."
    scene level2_2_1 with dissolve
    "{w=0.5}{nw}"
    scene level2_2_2 with dissolve
    play sound hit_table
    mc "Why are you avoiding me?" with hpunch
    scene level2_2_3 with dissolve
    neus "We should stop being a couple."
    scene level2_2_4 with dissolve
    mc "What? Why?"
    scene level2_2_5 with dissolve
    if incest_story:
        neus "Well... because your my brother (and I'm not sure your feelings for me are real...)"
    scene level2_2_6 with dissolve
    mc "I understand. I just need to give you even more love."
    scene level2_2_7 with dissolve
    if incest_story:
        neus "How the hell did you come to that conclusion? I'm your sister!"
    else:
        neus "How the hell did you come to that conclusion?"   
    mc "Don't worry, let me take care of this."
    scene level2_2_8 with dissolve
    neus "(Here we go again...)"
    scene level2_2_9 with dissolve
    play char1 penetration2
    neus "Haaa"
    play char3 sex2
    scene level2_2_10 with dissolve
    if incest_story:
        neus "You don't need to do this brother."
    else:
        neus "You don't need to do this."
    scene level2_2_11 with dissolve
    mc "Well, I believe this is the only way I can truly prove my love to you."
    mc "(Talking won't work, at least not until I've done this.)"
    stop char3
    play charM cum1 
    scene level2_2_12 with flash2   
    play char1 climax3 
    neus "Ahhh"
    scene level2_2_13 with dissolve
    neus "..."
    scene level2_2_14 with dissolve    
    neus "Hey, what are you doing?"
    stop ambience fadeout 1.0
    scene black with dissolve
    "You take her to your room."
    scene level2_2_15 with storyfx
    if incest_story:
        neus "Brother, please stop."
    else:
        neus "Please stop."
    mc "Do you really hate this that much?"
    scene level2_2_16 with dissolve
    neus "N..."    
    mc "?"
    scene level2_2_15 with dissolve
    neus "Y-Your feelings for me may not be real."
    mc "I am certain that my feelings for you are real."
    if incest_story:
        mc "I understand your insecurities due to us being siblings, but my feelings go beyond that; I love you as my partner.{w=4.5}{nw}"
        neus "Damn it, I'm not implying doubts about whether your feelings are more of sibling love than romantic (although I do have them), but I mean something else."
    else:
        mc "I understand your insecurities due to our friendship, but my feelings go beyond that; I love you as my partner.{w=4.5}{nw}"
        neus "Damn it, I'm not implying doubts about whether your feelings are more of friendship than love (although I have them), but I mean something else."
    scene level2_2_17 with dissolve   
    mc "Maybe I should approach this from a different angle."
    mc "They say even tough girls are weak here."
    scene level2_2_18 with dissolve
    neus "{sc=3}{=lust_style}Ahhh{/sc} H-Hey, don't put your finger there, I-I'm not a tough girl."
    scene level2_2_19 with dissolve
    mc "Relax, I've got this"
    scene level2_2_20 with dissolve
    neus "Mmmm"
    scene level2_2_21 with dissolve
    if incest_story:
        neus "N-No brother, please."
    else:
        neus "N-No, please."
    scene level2_2_22 with dissolve
    play char1 penetration1
    neus "(It's too big)"    
    mc "This hole is very tight."
    play char1 penetration3
    neus "Uhhh{w=0.5}{nw}"    
    play char3 sex2
    scene level2_2_23 with dissolve
    neus "(That feels strange.)"
    stop char3
    scene level2_2_24 with dissolve
    mc "I'm going to put it all the way in."
    neus "W-Wait, wait ...{w=1.0}{nw}"
    scene level2_2_25 with dissolve
    play char1 groan_hard1
    neus "ahhh"
    mc "I'm going to start moving now."
    if incest_story:
        neus "No, please brother, it's too big, it feels weird.{w=2.5}{nw}"
    else:
        neus "No, please, it's too big, it feels weird.{w=2.0}{nw}"
    play char3 sex2
    scene level2_2_26 with dissolve
    neus "You're going to break me." 
    neus "Please! No more, ahhh"   
    mc "No, not until you accept me."
    if incest_story:
        neus "... (He's my brother, it wouldn't be right to accept, I'm not worthy.)"
    else:
        neus "... (I have no right to accept, I'm not worthy.)"
    neus "I'm not going to accept."
    stop char3
    scene level2_2_27 with dissolve
    mc "In that case, a little more love won't hurt."
    neus "{bt=1}No more, please, I can't take it anymore.{/bt}"
    call splash_message(_("2 hours later...")) from _call_splash_message_34
    play char3 breathing1
    scene level2_2_28 with dissolve
    neus "Aah"    
    mc "If you accept to be my wife, I'll give you lots of love every day."    
    neus "... (It's not right, I shouldn't, if I accept, I'll be trash...)"  
    if incest_story:
        neus "(His feelings aren't real... They can't be, I'm his sister...)" 
    else:
        neus "(His feelings aren't real...)" 
    neus "({bt=3}but...{/bt})"
    neus "Do you promise to keep your {sc=2}{=lust_style}promise{/sc} no matter what happens?"
    if incest_story:
        mc "Of course little sister. I promise to give you lots of love every single day, no matter what."
    else:
        mc "Of course. I promise to give you lots of love every single day, no matter what."
    neus "..."
    stop char3 fadeout 1.0
    scene level2_2_29 with dissolve
    neus "{bt=3}I want more {=lust_style}love.{/bt}"   
    scene level2_2_30 with dissolve
    play char1 groan1
    if incest_story:
        neus "Ahhh, brother"
    else:
        neus "Ahhh"
    play char3 sex2
    scene level2_2_31 with dissolve    
    neus "Kiss me moreeeeeeee"    
    mc "Every time I kiss you, you tighten even more."    
    scene level2_2_32 with dissolve    
    neus "I want mooooore."    
    scene level2_2_31 with dissolve
    neus "Haaa Haaa Haaa"
    scene level2_2_31_1 with dissolve
    play char1 penetration4
    if incest_story:
        neus "Brother, I'm cumming!{w=2.0}{nw}"
    else:
        neus "I'm cumming!{w=2.0}{nw}"
    stop char3
    play charM cum1 
    scene level2_2_33 with flash2
    play char1 groan1
    neus "Haaaa"
    scene level2_2_33_1 with dissolve
    if incest_story:
        neus "{bt=4}That felt so good, big brother.{/bt}"
    else:
        neus "{bt=4}That felt so good.{/bt}"
    call splash_message(_("The next day")) from _call_splash_message_35
    play ambience morning_sounds fadein 1.0
    scene level2_2_34 with dissolve
    mc "Good morning, sleepyhead."
    scene level2_2_35 with dissolve
    neus "Good morning."
    mc "You were quite intense last night."
    scene level2_2_36 with dissolve
    neus "I'm sorry, I got carried away a bit."
    scene level2_2_37 with dissolve
    if incest_story:
        neus "Besides, it's your fault for saying those words to me... brother"
    else:
        neus "Besides, it's your fault for saying those words to me."
    neus "I hope you keep your promise, or else..."
    scene level2_2_38 with dissolve
    neus "You'll receive a stab."
    mc "..."
    scene level2_2_39 with dissolve
    neus "*Giggles* Hehehe, just kidding."
    scene level2_2_40 with dissolve
    neus "I think I've picked up some habits from those perverted magazines you read."
    scene level2_2_41 with dissolve
    mc "You mean my valuable collection that is very hard to obtain physically,"
    mc "and that you ruthlessly destroyed?"
    scene level2_2_42 with dissolve
    neus "Don't make it sound like a high-grade crime. Besides, I've already paid for my crime."
    mc "Maybe!"
    scene level2_2_43 with dissolve
    neus "By the way, you avoided my question last night."
    scene level2_2_44 with dissolve
    neus "In the past, you used to keep your distance from me."
    if incest_story:
        neus "Not to mention, you said mom called you asking for a grandchild. But our parents are ...{w=4.5}{nw}"
    else:
        neus "Not to mention that you said your mom wants a grandchild. I thought your parents were ...{w=3.5}{nw}"
    scene level2_2_45 with dissolve 
    mc "''I kept my distance from you'' Are you sure about asserting that?" 
    scene level2_2_45_1 with dissolve   
    mc "Besides, I'm still the same, nothing has changed."
    mc "Although I may have approached you in a somewhat aggressive way, but the normal approach wasn't working."
    scene level2_2_46 with dissolve
    neus "*Ignoring accusations.* Hmm, it certainly wasn't the best way."
    neus "Although I don't think I'm in a position to criticize your methods."
    scene level2_2_47 with dissolve
    neus "And if you say you're still the same, I feel more at ease. Besides, I'm not bothered that you're a little aggressive."
    neus "It complements my personality a bit."
    scene level2_2_48 with dissolve 
    if incest_story: 
        $ menu_text = "Hey brother"  
    else:
        $ menu_text = "Hey"
    menu:
        neus "[menu_text]... do you want to shower together? I'm still sweaty from last night, what do you say?"
        "Yes":
            stop ambience fadeout 1.0
            play char3 sex2
            scene level2_2_49 with storyfx
            neus "Haaa haaaa haaaa"            
            neus "When I said we should take a shower, I didn't mean you should fuck me in the shower."            
            stop char3                      
            scene level2_2_50 with dissolve
            if incest_story:
                neus "Hey, maybe we could stop, it still hurts from what you did to me last night... please brother." 
            else:
                neus "Hey, maybe we could stop, it still hurts from what you did to me last night... please." 
            mc "No{w=.5}{nw}"           
            scene level2_2_51 with dissolve
            play char1 climax1
            neus "Haahh"
            neus "Too deep."
            neus "(It's touching my {sc=2}...{/sc})"            
            mc "I'm going to start moving now."
            neus "W-Wait ...{w=.5}{nw}"   
            play char3 sex3         
            scene level2_2_52 with dissolve   
            if incest_story:
                neus "Ahhh, brother"
            else:         
                neus "Ahhh"
            neus "It's too big."
            neus "Haaa haaaa haaaa"
            scene level2_2_52_1 with dissolve
            stop char3
            play char1 penetration4
            neus "I'm cumming.{w=2.0}{nw}"
            scene level2_2_53 with flash2
            play charM cum1 
            neus "ohhhh"
            play char3 suck2 fadeout 1.0
            scene level2_2_54 with dissolve
            neus "Mmmm"
            mc "You've improved quite a bit in your blowjobs."
            stop char3
            scene level2_2_55 with dissolve
            "You can feel her throat."
            neus "Aghh"            
            scene level2_2_56 with dissolve
            neus "Haaa"           
            mc "That felt really good, can you-"
            scene level2_2_57 with dissolve
            neus "(I almost choked)"
            neus "({bt=1}but ...{/bt})"
            play char3 suck2 fadeout 1.0
            scene level2_2_58 with dissolve
            neus "*Glop Glop*"
            stop char3
            play charM cum1
            scene level2_2_59 with flash2
            neus "Hmmm"
            scene level2_2_60 with dissolve
            play char1 gulp1
            neus "..."
            play char1 ahegao3
            scene level2_2_61 with dissolve
            neus "It tastes bitter."
            if incest_story:
                neus "Mmmm... (My stomach is full of my brother's {bt=1}{=lust_style}cum.{/bt})"
            else:
                neus "Mmmm... (My stomach is full of his {bt=1}{=lust_style}fluids.{/bt})"
            scene level2_2_62 with dissolve
            neus "I think we should start taking more showers together."            
            scene black
            if incest_story:
                "You finish taking a shower with your sister."
            else:
                "You finish taking a shower with [neusname]."
        "No":
            stop ambience
            scene black
            "She leaves your room."             
    $renpy.end_replay()      
    $neus_love_hide=neus_love_real      
    if incest_story:
        call page_4_5_incest from _call_page_4_5_1_incest
    else: 
        call page_4_5 from _call_page_4_5_1
    $days_to_final_obsession=0 
    $neus_is_evading=False 
    call level_up(3) from _call_level_up_3
    $is_change_quest = True
    $ select_room="mc"
    if quest_v2:
        call addLust(5,69)
        $ questMain_v2_16.completion = True
        $ questMain_v2_select = empty_quest
    else:
        $questMain_9.completion = True
        $questMain_select=empty_quest 
        $neus_lust=70 
        call splash_message(_("Lust {color=cc0066}+20")) from _call_splash_message_50   
    call splash_message(_("Relationship level {color=cc0066}+1")) from _call_splash_message_36   
    call splash_message(_("{color=cc0066}PERSONALITY LOVE")) from _call_splash_message_38 
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_8
    python:
        achievement.grant("Girlfriend")
        achievement.sync()   
    jump expression "sleeping_event%s"%mc_event_lvl

    

