label ending_normal1:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        if persistent.gallery_pregnancy_censored:    
            $ set_active_pregnancy = False
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
        menu(screen="custom_choice_long"):
            "{size=+15}Do you know [neusname]' secret? (Change some dialogues.)"
            "Yes":
                $is_neus_sec_dis = True
            "No":
                $is_neus_sec_dis = False
    play music talk_and_walk volume 0.2 fadeout 1.0 if_changed
    scene end_nor1_0 with storyfx
    mc "...."
    neus "..."
    mc "..."
    scene end_nor1_1 with dissolve
    if incest_story:
        neus "Is something wrong, brother?"     
    else:
        neus "Is something wrong?"     
    mc "No, I'm just thinking."
    play music happy_memories volume 0.2 fadeout 1.0
    scene level0_1_9 at gray_scale with dissolve
    mc "We had our first kiss."
    scene level0_2_15 at gray_scale with dissolve
    mc "We had our first sexual experience."
    scene level1_1_10_1 at gray_scale with dissolve
    mc "We continued moving forward."
    scene level1_2_18 at gray_scale with dissolve
    mc "We slowed down a bit."
    scene level1_3_14_1 at gray_scale with dissolve
    mc "We took the next step."
    scene level2_0_31 at gray_scale with dissolve
    mc "After an intimate conversation, we became a couple."
    scene level2_1_16 at gray_scale with dissolve
    mc "We had our first problem."
    scene level2_2_22 at gray_scale with dissolve
    mc "Once again, a good conversation resolved it."
    scene end_nor1_2 with dissolve
    stop music fadeout 1.0
    mc "Don't you think it's time to take the next step?"
    scene end_nor1_3 with dissolve
    play music cold_fish volume 0.15 fadeout 1.0
    neus "*Sigh* I guess it can't be avoided."
    scene end_nor1_4 with dissolve
    neus "{size=-15}Although I suspect you're being manipulated... maybe with that hypnosis book that appeared in the attic. I'm not sure if it's even real.{w=0.25}{nw}"
    if incest_story:
        neus "{size=-15}But with your recent behavior, and the phone call you received from mom, it seems likely. And... I think I might be the culprit.{w=0.25}{nw}"
    else:
        neus "{size=-15}But with your recent behavior, and the phone call you received from your mom, it seems likely. And... I think I might be the culprit.{w=0.25}{nw}"
    scene end_nor1_5 with dissolve
    neus "{size=-15}Well, a part of me is. I've been having fainting spells, and they've been getting worse, especially since you started changing.{w=0.25}{nw}"
    neus "{size=-15}Before, it was subtle. I couldn't tell you, but I can't keep this lie going anymore.{w=0.25}{nw}"
    scene end_nor1_6 with dissolve  
    if incest_story:
        neus "I'm sorry brother, that's why I can't accept."
    else: 
        neus "I'm sorry, that's why I can't accept."
    scene end_nor1_7 with dissolve
    stop music fadeout 1.0
    if is_neus_sec_dis:
        mc "You spoke really fast, but I understand."
        mc "And I know how to make you feel better."
    else:    
        mc "You're speaking too fast, I didn't understand you."
        mc "But from the time we've spent together, I’ve learned how to make you feel better."
    scene end_nor1_8 with dissolve
    neus "But-"
    scene end_nor1_9 with dissolve
    mc "Shhhh"
    call splash_message(_("After a conversation")) from _call_splash_message_40
    scene end_nor1_10 with dissolve
    play music breathing2 volume 0.3 fadeout 1.0
    if incest_story:
        mc "Can you repeat what you promised little sister, just to make it clear?"
    else:
        mc "Can you repeat what you promised, just to make it clear?"
    scene end_nor1_11 with dissolve
    neus "I promise to be your woman. I-I promise to be your wife."
    mc "Excellent."
    scene end_nor1_12 with dissolve    
    neus "No {sc=2}more{/sc}, please."(multiple=2)
    play char1 climax1
    mc "I think you deserve a reward."(multiple=2)
    scene end_nor1_12_1 with dissolve
    mc "It's time for these wide hips to get to work."
    if incest_story:
        mc "I want us to have many children, darling sister."
    else:
        mc "I want us to have many children, darling."
    scene black with dissolve
    stop music fadeout 1.0    
    centered "{size=+50}She stopped taking the contraceptive pills, and a month later, the outcome was exactly what we expected."
    play music blueskyairport volume 0.4 fadeout .5
    if incest_story:
        neus "Brother!"
    scene end_nor1_13 with dissolve    
    neus "Look!"
    mc "Nice."
    scene end_nor1_14 with dissolve
    neus "*Sigh* I wish I wasn't pregnant."
    mc "?"    
    scene end_nor1_15 with dissolve
    neus "I would have liked to prepare myself to be a mother."
    scene end_nor1_16 with dissolve
    neus "Plus, I have small breasts. It's going to starve."
    mc "I heard that during pregnancy, breasts grow around 1 to 2 cup sizes, sometimes even 3 sizes."
    mc "And there's also formula milk."
    scene end_nor1_17 with dissolve
    neus "Well, I guess that solves my small breasts problem."
    mc "I think we should organize our wedding soon, before the dress no longer fits you."
    scene end_nor1_18 with dissolve
    if incest_story:
        neus "I suppose so. After all, I promised to be your wife, and somehow you got our auntie to be okay with it... so there's no avoiding it."
    else:
        neus "I suppose so. After all, I promised to be your wife, so there's no avoiding it."
    mc "Here we go again."
    scene end_nor1_19 with dissolve
    neus "I'm sorry, I find it hard to break that habit."
    scene end_nor1_20 with dissolve
    if incest_story:
        neus "I'm looking forward to being your wife. How’s that brother?"
    else:
        neus "I'm looking forward to being your wife. How’s that?"
    mc "A little better."
    call splash_message(_("2 month later")) from _call_splash_message_41
    scene end_nor1_21 with dissolve
    play music TheGirlFromBrasil_Hauser volume 0.4 fadeout .5
    ""
    scene end_nor1_22 with dissolve    
    neus "I do."
    mc "I do, I promise to give you lots of ''love''."  
    scene end_nor1_22_0 with dissolve  
    neus "Even more?"
    mc "Yes, by the way, isn't the dress a little tight?"
    scene end_nor1_23 with dissolve    
    neus "Well, it's not the most comfortable, but it doesn't squeeze my stomach."
    scene end_nor1_24 with dissolve
    neus "It's fine, really. You don't need to worry."
    mc "Okay." 
    if set_active_pregnancy: 
        scene black with dissolve
        stop music fadeout 1.0
        centered "{size=+50}Several months passed, the pregnancy progressed safely, her belly and breasts grew."        
        scene end_nor1_25 with dissolve
        if incest_story:
            neus "please be gentle, brother."
        else:
            neus "Be gentle, okay?"
        mc "Don't worry, I'll be as gentle as possible."
        scene end_nor1_26 with fadesex
        play char1 climax1
        neus "Haa."
        mc "I'm about to start moving."       
        scene end_nor1_27 with dissolve
        play char3 sex1 fadeout 1.0
        if incest_story:
            mc "How does it feel sis? If it hurts, let me know so I can stop."
        else:
            mc "How does it feel? If it hurts, let me know so I can stop."
        neus "Alright."       
        mc "After our baby is born, we should start working on having another one."
        neus "?"
        mc "It wouldn't be good if our child felt lonely. We should have another one to keep them company."
        mc "Around 9 or maybe 11 children."
        if incest_story:
            neus "That's a lot big brother. I don't think my body can handle having that many. {bt=1}{=lust_style}Haa haa haa.{/bt}"
        else:
            neus "That's a lot. I don't think my body can handle having that many. {bt=1}{=lust_style}Haa haa haa.{/bt}"
        scene end_nor1_27_1 with dissolve
        play char1 groan1
        neus "{bt=2}{=lust_style}I'm cumming.{/bt}"
        stop char3
        play charM cum1
        play char1 climax1
        scene end_nor1_28 with flash2
        if incest_story:
            neus "Haaa brother."
        else:
            neus "Haaa."
        mc "I think that's enough action for today."
        scene end_nor1_29 with dissolve
        neus "Mmm... I think I can handle a {bt=2}{=lust_style}little more{/bt} ...{e_heartbt=FF0000}" 
        if incest_story:
            neus "{bt=2}Please {=lust_style}brother...{/bt}"
            mc "Mmm... Okay sis, a little bit more, but then you have to rest."
        else:
            mc "Mmm... Okay, a little bit more, but then you have to rest."
        scene end_nor1_29_1 with dissolve
        neus "Yaaay!"  
        scene black with snow1    
        centered "{size=+50}We did it about two more times."
    else:
        scene black with dissolve
        "{size=+8}{color=#ff0000}Pregnant sex censorship activated."
    python:
        achievement.grant("Normal_Ending")
        achievement.sync()   
    if not ending_1_obtained:
        $ endings_obtained_count += 1
        $ ending_1_obtained = True
    centered "{size=+80}Normal Ending" 
    "You have obtained {color=#cc0066}Ending 1{/color} out of {color=#cc0066}[available_endings] possible endings{/color}."
    play music cold_fish volume 0.6 fadeout 1.0 
    neus "I'm sorry, in the end."
    neus "I'm a weak liar, and to make things worse, this decision actually makes me very happy."    
    scene end_nor1_30 with dissolve
    if is_neus_sec_dis:
        ""
    else:
        neus_yan "If lies aren't uncovered, they become truth."
    scene end_nor1_31 with dissolve
    play sound magical1 volume 0.3
    neus_yan "*Sniff* {font=fonts/Alkatra-Regular.ttf}P-Personality.{/font}{w=1.5}{nw}"
    scene end_nor1_32 with dissolve 
    if is_neus_sec_dis: 
        stop music fadeout 3.0       
        mc "After a dramatic and highly exaggerated scene—one that, from the outside, might seem deeply meaningful..."
        mc "I couldn't shake the feeling of sadness. I wish I could have given her love, too."       
    else:
        ""
    if _in_replay:
        $is_neus_sec_dis=persistent.is_neus_sec_dis    
    $renpy.end_replay()  
    $persistent.main_menu_b=1   
    jump menu_ending_normal  

label ending_obsession1:
    scene end_obs1_0 with dissolve 
    neus_yan "Oh, great!?"
    scene end_obs1_1 with dissolve 
    neus_yan "She will take time to disappear"
    scene end_obs1_2 with dissolve
    neus_yan "But from now on, you are only mine"
    scene end_obs1_3 with dissolve
    "{w=0.7}{nw}"
    scene end_obs1_4 with dissolve    
    if incest_story:
        neus_yan "I'm still amazed at how big your cock is brother."
    else:
        neus_yan "I'm still amazed at how big your cock is."
    scene end_obs1_5 with dissolve
    play char1 short_kiss2 volume 3.0
    neus_yan "And it is all mine." 
    scene end_obs1_6 with dissolve  
    neus_yan "Mmm"
    neus_yan "I could lick it all day."    
    neus_yan "It's so delicious."
    scene end_obs1_7 with dissolve
    neus_yan "I think I'm wet enough already."
    neus_yan "I'm going to ride this vigorous penis."
    scene end_obs1_8 with dissolve
    play char1 penetration3
    neus_yan "Ohhh"
    neus_yan "I need it deeper."
    scene end_obs1_9 with dissolve
    neus_yan "Yes, this is exactly what I need."
    neus_yan "I'm going to start moving"
    scene end_obs1_10 with dissolve
    play char3 sex2 fadeout 1.0
    neus_yan "{bt=2}Haa Haa Haaa{/bt}"
    neus_yan "{bt=2}More More More{/bt}"
    if incest_story:
        neus_yan "We’ll do this every day from now on, brother."
    else:
        neus_yan "From now on, we will do this every day"
    scene end_obs1_11 with dissolve
    neus_yan "It feels so good"
    neus_yan "It's better than the blurry memories I have."
    neus_yan "Our first time, it hurt."
    neus_yan "But now it doesn't hurt at all, it feels so good."
    scene end_obs1_12 with dissolve
    neus_yan "{bt=2}Mooooreeee{/bt}"
    neus_yan "{bt=2}Haaaaa Haaaa Haaaa{/bt}"
    scene end_obs1_13 with dissolve
    if incest_story:
        neus_yan "Cum inside me brother"    
    else:
        neus_yan "Cum inside me"    
    if incest_story:
        neus_yan "Your little sister wants you to impregnate her."
    else:
        neus_yan "I want you to impregnate me."
    scene end_obs1_14 with flash2
    stop char3 
    play charM cum1
    neus_yan "Ohhh"
    scene end_obs1_15 with dissolve
    if incest_story:
        neus_yan "From now on, I want you to cum inside me every day. I want to have lots of children with you."
    else:
        neus_yan "From now on, I want you to cum inside me every day. I want to have lots of children with you."
    scene end_obs1_16 with dissolve
    neus_yan "I won't let you rest."
    if incest_story:
        neus_yan "You are only mine, brother."
    else:
        neus_yan "You are only mine."
    scene black with dissolve
    mc "(We did it for another 2 hours)"
    mc "(Throughout that time, she was in control)"
    scene end_obs1_17 with dissolve
    neus_yan "Moreee moreee"(multiple=2)
    mc "(Even though her personality is different, as if she were another person, it seems like her body still has the same limit.)"(multiple=2) 
    scene end_obs1_18 with dissolve  
    neus_yan "Moreee moreee"(multiple=2)
    if incest_story:
        mc "Are you sure little sister?"(multiple=2)
    else:
        mc "Are you sure?"(multiple=2)
    scene end_obs1_19 with dissolve
    neus_yan "{size=-10}Yessss"
    scene black with dissolve
    mc "(We continued for a few more hours before she passed out)"
    if set_active_pregnancy:
        call splash_message(_("One month later.")) from _call_splash_message_42
        scene end_obs1_20 with dissolve
        neus_yan "Look, we did it."
        scene end_obs1_21 with dissolve    
        menu:
            neus_yan "What would you like it to be, a girl or a boy?"
            "Girl":
                scene end_obs1_22 with dissolve
                neus_yan "I feel the same way"
                scene end_obs1_23 with dissolve
                neus_yan "But we should have many children so they never feel lonely."
                if not incest_story:
                    neus_yan "I often felt lonely being an only child."
            "Boy":
                scene end_obs1_24 with dissolve
                neus_yan "Oh, I was hoping for a girl."
                scene end_obs1_23 with dissolve
                neus_yan "But that's okay. We're going to have many children anyway." 
        scene end_obs1_25 with dissolve               
        neus_yan "From now on, we have to work on creating many children."
        scene black with dissolve
        centered "{size=+50}Several months passed, the pregnancy progressed safely, her belly and breasts grew." 
        scene end_obs1_26 with dissolve
        neus_yan "I'm sorry you can't use my vagina, you'll have to settle for my ass."
        scene end_obs1_27 with dissolve
        if incest_story:
            neus_yan "How does it feel brother?"
        else:
            neus_yan "How does it feel?"
        mc "Very good"
        scene end_obs1_28 with dissolve
        play char3 sex2 fadeout 1.0
        neus_yan "Hehe, well, that was to be expected. After all, you've been using it for the past few months."    
        neus_yan "My ass has taken the shape of your cock."
        scene end_obs1_29 with flash2
        stop char3 
        play charM cum1
        neus_yan "I'm cumming, from your cock in my ass."
    else:
        scene black with dissolve
        "{size=+8}{color=#ff0000}Pregnant sex censorship activated."
    call splash_message(_("13 years later")) from _call_splash_message_43                
    mc "(We had 10 children.)"
    scene end_obs1_30 with dissolve
    if incest_story:
        neus "Brother, the kids will be staying with our auntie for the week."(multiple=2)
    else:
        neus "Darling, the kids will stay with my mom for a week."(multiple=2)
    mc "(Her other personality disappeared, and when that happened, I felt a little sad. I would have liked to show her a lot of love as well.)"(multiple=2)
    scene end_obs1_31 with dissolve
    neus "I want us to have our eleventh child."(multiple=2)
    mc  "(But this outcome isn't bad either.)" (multiple=2)
    neus "My belly feels lonely."
    if incest_story:
        neus "I want you to use that big dick of yours, to fill my tight hole and impregnate me once again, brother.{e_heartbt=FF0000}"
    else:
        neus "I want you to use that big dick of yours, to fill my tight hole and impregnate me once again.{e_heartbt=FF0000}"
    scene black with snow1
    python:
        achievement.grant("Obsession_Ending")
        achievement.sync()   
    if not ending_2_obtained:
        $ endings_obtained_count += 1
        $ ending_2_obtained = True
    centered "{size=+80}End of Obsession 1"
    "You have obtained {color=#cc0066}Ending 2{/color} out of {color=#cc0066}[available_endings] possible endings{/color}."    
    $renpy.end_replay()  
    $persistent.main_menu_b=2  
    jump menu_ending_confrontation

label ending_obsession2:
    scene end_obs2_0 with dissolve
    neus_yan "Mmmm, I understand..."
    scene end_obs2_1 with dissolve
    play music the_truth_is_in_the_dark volume 0.2 fadeout 1.0
    neus_yan "But I also hope you understand what I'm going to do."
    scene end_obs2_2 with dissolve
    neus_yan "I'm so sorry, my intention wasn't for you to meet me."   
    scene end_obs2_3 with dissolve
    neus_yan "After making sure I became your wife, I was going to use the book I gave you to disappear."
    scene end_obs2_4 with dissolve
    neus_yan "But even if you hate me, I can't accept handing you over to someone else."
    scene end_obs2_5 with dissolve
    stop music fadeout 2.0
    neus_yan "{=lust_style}I want you to be mine.{e_heartbt=FF0000}"
    scene bg_hypnosis2 with dissolve  
    play sound magical1 volume 0.1
    play char3 whisper volume 0.3
    pause 0.5
    if incest_story:
        centered "{size=+40}You want many children with your sister. You want many children with your sister. You want many children with your sister. You want many children with your sister. You want many children with your sister....{w=6.5}{nw}"
        centered "{size=+40}You only love your sister. You only love your sister. You only love your sister. You only love your sister. You only love your sister. You only love your sister. You only love your sister...{w=6.5}{nw}"
        "As my resistance crumbled, my desires were reshaped until the decision was no longer my own."(multiple=2)
        neus_yan "You are only mine... Brother {e_heartbt=FF0000}"(multiple=2)
    else:
        centered "{size=+40}You want many children with [neusname]. You want many children with [neusname]. You want many children with [neusname]. You want many children with [neusname]. You want many children with [neusname]....{w=4.5}{nw}"
        centered "{size=+40}You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]...{w=4.5}{nw}"
        "As my resistance crumbled, my desires were reshaped until the decision was no longer my own."(multiple=2)
        neus_yan "You are only mine.{e_heartbt=FF0000}"(multiple=2)
    stop char3 fadeout 0.5
    call splash_message(_("8 months later")) from _call_splash_message_44         
    play char3 sex2 fadeout 1.0
    scene end_obs2_6 with dissolve
    neus_yan "{=lust_style}Haaa haaa"
    neus_yan "{=lust_style}More, more."    
    if incest_story:
        neus_yan "Having my brother's cock inside me feels so {=lust_style}good."
    else:
        neus_yan "Having your cock inside me feels so {=lust_style}good."
    if set_active_pregnancy:
        scene end_obs2_7 with dissolve
        neus_yan "After our first child is born, we'll have another."
        neus_yan "And another, and another, and another."
        scene end_obs2_8 with dissolve  
        neus_yan "{=lust_style}Haaa haaa"
        scene end_obs2_9 with flash2
        stop char3 
        play charM cum1
        if incest_story:
            neus_yan "{bt=3}Ahhh, brother{/bt}"
        else:
            neus_yan "Ahhh"
        neus_yan "{bt=2}It feels so {=lust_style}good.{/bt}"
        scene end_obs2_10 with dissolve
        neus_yan "Your cock is so addictive, I can't live without using it every day."
        neus_yan "After our child is born, I want you to give me another child, and another, and another."         
    else:
        scene black with dissolve
        "{size=+8}{color=#ff0000}Pregnant sex censorship activated."       
    scene end_obs2_11 with dissolve
    neus_yan "We'll {color=#cc0066}always{/color} be {color=#cc0066}together.{/color} {e_heartbt=FF0000}"
    scene black with snow1
    if incest_story:
        neus_yan "You're {color=#cc0066}my brother{/color} and I will {color=#cc0066}never{/color} give you to anyone else."
    else:
        neus_yan "I will {color=#cc0066}never{/color} give you to anyone else."
    python:
        achievement.grant("No_Escape")
        achievement.sync()
    if not ending_3_obtained:
        $ endings_obtained_count += 1
        $ ending_3_obtained = True
    centered "{size=+80}End of Obsession 2"  
    "You have obtained {color=#cc0066}Ending 3{/color} out of {color=#cc0066}[available_endings] possible endings{/color}."       
    $renpy.end_replay() 
    $persistent.main_menu_b=3   
    jump menu_ending_confrontation

label menu_ending_confrontation:  
    scene black  
    $renpy.end_replay()    
    menu(screen="custom_choice_long"):
        "Continue":            
            jump confrontation_menu 
        "Main Menu":
            menu(screen="custom_choice_long"):
                "Are you sure you want to go to the main menu?"
                "Yes":
                    $ MainMenu(confirm=False)()
                "No":
                    jump menu_ending_confrontation        
label menu_ending_normal:  
    scene black  
    $renpy.end_replay()    
    menu(screen="custom_choice_long"):
        "Continue":            
            jump rooms 
        "Main Menu":
            menu(screen="custom_choice_long"):
                "Are you sure you want to go to the main menu?"
                "Yes":
                    $ MainMenu(confirm=False)()
                "No":
                    jump menu_ending_normal

        
                
                
