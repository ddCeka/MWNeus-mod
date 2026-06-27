
label confrontation:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        if persistent.gallery_pregnancy_censored:    
            $ set_active_pregnancy = False
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    stop music fadeout 2.0
    $is_neus_sec_dis=True
    $persistent.is_neus_sec_dis=True
    if quest_v2:
        $ questSide_v2_6.completion = True
    else:
        $questSide_5.completion=True
    $is_change_quest = True 
    if not _in_replay:
        call notify_personalized(_("Side Quest updated"))   
    # scene extra0_2 with dissolve
    # mc "Mmm..."
    scene extra0_3 with dissolve
    mc "Mmm..." # Moved
    mc "What should I do with this knowledge?"
    scene extra0_4 with dissolve
    "{w=0.7}{nw}"
    scene extra0_5 with storyfx
    play music talk_and_walk volume 0.3 fadeout 1.0
    neus "Mmm, this tastes amazing!"    
    scene extra0_6 with dissolve
    if incest_story:
        neus "(I'm sure my brother will love it.)"
    else:
        neus "(I'm sure [firstname] will love it.)"
    scene extra0_7 with dissolve
    neus "(I should invite him to try this with me.)"
    scene extra0_8 with dissolve
    neus "(It would be a good place for a date too.) hehehe."
    scene extra0_9 with dissolve
    ""
    play sound whoosh1
    scene extra0_10 with pushle
    stop music fadeout 1.5
    neus "?"
    scene extra0_11 with dissolve   
    neus "(Why is the attic open...)"
    scene extra0_12 with dissolve
    neus "*Yawns* (I'm so sleepy...){w=1.0}{nw}" 
    scene extra0_13 with dissolve
    play music the_truth_is_in_the_dark volume 0.3 fadeout 1.0
    "{w=1.0}{nw}"
    scene extra0_14 with dissolve 
    "" 
    scene extra0_15 with  pushu 
    ""
    scene extra0_16 with dissolve 
    if incest_story:
        mc "Hey, sis...{w=1.5}{nw}"
    else:
        mc "Hey, [neusname]...{w=1.5}{nw}"
    scene extra0_17_0 with dissolve
    "{w=1.0}{nw}"
    scene extra0_17_1 with dissolve  
    "{w=.3}{nw}"  
    scene extra0_17_2 with dissolve 
    stop music fadeout 1.0
    play sound hit1
    mc "It's true that I invaded your personal space." with hpunch
    scene extra0_18 with dissolve 
    mc "But don't you think trying to hit me on the head with a bat is a bit excessive?"
    scene extra0_19 with dissolve
    mc "Although I think you've done something worse to me...{w=3.5}{nw}"
    scene extra0_20 with dissolve
    mc "Mmm?{w=.8}{nw}" 
    play sound falling1
    scene extra0_21 with pushdo    
    mc "..."
    scene extra0_22 with dissolve  
    play sound magical1 volume 0.3
    neus_yan "{font=fonts/Alkatra-Regular.ttf}Truth!{/font}"
    scene extra0_23 with dissolve
    neus_yan "You know, you didn’t have to go digging around."
    neus_yan "You and her could have been happy."    
    scene extra0_24 with dissolve
    neus_yan "But no... here you are, prying into things you weren’t meant to see. What was it that brought you here?"
    mc "(I suppose that in this situation, it would be normal to feel scared, but...)"  
    scene extra0_25 with rain1 
    play music happy_memories volume 0.3 fadeout 1.0
    if incest_story:
        mc "(Our parents were leaders of a very large organization)"
        mc "(They died in an accident—or at least, that’s what was publicly announced.)"    
        scene extra0_26 with snow1
        neus "Brother, can I sleep with you again tonight? It's been helping a lot."(multiple=2)
        mc "(During that time, I realized how important she was to me. She’s my sister, but she became my whole world.)"(multiple=2)
    else:
        mc "(My parents were leaders of a very large organization)"
        mc "(They died in an accident—or at least, that’s what was publicly announced.)"    
        scene extra0_26 with snow1
        neus "Hey, are you free?"(multiple=2)
        mc "(During that time, I met her. She became someone incredibly important to me.)"(multiple=2)
    mc "(I could say from that moment on, I was already... infatuated.)"
    scene extra0_27 with dissolve 
    neus "It smells so good.{e_heartbt=FF0000}"(multiple=2)
    mc "(I was aware that she had some obsessive tendencies)"(multiple=2)    
    scene bg_hypnosis with dissolve
    mc "(Although at that moment, I didn't think she would go this far.)"
    scene extra0_28 with dissolve
    neus "I-I'm sorry, I-I'm busy."(multiple=2)
    mc "(Some time later, she started distancing herself from me.)"(multiple=2)
    if incest_story:
        mc "(So I decided to give her space, while I attended to our family's business, which eventually led me to move out.)"
    else:
        mc "(So I decided to give her space while I attended to my family matters.)"
    scene extra0_29 with dissolve
    neus "Wow, it's so big"(multiple=2)
    if incest_story:
        mc "(''Conveniently,'' she enrolled in a university near where I’d moved, so she ended up moving in with me.)"(multiple=2)
        scene  black with dissolve
        mc "(Living together motivated me to move our relationship forward, but since we're siblings, I chose to take things slowly.)"
    else:
        mc "(''Conveniently'', she enrolled in to a university near where I live.)"(multiple=2)
        scene  black with dissolve
        mc "(I decided to take my time with moving our relationship forward.)"
    mc "(Although in the end, I was considering taking a different approach.)"
    mc "(So I guess her actions only accelerated things.)"
    scene extra0_30 with dissolve
    play music lazy_night volume 0.7 fadeout 1.0
    neus_yan "Hmm, so that's how you felt."
    neus_yan "There was never any need for me to hold back."
    scene extra0_31 with dissolve
    neus_yan "I wasted so much time. I was worried some of those busty girls could have taken you from me. It wasn’t easy to scare them off, you know?"
    mc "(So that's why they backed off, although I didn't care much since I was only interested in her.)"
    scene extra0_32 with dissolve
    neus_yan "Oh, thanks."
    scene extra0_33 with dissolve
    mc "(Interesting, I can't hide any of my thoughts.)"
    scene extra0_34 with dissolve
    neus_yan "That would have been a very effective spell with her. That’s what you were thinking, right? Hehe."
    scene extra0_35 with dissolve
    neus_yan "Although there's no need for you to worry about that anymore."
    neus_yan "But as an apology for what I did..."
    scene extra0_36 with dissolve
    neus_yan "I'll let you choose which part of me you want."
    scene extra0_37 with dissolve
    play sound magical1 volume 0.3
    stop music fadeout 1.0
    neus_yan "Mmm?"(multiple=2)
    mc "{font=fonts/Alkatra-Regular.ttf}Cancel{/font}"(multiple=2)
    scene extra0_38 with dissolve
    mc "(So, as an apology for hypnotizing me, you'll let me choose.)"
    scene extra0_38_1 with dissolve
    mc "(Although, I've heard hypnosis doesn’t quite live up to its name.)"
    mc "(The victim's desire and the command must align... At least to some extent.)"
    scene black with dissolve
    mc "(but I suppose it was quite effective in my case.)"  
    if incest_story:
        mc "(I desired to make her mine. To the point where I dedicated a lot of time to our deceased parents' organization.)"   
    else:
        mc "(I desired to make [neusname] mine. To the point where I dedicated a lot of time to my deceased parents' organization.)"   
    mc "(So I could gather enough money and resources to have many, many children with her.)"    
    mc "(And shower her with love until her mind brea-)"    
    mc "(Ugh, I'm getting distracted.)"
    mc "(So I have to choose one of her personalities.)"
    scene extra0_39 with dissolve
    mc "(A tsundere that contains her feelings, where over time her dere side becomes more dominant.)"
    scene extra0_40 with dissolve
    mc "(Or her, which in part reminds me of the [neusname] from the past.)"
    scene bg_hentai_magazine at gray_blur5 with dissolve
    mc "(And maybe the reason I’m attracted to a certain type of woman.)"
    scene extra0_41 with dissolve
    mc "(But why do I have to choose only one part of her? Why can't I have it all?)"
    label confrontation_menu:
        scene extra0_41
        menu:
            "{color=#cc0066}You can change this decision later.{/color}"
            "Everything":                
                play music lazy_night volume 0.7 fadeout 1.0
                scene extra0_49 with dissolve
                neus_yan "Ehhh."(multiple=2)
                mc "Why do I have to choose? I want all of you."(multiple=2)
                scene extra0_50 with dissolve
                neus_yan "Mmm?"(multiple=2)
                mc "You want to be completely loved, don't you?"(multiple=2) 
                scene extra0_51 with dissolve              
                mc "I see you also have that bad habi-{w=2.5}{nw}"
                scene extra0_52 with dissolve
                neus_yan "I didn't think you'd want that... I thought you'd hate me."                
                neus_yan "I never planned for you to meet me... and love me as well."
                scene extra0_53 with dissolve
                neus_yan "Loving her... that would have been enough."
                scene extra0_54 with dissolve
                neus_yan "Then I would have just disappeared..."
                scene extra0_55 with dissolve
                neus_yan "Uhhh." 
                scene extra0_56 with dissolve               
                mc "I don't care. I want your entire being to be mine."
                mc "I want to give all of you the love you desire."
                scene extra0_57 with dissolve 
                neus_yan "Really?"
                mc "Yes."
                scene extra0_58 with dissolve 
                neus_yan "I want another {bt=1}kiss.{/bt}"
                scene extra0_59 with dissolve 
                neus_yan "Uhhh."
                scene extra0_60 with dissolve
                neus_yan "Wait, she's about to wake up."
                scene extra0_48 with dissolve
                neus_yan "You should talk to her about this, unless you've changed your mind."
            "Tsundere": 
                play music lazy_night volume 0.7 fadeout 1.0 
                scene extra0_42 with dissolve              
                neus_yan "I suppose I was expecting this outcome."
                scene extra0_43 with dissolve
                neus_yan "But I'm afraid I can't disappear just yet."               
                scene extra0_44 with dissolve
                neus_yan "I have to make sure we end up together, and then I'll use the book I gave you to disappear."
                scene extra0_45 with dissolve
                neus_yan "Although you can change your mind at any point."
                scene extra0_46 with dissolve
                neus_yan "Well, I'll leave you now."
                scene extra0_47 with dissolve
                neus_yan "She's about to wake up, it would be bad if she found out this way."
                scene extra0_48 with dissolve
                neus_yan "You could tell her everything... or keep her in the dark, hehehe."                                
            "Her ({color=#cc0066}Ending 1{/color})":
                jump ending_obsession1                                           
            "None ({color=#cc0066}Ending 2{/color})":
                jump ending_obsession2  
        scene extra0_61 with dissolve
        neus_yan "Although there might be another path."
        $renpy.end_replay() 
        scene black with dissolve
        $spell_3_2.start=True
        #$spell_3_2.is_active=True
        centered "{size=+50}The spell {color=#cc0066}''Personality''{/color} has been unlocked."
        $neus_obsession_name = _("Obsession:")
        python:
            achievement.grant("Secret")
            achievement.sync()  
        call rooms_music 
        jump attic_room    
    jump rooms  
    