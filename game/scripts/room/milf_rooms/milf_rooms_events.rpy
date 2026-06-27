image milf_event_mc_eve0_4 = DynamicAnimation(
["rooms/milf/milf_event_mc_eve0_4_0.webp",
"rooms/milf/milf_event_mc_eve0_4_1.webp",
"rooms/milf/milf_event_mc_eve0_4_2.webp",])
image milf_event_mc_eve_pregnant2_0 = DynamicAnimation(
["rooms/milf/milf_event_mc_eve_pregnant2_0_0.webp",
"rooms/milf/milf_event_mc_eve_pregnant2_0_1.webp",
"rooms/milf/milf_event_mc_eve_pregnant2_0_2.webp",])
image milf_event_mc_eve_pregnant3_0 = DynamicAnimation(
["rooms/milf/milf_event_mc_eve_pregnant3_0_0.webp",
"rooms/milf/milf_event_mc_eve_pregnant3_0_1.webp",
"rooms/milf/milf_event_mc_eve_pregnant3_0_2.webp",])
image milf_event_mc_eve_pregnant3_outfit_cow_0 = DynamicAnimation(
["rooms/milf/milf_event_mc_eve_pregnant3_outfit_cow_0_0.webp",
"rooms/milf/milf_event_mc_eve_pregnant3_outfit_cow_0_1.webp",
"rooms/milf/milf_event_mc_eve_pregnant3_outfit_cow_0_2.webp",])
default milf_event_kitchen_count_normal=0
default milf_event_kitchen_count_pregnant2=0
default milf_event_kitchen_count_pregnant3=0
default milf_event_bath_count_normal=0
default milf_event_bath_count_pregnant2=0
default milf_event_bath_count_pregnant3=0
default is_view_intro_milf_mc_eve=False
default milf_is_boy_girl=False
default milf_is_you_win_name=False
default milf_is_view_name_baby=False
default milfnamebaby=""
default is_view_intro_milf_outfit_cow=False
default is_milf_outfit_cow_nomal=True
label menu_milf_ending:
    menu:        
        "Ending":
            jump milf_true_ending
        "Leave":
            jump milf_rooms
#----------------------------kitchen----------------------------
label milf_event_kitchen_control:
    if milf_event_kitchen_count_normal==0:
        $ milf_event_kitchen_count_normal=1
        jump milf_event_kitchen0 
    elif milf_event_kitchen_count_normal==1:
        $ milf_event_kitchen_count_normal=2
        jump milf_event_kitchen1
    else:
        menu:
            "Event 0":
                jump milf_event_kitchen0                
            "Event 1":
                jump milf_event_kitchen1
            "Leave":
                jump milf_rooms
label milf_event_kitchen0:
    play ambience morning_sounds
    scene milf_event_kitchen0_0 with storyfx
    neus "*humming * La la la"
    scene milf_event_kitchen0_1 with dissolve
    mc "I see that breakfast is ready."
    scene milf_event_kitchen0_2 with dissolve
    if incest_story:
        neus "Hehe, I see you don't miss an opportunity, brother"
    else:
        neus "Hehe, I see you don't miss an opportunity, darling"
    scene milf_event_kitchen0_3 with dissolve
    mc "Thanks for the meal."   
    scene milf_event_kitchen0_4 with dissolve 
    play char1 penetration2
    neus "Uh!"
    scene milf_event_kitchen0_5 with dissolve
    play char3 sex7
    mc "It always feels so good."
    mc "Your pussy is amazing."
    if incest_story:
        neus "Well, your sister's little pussy was trained for 17 years to be the perfect fit for your cock."
    else:
        neus "Well, my little pussy was trained for 17 years to be the perfect fit for your cock."
    neus "Plus, your cock touches all my sensitive spots."
    neus "The compatibility is so high that I cum!"
    stop char3
    play charM cum1
    scene milf_event_kitchen0_6 with dissolve
    play char1 climax1
    neus "{sc=2}{=lust_style}Uh!{/sc}"
    scene milf_event_kitchen0_7 with dissolve
    if incest_story:
        neus "Brother, I love it when you fill me."
    else:
        neus "I love it when you fill me."
    neus "But I want more."
    scene milf_event_kitchen0_8 with dissolve
    play char3 sex7
    neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
    if is_milf_pregnant:
        neus "I shouldn't, but-"
        if incest_story:
            neus "My pregnant little pussy is addicted to being filled by my brother."
        else:
            neus "My pregnant little pussy is addicted to being filled."
    else:
        neus "I shouldn't, but I want to get pregnant again."
        if incest_story:
            neus "My pussy is addicted to being filled by my brother."
        else:
            neus "My pussy is addicted to being filled."
    scene milf_event_kitchen0_9 with dissolve
    neus "Cum inside."
    stop char3
    play charM cum1
    scene milf_event_kitchen0_10 with dissolve
    play char1 climax1
    neus "{sc=2}{=lust_style}Uh!{/sc}"
    scene black with dissolve
    neus "Well, let's have breakfast."
    scene milf_event_kitchen0_11 with w18
    ""    
    stop ambience
    jump milf_time_advances
label milf_event_kitchen1:
    play ambience morning_sounds
    scene milf_event_kitchen1_0 with storyfx
    play char3 deep_suck1
    neus "*Suck suck*"
    neus "*Lick lick*"
    neus "{e_heartbt2=FF0000}"
    scene milf_event_kitchen1_1 with dissolve
    neus "(Delicious {e_heartbt=FF0000})"
    if incest_story:
        "You feel like you're about to cum in your sister's mouth"    
    else:
        "You feel like you're about to cum in her mouth"    
    scene milf_event_kitchen1_0 with dissolve     
    menu:
        "With what force will you cum in her mouth?"
        "Strong":
            stop char3
            play charM cum1
            scene milf_event_kitchen1_2 with flash2 
            "{e_heartbt2=FF0000}"           
        "Gentle":
            stop char3
            play charM cum1
            scene milf_event_kitchen1_3 with flash2
            "{e_heartbt2=FF0000}"
    scene milf_event_kitchen1_4 with dissolve
    if incest_story:
        neus "Did you enjoy breakfast, brother?"
    else:
        neus "Did you enjoy breakfast, darling?"
    mc "Yes, I loved it"
    scene milf_event_kitchen1_5 with dissolve
    neus "Hehe, great, I also enjoyed the breakfast you gave me {e_heartbt=FF0000}"
    scene black with dissolve
    "..."    
    stop ambience
    jump milf_time_advances

label milf_event_kitchen_pregnant2:
    $ milf_event_kitchen_count_pregnant2=1
    scene milf_event_kitchen_pregnant2_0 with storyfx
    if incest_story:
        mc "Good morning, sister."
        neus "Good morning, brother."
    else:
        mc "Good morning."
        neus "Good morning, darling."
    scene milf_event_kitchen_pregnant2_1 with dissolve
    neus "Could you pass me the sugar?"
    scene milf_event_kitchen_pregnant2_2 with dissolve
    neus "Thank you."
    scene milf_event_kitchen_pregnant2_3 with w33
    neus "How are the cookies?"
    mc "Very tasty."
    neus "Hehe."
    menu:
        "Ask for milk":
            scene milf_event_kitchen_pregnant2_4 with dissolve
            if incest_story:
                neus "Here you go brother."
            else:
                neus "Here you go."
            mc "Thank you."    
            scene milf_event_kitchen_pregnant2_5 with dissolve  
            if incest_story:
                "You enjoy a delicious breakfast with your sister."
            else:  
                "You enjoy a delicious breakfast."
        "Ask for breast milk":
            mc "You're already producing breast milk, right?"
            scene milf_event_kitchen_pregnant2_6 with dissolve
            neus "Oh, I see where this is going, fine."
            scene milf_event_kitchen_pregnant2_7 with dissolve
            neus "But don't drink too much, you don't want to leave the baby without food."
            scene milf_event_kitchen_pregnant2_8 with w9
            play char1 groan_slow1
            neus "Uhhh."
            scene milf_event_kitchen_pregnant2_9 with dissolve
            play char3 groan_music
            neus "My nipples."
            if incest_story:
                neus "Don't stimulate them so much, brother."
            else:
                neus "Don't stimulate them so much."
            neus "You'll make my breast milk spill."
            scene milf_event_kitchen_pregnant2_10 with dissolve
            play char3 groan_music2
            neus "Uh!"
            neus "I'm being milked."
            neus "Like a dairy cow."
            if incest_story:
                neus "Remember your promise brother, you shouldn't drink it all."
            else:
                neus "Remember your promise, you shouldn't drink it all."
            stop char3 fadeout 1.0
            scene milf_event_kitchen_pregnant2_11 with dissolve
            mc "That was delicious, I never get tired of milking you, my little cow."
            scene milf_event_kitchen_pregnant2_12 with dissolve
            mc "What a waste."
            scene milf_event_kitchen_pregnant2_8 with dissolve
            neus "There's no need for you to do that."
            scene milf_event_kitchen_pregnant2_13 with dissolve
            play char1 groan_slow1
            neus "{e_heartbt2=FF0000}"
            scene milf_event_kitchen_pregnant2_14 with dissolve
            "You enjoy a good breakfast."
    jump milf_time_advances
label milf_event_kitchen_pregnant3:
    $ milf_event_kitchen_count_pregnant3=1
    scene milf_event_kitchen_pregnant3_0 with storyfx
    if incest_story:
        neus "Good morning, brother."
    else:
        neus "Good morning, darling."
    scene milf_event_kitchen_pregnant3_1 with dissolve
    neus "Wait a moment, I'll be done soon."
    scene milf_event_kitchen_pregnant3_2 with dissolve
    neus "Or do you want me to be your breakfast?"
    menu:
        "You":
            scene milf_event_kitchen_pregnant3_3 with dissolve
            neus "Hehe."
            play char1 groan1
            scene milf_event_kitchen_pregnant3_4 with dissolve
            neus "Uh!"
            scene milf_event_kitchen_pregnant3_5 with fadesex
            play char3 sex7
            neus "ha ha ha ha."
            if incest_story:
                neus "I missed this feeling brother, you know, it is very hard to reduce my dosage of pleasure."
            else:
                neus "I missed this feeling, you know, it is very hard to reduce my dosage of pleasure."
            mc "Did you miss it so much that you want to bake another one?"
            scene milf_event_kitchen_pregnant3_6 with fadesex
            neus "Hehe, that wouldn't be bad, but remember our promise."
            neus "Besides, I don't think my body can handle anymore."
            mc "Yes, I suppose that's true."
            if incest_story:
                mc "But that doesn't mean we stop having fun, right sister?"
            else:
                mc "But that doesn't mean we stop having fun, right?"
            scene milf_event_kitchen_pregnant3_5 with fadesex
            neus "Hehe, obviously."
            neus "I want you to fuck me a lot."
            neus "And fill me up, just to feel my stomach full."
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_kitchen_pregnant3_7 with dissolve
            play char1 climax1
            neus "Uh!"
            scene milf_event_kitchen_pregnant3_8 with dissolve
            if incest_story:
                neus "Brother, I missed this feeling so much."
            else:
                neus "I missed this feeling so much."
        "Not for now":
            scene milf_event_kitchen_pregnant3_9 with dissolve
            neus "I understand. Besides, the cookie dough is just about ready to go in the oven."
    play sound whoosh1
    scene milf_event_kitchen_pregnant3_10 with pushri
    mc "Your cookies are so delicious."
    scene milf_event_kitchen_pregnant3_11 with dissolve
    neus "Thank you, do you also want some ''milk''?"
    menu:
        "Breast milk":
            scene milf_event_kitchen_pregnant3_12 with dissolve
            ""
            scene milf_event_kitchen_pregnant3_13 with dissolve
            mc "Delicious."
            scene milf_event_kitchen_pregnant3_14 with dissolve
            play char1 penetration2
            neus "{e_heartbt2=FF0000}"(multiple=2)
            mc "But nothing beats drinking it straight from the source."(multiple=2)
            if incest_story:
                "You enjoy a delicious breakfast with your sister."
            else:
                "You enjoy a delicious breakfast."
        "Milk":
            scene milf_event_kitchen_pregnant3_15 with dissolve
            if incest_story:
                "You enjoy a delicious breakfast with your sister."
            else:
                "You enjoy a delicious breakfast."
    jump milf_time_advances
#----------------------------bath----------------------------
label milf_event_bath_control:
    if milf_event_bath_count_normal==0:
        $ milf_event_bath_count_normal=1
        jump milf_event_bath0
    elif milf_event_bath_count_normal==1:
        $ milf_event_bath_count_normal=2
        jump milf_event_bath1
    else:
        menu:
            "Event 0":
                jump milf_event_bath0
            "Event 1":
                jump milf_event_bath1
            "Leave":
                jump milf_rooms
label milf_event_bath0:
    play ambience bathtub fadeout 0.5 volume 0.3
    scene milf_event_bath0_0 with wet
    neus "This is so relaxing"
    neus "The atmosphere is so quiet"
    scene milf_event_bath0_1 with dissolve
    neus "And I can enjoy as much time as I want"
    mc "You sound like a grandma saying that, but I understand"
    scene milf_event_bath0_2 with dissolve
    neus "The old man speaks"
    scene milf_event_bath0_1 with dissolve
    mc "Oh, did that offend you?"
    scene milf_event_bath0_3 with dissolve
    if incest_story:
        neus "Hehe, I see you haven't lost the habit of trying to annoy me, brother"
    else:
        neus "Hehe, I see you haven't lost the habit of trying to annoy me, darling"
    neus "Although I suppose in a few years I'll be a grandma"
    neus "By the way, how long has it been since we did it in the bathroom?"
    scene milf_event_bath0_4 with dissolve
    if incest_story:
        mc "I guess since the last time auntie offered to take care of the kids"
    else:
        mc "I guess since the last time your mom offered to take care of the kids"
    scene milf_event_bath0_3 with dissolve
    neus "That's a long time, I suppose"
    scene milf_event_bath0_5 with dissolve
    if incest_story:
        neus "I want to continue enjoying this moment of peace, but I don't think we'll have the house to ourselves again. Don't you agree, brother?"
    else:
        neus "I want to continue enjoying this moment of peace, but I don't think we'll have the house to ourselves again. Don't you agree, darling?"
    scene milf_event_bath0_6 with dissolve
    play char3 sex6
    neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
    if incest_story:
        neus "As always, the compatibility of our bodies is great, brother"
    else:
        neus "As always, the compatibility of our bodies is great"
    neus "Or maybe we developed this compatibility by doing it for 17 years"
    neus "Well, it doesn't really matter, this feels amazing"
    neus "I'm about to cum"
    scene milf_event_bath0_7 with dissolve
    if incest_story:
        neus "You can cum inside brother, I want you to bathe my insides with your milk"
    else:
        neus "You can cum inside, I want you to bathe my insides with your milk"
    stop char3
    play charM cum1
    scene milf_event_bath0_8 with dissolve
    play char1 climax1
    neus "That was so good"
    neus "But not enough"
    scene milf_event_bath0_9 with dissolve
    neus "Next time, we should do it in the shower, on the floor, with the door open and all over the house"
    scene milf_event_bath0_10 with dissolve
    play ambience bathtub fadein 1.0 volume 0.3 if_changed
    neus "Although for now, I want some moments of relaxation"
    stop ambience fadeout 1.0
    scene black with dissolve
    "You enjoy your moments of peace"
    jump milf_time_advances
label milf_event_bath1:
    play ambience shower2 fadeout 0.3 fadein 0.3 volume 0.5
    scene milf_event_bath1_0 with wet
    play char3 sex7
    neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
    neus "Yes, that's exactly the spot."
    if is_milf_pregnant:
        if incest_story:
            neus "I love the kisses you give to my pregnant uterus, brother."
        else:
            neus "I love the kisses you give to my pregnant uterus."
    else:
        if incest_story:
            neus "I love the kisses you give to my uterus, brother."
        else:
            neus "I love the kisses you give to my uterus."
    scene milf_event_bath1_1 with dissolve
    neus "{bt=2}{=lust_style}oh oh oh oh{/bt}"
    neus "My uterus wants you to fill it."
    if incest_story:
        neus "Please fill my uterus, it's addicted to being drowned in my brother's semen."
    else:
        neus "Please fill my uterus, it's addicted to being drowned in semen."
    stop char3
    play charM cum1
    scene milf_event_bath1_2 with dissolve
    play char1 climax1
    neus "{sc=2}{=lust_style}Uh!{/sc}"
    if is_milf_pregnant:
        if incest_story:
            neus "I love the sensation of my fertilized eggs bathing in lots of my brother's semen." 
        else:
            neus "I love the sensation of my fertilized eggs bathing in lots of your semen." 
    else:
        if incest_story:
            neus "I love the sensation of my eggs drowning in lots of my brother's seed, so we can make incest babies."
        else:
            neus "I love the sensation of my eggs drowning in lots of your seed, so we can make babies."
    scene milf_event_bath1_3 with dissolve
    play ambience shower2 fadein 1.0 volume 0.5 if_changed
    neus "It's really hot."
    if is_milf_pregnant:
        play ambience shower2 fadein 1.0 volume 0.5 if_changed
        neus "If I weren't already pregnant, my eggs would have surely been fertilized again."
    stop ambience fadeout 1.0
    scene  black with dissolve
    if incest_story:
        "You enjoy a relaxing and exciting shower with your sister."
    else:
        "You enjoy a relaxing and exciting shower."
    jump milf_time_advances

label milf_event_bath_pregnant2:
    play ambience bathtub fadeout 0.4 fadein 0.2 volume 0.15
    $ milf_event_bath_count_pregnant2=1
    scene milf_event_bath_pregnant2_0 with wet
    neus "You really enjoy massaging my belly, huh?"
    neus "You like to caress the baby, huh?!"
    neus "Although this also relaxes me a lot, Hehe."
    menu:
        "Keep massaging":
            play ambience bathtub fadein 1.0 volume 0.15 if_changed
            if incest_story:
                "You enjoy a moment of relaxation with your sister."
            else:
                "You enjoy a moment of relaxation with [neusname]."
            stop ambience fadeout 1.0
            scene black with dissolve
            "..."
        "Massage her breasts":
            play char3 groan_music
            scene milf_event_bath_pregnant2_1 with dissolve
            neus "Uh."
            neus "I see that, as always, you don't miss your chance."
            if incest_story:
                neus "But I hope you remember that, because of you, brother, my nipples are very sensitive."
            else:
                neus "But I hope you remember that, because of you, my nipples are very sensitive."
            neus "Because of all those massages you used to give me."
            scene milf_event_bath_pregnant2_2 with dissolve
            neus "Oh, damn!"
            stop char3
            scene milf_event_bath_pregnant2_3 with dissolve
            play char1 climax1
            neus "I'm cumming {e_heartbt=FF0000}"
            scene milf_event_bath_pregnant2_4 with dissolve
            if incest_story:
                neus "Your massages are amazing, brother. {e_heartbt=FF0000}"
                scene milf_event_bath_pregnant2_5 with dissolve
                play ambience bathtub fadein 1.0 volume 0.15 if_changed
                "You enjoy a moment of relaxation while making your sister climax 2 more times."
            else:
                neus "Your massages are amazing. {e_heartbt=FF0000}"
                scene milf_event_bath_pregnant2_5 with dissolve
                play ambience bathtub fadein 1.0 volume 0.15 if_changed
                "You enjoy a moment of relaxation while making her climax 2 more times."
            stop ambience fadeout 1.0
            scene black with dissolve
            "..."
    jump milf_time_advances
label milf_event_bath_pregnant3:
    play ambience shower2 fadeout 0.4 fadein 0.2 volume 0.2
    $ milf_event_bath_count_pregnant3=1
    scene milf_event_bath_pregnant3_0 with wet
    play char3 sex7
    neus "{bt=1}{=lust_style}Ha ha ha ha{/bt}"
    if incest_story:
        neus "Yes, take all of me, brother"
        neus "Give lots of love to your sister, that you impregnated."
    else:
        neus "Yes, take all of me, darling"
        neus "Give me lots of love"
    neus "This is great, it makes me-"
    scene milf_event_bath_pregnant3_1 with dissolve
    neus "I'm cumming {e_heartbt=FF0000}"
    stop char3
    play charM cum1
    scene milf_event_bath_pregnant3_2 with dissolve
    play char1 climax1
    neus "{sc=2}{=lust_style}Uh!{/sc}"
    stop char1 fadeout 1.5
    scene milf_event_bath_pregnant3_3 with dissolve
    play ambience shower2 fadein 1.0 volume 0.2 if_changed
    neus "Phew {e_heartbt=FF0000}"
    stop ambience fadeout 1.0
    scene black with dissolve
    if incest_story:
        "You enjoy a pleasant shower with your sister"
    else:
        "You enjoy a pleasant shower"
    jump milf_time_advances
#----------------------------mc_evening----------------------------
label milf_event_mc_eve_control:
    if not(is_view_intro_milf_mc_eve):
        $ is_view_intro_milf_mc_eve=True
        scene milf_event_mc_eve0_0 with storyfx
        ""
        scene milf_event_mc_eve0_1 with dissolve
        if incest_story:
            "Your sister makes a gesture for you to come closer."
        else:
            "She makes a gesture for you to come closer."
        play sound whoosh1
        scene milf_event_mc_eve0_2 with pushri
        neus "Hehe, I love this position."
        scene milf_event_mc_eve0_3 with dissolve
        if incest_story:
            neus "By the way, what do you want to do, brother?"
        else:
            neus "By the way, what do you want to do?"
    scene milf_event_mc_eve0_4 with dissolve
    menu:
        "How are you?" if is_milf_pregnant:
            $ milf_is_view_name_baby=True
            scene milf_event_mc_eve1_0 with dissolve
            neus "Just the classic cravings"
            neus "Like ice cream with tuna or grapes with sausages"
            scene milf_event_mc_eve1_1 with dissolve
            mc "So everything is going well"
            scene milf_event_mc_eve1_2 with dissolve
            neus "Yes"
            scene milf_event_mc_eve1_3 with dissolve
            if incest_story:
                neus "Brother, I know we always plan the baby's name in the second trimester"
            else:
                neus "Darling, I know we always plan the baby's name in the second trimester"
            neus "When we already know the gender"
            scene milf_event_mc_eve1_4 with dissolve
            neus "But wouldn't you like to speculate about the gender?"
            neus "And what name you'd give?"
            scene milf_event_mc_eve1_5 with dissolve
            neus "I'll start"
            neus "I would like it to be a girl and her name to be Mary"
            menu:
                "Boy":
                    $ milfnamebaby = renpy.input(_("What would you like to name him?"), exclude='\\[{') 
                    $ milfnamebaby = milfnamebaby.title()
                    $ milfnamebaby = milfnamebaby.strip() 
                    $ milf_is_boy_girl=False
                    scene milf_event_mc_eve1_2 with dissolve
                    if milfnamebaby.lower() == firstname.lower():
                        neus "You want to name him after yourself?"
                    neus "Well, if it's a boy, we'll name him that"
                    scene milf_event_mc_eve1_6 with dissolve
                    neus "Although there are still a few months to go before that"
                    neus "What would you like to do now?"
                "Girl":
                    $ milfnamebaby = renpy.input(_("What would you like to name her?"), exclude='\\[{') 
                    $ milfnamebaby = milfnamebaby.title()
                    $ milfnamebaby = milfnamebaby.strip() 
                    $ milf_is_boy_girl=True
                    scene milf_event_mc_eve1_2 with dissolve
                    if (milfnamebaby.lower() == "mary") or (milfnamebaby.lower() == ""):
                        mc "I like the name mary"
                        neus "Well, I guess when the time comes we know what to call her"
                        neus "Although there are still a few months to go before that"
                        neus "What would you like to do now?"
                        $ milf_is_you_win_name=False  
                    else:
                        if milfnamebaby.lower() == neusname.lower():
                            neus "You want to name her after me?"
                        neus "Well, if it's a girl, I guess we'll have to compete again, to see who gets to name her."
                        mc "6-0"
                        scene milf_event_mc_eve1_7 with dissolve
                        neus "Enjoy it while you can hehe, because I'm going to take away that undefeated record from you"
                        scene milf_event_mc_eve1_8 with dissolve
                        if incest_story:
                            neus "Dar-ling bro-ther"
                        else:
                            neus "Dar-ling"
                        scene milf_event_mc_eve1_6 with dissolve
                        neus "Although there are still a few months to go before that"
                        neus "What would you like to do now?"
                        scene black with dissolve                  
                        menu(screen="custom_choice_long"):
                            "Who will win this competition?"
                            "[neusname] wins":
                                $ milf_is_you_win_name=False 
                            "[neusname] loses":
                                $ milf_is_you_win_name=True 
            jump milf_event_mc_eve_control
        "Blowjob":
            play sound whoosh1
            scene milf_event_mc_eve0_5 with pushdo
            neus "*Lick*"
            scene milf_event_mc_eve0_6 with dissolve
            play char3 deep_suck1
            neus "*Suck suck*"
            neus "*Sucking* lick lick"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_eve0_7 with dissolve
            neus "Mmm"
            scene milf_event_mc_eve0_8 with dissolve        
            play char1 ahegao3    
            neus "Ahhhh"           
            stop char1 fadeout 0.5 
            scene milf_event_mc_eve0_9 with dissolve
            neus "*Suck*"
            scene black with dissolve
            "..."
            jump milf_event_mc_eve_control
        "Sex":
            scene milf_event_mc_eve0_10 with dissolve
            ""
            play sound clothes
            scene milf_event_mc_eve0_11 with dissolve
            ""
            scene milf_event_mc_eve0_12 with dissolve
            ""
            scene milf_event_mc_eve0_13 with dissolve
            neus "Well, here I go"            
            scene milf_event_mc_eve0_14 with vpunch
            play char1 penetration3
            neus "Uh!"
            neus "I'm going to start moving now."
            scene milf_event_mc_eve0_15 with dissolve
            play char3 sex7
            neus "{bt=1}{=lust_style}Ha ha ha ha{/bt}"
            if incest_story:
                neus "I love riding you, brother"
            else:
                neus "I love riding you"
            neus "I can make your cock go even deeper"
            neus "And make it touch all my sensitive spots"
            neus "Which makes me reach climax even faster"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_eve0_16 with dissolve
            play char1 climax1
            neus "{sc=2}{=lust_style}Ah!{/sc}"
            play char3 breathing1
            scene milf_event_mc_eve0_17 with dissolve            
            neus "*Breathing heavily* Ufff"
            play ambience morning_sounds if_changed
            neus "That felt amazing"
            stop char3 fadeout 1.5
            stop ambience fadeout 1.0
            scene black with dissolve
            "..."
            jump milf_time_advances
        "Leave":
            jump milf_rooms
    jump milf_event_mc_eve_control

label milf_event_mc_eve_control_pregnant2:
    scene milf_event_mc_eve_pregnant2_0 with storyfx
    menu:        
        "Hike in the park (Picnic)":            
            mc "How about we take a walk in the park?"
            scene milf_event_mc_eve_pregnant2_1 with dissolve
            neus "That sounds great, and what if we also have a small picnic?"
            mc "Deal!"
            play sound whoosh1
            scene milf_event_mc_eve_pregnant2_2 with pushri
            ""
            play sound whoosh1
            scene milf_event_mc_eve_pregnant2_3 with pushle
            ""
            play sound whoosh1
            scene milf_event_mc_eve_pregnant2_4 with pushu
            if incest_story:
                neus "Brother, this seems like a nice spot."
            else:
                neus "This seems like a nice spot."
            scene milf_event_mc_eve_pregnant2_5 with dissolve
            neus "It seems like not many people pass by here."            
            scene milf_event_mc_eve_pregnant2_6 with dissolve
            neus "This is so relaxing."  
            if incest_story:
                neus "Brother, I know we talked about reducing our sexual activity for the second trimester of the pregnancy."
            else:         
                neus "Honey, I know we talked about reducing our sexual activity for the second trimester of the pregnancy."
            scene milf_event_mc_eve_pregnant2_7 with dissolve
            neus "But it would be exciting to do it outdoors, don't you think?"
            menu:
                "That sounds great":
                    scene milf_event_mc_eve_pregnant2_8 with w9
                    mc "I think this place is perfect."
                    play sound whoosh1
                    scene milf_event_mc_eve_pregnant2_9 with pushle
                    if incest_story:
                        neus "Brother, I can't wait anymore, I want you to fuck me."
                    else:
                        neus "Honey, I can't wait anymore, I want you to fuck me."
                    play char1 penetration1
                    scene milf_event_mc_eve_pregnant2_10 with dissolve
                    neus "Uh!"
                    play char3 sex7
                    scene milf_event_mc_eve_pregnant2_11 with dissolve                    
                    neus "{bt=1}{=lust_style}Ha ha ha{/bt}"
                    neus "This is so exciting."
                    neus "The risk of someone catching us turns me on so much."
                    scene milf_event_mc_eve_pregnant2_12 with dissolve
                    if incest_story:
                        neus "But what excites me even more is my brother filling me with his semen"
                    else:
                        neus "But what excites me even more is you filling me with your semen"
                    neus "And walking back home with my vagina full"
                    neus "Just thinking about it is pushing me to the edge of orgasm."
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene milf_event_mc_eve_pregnant2_13 with dissolve
                    play char1 climax1
                    neus "Mmm."
                    stop char1 fadeout 1.5
                    scene milf_event_mc_eve_pregnant2_14 with dissolve
                    play ambience morning_sounds if_changed
                    if incest_story:
                        neus "That was amazing, brother."
                        stop ambience fadeout 1.0
                        scene black with dissolve
                        "After picking up the picnic things, you return home with your sister."
                    else:
                        neus "That was amazing."
                        stop ambience fadeout 1.0
                        scene black with dissolve
                        "After picking up the picnic things, you both return home."
                "Too risky":
                    scene milf_event_mc_eve_pregnant2_15 with dissolve
                    play ambience morning_sounds if_changed
                    neus "You're right."
                    stop ambience fadeout 1.0
                    scene black with dissolve
                    if incest_story:
                        "After enjoying the picnic, you return home with your sister."
                    else:
                        "After enjoying the picnic, you both return home."
            jump milf_time_advances
        "Buttjob":
            play sound whoosh1
            scene milf_event_mc_eve_pregnant2_16 with pushup
            ""
            scene milf_event_mc_eve_pregnant2_17 with dissolve
            neus "You love my ass, huh?"
            if incest_story:
                mc "Yes, I love your chubby little butt, sister"
            else:
                mc "Yes, I love your chubby little butt"
            scene milf_event_mc_eve_pregnant2_18 with dissolve
            neus "Hehe"
            scene milf_event_mc_eve_pregnant2_19 with dissolve
            play char3 handjob2
            neus "I guess, as usual, I'll have to make you cum with my little ass"
            neus "I'm going to massage your cock with my thick glutes"
            neus "Come on, come on, cum and cover my cute ass with your semen"
            if incest_story:
                neus "Mark your sister's ass as yours once again"
            else:
                neus "Mark your wife's ass as yours once again"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_eve_pregnant2_20 with dissolve
            neus "Oh"
            scene milf_event_mc_eve_pregnant2_21 with dissolve
            neus "Hehe, it seems like I've gotten really good at my assjob"
            scene black with dissolve
            "..."
            jump milf_event_mc_eve_control_pregnant2
        "Leave":
            jump milf_rooms
label milf_event_mc_eve_control_pregnant3:
    scene milf_event_mc_eve_pregnant3_0 with storyfx
    menu:
        "Cow bikini"(milf_outfit_is_active_outfit):
            if not(is_view_intro_milf_outfit_cow):
                $ is_view_intro_milf_outfit_cow=True
                scene milf_event_mc_eve_pregnant3_outfit_cow_2 with dissolve
                neus "Hehe, let me see that gift."
                scene milf_event_mc_eve_pregnant3_outfit_cow_3 with dissolve
                if incest_story:
                    neus "I have nothing against it, brother, but I don't think someone my age should wear this."
                else:
                    neus "I have nothing against it, but I don't think someone my age should wear this."
                scene milf_event_mc_eve_pregnant3_outfit_cow_4 with dissolve
                neus "It's a bit embarrassing."
                mc "Well, I think it looks great on you."
                scene milf_event_mc_eve_pregnant3_outfit_cow_5 with dissolve
                mc "My cute little cow."
                mc "You could be my milk cow."
                scene milf_event_mc_eve_pregnant3_outfit_cow_6 with dissolve
                neus "My breasts might hurt a bit."
                scene milf_event_mc_eve_pregnant3_outfit_cow_7 with dissolve
                neus "Would you like to milk this little cow?"
            else:
                scene milf_event_mc_eve_pregnant3_12 with dissolve 
                neus "Okey"
            $ is_milf_outfit_cow_nomal=False
            jump milf_event_mc_eve_control_pregnant3_outfit_cow
        "Thighjob":
            scene milf_event_mc_eve_pregnant3_1 with dissolve
            ""
            scene milf_event_mc_eve_pregnant3_8 with dissolve
            if incest_story:
                neus "Hehe, do you like my pregnant thighs brother?"
            else:
                neus "Hehe, do you like my pregnant thighs?"
            scene milf_event_mc_eve_pregnant3_9 with dissolve
            play char3 handjob2
            mc "Your thighs are so soft."
            neus "Remember that you can't impregnate my thighs, right?"
            mc "Yes, that's very unfortunate."
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_eve_pregnant3_10 with dissolve
            neus "Oh."
            scene milf_event_mc_eve_pregnant3_11 with dissolve
            if incest_story:
                neus "As usual, you like to claim my thighs as yours, don't you? Brother."
            else:
                neus "As usual, you like to claim my thighs as yours, don't you? Sweetheart."
            neus "With all this cum, surely my thighs and belly would get pregnant"
            scene milf_event_mc_eve_pregnant3_11_1 with dissolve
            neus "Although my belly is already impregnated, hehe"
            scene black with dissolve
            "She cleans herself up"
            jump milf_event_mc_eve_control_pregnant3
        "Titjob":
            scene milf_event_mc_eve_pregnant3_12 with dissolve
            if incest_story:
                neus "So you want to feel your sister's breasts that are full of breast milk, huh?"
                scene milf_event_mc_eve_pregnant3_13 with dissolve  
                neus "How do my breasts feel, brother?"
            else:          
                neus "So you want to feel my breasts that are full of breast milk, huh?"
                scene milf_event_mc_eve_pregnant3_13 with dissolve  
                neus "How do my breasts feel?"
            mc "Great."
            scene milf_event_mc_eve_pregnant3_14 with dissolve
            play char3 handjob1
            neus "This reminds me of when we were younger and my little breasts couldn't fully cover your cock."
            neus "Although, they're not that big now either, they're average for my age."
            mc "*Mocking tone* That bothers you."
            if incest_story:
                neus "I see what you're trying to do, brother, but I don't really care about the size of my breasts much anymore."
            else:
                neus "I see what you're trying to do, darling, but I don't really care about the size of my breasts much anymore."
            neus "Besides, I know you prefer another part of my body."
            neus "Not to mention the fact that at this age, if I had giant breasts, I would have back problems, hehe."
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_eve_pregnant3_15 with dissolve
            neus "Oh."
            scene milf_event_mc_eve_pregnant3_16 with dissolve
            neus "You like my breasts, huh? There's a lot of semen."
            scene black with dissolve
            "She cleans herself up"
            jump milf_event_mc_eve_control_pregnant3
        "Anal":
            scene milf_event_mc_eve_pregnant3_1 with dissolve
            ""
            scene milf_event_mc_eve_pregnant3_2 with dissolve 
            neus "Hehe, well, it's time to eat this cock"
            play char1 penetration1
            scene milf_event_mc_eve_pregnant3_3 with dissolve             
            neus "Uh! {e_heartbt=FF0000}"
            scene milf_event_mc_eve_pregnant3_4 with fadesex 
            play char3 fx_cowgirl1
            neus "{bt=1}{=lust_style}Ha ha ha{/bt}"
            if incest_story:
                neus "Do you like watching your sister's ass bounce?"
            else:
                neus "Do you like watching my ass bounce?"
            neus "Because I love jumping on your cock"
            neus "And making you cum with my movements"
            neus "Although, I think I'm getting close to climaxing"            
            scene milf_event_mc_eve_pregnant3_5 with dissolve             
            neus "I'm cumming {e_heartbt=FF0000}"
            stop char3
            play charM cum1
            scene milf_event_mc_eve_pregnant3_6 with dissolve 
            play char1 climax1
            neus "{sc=2}{=lust_style}Mmm!{/sc}"
            stop char1 fadeout 1.5
            scene milf_event_mc_eve_pregnant3_7 with dissolve 
            play ambience morning_sounds if_changed
            if incest_story:
                neus "Ugh, my ass is so full, does my brother also want to impregnate my ass, hehe?"
            else:
                neus "Ugh, my ass is so full, do you also want to impregnate my ass, hehe?"
            stop ambience fadeout 1.0
            scene black with dissolve
            "She cleans herself up"
            jump milf_time_advances
        "Leave":
            jump milf_rooms
    jump milf_event_mc_eve_control_pregnant3
label milf_event_mc_eve_control_pregnant3_outfit_cow:
    scene milf_event_mc_eve_pregnant3_outfit_cow_0 with storyfx
    menu:
        "Regular outfit":
            scene milf_event_mc_eve_pregnant3_outfit_cow_1 with dissolve
            neus "Okey"
            $ is_milf_outfit_cow_nomal=True
            jump milf_event_mc_eve_control_pregnant3
        "Milk":
            scene milf_event_mc_eve_pregnant3_outfit_cow_1 with dissolve
            neus "So you're going to milk my udders"
            scene milf_event_mc_eve_pregnant3_outfit_cow_8 with dissolve
            neus "Then come here"
            scene milf_event_mc_eve_pregnant3_outfit_cow_9 with fadesex
            play char3 groan_music
            neus "This is really turning me on"
            neus "Yes, yes, milk me, treat me like a little cow that only serves to produce milk"
            neus "This is so intense that just by being milked I'm..."
            scene milf_event_mc_eve_pregnant3_outfit_cow_10 with dissolve
            neus "I'm cumming!"
            stop char3
            scene milf_event_mc_eve_pregnant3_outfit_cow_11 with dissolve
            play char1 climax2
            neus "Mooooo"
            stop char1 fadeout 1.5
            scene milf_event_mc_eve_pregnant3_outfit_cow_12 with dissolve
            mc "I hadn't heard of cows climaxing from being milked"
            mc "You're a horny cow"
            scene milf_event_mc_eve_pregnant3_outfit_cow_13 with dissolve
            neus "It's your fault for making it so intense"
            menu:
                "More":
                    play char1 groan1
                    scene milf_event_mc_eve_pregnant3_outfit_cow_14 with dissolve
                    if incest_story:
                        neus "Brother, wait, wait, I'm still sensitive"
                    else:
                        neus "Wait, wait, I'm still sensitive"
                    scene milf_event_mc_eve_pregnant3_outfit_cow_15 with w21
                    play ambience morning_sounds if_changed
                    if incest_story:
                        "You let your sister rest after making her climax 2 more times"
                    else:
                        "You let her rest after making her climax 2 more times"
                    stop ambience fadeout 1.0
                    scene black with dissolve
                    "..."
                    jump milf_time_advances
                "Leave":
                    scene black with dissolve
                    "..."   
        "Sex":
            scene milf_event_mc_eve_pregnant3_outfit_cow_1 with dissolve
            neus "{e_heartbt2=FF0000}" 
            scene milf_event_mc_eve_pregnant3_outfit_cow_16 with dissolve
            if incest_story:
                neus "Brother, I can't wait any longer, please make love to me."
            else:
                neus "I can't wait any longer, please make love to me."
            scene milf_event_mc_eve_pregnant3_outfit_cow_17 with dissolve
            neus "Uh, yes!"
            if incest_story:
                mc "Did you need it that badly, little sister?"
            else:
                mc "Did you need it that badly?"
            scene milf_event_mc_eve_pregnant3_outfit_cow_18 with fadesex
            play char3 sex2
            neus "Yes, I desired it a lot."
            neus "Because of the promise we made."
            neus "I have been suffering from withdrawal symptoms."
            if incest_story:
                neus "All the time I wanted to devour my brother's cock, which is only mine."
            else:
                neus "All the time I wanted to devour my husband's cock, which is only mine."
            neus "And for him to fill me with a lot of his cum."
            scene milf_event_mc_eve_pregnant3_outfit_cow_19 with dissolve
            if incest_story:
                neus "I need it, brother."
            else:
                neus "I need it."
            scene milf_event_mc_eve_pregnant3_outfit_cow_18 with fadesex
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_eve_pregnant3_outfit_cow_20 with flash
            play char1 climax2
            neus "Moo!"
            scene milf_event_mc_eve_pregnant3_outfit_cow_21 with dissolve
            stop char1 fadeout 1.5
            play ambience morning_sounds if_changed
            neus "I have missed this so much."
            stop ambience fadeout 1.0
            scene black with dissolve
            "..." 
            jump milf_time_advances
        "Leave":
                jump milf_rooms
    jump milf_event_mc_eve_control_pregnant3_outfit_cow
#----------------------------mc_night----------------------------
label milf_event_mc_night_control:    
    scene milf_event_mc_night0_0 with dissolve
    if is_milf_pregnant:
        $ menu_text = ""
    else:
        $ menu_text = " (pregnancy)"
    menu:
        "Sleep":
            play ambience night_ambience volume 0.1 if_changed
            scene milf_event_mc_night0_1 with dissolve
            ""
            stop ambience fadeout 1.0
            scene black with eyeclose
            ""           
            scene milf_event_mc_night0_2 with eyeopen            
            jump milf_sleeping_event
        "Sex[menu_text]":
            scene milf_event_mc_night0_3 with dissolve
            neus "Hehe"
            scene milf_event_mc_night0_4 with dissolve
            neus "These boxers are in the way."
            play sound whoosh1
            scene milf_event_mc_night0_5 with pushu
            if incest_story:
                neus "Well, let's start, big brother"
            else:
                neus "Well, let's start, darling"
            scene milf_event_mc_night0_6 with fadesex
            play char3 sex7
            neus "{bt=1}{=lust_style}ha ha ha ha{/bt}"
            neus "This bedtime activity is my favorite"
            if incest_story:
                neus "I love devouring my brother's cock"
            else:
                neus "I love devouring your cock"
            mc "You're a pro at it"
            scene milf_event_mc_night0_7 with dissolve
            if incest_story:
                neus "Hehe, with 17 years of experience riding my brother's cock, it’s only natural."
            else:
                neus "Hehe, with 17 years of experience riding your cock, it’s only natural."
            neus "My pussy has the perfect shape for your cock"
            neus "Just by putting your cock inside, I'm able to cum"
            neus "And right now, I'm..."
            scene milf_event_mc_night0_8 with dissolve             
            neus "I'm cumming"
            scene milf_event_mc_night0_6 with dissolve
            neus "Cum inside, please"
            if not is_milf_pregnant:
                if incest_story:
                    neus "Flood all my eggs and impregnate me brother"
                else:
                    neus "Flood all my eggs and impregnate me"
            stop char3
            play charM cum1
            scene milf_event_mc_night0_9 with dissolve
            play char1 climax2
            neus "{sc=2}{=lust_style}Uh!{/sc}"
            stop char1 fadeout 2.0
            scene milf_event_mc_night0_10 with dissolve
            neus "That was amazing"
            if is_milf_pregnant:
                scene milf_event_mc_night0_34 with dissolve
                neus "Although, we should probably get some rest now."
                scene milf_event_mc_night0_1 with dissolve
                ""
                scene black with eyeclose
                ""               
                scene milf_event_mc_night0_2 with eyeopen  
                jump milf_sleeping_event # Pregnant end scene

            scene milf_event_mc_night0_11 with dissolve
            neus "By the way, I feel like getting pregnant by you once again"
            neus "I swear, this will be the last time I ask you"
            scene milf_event_mc_night0_12 with dissolve
            if incest_story:
                neus "So, what do you say, brother?"
                neus "Do you want to impregnate your little sister one more time?"
            else:
                neus "So, what do you say, darling?"
                neus "Do you want to impregnate your wife one more time?"
            menu:
                "Pregnancy"(set_active_pregnancy):
                    scene milf_event_mc_night0_13 with dissolve
                    neus "Oh, we're going to do it in this position"
                    scene milf_event_mc_night0_14 with dissolve
                    mc "I'm going to start now"
                    scene milf_event_mc_night0_15 with dissolve
                    play char1 penetration1
                    neus "Uh!"
                    if incest_story:
                        neus "Brother, your cock is kissing my uterus"
                    else:
                        neus "Your cock is kissing my uterus"
                    scene milf_event_mc_night0_16 with dissolve
                    play char3 sex7
                    neus "ha ha ha"
                    neus "In this position, your cock gives me so much love"
                    neus "I love it"
                    scene milf_event_mc_night0_17 with dissolve
                    if incest_story:
                        neus "Please release all your cum inside me brother"                 
                        neus "Drown all your sister's eggs"
                    else:
                        neus "Please release all your cum inside me"                    
                        neus "Drown all my eggs"
                    neus "I want you to leave me with a big belly"
                    scene milf_event_mc_night0_16 with dissolve
                    neus "I want to have your child"
                    neus "Fill my belly a lot"
                    stop char3
                    play charM cum1
                    scene milf_event_mc_night0_18 with dissolve
                    play char1 climax2
                    neus "Uh!"
                    stop char1 fadeout 2.0
                    scene milf_event_mc_night0_19 with dissolve
                    neus "My belly is very full"
                    scene milf_event_mc_night0_20 with dissolve
                    if incest_story:
                        mc "But it's not enough, right sister?"
                    else:
                        mc "But it's not enough, right?"
                    scene milf_event_mc_night0_21 with dissolve
                    play char1 penetration2
                    neus "Uh!"
                    scene milf_event_mc_night0_22 with dissolve
                    neus "How intense"
                    scene milf_event_mc_night0_23 with dissolve
                    if incest_story:
                        neus "Despite all these years, I still can't keep up with you, brother"
                    else:
                        neus "Despite all these years, I still can't keep up with you, darling"
                    play charM cum1
                    scene milf_event_mc_night0_24 with dissolve
                    play char1 climax2
                    neus "Uh!"
                    stop char1 fadeout 2.0
                    scene milf_event_mc_night0_25 with dissolve
                    neus "I'm so full of your semen that it's overflowing"
                    play ambience morning_sounds fadein 0.5
                    scene milf_event_mc_night0_26 with dissolve
                    neus "Just 5 more minutes"
                    scene milf_event_mc_night0_27 with dissolve
                    neus "..."
                    scene milf_event_mc_night0_28 with dissolve
                    neus "Thank you"
                    scene black with dissolve
                    ""
                    scene milf_event_mc_night0_29 with snow1
                    if incest_story:
                        neus "Hehe, look brother!"
                    else:
                        neus "Hehe, look!"
                    scene milf_event_mc_night0_30 with dissolve
                    neus "Although now I have cravings"
                    scene milf_event_mc_night0_31 with dissolve
                    neus "See you in the kitchen"  
                    $ is_milf_pregnant=True
                    $ milf_is_pregnancy_stages=True                  
                    jump milf_sleeping_event
                "Postpone":
                    scene milf_event_mc_night0_32 with dissolve
                    neus "Hmm, I understand."
                    scene milf_event_mc_night0_33 with dissolve
                    neus "But if you change your mind, just let me know, I'm always ready."
                    scene milf_event_mc_night0_34 with dissolve
                    neus "Although for now, it's better to rest."
                    scene milf_event_mc_night0_1 with dissolve
                    play ambience night_ambience volume 0.1 if_changed
                    ""
                    stop ambience fadeout 1.0
                    scene black with eyeclose
                    ""           
                    scene milf_event_mc_night0_2 with eyeopen                    
                    jump milf_sleeping_event
        "Leave":
            jump milf_rooms
    jump milf_event_mc_night_control
label milf_event_mc_night_control_pregnant2:
    scene milf_event_mc_night2_0 with dissolve
    menu:
        "Sleep":
            scene milf_event_mc_night2_1 with dissolve
            play ambience night_ambience volume 0.1 if_changed
            ""
            stop ambience fadeout 1.0
            scene black with eyeclose
            ""           
            scene milf_event_mc_night0_2 with eyeopen            
            jump milf_sleeping_event
        "Eating pussy":
            scene milf_event_mc_night2_2 with dissolve
            neus "Hehe"
            scene milf_event_mc_night2_3 with dissolve
            ""
            scene milf_event_mc_night2_4 with dissolve
            mc "Well, let's start."
            scene milf_event_mc_night2_5 with dissolve
            play char3 groan_music
            neus "{bt=1}{=lust_style}Ha ha ha ha{/bt}"
            neus "Why are you always so good at working your tongue?"
            neus "Damn, you're touching all my sensitive spots."
            if incest_story:
                neus "Your tongue is so deep inside me brother."
            else:
                neus "Your tongue is so deep."
            neus "Don't move it so fast."
            stop char3 fadeout 1.0
            scene milf_event_mc_night2_6 with dissolve
            neus "I'm cumming {e_heartbt=FF0000}"
            play char1 climax1
            scene milf_event_mc_night2_7 with dissolve
            neus "Uh!"
            scene milf_event_mc_night2_8 with dissolve
            if incest_story:
                neus "Phew, that was great. Thank you, brother."
            else:
                neus "Phew, that was great. Thank you, honey."
            menu:
                "More":
                    scene milf_event_mc_night2_9 with dissolve
                    if incest_story:
                        neus "Brother, wait, wait, I'm still sensitive."
                    else:
                        neus "Wait, wait, I'm still sensitive."
                    scene milf_event_mc_night2_10 with dissolve
                    neus "If you keep this up, you'll make me completely lose my mind from pleasure."                    
                    scene black with dissolve
                    if incest_story:
                        "You make your sister climax 3 more times."
                    else:
                        "You make her climax 3 more times."
                    play char1 climax2
                    scene milf_event_mc_night2_11 with dissolve                    
                    ""
                    stop char1 fadeout 1.5
                    scene black with dissolve
                    "..."
                    scene milf_event_mc_night2_1 with dissolve
                    play ambience night_ambience volume 0.1 if_changed
                    ""
                    stop ambience fadeout 1.0
                    scene black with eyeclose
                    ""           
                    scene milf_event_mc_night0_2 with eyeopen            
                    jump milf_sleeping_event 
                "Leave":
                    scene black with dissolve
                    "..."
                    jump milf_event_mc_night_control_pregnant2               
        "Thighjob":
            scene milf_event_mc_night2_2 with dissolve
            ""
            scene milf_event_mc_night2_12 with dissolve 
            neus "So you're going to fuck my thighs"
            scene milf_event_mc_night2_13 with dissolve
            play char3 handjob2
            if incest_story:
                neus "How do my thighs feel, brother?"
            else:
                neus "How do my thighs feel?"
            mc "Great"
            neus "So you're also going to mark my thighs as yours again, hehe"
            neus "Cover them with lots of your milk"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_night2_14 with flash
            ""
            scene milf_event_mc_night2_15 with dissolve
            neus "With all this milk, my thighs could also get pregnant, hehe"
            scene black with dissolve
            "She cleans herself"
        "Leave":
            jump milf_rooms
    jump milf_event_mc_night_control_pregnant2
label milf_event_mc_night_control_pregnant3:
    scene milf_event_mc_night3_0 with dissolve
    menu:
        "Sleep":
            play ambience night_ambience volume 0.1 if_changed
            scene milf_event_mc_night3_1 with dissolve
            ""
            stop ambience fadeout 1.0
            scene black with eyeclose
            ""           
            scene milf_event_mc_night0_2 with eyeopen            
            jump milf_sleeping_event
        "Footjob":
            scene milf_event_mc_night3_2 with dissolve
            if incest_story:
                neus "So you want a footjob from your sister, huh? Alright."
            else:
                neus "So you want a footjob, huh? Alright."
            scene milf_event_mc_night3_7 with dissolve
            neus "I'm going to start now."
            scene milf_event_mc_night3_8 with dissolve
            play char3 handjob1
            if incest_story:
                neus "How do my feet feel, brother?"
            else:
                neus "How do my feet feel?"
            mc "Good, actually I think you've improved a lot."
            if incest_story:
                neus "Well, thanks to my big brother, I've had plenty of practice."
            else:
                neus "Well, thanks to someone, I've had plenty of practice."
            mc "Haha."
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_night3_9 with dissolve
            neus "{e_heartbt=FF0000}"
            scene milf_event_mc_night3_10 with dissolve
            neus "Wow, you released a really big load."
            scene black with dissolve
            "She cleans herself up"
            jump milf_event_mc_night_control_pregnant3
        "Sex":
            scene milf_event_mc_night3_2 with dissolve
            neus "Hehe, I've been waiting for this"
            scene milf_event_mc_night3_3 with dissolve
            if incest_story:
                neus "I can't wait any longer, brother {e_heartbt=FF0000}"
            else:
                neus "I can't wait any longer, darling {e_heartbt=FF0000}"
            scene milf_event_mc_night3_4 with fadesex
            play char3 sex2
            neus "I have wanted this so badly"
            neus "{bt=1}{=lust_style}Oh oh oh{/bt}"
            if incest_story:
                neus "Yes, yes, please, keep going brother, fuck me a lot."
            else:
                neus "Yes, yes, please, keep going, fuck me a lot."
            neus "I want you to fill me with your cum."
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene milf_event_mc_night3_5 with dissolve
            play char1 climax2
            neus "{bt=1}{=lust_style}Uh!{/bt}{e_heartbt=FF0000}"
            stop char1 fadeout 1.5
            scene milf_event_mc_night3_6 with dissolve
            ""
            play ambience night_ambience volume 0.1 if_changed
            scene milf_event_mc_night3_1 with dissolve
            ""
            stop ambience fadeout 1.0
            scene black with eyeclose
            ""           
            scene milf_event_mc_night0_2 with eyeopen            
            jump milf_sleeping_event
        "Leave":
            jump milf_rooms
    jump milf_event_mc_night_control_pregnant3
label milf_true_ending:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    stop ambience fadeout 1.0
    $ renpy.music.set_volume(0.2, channel='music')
    play music a_stray_cat_aimed_for_space fadein 1.5
    scene black with dissolve
    "With the passage of time, your eleventh child was born."
    scene milf_true_ending0 with dissolve
    ""
    if milf_is_view_name_baby:
        if milf_is_boy_girl:
            if (milfnamebaby.lower() == "mary") or (milfnamebaby.lower() == ""):
                "You both agreed to name your daughter [milfnamebaby]."
            elif milf_is_you_win_name:
                scene milf_true_ending1 with snow1
                neus "..."(multiple=2)
                "7-0"(multiple=2)                
                "The name of your daughter was [milfnamebaby]."
            else:
                scene milf_true_ending2 with snow1      
                neus "Hehe"(multiple=2)
                "6-1"(multiple=2)
                "The name of your daughter was Mary."
        else:
            "The name of your daughter was Mary."
    $ renpy.music.set_volume(0.6,delay=2.5, channel='music')
    scene black with dissolve    
    if incest_story:
        "You enjoyed many fun moments with your sister"
    else:
        "You enjoyed many fun moments with [neusname]"
    scene milf_true_ending3_1 with dissolve
    ""
    show milf_true_ending3_2  at rotate_15 with dissolve
    ""
    show milf_true_ending3_3  at rotate_15_degrees with dissolve
    ""  
    $ renpy.music.set_volume(0.3,delay=1.5, channel='music')  
    show milf_true_ending3_4 at rotate_15 with dissolve      
    ""
    show milf_true_ending4 with zoomin   
    play music escort fadeout 0.5
    ""
    hide milf_true_ending3_1
    hide milf_true_ending3_2 
    hide milf_true_ending3_3 
    hide milf_true_ending3_4 
    neus "How quickly time passes."    
    scene milf_true_ending5 with dissolve
    neus "I remember when I used to contain my feelings."
    scene milf_true_ending6 with dissolve
    mc "When you were obsessed with me... have you let go those obsessive feelings then?"
    scene milf_true_ending7 with dissolve
    neus "Maybe not completely, but I’ve learned to manage them better."
    neus "I do question a lot, though. I see now that my feelings were toxic, and I wish I’d handled them better."
    neus "Back then, it felt like it didn’t matter—but all it did was make things harder for both of us."
    scene milf_true_ending8 with dissolve
    mc "Maybe, although I didn't handle things in the best way either."
    scene milf_true_ending9 with dissolve
    neus "I wish we took things slower and made it more special."
    scene milf_true_ending10 with dissolve
    mc "I'm know, I'm sorry. I have apologized to you many times for that."   
    scene milf_true_ending11 with dissolve   
    mc "Besides, part of that could be someone else's fault."
    scene milf_true_ending12 with dissolve
    neus "*Ignoring comment* Haha."
    scene milf_true_ending13 with dissolve
    neus "Despite how weird those times were, they were a lot of fun."
    scene milf_true_ending14 with dissolve
    mc "They were."
    scene milf_true_ending15 with pushuplong  
    $ renpy.music.set_volume(0.05,delay=2.0, channel='music')  
    python:
        achievement.grant("True_Ending_1")
        achievement.sync()           
    if not ending_4_obtained:
        $ endings_obtained_count += 1
        $ ending_4_obtained = True
    centered "{color=#cc0066}{size=+200}True Ending 1" 
    play sound glass_breaking   volume 0.1
    granddaughter "Grandma, someone broke a vase."
    neus "Hehe, it seems they're still just as mischievous."
    neus "Let's see who was guilty this time!"    
    scene black with snow1
    $ renpy.music.set_volume(0.2,delay=1.0, channel='music')   
    "You have obtained {color=#cc0066}Ending 4{/color} out of {color=#cc0066}[available_endings] possible endings{/color}."
    stop music fadeout 3.0
    centered "{color=#cc0066}{size=+100}Thank you for playing." 
    $ renpy.music.set_volume(1.0,delay=1.0, channel='music')      
    $renpy.end_replay()
    jump menu_milf_true_ending
label menu_milf_true_ending:  
    scene black        
    menu(screen="custom_choice_long"):
        "Continue":            
            jump milf_rooms 
        "Main Menu":
            menu(screen="custom_choice_long"):
                "Are you sure you want to go to the main menu?"
                "Yes":
                    $ MainMenu(confirm=False)()
                "No":
                    jump menu_milf_true_ending
