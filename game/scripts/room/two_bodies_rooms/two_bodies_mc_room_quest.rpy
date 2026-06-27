image two_bodies_kitchen0_1 = DynamicAnimation(
["rooms/tb/kitchen/two_bodies_kitchen0_1_0.webp",
"rooms/tb/kitchen/two_bodies_kitchen0_1_1.webp",
"rooms/tb/kitchen/two_bodies_kitchen0_1_2.webp",])
image two_bodies_bath0_1 = DynamicAnimation(
["rooms/tb/bath/two_bodies_bath0_1_0.webp",
"rooms/tb/bath/two_bodies_bath0_1_1.webp",
"rooms/tb/bath/two_bodies_bath0_1_2.webp",])
image two_bodies_mc_evening0_2 = DynamicAnimation(
["rooms/tb/mc/two_bodies_mc_evening0_2_0.webp",
"rooms/tb/mc/two_bodies_mc_evening0_2_1.webp",
"rooms/tb/mc/two_bodies_mc_evening0_2_2.webp",])
image two_bodies_mc_evening0_15 = DynamicAnimation(
["rooms/tb/mc/two_bodies_mc_evening0_15_0.webp",
"rooms/tb/mc/two_bodies_mc_evening0_15_1.webp",
"rooms/tb/mc/two_bodies_mc_evening0_15_2.webp",])
image two_bodies_mc_night0_5 = DynamicAnimation(
["rooms/tb/mc/two_bodies_mc_night0_5_0.webp",
"rooms/tb/mc/two_bodies_mc_night0_5_1.webp",
"rooms/tb/mc/two_bodies_mc_night0_5_2.webp",])
image tb_kitchen_pregnant2_1 = DynamicAnimation(
["rooms/tb/kitchen/tb_kitchen_pregnant2_1_0.webp",
"rooms/tb/kitchen/tb_kitchen_pregnant2_1_1.webp",
"rooms/tb/kitchen/tb_kitchen_pregnant2_1_2.webp",])
image tb_bath_pregnant2_1 = DynamicAnimation(
["rooms/tb/bath/tb_bath_pregnant2_1_0.webp",
"rooms/tb/bath/tb_bath_pregnant2_1_1.webp",
"rooms/tb/bath/tb_bath_pregnant2_1_2.webp",])
image tb_evening_pregnant2_1 = DynamicAnimation(
["rooms/tb/mc/tb_evening_pregnant2_1_0.webp",
"rooms/tb/mc/tb_evening_pregnant2_1_1.webp",
"rooms/tb/mc/tb_evening_pregnant2_1_2.webp",])
image tb_night_pregnant2_1 = DynamicAnimation(
["rooms/tb/mc/tb_night_pregnant2_1_0.webp",
"rooms/tb/mc/tb_night_pregnant2_1_1.webp",
"rooms/tb/mc/tb_night_pregnant2_1_2.webp",])
image tb_kitchen_pregnant3_1 = DynamicAnimation(
["rooms/tb/kitchen/tb_kitchen_pregnant3_1_0.webp",
"rooms/tb/kitchen/tb_kitchen_pregnant3_1_1.webp",
"rooms/tb/kitchen/tb_kitchen_pregnant3_1_2.webp",])
image tb_bath_pregnant3_1 = DynamicAnimation(
["rooms/tb/bath/tb_bath_pregnant3_1_0.webp",
"rooms/tb/bath/tb_bath_pregnant3_1_1.webp",
"rooms/tb/bath/tb_bath_pregnant3_1_2.webp",])
image tb_evening_pregnant3_1 = DynamicAnimation(
["rooms/tb/mc/tb_evening_pregnant3_1_0.webp",
"rooms/tb/mc/tb_evening_pregnant3_1_1.webp",
"rooms/tb/mc/tb_evening_pregnant3_1_2.webp",])
image tb_night_pregnant3_1 = DynamicAnimation(
["rooms/tb/mc/tb_night_pregnant3_1_0.webp",
"rooms/tb/mc/tb_night_pregnant3_1_1.webp",
"rooms/tb/mc/tb_night_pregnant3_1_2.webp",])
default bt_mc_point=0
default bt_neus_point=0
default unlock_nym=False
default tb_side_quests1=False
default is_view_two_bodies_personality3=False
default is_view_intro_two_bodies_outfit_cat=False
default is_two_bodies_outfit_cat=False
default is_view_tb_chess=False
#----------------------------------------mc_room_quest----------------------------------------
screen two_bodies_mc_room_quest:  
    if not(two_bodies_outfit_is_active_outfit):
        imagebutton:
            auto "btn_old_photo_s_%s"     
            action Jump("two_bodies_outfit_unluck")
            tooltip _("Special photo")
            pos 600,580  
    imagebutton:
        auto "btn_event_%s"                   
        tooltip _("Endings") 
        xpos 0
        ypos 140      
        action Jump("menu_two_bodies_ending")
        at event_animation_ending
    if two_bodies_time==2: 
        if is_tb_pregnant:
            if is_tb_pregnant_trimester==1:
                if not(is_two_bodies_outfit_cat):
                    imagebutton:
                        auto "rooms/tb/mc/two_bodies_mc_evening0_0_%s.png"            
                        focus_mask True            
                        action Jump("two_bodies_mc_evening")
                        tooltip "%s"%neusname 
                if is_two_bodies_outfit_cat:
                    imagebutton:
                        auto "rooms/tb/mc/two_bodies_mc_evening0_1_%s.png"            
                        focus_mask True            
                        action Jump("two_bodies_mc_evening_outfit_cat")
                        tooltip "%s"%neusname
            if is_tb_pregnant_trimester==2: 
                imagebutton:
                    auto "rooms/tb/mc/tb_evening_pregnant2_0_%s.png"            
                    focus_mask True            
                    action Jump("two_bodies_mc_evening2")
                    tooltip "%s"%neusname
            if is_tb_pregnant_trimester==3: 
                imagebutton:
                    auto "rooms/tb/mc/tb_evening_pregnant3_0_%s.png"            
                    focus_mask True            
                    action Jump("two_bodies_mc_evening3")
                    tooltip "%s"%neusname
        else: 
            if not(is_two_bodies_outfit_cat):
                imagebutton:
                    auto "rooms/tb/mc/two_bodies_mc_evening0_0_%s.png"            
                    focus_mask True            
                    action Jump("two_bodies_mc_evening")
                    tooltip "%s"%neusname 
            if is_two_bodies_outfit_cat:
                imagebutton:
                    auto "rooms/tb/mc/two_bodies_mc_evening0_1_%s.png"            
                    focus_mask True            
                    action Jump("two_bodies_mc_evening_outfit_cat")
                    tooltip "%s"%neusname
    if two_bodies_time==3: 
        if is_tb_pregnant:
            if is_tb_pregnant_trimester==1:
                imagebutton:
                    auto "rooms/tb/mc/two_bodies_mc_night0_0_%s.png"            
                    focus_mask True            
                    action Jump("two_bodies_mc_night")
                    tooltip "%s"%neusname
            if is_tb_pregnant_trimester==2: 
                imagebutton:
                    auto "rooms/tb/mc/tb_night_pregnant2_0_%s.png"            
                    focus_mask True            
                    action Jump("two_bodies_mc_night2")
                    tooltip "%s"%neusname
            if is_tb_pregnant_trimester==3:
                imagebutton:
                    auto "rooms/tb/mc/tb_night_pregnant3_0_%s.png"            
                    focus_mask True            
                    action Jump("two_bodies_mc_night3")
                    tooltip "%s"%neusname
        else:
            imagebutton:
                auto "rooms/tb/mc/two_bodies_mc_night0_0_%s.png"            
                focus_mask True            
                action Jump("two_bodies_mc_night")
                tooltip "%s"%neusname 
    
label menu_two_bodies_ending:
    $ xsize_value = 750
    menu(screen="custom_choice_enhanced"):
        "Choose your ending"
        "Ending (Pregnant)" if is_tb_pregnant:
            jump tb_ending_event
        "Ending" if not is_tb_pregnant:
            jump tb_ending_event
        "Another personality, again?" if not(is_tb_pregnant):            
            jump two_bodies_personality3
        "This option is not available while she is pregnant"(False) if is_tb_pregnant:
            pass
        "Leave":
            jump two_bodies_rooms
label tb_ending_event:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        if persistent.gallery_pregnancy_censored:    
            $ is_tb_pregnant = False
        else:
            menu(screen="custom_choice_long"):
                "{size=+15}Are [neusname] and [neusname_lyra] pregnant?"
                "Yes":
                    $ is_tb_pregnant = True
                "No":                        
                    $ is_tb_pregnant = False   
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
        $ neusname_lyra = persistent.gallery_lyra    
    play music a_stray_cat_aimed_for_space volume 0.5 fadein 2.0
    scene tb_end_0 with dissolve
    stop ambience fadeout 1.0
    "Over time, you organize your wedding."
    if is_tb_pregnant:   
        scene tb_end_1 with snow1             
        neus_lyra_neus "{bt=2}{=lust_style}I accept.{/bt}{e_heartbt=FF0000}"
        scene tb_end_2 with w33
        if incest_story:
            neus_lyra "Big brother, aren't you going to give love to your cock hungry little sister?"
            scene tb_end_3 with dissolve
            neus "Yes, give love to your pregnant sister."
        else:
            neus_lyra "Future dad, aren't you going to give love to these moms who are hungry for your cock?"
            scene tb_end_3 with dissolve
            neus "Yes, give love to your pregnant wife."
        scene tb_end_4 with dissolve
        neus_lyra "When our child is born, I want you to impregnate my belly again."
        scene tb_end_5 with dissolve
        neus "I never want to feel my belly empty again, I always want you to fill me."
        $ renpy.music.set_volume(0.1,delay=2.5,channel='music')
        scene tb_end_6 with dissolve
        play char1 double_penetration1
        neus_lyra_neus "{bt=2}{=lust_style}Mmmm{/bt}"
        scene tb_end_7 with fadesex
        play char3 double_sex3
        neus_lyra_neus "{bt=2}{=lust_style}Ha ha ha{/bt}"
        neus_lyra_neus "This pregnant mommy is losing her mind."                
        scene tb_end_8 with dissolve
        neus_lyra_neus "{sc=2}{=lust_style}I'm cumming{/sc}"
        stop char3
        play charM cum1
        scene tb_end_9 with hpunch
        play char1 double_climax2
        neus_lyra_neus "{sc=2}{=lust_style}Uh!{/sc}"
        stop char1 fadeout 2.0
        scene tb_end_10 with dissolve
        if incest_story:
            neus_lyra_neus "That was wonderful, please keep giving us love, brother."
        else:
            neus_lyra_neus "That was wonderful, please keep giving us love, darling."
        scene tb_end_11 with dissolve
        neus_lyra_neus "{bt=2}{=lust_style}I love you.{/bt}{e_heartbt=FF0000}"
        scene black with dissolve
        $ renpy.music.set_volume(1.0,delay=2.5,channel='music')
        if incest_story:
            "You continued to give love to your sister, now also your wife."
        else:
            "You continued to give love to your childhood friend, now turned into your wife."
        scene tb_end_12 with dissolve
        "You formed a large family."
        scene tb_end_13 with snow1 
        ""
        python:
            achievement.grant("True_Ending_2")
            achievement.sync()
        if not ending_5_obtained:
            $ endings_obtained_count += 1
            $ ending_5_obtained = True
        centered "{color=#cc0066}{size=+200}True ending 2"                
        scene black with snow1                
        "You have obtained {color=#cc0066}Ending 5{/color} out of {color=#cc0066}[available_endings] possible endings{/color}."
        if set_active_pregnancy:
            "There are 2 versions of {color=#cc0066}Ending 5{/color}, pregnant and not pregnant."
        stop music3 fadeout 3.0
        centered "{color=#cc0066}{size=+100}Thank you for playing."               
    else:
        scene tb_end_14 with snow1
        neus_lyra_neus "{bt=2}{=lust_style}I accept.{/bt}{e_heartbt=FF0000}"
        scene tb_end_15 with w33
        if incest_story:
            neus_lyra_neus "Big brother, what are you waiting for? Come make love to your wife."
        else:
            neus_lyra_neus "Darling, what are you waiting for? Come make love to your wife."
        scene tb_end_16 with dissolve
        neus_lyra "I want you to give me lots of love."
        scene tb_end_17 with dissolve
        neus "I want my womb to be filled with my husband's cum."
        $ renpy.music.set_volume(0.1,delay=2.5,channel='music')
        scene tb_end_18 with dissolve
        play char3 double_sex3
        neus_lyra_neus "{bt=2}{=lust_style}Ha ha ha{/bt}"
        neus_lyra_neus "My womb is only for you to fill."
        if incest_story:
            neus_lyra_neus "I want to give you many children big brother."
        else:
            neus_lyra_neus "I want to give you many children."
        neus "I'm about to reach climax, my pussy is addicted to your dick."
        scene tb_end_19 with dissolve
        neus_lyra_neus "{sc=2}{=lust_style}I'm cumming{/sc}"
        stop char3
        play charM cum1
        scene tb_end_20 with hpunch
        play char1 double_climax2
        neus_lyra_neus "Impregnate me!"
        stop char1 fadeout 2.0
        scene tb_end_21 with dissolve
        play char3 sex5
        neus_lyra "{bt=2}{=lust_style}Ha ha ha{/bt}"
        mc "I suppose now all I have left is to fill this vagina."
        if incest_story:
            neus_lyra "Yes, please do it brother."
            neus_lyra "My pussy only exists to be impregnated by you."
            neus_lyra "Fill your little sister with lots of cum to make incest babies."
        else:
            neus_lyra "Yes, please do it."
            neus_lyra "My pussy only exists to be impregnated by you."
            neus_lyra "Fill me with lots of cum to make babies."
        stop char3
        play charM cum1
        scene tb_end_22 with hpunch
        play char1 climax2
        neus_lyra_neus "{sc=2}{=lust_style}Uh!{/sc}"
        stop char1 fadeout 2.0
        scene tb_end_23 with dissolve
        neus_lyra_neus "That was amazing... please keep using my body and giving me lots of love, I am only yours."
        scene tb_end_11 with dissolve
        if incest_story:
            neus_lyra_neus "{bt=2}{=lust_style}I love you big brother.{/bt}{e_heartbt=FF0000}"
            scene black with dissolve
            $ renpy.music.set_volume(1.0,delay=2.5,channel='music')
            "You enjoyed a very loving night with your sister, now also your wife."
        else:
            neus_lyra_neus "{bt=2}{=lust_style}I love you.{/bt}{e_heartbt=FF0000}"
            scene black with dissolve
            $ renpy.music.set_volume(1.0,delay=2.5,channel='music')
            "You enjoyed a very loving night with your wife."
        scene tb_end_24 with dissolve
        "And with all the semen you pumped into her womb, it was inevitable that she would become pregnant."
        "You formed a large family."
        scene tb_end_13 with snow1                
        ""
        python:
            achievement.grant("True_Ending_2")
            achievement.sync()
        if not ending_5_obtained:
            $ endings_obtained_count += 1
            $ ending_5_obtained = True
        centered "{color=#cc0066}{size=+200}True ending 2"                
        scene black with snow1                
        "You have obtained {color=#cc0066}Ending 5{/color} out of {color=#cc0066}[available_endings] possible endings{/color}."
        if set_active_pregnancy:
            "There are 2 versions of {color=#cc0066}Ending 5{/color}, pregnant and not pregnant."
        stop music3 fadeout 3.0
        centered "{color=#cc0066}{size=+100}Thank you for playing."
    $renpy.end_replay()
    $ persistent.main_menu_b=5
    jump menu_tb_true_ending
label menu_tb_true_ending:  
    scene black        
    menu(screen="custom_choice_long"):
        "Continue":            
            jump two_bodies_rooms 
        "Main Menu":
            menu(screen="custom_choice_long"):
                "Are you sure you want to go to the main menu?"
                "Yes":
                    $ MainMenu(confirm=False)()
                "No":
                    jump menu_tb_true_ending

label two_bodies_personality3:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
        $ neusname_lyra = persistent.gallery_lyra   
    if not(is_view_two_bodies_personality3):
        scene tb_p3_0 with dissolve
        if incest_story:
            neus_lyra "Hey brother, do you want to have a competition?"
        else:
            neus_lyra "Hey, do you want to have a competition?"
        mc "What kind?"
        scene tb_p3_1 with dissolve
        neus_lyra "A sex competition."
        mc "Alright."
        scene tb_p3_2 with dissolve
        neus_lyra "Great. The rules are simple: whoever manages to make their opponent have more orgasms, wins."
        scene tb_p3_3 with dissolve
        mc "Not that I doubt your abilities, but I don't think endurance is your strong suit."
        scene tb_p3_4 with dissolve
        neus_lyra "Hehe, yes, I know that, that's why I have this."
        mc "Mmm, I think I'll pass."
        scene tb_p3_5 with dissolve
        neus "Scared?"
        mc "Well, if I'm not mistaken, that object has a rumor that says..."
        scene tb_p3_6 with dissolve
        neus "*chicken clucks*cluck-cluck"
        scene tb_p3_7 with dissolve
        neus "Are you a chicke-"
        scene tb_p3_8 with dissolve
        mc "Fine, let's do it."
        scene tb_p3_7 with dissolve
        neus "Great (finally, I'll get my revenge)."
        scene tb_p3_9 with dissolve
        neus "By the way, how does this thing work?"
        scene tb_p3_10 with dissolve
        neus_lyra "Well, it came with the promotion ''Spice up your relationship.''"
        scene tb_p3_11 with dissolve
        neus_lyra "Along with this book."
        scene tb_p3_12 with dissolve
        neus_lyra "All it does is provide energy until it turns red, at which point it can no longer provide any more energy."
        scene tb_p3_13 with dissolve
        neus "That sounds great, what's the catch?"
        scene tb_p3_14 with dissolve
        neus_lyra "There's a rumor that when it turns red, something amazing happens."
        neus_lyra "Like the feelings you have for your partner multiply by 100, based on the number of orgasms you've had during the competition."
        scene tb_p3_15 with dissolve
        neus_lyra "Or that you become completely obsessed with your partner, unable to think about anything else."
        scene tb_p3_16 with dissolve
        neus_lyra "You know, typical relationship stuff."
        scene tb_p3_17 with dissolve
        neus_lyra "Although it's most likely that those rumors are just a marketing strategy to sell more."
        scene tb_p3_18 with dissolve
        neus_lyra "Still, I believe there was another rumor that said it enhanced the last spells in the book or something like that."
        scene tb_p3_19 with dissolve
        neus "(mmm, rumors... huh?)"
        if not(_in_replay):
            $ is_view_two_bodies_personality3=True
    scene tb_p3_20 with dissolve        
    menu:
        neus_lyra "So, what do you say? Shall we continue?"
        "Yes":
            $ bt_mc_point=0
            $ bt_neus_point=0
            scene tb_p3_24 with dissolve
            ""
            scene tb_p3_25 with dissolve
            ""
            scene tb_p3_26 with dissolve
            neus_lyra "Great, let's get started"            
            scene tb_p3_27 with w9
            play char3 finger1
            show screen tb_point_personality3
            neus "{bt=2}{=lust_style}ah ah ah{/bt}"
            if incest_story:
                neus "Brother, your fingers feel so good"
            else:
                neus "Your fingers feel so good"
            neus_lyra "*suck suck*"
            neus "You're touching my sensitive spot {e_heartbt=cc0066}"
            stop char3 fadeout 1.0
            play char1 climax1
            scene tb_p3_28 with dissolve
            neus "{sc=2}I'm cumming{/sc}"
            scene tb_p3_29 with dissolve            
            mc "1 point for me, I guess"
            $ bt_mc_point+=1
            "{size=+30}{color=#cc0066}+1{/color}"
            scene tb_p3_30 with dissolve            
            neus "Half a point"
            $ bt_mc_point-=0.5
            "{size=+30}{color=#cc0066}-0.5{/color}"
            scene tb_p3_31 with leafwipe
            play char3 kissing1
            neus_lyra "*kiss kiss*"
            if incest_story:
                neus_lyra "Your kisses are so delicious brother"
            else:
                neus_lyra "Your kisses are so delicious"
            neus_lyra "I want more, they turn me on so much."
            scene tb_p3_32 with dissolve
            neus_lyra "I'm cumming just from you kissing me."
            stop char3
            play char1 climax1
            scene tb_p3_33 with dissolve
            $ bt_mc_point+=0.5
            "{size=+30}{color=#cc0066}+0.5{/color}"
            scene tb_p3_34 with w17
            play char3 suck4            
            neus_lyra "*lick suck*"
            neus "*lick lick*"
            neus_lyra "*suck*(How delicious)"
            neus_lyra "(Please cum in my mouth)"
            stop char3
            play charM cum1
            scene tb_p3_35 with dissolve            
            neus_lyra "{color=#cc0066}Uh!"
            play char1 gulp1
            scene tb_p3_36 with dissolve
            $ bt_neus_point+=1.0
            neus "{size=+30}{color=#0000FF}+1 point{/color}"
            scene tb_p3_37 with w18
            play char3 sex5
            neus "{bt=2}{=lust_style}ah ah ah{/bt}"
            neus_lyra "Yes, yes, fuck me hard"
            if incest_story:
                neus_lyra "Do you like your sister's pussy that is exclusively for you?"
            else:
                neus_lyra "Do you like my exclusive pussy just for you?"
            neus_lyra "Please cum inside"
            if incest_story:
                neus_lyra "Impregnate your little sister"  
            else:
                neus_lyra "Impregnate me"   
            stop char3
            play charM cum1        
            scene tb_p3_38 with dissolve
            play char1 climax2
            neus "{sc=3}{=lust_style}Uh!!{/sc}"
            stop char1 fadeout 2.5
            scene tb_p3_39 with dissolve
            $ bt_mc_point+=0.5
            $ bt_neus_point+=1.0
            "{size=+30}{color=#cc0066}+0.5{/color} {color=#0000FF}+1{/color}"  
            scene tb_p3_40 with dissolve 
            if incest_story:
                neus_lyra "Brother, I want some too"
            else:        
                neus_lyra "I want some too"
            scene tb_p3_41 with snakes
            $ bt_mc_point+=0.5
            $ bt_neus_point+=1.0
            "{size=+30}{color=#cc0066}+0.5{/color} {color=#0000FF}+1{/color}"
            scene tb_p3_42 with w33
            play char3 sex1
            neus_lyra "{bt=2}{=lust_style}Ah ah ah{/bt}"
            neus_lyra "How intense{sc=2}{=lust_style}!!{/sc}"
            scene tb_p3_43 with dissolve
            stop char3 fadeout 1.0
            play char2 climax1
            $ bt_mc_point+=0.5
            "{size=+30}{color=#cc0066}+0.5{/color}"
            scene tb_p3_44 with dissolve
            play char2 climax3
            $ bt_mc_point+=0.5
            "{size=+30}{color=#cc0066}+0.5{/color}"
            scene tb_p3_45 with dissolve
            play char1 climax4
            $ bt_mc_point+=0.5
            "{size=+30}{color=#cc0066}+0.5{/color}"
            scene tb_p3_46 with dissolve
            play char2 double_climax1
            neus_lyra_neus "{sc=2}UH!{/sc} {e_heartbt=FF0000}"
            $ bt_mc_point+=1
            "{size=+30}{color=#cc0066}+1{/color}"
            scene tb_p3_47 with dissolve
            play char3 kissing1
            neus "*Kiss kiss kiss*"
            stop char3 fadeout 2.0
            play charM cum1
            scene tb_p3_48 with dissolve
            play char2 climax3
            $ bt_mc_point+=0.5
            $ bt_neus_point+=1.0
            "{size=+30}{color=#cc0066}+0.5{/color} {color=#0000FF}+1{/color}"
            scene tb_p3_49 with dissolve
            play char3 kissing1
            neus_lyra "I guess I used up the first energy charge"
            neus "*Kiss kiss*"            
            scene black with dissolve
            $ bt_mc_point+=3
            $ bt_neus_point+=1
            stop char3 fadeout 1.0
            "{size=+30}{color=#cc0066}+3{/color} {color=#0000FF}+1{/color}"
            scene tb_p3_50 with dissolve
            play char1 climax3
            neus "{sc=2}Uh!!{/sc}"
            scene tb_p3_51 with dissolve
            neus "Second energy charge"
            play char3 finger1 fadeout 0.5
            scene tb_p3_52 with dissolve
            neus "Yes, right there"
            play char3 sex1 fadeout 0.5
            scene tb_p3_53 with dissolve
            neus_lyra "Yes, give me lots of love"
            scene tb_p3_54 with dissolve
            neus "How long have we been at it? It's starting to get dark"
            play char3 sex2 fadeout 0.5
            scene tb_p3_55 with dissolve
            neus_lyra "Nothing like making love in the middle of the night"            
            scene tb_p3_56 with dissolve
            neus "Yes, we did it all night long"
            play char3 sex1 fadeout 0.5
            scene tb_p3_57 with dissolve
            neus_lyra "It seems like the sun is hiding again"
            neus "{bt=2}{=lust_style}Ah ah ah{/bt}"
            stop char3 fadeout 0.5
            play char1 climax1
            scene tb_p3_58 with dissolve
            $ bt_mc_point+=9
            $ bt_neus_point+=2
            "{size=+30}{color=#cc0066}+9{/color} {color=#0000FF}+2{/color}"
            play char3 sex2 fadeout 0.5
            scene tb_p3_59 with dissolve
            $ bt_mc_point+=9
            $ bt_neus_point+=2
            "{size=+30}{color=#cc0066}+9{/color} {color=#0000FF}+2{/color}"
            stop char3 fadeout 0.5
            scene tb_p3_60 with dissolve
            play char1 groan1
            $ bt_mc_point+=9
            $ bt_neus_point+=2
            "{size=+30}{color=#cc0066}+9{/color} {color=#0000FF}+2{/color}"
            scene tb_p3_61 with dissolve
            play char3 finger1 fadeout 1.0
            neus "What day is it?"
            neus "Why do you always do it with her recently?"
            neus "And with me, you only use your fingers"
            hide screen tb_point_personality3
            scene tb_p3_62 with dissolve
            neus "I need it too"
            mc "What is it that you need?"
            neus "You know, that thing down there"
            mc "You know, I'm not sure how many days it has been. I think my ability to reason has decreased. You need to be clearer"
            play char3 breathing1 fadeout 1.0
            scene tb_p3_63 with dissolve            
            neus "Damn it, don't lie. I don't even see you sweating. You're just bothering me"
            scene tb_p3_64 with dissolve
            neus "(Although I'm not sure if at this point containing my lust is the smartest thing to do)"
            if incest_story:
                neus "(He will definitely become my husband.)"
                neus "(And most likely, in the future, I'm going to have many children with him)"
            else:
                neus "(He's my boyfriend and he will definitely become my husband)"
                neus "(Most likely, in the future, I'm going to have many children with him)"
            scene tb_p3_65 with dissolve
            mc "If you tell me what you want, I will fulfill your wish"
            neus "(It's not fair)"
            scene tb_p3_66 with dissolve
            stop char3 fadeout 0.5
            if incest_story:
                neus "Please brother, give lots of love to this cock-hungry vagina"
                neus "Fertilize the vagina of your little sister and future wife, they are exclusively for you"
            else:
                neus "Please, give a lot of love to this cock-hungry vagina"
                neus "Fertilize the vagina of your girlfriend and future wife, they are exclusively for you"
            scene tb_p3_67 with dissolve
            neus "Drown all my eggs in your sperm"
            scene tb_p3_68 with dissolve
            play char3 sex5 fadeout 0.5
            neus "{bt=2}{=lust_style}Ah ah ah{/bt}"
            neus "(I have accepted my {bt=1}{=lust_style}lascivious side{/bt})"
            if incest_story:
                neus "(I am nothing more than a {bt=1}{=lust_style}succubus{/bt} who wants to be inseminated by my big brother's cock)"        
            else:
                neus "(I am nothing more than a {bt=1}{=lust_style}succubus{/bt} who wants to be inseminated by your cock)"            
            scene tb_p3_69 with w21
            play char3 sex1 fadeout 0.5
            neus "(But I don't care anymore, all I want is for him to love me completely)"
            neus "{bt=2}{=lust_style}Oh oh oh{/bt}"            
            neus "Give me so much love that it blows my mind and leaves me blank"
            scene tb_p3_70 with dissolve
            neus "I'm cummiiiing!"
            stop char3 fadeout 1.5
            play char1 climax1
            scene tb_p3_71 with dissolve
            play char2 climax2 
            neus "{sc=4}{=lust_style}Uh!!!!!{/sc}"
            play sound magic_break_crystal
            scene black with shatter
            ""
            scene tb_p3_72 with shatter
            neus_ny "Uuaa"           
            neus_ny "Good morning world"            
            mc "Oh, so there was still another part... great"
            scene tb_p3_73 with dissolve
            neus_ny "Thank you for the welcome"
            scene tb_p3_74 with dissolve
            neus_ny "But could I ask for a welcome gift?"
            mc "Of course"
            play char3 suck4
            scene tb_p3_75 with dissolve
            neus "Damn, my body hurts, I need some water"
            scene tb_p3_76 with dissolve
            neus_lyra "Oh, it seems like I passed out, that was great, but I'm thirsty"
            stop char3 fadeout 1.0
            scene tb_p3_77 with dissolve
            neus_ny "Delicious"
            scene tb_p3_78 with dissolve
            if incest_story:
                neus_ny "Please feed me with your milk big brother"
            else:
                neus_ny "Please feed me with your milk"
            scene tb_p3_79 with dissolve
            neus_ny "Lick Suck"
            scene tb_p3_80 with dissolve
            neus_lyra "It seems like there's a new member, although..."
            scene tb_p3_81 with dissolve
            neus "There's something that bothers me"
            scene tb_p3_82 with dissolve
            neus_lyra "I feel like it's a part of me"
            scene tb_p3_83 with dissolve
            neus "But there's something about her that makes me doubt that and..."
            scene tb_p3_84 with dissolve
            neus_lyra "It fills me with hostility"
            scene tb_p3_85 with dissolve
            if incest_story:
                neus_lyra_neus "Hey brother, I've always avoided asking you this question, but..."
            else:
                neus_lyra_neus "Hey, I've always avoided asking you this question, but..."
            scene tb_p3_86 with dissolve
            neus_lyra_neus "What do you like more, butts or breasts?"
            mc "..."
            menu:
                mc "I like..."
                "Butts":
                    scene tb_p3_87 with dissolve
                    mc "I like butts"
                    ly_ne_ny "{e_heartbt=FF0000}"
                    mc "By the way, didn't I hear you say you were thirsty?"
                    scene tb_p3_88 with dissolve
                    neus_lyra_neus "Oh, yes, I was going to do that"
                "Boobs":
                    mc "I like boobs"
                    scene tb_p3_89 with dissolve
                    neus "..."(multiple=3)                    
                    neus_ny "{e_heartbt=FF0000}"(multiple=3)
                    neus_lyra "..."(multiple=3)
                    "You feel a great tension in the air"
                    mc "By the way, didn't I hear you say you were thirsty?"
                    scene tb_p3_90 with dissolve
                    neus_lyra_neus "Oh, yes, I was going to do that"
                "Both":                    
                    mc "I like butts"
                    scene tb_p3_87 with dissolve
                    ly_ne_ny "{e_heartbt=FF0000}"
                    mc "and also boobs"
                    scene tb_p3_91 with dissolve
                    neus "..."(multiple=3)                    
                    neus_ny "{e_heartbt=FF0000}"(multiple=3)
                    neus_lyra "..."(multiple=3)
                    "You feel a great tension in the air"
                    mc "By the way, didn't I hear you say you were thirsty?"
                    scene tb_p3_92 with dissolve
                    neus_lyra_neus "Oh, yes, I was going to do that"
                "Avoid the question":
                    mc "By the way, didn't I hear you say you were thirsty?"
                    scene tb_p3_90 with dissolve
                    neus_lyra_neus "Oh, yes, I was going to do that"
            scene tb_p3_93 with dissolve
            neus_ny "I can't take it anymore"
            neus_ny "I want to have you inside"
            scene tb_p3_94 with dissolve
            neus_ny "But first, I want to amplify the sensation"
            play sound magical1 volume 0.3            
            scene tb_p3_95 with dissolve
            neus "Uh!!"(multiple=2)
            neus_lyra "{e_heartbt=FF0000}"(multiple=2)
            scene tb_p3_96 with dissolve
            neus_ny "Here I go"            
            play char2 penetration2
            play char1 double_penetration2
            scene tb_p3_97 with dissolve            
            neus_ny "Uh!!"
            neus_ny "It feels so good"
            neus_ny "I'm going to start moving now"
            scene tb_p3_98 with dissolve
            $ renpy.music.set_volume(1.0, channel='char3')
            play char3 threesome_sex1
            neus_ny "{bt=2}{=lust_style}Ah ah ah{/bt}"
            neus_ny "{e_heartbt2=FF0000}"
            ly_ne_ny "{bt=2}{=lust_style}Ah ah ah{/bt}"
            $ renpy.music.set_volume(0.5,delay=1.0, channel='char3')
            scene tb_p3_99 with dissolve
            neus "(I'm not touching her, but we're still sharing the sensations)"
            scene tb_p3_100 with dissolve
            neus_lyra "(Also, this shared pleasure feels like it's amplified by 3)"
            $ renpy.music.set_volume(1.0,delay=1.0, channel='char3')
            scene tb_p3_98 with dissolve
            if incest_story:
                neus_ny "Please brother, make love to me hard"
            else:
                neus_ny "Please, make love to me hard"
            stop char3 fadeout 1.0
            scene tb_p3_101 with w39            
            play char3 threesome_sex2
            neus_ny "Yes, please, choke me harder"
            neus_ny "Destroy me, make love to me hard"
            neus_ny "I'll do my best to squeeze your cock with my cock-addicted vagina"
            neus_ny "Please, make love to me really hard"
            neus_ny "You can tell me you love me while saying my name"
            neus_ny "Please, it will increase my pleasure if you say that"
            mc "(Her name, huh?)"
            if persistent.gallery_sylvia != "Sylvia":
                $ neusname_sylvia = renpy.input(_("What is the name you want to give her? (Default: Sylvia)"), default=persistent.gallery_sylvia, exclude='\\[{') 
            else:
                $ neusname_sylvia = renpy.input(_("What is the name you want to give her? (Default: Sylvia)"), exclude='\\[{') 
            $ neusname_sylvia = neusname_sylvia.title()
            $ neusname_sylvia = neusname_sylvia.strip()
            if neusname_sylvia == "":
                $ neusname_sylvia = "Sylvia"
            $ renpy.music.set_volume(0.5,delay=1.0, channel='char3')
            scene tb_p3_102 with dissolve
            mc "I love you [neus_sylvia]"
            $ renpy.music.set_volume(1.0,delay=1.0, channel='char3')
            scene tb_p3_103 with dissolve
            neus_sylvia "I feel like I'm about to cum just by hearing those words"
            neus_sylvia "And I love how your dick kisses my lustful uterus"
            neus_sylvia "Which is a slave to your dick and wants to be filled with your semen"
            neus_sylvia "It's begging to be impregnated"
            if incest_story:
                neus_sylvia "Please brother, ejaculate inside me"
            else:
                neus_sylvia "Please, ejaculate inside"
            $ renpy.music.set_volume(0.5,delay=1.0, channel='char3')
            scene tb_p3_104 with dissolve
            ly_ne_syl "I'm going to cum... I'm going to..."
            stop char3
            $ renpy.music.set_volume(1.0,delay=1.0, channel='char3')
            play charM cum1
            scene tb_p3_105 with dissolve
            play char1 double_climax2
            play char2 double_climax2
            ly_ne_syl "{e_heartbt2=cc0066} {bt=2}{=lust_style}UH!{/bt} {e_heartbt2=cc0066}"
            scene tb_p3_106 with dissolve
            ly_ne_syl "That was amazing..."
            stop char1 fadeout 2.0   
            stop char2 fadeout 2.0          
            scene tb_p3_107 with dissolve
            ""
            scene tb_p3_108 with dissolve
            mc "(Oh, it seems she doesn't have any more energy.)"
            mc "(Although I'm also a bit tired, I should rest and bring them some water)"
            play ambience shower2 fadein 0.5
            scene black with dissolve
            "After giving them water to drink and taking them to the shower to clean off the sweat"
            stop ambience fadeout 1.0
            scene tb_p3_109 with dissolve
            "You put them to bed so they can rest."
            scene black with dissolve
            centered "{size=+60}Subphase {color=#cc0066}''Nymphomania''"      
            if not(_in_replay):      
                $ unlock_nym=True
                $ tb_side_quests1=True
            $ renpy.end_replay()
            python:
                achievement.grant("Another_Personality_Again")
                achievement.sync()
            jump nym_rooms
        "No":
            scene tb_p3_21 with dissolve
            neus_lyra "Oh, I understand."
            neus_lyra "Actually, I never had any plans to use this thing."
            scene tb_p3_22 with dissolve
            neus_lyra "I was already aiming high with the plan of using that book."
            neus_lyra "Honestly, I just wanted to have some fun."
            scene tb_p3_23 with dissolve
            neus_lyra "But if you change your mind, I'm always available."
            $ renpy.end_replay()
            jump two_bodies_rooms
screen tb_point_personality3:
    vbox:
        xpos 10
        ypos 10                           
        text __("You: %s")%bt_mc_point:
            outlines [ (4, gui.accent_color) ]
            size 40            
        text _("[neusname]: %s")%bt_neus_point:
            outlines [ (4, gui.accent_color) ]
            size 40    

screen tb_preegnancy_screen:      
    imagebutton:
        idle 'icon_chance_pregnancy'                                      
        action NullAction()
        xalign 0.99
        ypos 10  
    hbox:  
        xsize 150         
        xalign 0.99
        ypos 57                             
        text _("%s%%")%(probability_of_pregnancy+probability_of_pregnancy_bonus):
            outlines [ (4, gui.accent_color) ]
            xalign 0.5
#----------------------------------------kitchen_room_quest----------------------------------------  
label tb_pregnancy_ramdom_check(message=""):
    if not(is_tb_pregnant_start):
        $ probability_of_pregnancy_aux= probability_of_pregnancy+probability_of_pregnancy_bonus
        if set_active_pregnancy:
            if message not in [""]:
                neus_lyra_neus "[message!t]"            
            "Pregnancy possibility [probability_of_pregnancy_aux]%%."                        
            $ probability_of_pregnancy_random=random.randint(0,99)
            if probability_of_pregnancy_random<=probability_of_pregnancy_aux:
                "They got pregnant."
                "{=lust_style}To begin the pregnancy stage, one day must pass."
                $ is_tb_pregnant_start=True
            else:
                "They did not get pregnant"
        else:
            ""        
    else:
        ""
    hide screen tb_preegnancy_screen
    return
screen two_bodies_kitchen_room_quest:  
    if is_tb_pregnant:
        if is_tb_pregnant_trimester==1:
            imagebutton:
                auto "rooms/tb/kitchen/two_bodies_kitchen0_0_%s.png"            
                focus_mask True            
                action Jump("two_bodies_kitchen")
                tooltip "%s"%neusname
        if is_tb_pregnant_trimester==2:
            imagebutton:
                auto "rooms/tb/kitchen/tb_kitchen_pregnant2_0_%s.png"            
                focus_mask True            
                action Jump("two_bodies_kitchen2")
                tooltip "%s"%neusname
        if is_tb_pregnant_trimester==3:
            imagebutton:
                auto "rooms/tb/kitchen/tb_kitchen_pregnant3_0_%s.png"            
                focus_mask True            
                action Jump("two_bodies_kitchen3")
                tooltip "%s"%neusname                    
    else:          
        imagebutton:
            auto "rooms/tb/kitchen/two_bodies_kitchen0_0_%s.png"            
            focus_mask True            
            action Jump("two_bodies_kitchen")
            tooltip "%s"%neusname  
label  two_bodies_kitchen:
    scene two_bodies_kitchen0_1 with storyfx
    menu:
        "Cookies":
            scene two_bodies_kitchen0_2 with dissolve
            if incest_story:
                neus_lyra "Oh, I would love for you to try my cookies, brother."
            else:
                neus_lyra "Oh, I would love for you to try my cookies."
            scene two_bodies_kitchen0_3 with dissolve
            neus_lyra "I prepared them with a lot of love and I think you'll like the secret ingredient."
            scene two_bodies_kitchen0_4 with dissolve
            neus_lyra "I call it ''love juice''."
            scene two_bodies_kitchen0_5 with dissolve            
            menu:
                neus "{size=-15}''Love juice''?"
                "Eat cookies":
                    scene two_bodies_kitchen0_6 with dissolve
                    if incest_story:
                        neus "Brother, I wouldn't recommend eating that cookie."(multiple=2)
                    else:
                        neus "I wouldn't recommend eating that cookie."(multiple=2)
                    "You take a bite of the cookie, it's delicious but you taste something peculiar."(multiple=2)                                     
                    mc "Delicious."
                    scene two_bodies_kitchen0_7 with dissolve
                    neus_lyra "I'm glad you liked it, that makes me very happy. {e_heartbt=cc0066}"
                    scene two_bodies_kitchen0_8 with dissolve
                    neus "Degenerate!"
                    scene two_bodies_kitchen0_9 with dissolve
                    neus "(Although it's me, I'm a degenerate)"(multiple=2)
                    neus_lyra "If you want, you can have more cookies."(multiple=2)
                    menu:
                        "Drink the ''Love juice'' straight from the source":
                            scene two_bodies_kitchen0_10 with dissolve
                            neus "Hey, why are you lifting me up?"
                            scene two_bodies_kitchen0_11 with dissolve
                            play char1 groan1
                            neus "Uh?"
                            scene two_bodies_kitchen0_12 with fadesex
                            play char3 groan_music volume 2.5
                            if incest_story:
                                neus "Brother, don't lick me there."
                            else:
                                neus "Don't lick me there."
                            neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
                            neus "You're going to make me cum."
                            stop char3 fadeout 1.0
                            scene two_bodies_kitchen0_13 with dissolve
                            play char1 climax1
                            neus "Uh."
                            play char3 breathing1 volume 1.5
                            scene two_bodies_kitchen0_14 with dissolve                            
                            mc "Nothing like drinking straight from the source."
                            mc "Although I still want a little more."                            
                            scene two_bodies_kitchen0_15 with w33
                            "You enjoy a good breakfast with lots of ''love juice''."
                            stop char3 fadeout 1.0                            
                            scene black with dissolve                           
                            ""
                            jump two_bodies_time_advances
                        "Stop eating":
                            scene two_bodies_kitchen0_16 with dissolve
                            neus_lyra "I guess you don't just want to have cookies for breakfast, hehe."
                "Pass":
                    scene two_bodies_kitchen0_17 with dissolve
                    neus_lyra "Uh, I understand."
        "Blowjob":
            scene two_bodies_kitchen0_18 with dissolve
            neus "{e_heartbt2=FF0000}"(multiple=2)
            neus_lyra "Hehe"(multiple=2)            
            scene two_bodies_kitchen0_19 with dissolve
            neus "*Lick*"(multiple=2)  
            neus_lyra "*Lick*"(multiple=2)  
            scene two_bodies_kitchen0_20 with dissolve 
            play char3 suck1 volume 1.5        
            neus_lyra "*Lick lick*"(multiple=2) 
            neus "*Suck* (Delicious)"(multiple=2)     
            if incest_story:
                neus "*Suck* (Damn, I love sucking my brother's cock)"    
            else:                
                neus "*Suck* (Damn, I love sucking his cock)"           
            neus "*Suck* (I guess I've gotten used to the taste to the point where I now love this)"           
            neus "*Suck* (I want to suck his cock forever)"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene two_bodies_kitchen0_21 with dissolve
            neus "Uh!"
            scene two_bodies_kitchen0_22 with dissolve                     
            ""  
            play char1 [gulp1, ahegao1] fadeout 2.5       
            scene two_bodies_kitchen0_23 with dissolve                   
            neus "{bt=2}{=lust_style}Ah!{/bt}"(multiple=2) 
            if incest_story:
                neus_lyra "Thanks for breakfast, big brother {e_heartbt=FF0000}"(multiple=2) 
            else:
                neus_lyra "Thanks for breakfast {e_heartbt=FF0000}"(multiple=2) 
            scene black with dissolve                           
            ""
        "Sex":
            scene two_bodies_kitchen0_18 with dissolve
            neus "{e_heartbt2=FF0000}"(multiple=2)
            neus_lyra "Hehe"(multiple=2) 
            scene two_bodies_kitchen0_24 with dissolve 
            if incest_story:
                neus_lyra "I want your cock inside me, brother"
            else:
                neus_lyra "I want your cock inside me"
            scene two_bodies_kitchen0_25 with dissolve
            play char1 penetration1
            neus "{sc=2}{=lust_style}UH!{/sc}"
            neus_lyra "Please fuck my pussy"
            scene two_bodies_kitchen0_26 with dissolve
            play char3 sex7
            neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            if incest_story:
                neus_lyra "Yes brother, like that"
            else:
                neus_lyra "Yes, like that"
            neus_lyra "My pussy belongs to you, give it lots of love"
            neus "This feels so good"(multiple=2)
            neus_lyra "My pussy desires to be pounded by your magnificent cock"(multiple=2)
            scene two_bodies_kitchen0_27 with fadesex
            neus_lyra "My uterus is longing to be filled"
            if not is_tb_pregnant:
                neus_lyra "I want you to put a lot of dough in my oven, I want you to impregnate me"
            else:
                neus_lyra "I want you to put a lot of dough in my oven"
            if incest_story:
                neus "Please fill me up, brother"
            else:
                neus "Please fill me up"
            menu:
                "Inside": 
                    $ probability_of_pregnancy_bonus=0
                    stop char3
                    play charM cum1
                    scene two_bodies_kitchen0_28 with dissolve
                    if set_active_pregnancy and not(is_tb_pregnant_start):
                        show screen tb_preegnancy_screen
                    play char1 climax1
                    neus "Uh!"
                    stop char1 fadeout 1.0
                    scene two_bodies_kitchen0_29 with dissolve
                    neus_lyra "I can feel my uterus being flooded"
                    if not is_tb_pregnant:
                        neus_lyra "My eggs are already swimming in your semen"
                        neus_lyra "They are going to be fertilized"
                        scene two_bodies_kitchen0_30 with dissolve
                        mc "I think I'm missing someone to fertilize"
                        scene two_bodies_kitchen0_31 with dissolve
                        if incest_story:
                            neus_lyra "Yes, brother! My uterus feels very empty. I want you to fill it up"
                        else:
                            neus_lyra "Yes! My uterus feels very empty. I want you to fill it up"
                    else:
                        neus_lyra "It feels so good"
                        scene two_bodies_kitchen0_30 with dissolve
                        mc "I think I'm missing someone who needs their uterus filling"
                        scene two_bodies_kitchen0_31 with dissolve
                        if incest_story:
                            neus_lyra "Yes, brother! I want you to fill it up"
                        else:
                            neus_lyra "Yes! I want you to fill it up"
                    scene two_bodies_kitchen0_32 with fadesex
                    play char3 sex7
                    neus_lyra "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
                    neus_lyra "This feels so good"
                    neus_lyra "I'm cumming {e_heartbt=FF0000}"
                    stop char3
                    play charM cum1
                    scene two_bodies_kitchen0_33 with dissolve
                    play char1 climax1
                    neus_lyra "Uh"
                    stop char1 fadeout 1.0
                    menu: 
                        "More":
                            scene two_bodies_kitchen0_34 with dissolve
                            neus_lyra "Phew, that was intense"
                            scene two_bodies_kitchen0_35 with dissolve
                            play char3 sex7
                            neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
                            if not is_tb_pregnant:
                                neus_lyra "So you want to make sure I get pregnant. In that case, you should also fill me up afterwards"
                            else:
                                neus_lyra "So you want to make sure that we are pregnant. In that case, you should also fill me up afterwards"
                            neus "I'm cumming {e_heartbt=FF0000}"
                            stop char3
                            play charM cum1
                            scene two_bodies_kitchen0_36 with dissolve
                            play char1 climax1
                            neus "Uh"   
                            if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start): 
                                $ probability_of_pregnancy_bonus+=10                
                                "Chance of pregnancy increased by 10%%"
                            stop char1 fadeout 1.0
                            scene two_bodies_kitchen0_37 with dissolve
                            play char2 climax3
                            neus_lyra "{sc=2}{=lust_style}Oh!{/sc}"
                            if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start):
                                $ probability_of_pregnancy_bonus+=10 
                                "Chance of pregnancy increased by 10%%"             
                            scene two_bodies_kitchen0_38 with dissolve
                            play char1 climax4
                            neus "{sc=2}{=lust_style}Uh!{/sc}"
                            if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start):
                                $ probability_of_pregnancy_bonus+=10
                                "Chance of pregnancy increased by 10%%"
                            scene two_bodies_kitchen0_39 with dissolve
                            neus "I need some water"
                            scene two_bodies_kitchen0_40 with dissolve
                            if incest_story:
                                neus "Wait, wait, brother. Please let me rest a bit"
                            else:
                                neus "Wait, wait. Please let me rest a bit"
                            menu: 
                                "More":
                                    scene two_bodies_kitchen0_41 with dissolve
                                    play char3 sex7
                                    neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
                                    if incest_story:
                                        neus "Brother you're going to break me. My special oven is already at maximum capacity"
                                    else:
                                        neus "You're going to break me. My special oven is already at maximum capacity"
                                    neus "I'm cumming {e_heartbt=FF0000}"
                                    stop char3
                                    play charM cum1
                                    scene two_bodies_kitchen0_42 with dissolve
                                    play char1 climax2
                                    neus "{sc=2}{=lust_style}Uh!{/sc}"
                                    if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start):
                                        $ probability_of_pregnancy_bonus+=10 
                                        "Chance of pregnancy increased by 10%%"
                                    stop char1 fadeout 1.0
                                    scene two_bodies_kitchen0_43 with dissolve
                                    if incest_story:
                                        neus_lyra "Brother I would love to receive more love, but I don't think my body can handle it anymore"   
                                    else:
                                        neus_lyra "I would love to receive more love, but I don't think my body can handle it anymore"                    
                                    neus_lyra "Besides, my oven is already very full. I don't think there's room for more"
                                    menu: 
                                        "More":
                                            scene two_bodies_kitchen0_44 with dissolve
                                            play char3 sex7
                                            neus_lyra "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
                                            neus_lyra "This feels so good"
                                            if not is_tb_pregnant:
                                                if incest_story:
                                                    neus_lyra "Yes brother, break me until my mind can only think about getting pregnant"
                                                else:
                                                    neus_lyra "Yes, break me until my mind can only think about getting pregnant"
                                            else:
                                                if incest_story:
                                                    neus_lyra "Yes brother, break me until my mind can only think about being filled with your cum"
                                                else:
                                                    neus_lyra "Yes, break me until my mind can only think about being filled with your cum"
                                            stop char3
                                            play charM cum1
                                            scene two_bodies_kitchen0_45 with dissolve
                                            play char2 climax2
                                            neus_lyra "{sc=2}{=lust_style}Uh!{/sc}"
                                            if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start):
                                                $ probability_of_pregnancy_bonus+=9
                                                "Chance of pregnancy increased by 9%%"
                                            stop char2 fadeout 1.0
                                            stop music fadeout 1.0
                                        "Stop":
                                            pass
                                "Stop":
                                    pass
                        "Stop":
                            pass                  
                    scene two_bodies_kitchen0_46 with w21
                    call tb_pregnancy_ramdom_check(_("My uterus is so full of semen, I'm sure I'll get pregnant.")) from _call_tb_pregnancy_ramdom_check                   
                    scene black with dissolve                           
                    ""
                    jump two_bodies_time_advances
                "Outside":
                    stop char3
                    play charM cum1
                    scene two_bodies_kitchen0_47 with dissolve
                    play char1 climax1
                    neus "UH"
                    stop char1 fadeout 1.0
                    scene two_bodies_kitchen0_48 with dissolve
                    neus_lyra "What a waste, I would have liked you to pour it into my uterus"                    
                    neus_lyra "But it doesn't matter, there are always more opportunities"
                    scene black with dissolve                           
                    ""
                    jump two_bodies_time_advances
        "Back":
            jump two_bodies_rooms
    jump two_bodies_kitchen
label  two_bodies_kitchen2:
    scene tb_kitchen_pregnant2_1 with storyfx
    menu:
        "Milk":
            scene tb_kitchen_pregnant2_2 with dissolve
            neus_lyra "Oh? You want some milk?"
            scene tb_kitchen_pregnant2_3 with dissolve
            neus_lyra "Although, as you can see, there is very little left."
            mc "Oh... That's very sad, I hope that cow can produce more milk than that in the future."
            scene tb_kitchen_pregnant2_4 with dissolve
            neus_lyra "Yes, unfortunately, the cow has small udders."
            if incest_story:
                neus_lyra "I hope this little bit of milk is enough to satisfy you, big brother."
            else:
                neus_lyra "I hope this little bit of milk is enough to satisfy you."
            scene tb_kitchen_pregnant2_5 with dissolve
            mc "Delicious, although I want a little more."
            scene tb_kitchen_pregnant2_6 with dissolve
            neus_lyra "Unfortunately, there is no more left..."
            scene tb_kitchen_pregnant2_7 with dissolve
            neus "There are still two cartons of 100%% real cow's milk in the fridge."
            menu:            
                "Special milk":
                    scene tb_kitchen_pregnant2_8 with dissolve
                    mc "I prefer the milk from my special little cow."
                    scene tb_kitchen_pregnant2_9 with dissolve
                    neus "Eh!"
                    mc "Also, I've heard that cows can give more milk depending on the milking technique."
                    scene tb_kitchen_pregnant2_10 with fadesex
                    play char3 groan_music
                    neus "Mmm.."
                    if incest_story:
                        neus "Don't suck my udders so hard brother."
                    else:
                        neus "Don't suck my udders so hard."
                    neus "You're going to make what little milk I have left come out."
                    neus "I'm climaxing."
                    stop char3
                    scene tb_kitchen_pregnant2_11 with dissolve
                    play char1 climax1
                    neus "I'm reaching climax while you're milking me."
                    scene tb_kitchen_pregnant2_12 with dissolve
                    neus "Ufff {e_heartbt=FF0000}"
                    scene tb_kitchen_pregnant2_13 with dissolve
                    neus_lyra "You know, this little cow doesn't have much milk left."
                    neus_lyra "But maybe with that milking technique of yours,"
                    neus_lyra "Maybe she can produce more milk."
                    scene tb_kitchen_pregnant2_14 with fadesex
                    play char3 groan_music2
                    neus_lyra "Uhhh."
                    if incest_story:
                        neus_lyra "Yes, brother, that's exactly the spot."
                    else:
                        neus_lyra "Yes, that's exactly the spot."
                    neus_lyra "Yes, yes, suck my nipples."
                    neus_lyra "Milk this dairy cow."
                    neus_lyra "That will produce exclusive milk for you."
                    stop char3
                    scene tb_kitchen_pregnant2_15 with dissolve
                    play char1 climax2
                    neus_lyra "{sc=2}{=lust_style}Uhhh{/sc} {e_heartbt=FF0000}"
                    stop char1 fadeout 2.0
                    scene tb_kitchen_pregnant2_16 with w9
                    if incest_story:
                        "You enjoy a pleasant breakfast with your sister."
                    else:
                        "You enjoy a pleasant breakfast."
                    jump two_bodies_time_advances
                "Cow's milk":
                    "You take a glass of cow's milk from the refrigerator."
        "Bellyjob":
            scene tb_kitchen_pregnant2_17 with dissolve
            neus_lyra_neus "Okay"
            scene tb_kitchen_pregnant2_18 with dissolve
            neus_lyra "Let's start moving"
            scene tb_kitchen_pregnant2_19 with dissolve
            play char3 handjob2
            ""
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_kitchen_pregnant2_20 with dissolve
            ""
            neus "Hehe"
            scene black with dissolve
            "They clean themselves"
        "Back":
            jump two_bodies_rooms
    jump two_bodies_kitchen2
label  two_bodies_kitchen3:
    scene tb_kitchen_pregnant3_1 with storyfx
    menu:
        "Milk":
            scene tb_kitchen_pregnant3_2 with dissolve
            neus_lyra "Hehe, this time the glass is full, although it did take two cows."
            scene tb_kitchen_pregnant3_3 with dissolve
            neus "..."
            menu:            
                "Drink":
                    scene tb_kitchen_pregnant3_4 with dissolve
                    "You drink the full glass of milk."
                    scene tb_kitchen_pregnant3_5 with dissolve
                    if incest_story:
                        neus_lyra "Did you like it brother?"
                    else:
                        neus_lyra "Did you like it?"
                    mc "Yes."
                    scene tb_kitchen_pregnant3_6 with dissolve
                    mc "Although I want a little more."
                    scene tb_kitchen_pregnant3_7 with dissolve
                    neus_lyra "... I understand."
                    scene tb_kitchen_pregnant3_8 with w33
                    "You enjoy a good breakfast."
                    scene black with dissolve
                    ""
                    jump two_bodies_time_advances
                "Pass":
                    scene tb_kitchen_pregnant3_9 with dissolve
                    neus_lyra "Okay, whenever you feel like it you can always ask me."
        "Sex":
            scene tb_kitchen_pregnant3_10 with dissolve
            neus_lyra_neus "{e_heartbt2=FF0000}"
            scene tb_kitchen_pregnant3_11 with dissolve
            if incest_story:
                neus_lyra "Brother, I want it inside, I've been holding back a lot"
            else:
                neus_lyra "I want it inside, I've been holding back a lot"
            neus "I want you to fill me up with a lot of milk"
            scene tb_kitchen_pregnant3_12 with dissolve
            neus_lyra "Give me a lot of love"
            scene tb_kitchen_pregnant3_13 with dissolve
            play char1 double_penetration2
            neus_lyra_neus  "UH!"
            scene tb_kitchen_pregnant3_14 with dissolve
            play char3 double_sex2
            neus_lyra_neus  "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            neus_lyra "My pregnant pussy is perfectly molded for your cock"
            neus "It feels so good, please keep using my pussy exclusive for you"            
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_kitchen_pregnant3_15 with dissolve
            play char1 double_climax2
            neus_lyra_neus  "Mmm"
            stop char1 fadeout 2.0
            scene tb_kitchen_pregnant3_16 with dissolve
            if incest_story:
                neus "I also need you to fill me up, please put it in me brother"
            else:
                neus "I also need you to fill me up, please put it in me"
            scene tb_kitchen_pregnant3_17 with dissolve
            play char3 sex6
            neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            neus "{e_heartbt2=FF0000}"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_kitchen_pregnant3_18 with dissolve
            play char1 climax2
            neus "Uh!"
            stop char1 fadeout 2.0
            scene tb_kitchen_pregnant3_19 with dissolve
            ""
            scene black with dissolve
            "They clean themselves"
        "Back":
            jump two_bodies_rooms
    jump two_bodies_kitchen3
#----------------------------------------bath_room_quest---------------------------------------- 
screen two_bodies_bath_room_quest:   
    if is_tb_pregnant:
        if is_tb_pregnant_trimester==1: 
            imagebutton:
                auto "rooms/tb/bath/two_bodies_bath0_0_%s.png"            
                focus_mask True            
                action Jump("two_bodies_bath")
                tooltip "%s"%neusname
        if is_tb_pregnant_trimester==2: 
            imagebutton:
                auto "rooms/tb/bath/tb_bath_pregnant2_0_%s.png"            
                focus_mask True            
                action Jump("two_bodies_bath2")
                tooltip "%s"%neusname
        if is_tb_pregnant_trimester==3: 
            imagebutton:
                auto "rooms/tb/bath/tb_bath_pregnant3_0_%s.png"            
                focus_mask True            
                action Jump("two_bodies_bath3")
                tooltip "%s"%neusname
    else:         
        imagebutton:
            auto "rooms/tb/bath/two_bodies_bath0_0_%s.png"            
            focus_mask True            
            action Jump("two_bodies_bath")
            tooltip "%s"%neusname
label  two_bodies_bath:
    play ambience bathtub fadein 1.0 volume 0.15
    scene two_bodies_bath0_1 with storyfx
    menu:
        "Assjob":
            scene two_bodies_bath0_2 with dissolve
            neus_lyra_neus "Hehe"
            scene two_bodies_bath0_3 with wet
            neus "I see you want to feel my big butt"
            scene two_bodies_bath0_4 with dissolve
            neus_lyra "I may not be able to give you the best titjob"
            scene two_bodies_bath0_3 with dissolve
            neus "But I trust my attributes to give you the best assjob"
            scene two_bodies_bath0_5 with dissolve
            play char3 handjob2
            if incest_story:
                neus_lyra "How does it feel to have your sister's butt giving you an assjob?"
                mc "I could never have imagined receiving a double assjob from my cute little sister"
            else:
                neus_lyra "How does it feel to have your girlfriend's butt giving you an assjob?"
                mc "I could never have imagined receiving a double assjob from my cute girlfriend"
            mc "Your cute butt feels great"
            neus_lyra_neus "{e_heartbt2=FF0000}"
            stop char3 fadeout 1.0
            scene two_bodies_bath0_6 with dissolve
            neus "I guess it can't be helped, I'll have to put in a little more effort"
            scene two_bodies_bath0_7 with dissolve
            if incest_story:
                neus_lyra "Those words made me very happy brother, I'm going to try to give you the best assjob of your life"
            else:
                neus_lyra "Those words made me very happy, I'm going to try to give you the best assjob of your life"
            scene two_bodies_bath0_8 with dissolve
            play char3 handjob2 volume 2.0
            neus_lyra_neus "I'm going to make you ejaculate a lot and release a lot of milk"
            if incest_story:
                neus_lyra_neus "I want my brother to cover my fat butt with his milk"
                neus_lyra_neus "Making it smell of his essence for many weeks"
            else:
                neus_lyra_neus "I want you to cover my fat butt with your milk"
                neus_lyra_neus "Making it smell of your essence for many weeks"
            neus_lyra_neus "And everyone will know who my little butt belongs to"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene two_bodies_bath0_9 with dissolve
            ""
            scene two_bodies_bath0_10 with dissolve
            if incest_story:
                neus_lyra_neus "Wow brother, that's a lot"
            else:
                neus_lyra_neus "Wow, that's a lot"
            if not is_tb_pregnant:
                neus_lyra_neus "With all this milk my butt could surely get pregnant hehe"
            else:
                neus_lyra_neus "With all this milk my butt could surely also get pregnant hehe"
            scene two_bodies_bath0_11 with dissolve
            neus_lyra_neus "Not to mention that now everyone will know who my butt belongs to"
            scene black with dissolve
            ""
        "Sex":
            scene two_bodies_bath0_11_1 with dissolve
            neus_lyra_neus "{e_heartbt2=FF0000}"
            scene two_bodies_bath0_12 with dissolve
            neus "Well, I'm going to start moving now"
            scene two_bodies_bath0_13 with dissolve
            play char3 sex7
            play char2 kissing1 loop #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            if incest_story:
                neus "Your cock is perfect for my pussy, brother"
            else:
                neus "Your cock is perfect for my pussy"
            neus "For all the times we have made love, my body has perfectly adapted to yours"
            neus_lyra "*kissing*"
            menu:
                "Inside": 
                    $ probability_of_pregnancy_bonus=0
                    stop char3
                    stop char2
                    play charM cum1
                    scene two_bodies_bath0_14 with dissolve
                    if set_active_pregnancy and not(is_tb_pregnant_start):
                        show screen tb_preegnancy_screen
                    play char1 climax2
                    neus "Uh!"
                    stop char1 fadeout 1.0                    
                    scene two_bodies_bath0_15 with dissolve
                    neus "You definitely filled me up a lot"
                    if not is_tb_pregnant:
                        if incest_story:
                            neus "Brother, you know I'm not on birth control, right?"
                            mc "Yes little sister, I know"
                        else:
                            neus "You know I'm not on birth control, right?"
                            mc "Yes, I know"
                    else:
                        if incest_story:
                            neus "Brother, you know I'm already pregnant, right?"
                            mc "Yes, I know little sister"
                        else:
                            neus "You know I'm already pregnant, right?"
                            mc "Yes, I know"
                    scene two_bodies_bath0_16 with dissolve
                    neus "{e_musical2=FFF}"
                    scene two_bodies_bath0_17 with w9    
                    if not is_tb_pregnant:
                        if incest_story:
                            neus_lyra "You know brother, my eggs also want to be fertilized"   
                        else:                
                            neus_lyra "You know, my eggs also want to be fertilized"    
                    else:
                        if incest_story:
                            neus_lyra "You know brother, you should cum inside me too, that way both of our eggs are doubly fertilized"   
                        else:                
                            neus_lyra "You know, you should cum inside me too, that way both of our eggs are doubly fertilized"    
                    scene two_bodies_bath0_18 with dissolve   
                    play char3 sex7             
                    neus_lyra "I want you to fill me up a lot"
                    neus_lyra "I want you to drown my eggs with your sperm so they can't escape"
                    if not is_tb_pregnant:
                        neus_lyra "And get them fertilized"
                    else:
                        neus_lyra "And make sure they're fertilized"
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene two_bodies_bath0_19 with dissolve
                    play char1 climax1
                    neus_lyra "UH!"
                    stop char1 fadeout 1.0
                    menu:
                        "More":
                            scene two_bodies_bath0_20 with dissolve
                            play char1 double_climax2
                            neus_lyra_neus "I'm cumming {e_heartbt=FF0000}"
                            if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start): 
                                $ probability_of_pregnancy_bonus+=20                
                                "Chance of pregnancy increased by 20%%"
                    scene two_bodies_bath0_21 with w21
                    play ambience bathtub fadein 1.0 volume 0.15 if_changed
                    call tb_pregnancy_ramdom_check(_("My uterus is so full of semen, I'm sure I'll get pregnant.")) from _call_tb_pregnancy_ramdom_check_1 
                    stop ambience fadeout 1.0
                    scene black with dissolve                           
                    ""
                    jump two_bodies_time_advances                                 
                "Outside":
                    stop char3
                    stop char2
                    play charM cum1
                    scene two_bodies_bath0_22 with dissolve
                    play char1 climax1
                    neus "Oh!"                          
                    scene two_bodies_bath0_23 with dissolve
                    ""
                    stop char1 fadeout 1.0
                    scene black with dissolve                           
                    ""
                    jump two_bodies_bath                          
        "Back":
            jump two_bodies_rooms
    jump two_bodies_bath
label  two_bodies_bath2:
    play ambience bathtub fadein 1.0 volume 0.15
    scene tb_bath_pregnant2_1 with storyfx
    menu:
        "Assjob":
            scene tb_bath_pregnant2_2 with dissolve
            neus "I guess it's inevitable"
            scene tb_bath_pregnant2_3 with dissolve
            neus_lyra "I'm going to make you feel very good with my big ass"
            neus "..."
            scene tb_bath_pregnant2_4 with dissolve
            if incest_story:
                neus_lyra "Are you enjoying the view brother?"
                mc "Yeah, I love my sister's little ass"
            else:
                neus_lyra "Are you enjoying the view?"
                mc "Yeah, I love that little ass"
            scene tb_bath_pregnant2_5 with dissolve
            neus "Hehe, well, let's get started"
            scene tb_bath_pregnant2_6 with dissolve
            play char3 handjob2
            neus_lyra "I'm going to make you feel very good with my ass"
            neus_lyra "So much so, that you impregnate my ass like you did with my uterus"
            if incest_story:
                neus_lyra "Bathe my ass with lots of your semen brother!"
            else:
                neus_lyra "Bathe my ass with lots of your semen!"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_bath_pregnant2_7 with dissolve
            ""
            neus "Wow, I see you're also trying to impregnate my ass, hehe"
            scene black with dissolve
            "They clean themselves"
        "Massage belly":
            scene tb_bath_pregnant2_8 with dissolve
            if incest_story:
                neus "A free massage from my brother... I guess it's impossible to turn that down."
            else:
                neus "A free massage... I guess it's impossible to turn that down."
            scene tb_bath_pregnant2_9 with w33
            play char3 handjob2
            neus "You like to caress my pregnant belly. Huh? {e_heartbt=cc0066}"
            neus_lyra "I love your massage, it feels so good."
            scene tb_bath_pregnant2_10 with dissolve
            stop char3 fadeout 1.5
            if incest_story:
                "You have a good time with your sister."
            else:
                "You have a good time with [neusname] and [neusname_lyra]."
            scene black with dissolve
            ""
            jump two_bodies_time_advances
        "Back":
            jump two_bodies_rooms
    jump two_bodies_bath2
label  two_bodies_bath3:
    play ambience bathtub fadein 1.0 volume 0.15
    scene tb_bath_pregnant3_1 with storyfx
    menu:
        "Assjob":
            scene tb_bath_pregnant3_2 with dissolve
            neus_lyra "Hehe"
            scene tb_bath_pregnant3_3 with dissolve
            if incest_story:
                neus_lyra "Do you like to feel my pregnant ass brother?"
            else:
                neus_lyra "Do you like to feel my pregnant ass?"
            mc "Yes"
            scene tb_bath_pregnant3_4 with dissolve
            neus_lyra_neus "{e_heartbt=FF0000}"
            scene tb_bath_pregnant3_5 with dissolve
            play char3 handjob2
            neus_lyra "Come on, come on, cum on my ass"
            neus "Mark it as yours"
            neus_lyra "Just like you did with my uterus"
            ""
            stop char3
            play charM cum1
            scene tb_bath_pregnant3_6 with dissolve
            ""
            scene tb_bath_pregnant3_7 with dissolve
            if incest_story:
                neus "Wow, brother, that's a lot"
            else:
                neus "Wow, that's a lot"
            neus_lyra "With this much cum my ass will always be impregnated with your smell"
            scene black with dissolve
            "They clean themselves"
        "Sex":
            scene tb_bath_pregnant3_8 with dissolve
            neus_lyra_neus "{e_heartbt2=FF0000}"
            scene tb_bath_pregnant3_9 with dissolve
            play char1 double_penetration2
            neus_lyra_neus "Mmm!"
            scene tb_bath_pregnant3_10 with dissolve
            play char3 double_sex1
            neus_lyra_neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            if incest_story:
                neus_lyra_neus "Brother, it feels so good"
            else:
                neus_lyra_neus "It feels so good"
            neus_lyra_neus "I've been desperately wanting this"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_bath_pregnant3_11 with dissolve
            play char1 double_climax2
            neus_lyra_neus "{sc=2}{=lust_style}Uh!{/sc}"
            stop char1 fadeout 2.0
            scene tb_bath_pregnant3_12 with dissolve
            ""
            scene black with dissolve
            "They clean themselves"
        "Back":
            jump two_bodies_rooms
    jump two_bodies_bath3
#----------------------------------------mc_evening_room_quest----------------------------------------
label  two_bodies_mc_evening:
    scene two_bodies_mc_evening0_2 with storyfx
    menu:
        "Cat lingerie"(two_bodies_outfit_is_active_outfit):
            if not(is_view_intro_two_bodies_outfit_cat):
                $ is_view_intro_two_bodies_outfit_cat=True                
                scene two_bodies_mc_evening0_3 with dissolve 
                neus "..."(multiple=2) 
                neus_lyra "I would love to try it on."(multiple=2)
                scene two_bodies_mc_evening0_4 with w33
                neus "..."
                scene two_bodies_mc_evening0_5 with dissolve
                neus "I don't like this cat outfit."
                scene two_bodies_mc_evening0_6 with dissolve
                neus "I'm going to change back into my regular clothes."
                scene two_bodies_mc_evening0_7 with dissolve
                play sound magical1 volume 0.3
                neus "{sc=1}Eh!?{/sc}"(multiple=2) 
                neus_lyra "{font=fonts/Alkatra-Regular.ttf}Touch{/font}"(multiple=2)
                play sound2 whoosh1
                scene two_bodies_mc_evening0_8 with pushri
                if incest_story:
                    neus "Big brother, I love this outfit, it's so cute."
                else:
                    neus "I love this outfit, it's so cute."
                neus "And it shows my true form."
                scene two_bodies_mc_evening0_9 with dissolve
                if incest_story:
                    neus "A hungry kitten who wants to be fed lots of her brother's milk."
                    neus "And have many litters of kittens with him."
                    scene two_bodies_mc_evening0_10 with dissolve
                    neus_lyra "What would you like to do first, brother?"
                else:
                    neus "A hungry kitten who wants to be fed lots of milk."
                    neus "And have many litters of kittens."
                    scene two_bodies_mc_evening0_10 with dissolve
                    neus_lyra "What would you like to do first?"
                scene two_bodies_mc_evening0_11 with dissolve
                play char1 ahegao1
                neus "{bt=2}{=lust_style}Ahhhhh{/bt}"(multiple=2) 
                neus_lyra "Feed your hungry kittens?"(multiple=2)
                stop char1 fadeout 2.0
                scene two_bodies_mc_evening0_12 with dissolve
                ""
                scene two_bodies_mc_evening0_13 with dissolve
                if not is_tb_pregnant:
                    neus  "Or impregnate your little kittens who are in heat and only think about reproducing?"   
                else:
                    neus  "Or fill your impregnated little kittens with lots of your milk?"               
            else:
                scene two_bodies_mc_evening0_14 with dissolve 
                neus_lyra_neus "Okey"
            $ is_two_bodies_outfit_cat=True
            jump two_bodies_mc_evening_outfit_cat
        "Pole dance":
            scene two_bodies_mc_evening0_109 with dissolve
            neus "mmm... so that's what that pole is for."
            scene two_bodies_mc_evening0_110 with dissolve
            neus_lyra "I would love..."
            scene two_bodies_mc_evening0_111 with dissolve
            neus "You know, I'm not good at dancing, but I could try if you also dance for me."
            scene two_bodies_mc_evening0_110 with dissolve
            neus_lyra "I like that idea."
            menu:
                "Accept":                    
                    mc "I'd love to, though I didn't expect you to ask."
                    scene two_bodies_mc_evening0_112 with dissolve
                    if incest_story:
                        neus "What's wrong with that? I just want to see my big brother dance."
                    else:
                        neus "What's wrong with that? I just want to see my boyfriend dance."
                    neus "Considering we're a couple, isn't that a pretty normal thing to ask for?"
                    scene two_bodies_mc_evening0_113 with dissolve
                    mc "I guess so."
                    mc "Although I'm going to miss your cute embarrassed reactions."
                    scene two_bodies_mc_evening0_114 with dissolve
                    if incest_story:
                        neus "Hehe, well sorry brother, from now on, you will never see those expressions on my face again."
                    else:
                        neus "Hehe, well sorry, from now on, you will never see those expressions on my face again."
                    scene two_bodies_mc_evening0_115 with storyfx
                    neus "This outfit is a bit..."
                    mc "I love it, and not to mention it comes with that cute reaction."
                    scene two_bodies_mc_evening0_116 with dissolve
                    neus "Agh..."
                    scene two_bodies_mc_evening0_117 with dissolve
                    $ xsize_value = 650
                    menu(screen="custom_choice_enhanced"):
                        neus_lyra_neus "What would you like us to call you?"
                        "Customer (default)":
                            $ customer_name = "dear ''customer''"
                        "Brother" if incest_story:
                            $ customer_name = "brother"
                        "Enter custom name":
                            if persistent.gallery_customer_name != "dear ''customer''":
                                $ customer_name = renpy.input(_("What would you like them to call you? (Default: customer)"), default=persistent.gallery_customer_name, exclude='\\[{')
                            else:
                                $ customer_name = renpy.input(_("What would you like them to call you? (Default: customer)"), exclude='\\[{') 
                            $ customer_name = customer_name.strip()
                            if customer_name == "":
                                $ customer_name = "dear ''customer''" 
                            $ persistent.gallery_customer_name = customer_name
                    neus_lyra "Well Well, [customer_name], what would you like first?"
                    mc "Mmm ... a dance would be nice."                    
                    play music funk_funkadelic_funkstorm
                    neus_lyra "Hehe, At your service, [customer_name]." 
                    play sound whoosh2                                     
                    scene two_bodies_mc_evening0_118 with pushri
                    ""
                    scene two_bodies_mc_evening0_119 with dissolve
                    ""
                    scene two_bodies_mc_evening0_120 with dissolve
                    ""
                    scene two_bodies_mc_evening0_121 with dissolve
                    ""
                    $ renpy.music.set_volume(0.3,delay=3.5,channel='music')
                    scene two_bodies_mc_evening0_122 with spellfx
                    neus "Did you like the show, [customer_name]?"
                    scene two_bodies_mc_evening0_123 with dissolve
                    mc "Yes, I loved it."
                    neus "Please, [customer_name], it is forbidden to touch the staff."
                    scene two_bodies_mc_evening0_124 with dissolve
                    mc "Could an exception be made?"
                    neus "It could be considered, but you will have to meet a condition."
                    scene two_bodies_mc_evening0_125 with dissolve
                    neus_lyra "This hole feels so lonely."
                    neus_lyra "and it's very hungry for milk."
                    scene two_bodies_mc_evening0_126 with dissolve
                    neus "You could fill it with your milk [customer_name]"
                    scene two_bodies_mc_evening0_127 with dissolve
                    ""
                    scene two_bodies_mc_evening0_128 with dissolve
                    play char1 penetration1
                    neus "Uh!"
                    $ renpy.music.set_volume(0.05,delay=1.5,channel='music')
                    scene two_bodies_mc_evening0_129 with dissolve
                    play char3 sex6
                    neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
                    neus "{e_heartbt2=cc0066}"
                    menu:
                        "Cum":
                            stop char3
                            play charM cum1
                    if set_active_pregnancy and not(is_tb_pregnant_start):
                        show screen tb_preegnancy_screen
                    scene two_bodies_mc_evening0_130 with hpunch
                    play char1 climax1
                    neus "{sc=2}{=lust_style}Uh!{/sc}"
                    $ renpy.music.set_volume(0.35,delay=3.5,channel='music')
                    scene two_bodies_mc_evening0_131 with dissolve
                    ""
                    scene two_bodies_mc_evening0_132 with dissolve
                    play char2 penetration2
                    neus_lyra "Uh!"
                    $ renpy.music.set_volume(0.05,delay=1.5,channel='music')
                    scene two_bodies_mc_evening0_133 with dissolve
                    play char3 sex4
                    neus_lyra "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
                    neus_lyra "{e_heartbt2=cc0066}"
                    menu:
                        "Cum":
                            stop char3
                            play charM cum1
                    scene two_bodies_mc_evening0_134 with hpunch
                    play char2 climax1
                    neus_lyra "{sc=2}{=lust_style}Uh!{/sc}"
                    stop music fadeout 2.0
                    scene black with dissolve               
                    if incest_story:
                        "You have a little more fun with your sister."
                    else:     
                        "You have a little more fun with [neusname] and [neusname_lyra]."
                    if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start): 
                        $ probability_of_pregnancy_bonus+=30
                        "Chance of pregnancy increased by 30%%"
                    play char3 breathing1
                    scene two_bodies_mc_evening0_135 with dissolve
                    if incest_story:
                        neus "Uff, that was so intense brother."
                    else:
                        neus "Uff, that was so intense brother."
                    scene two_bodies_mc_evening0_136 with dissolve
                    neus_lyra "I hope you haven't forgotten your promise."
                    neus "I want you to dance for me."
                    stop char3 fadeout 1.0
                    $ renpy.music.set_volume(1.0,delay=1.0,channel='music')
                    scene black with dissolve
                    if incest_story:
                        "You spend quality time with your little sister."
                    else:
                        "You spend quality time with [neusname] and [neusname_lyra]."
                    call tb_pregnancy_ramdom_check() from _call_tb_pregnancy_ramdom_check_3
                    jump two_bodies_time_advances
                "Reject":
                    scene two_bodies_mc_evening0_111 with dissolve
                    neus "In that case, I also reject."
                    scene two_bodies_mc_evening0_110 with dissolve
                    if incest_story:
                        neus_lyra "I'm sorry brother, even though I would love to dance on that pole for you."
                    else:
                        neus_lyra "I'm sorry, even though I would love to dance on that pole for you."
                    neus_lyra "I also want to see you dance."
        "Date":
            scene two_bodies_mc_evening0_14 with dissolve 
            if incest_story:
                neus_lyra_neus "I would love to, brother."
            else:
                neus_lyra_neus "I would love to."
            play ambience people volume 0.2
            scene two_bodies_mc_evening0_39 with w33 
            neus_lyra "That was a long journey."
            scene two_bodies_mc_evening0_40 with dissolve 
            mc "I like your outfits."
            scene two_bodies_mc_evening0_41 with dissolve 
            neus_lyra_neus "Thank you"
            scene two_bodies_mc_evening0_42 with w24 
            waitress "Your food will be served shortly."
            scene two_bodies_mc_evening0_43 with dissolve
            if incest_story:
                neus_lyra "Hey brother, while we're waiting for the food..."
            else:
                neus_lyra "Hey, while we're waiting for the food..."
            neus_lyra "How about we have some fun?"
            menu:
                "Diversion":
                    play sound whoosh1
                    scene two_bodies_mc_evening0_44 with pushdolong
                    neus_lyra "Hehe"
                    scene two_bodies_mc_evening0_45 with dissolve
                    play char3 suck2
                    neus_lyra "Lick suck"
                    neus_lyra "Delicious"
                    neus "Hey, can you stop doing that?"
                    scene two_bodies_mc_evening0_46 with dissolve
                    waitress "Here are the three appetizers you ordered."
                    waitress "Excuse me for asking, but I notice you're missing someone."
                    neus "S-She had to go to the bathroom."
                    waitress "I understand. If you'll excuse me, I'll withdraw.."
                    stop char3
                    scene two_bodies_mc_evening0_47 with dissolve
                    neus "Can you stop?"
                    neus_lyra "Don't you want this appetizer?"
                    scene two_bodies_mc_evening0_48 with dissolve
                    neus "Well… if it's just an appetizer."
                    scene two_bodies_mc_evening0_49 with dissolve
                    play char3 double_suck1
                    neus_lyra_neus "*Suck lick*"
                    menu:
                        "Cum":
                            pass
                    scene two_bodies_mc_evening0_50 with dissolve
                    stop char3
                    play charM cum1
                    ""
                    scene two_bodies_mc_evening0_51 with dissolve
                    neus "What a waste, all his milk is spilling."
                    scene two_bodies_mc_evening0_52 with dissolve
                    if incest_story:
                        "Your little sister cleans your cock until it's shiny, though there were a few lipstick stains left behind."
                    else:
                        "They clean your cock until it's shiny, though there were a few lipstick stains left behind."
                    scene two_bodies_mc_evening0_53 with pushuplong2
                    waitress "Here's your first course."
                    scene two_bodies_mc_evening0_54 with circlefx
                    neus "That was delicious."
                    scene two_bodies_mc_evening0_55 with dissolve
                    neus "But I think I should head to the bathroom now, and fix up my makeup before anyone notices."
                    scene two_bodies_mc_evening0_56 with dissolve
                    mc "(That food was good, although I prefer simpler things-)"
                    scene two_bodies_mc_evening0_57 with dissolve
                    strange_woman "Hello, how are you handsome? Do you want to have a good time?"
                    strange_woman "I’m sure I have qualities that could satisfy your needs."(multiple=2)
                    mc "No thanks, I'm not interested"(multiple=2)
                    scene two_bodies_mc_evening0_58 with dissolve
                    strange_woman "Are you sure you wouldn't prefer qualities that are a bit more... substantial, ones that fill your hand?"
                    strange_woman "Bla bla bla"(multiple=2)
                    "After a while you stop paying attention to what the woman is babbling."(multiple=2)
                    scene two_bodies_mc_evening0_59 with dissolve
                    strange_woman "Bla bla bla"(multiple=2)
                    mc "(The previous dishes were fine, but this one in particular is delicious.)"(multiple=2)
                    mc "(I wonder how they prepared it)"
                    mc "(Maybe I could ask the chef for the recipe-)"
                    scene two_bodies_mc_evening0_60 with dissolve
                    strange_woman "Hey, are you paying attention to me?"
                    scene two_bodies_mc_evening0_61 with dissolve
                    mc "Oh, I'm sorry, I didn't realize you were still here."
                    mc "Doctors diagnosed me with attention deficit disorder, I struggle paying attention to things that I'm not very interested in, sorry."
                    strange_woman "Hah!"
                    scene two_bodies_mc_evening0_62 with dissolve
                    neus_lyra "That was so refreshing."
                    strange_woman "Tsk"
                    scene two_bodies_mc_evening0_63 with dissolve
                    strange_woman "*Murmuring as she walks away* {size=-15}If it wasn’t for his obvious wealth, I wouldn’t have wasted my time on someone with such a hideous haircut."(multiple=2)
                    neus_lyra "Who was that woman?"(multiple=2)
                    scene two_bodies_mc_evening0_64 with dissolve
                    strange_woman "{sc=2}{size=-15}Mushroom head{/sc}"(multiple=2)
                    mc "No clue, probably just another gold digger looking for her next target."(multiple=2)
                    scene two_bodies_mc_evening0_63 with dissolve
                    neus_lyra "You seem to attracted those kind of woman."
                    neus_lyra "Although thanks to that I haven't had any real competition."
                    scene two_bodies_mc_evening0_65 with dissolve
                    mc "I'm surprised that woman still has her head attached to her body."
                    scene two_bodies_mc_evening0_66 with dissolve
                    neus_lyra "What kind of psychopath do you think I am? That would be very rude of me after you invited us on this date."
                    neus_lyra "Besides, you rejected her, so I have no reason to be jealous."
                    scene two_bodies_mc_evening0_67 with dissolve
                    mc "Hmm..."
                    menu:
                        "Mess with her":
                            mc "I'm sorry for doubting you, but I thought a yandere was supposed to be calculating and ruthless."
                            mc "It's true that I rejected her and only love you, but shouldn't a true yandere make sure to eliminate any possibility of failure?"
                            mc "Are you sure you're really a yandere? You’re not an imposter, are you?"
                            scene two_bodies_mc_evening0_68 with dissolve
                            neus_lyra "Hah, do you think I don't feel like gutting her?"
                            scene two_bodies_mc_evening0_66 with dissolve
                            if incest_story:
                                neus_lyra "Heh, I see what you're trying to do, brother."
                            else:
                                neus_lyra "Heh, I see what you're trying to do."
                            neus_lyra "You know, I am well aware that my feelings are twisted"
                            neus_lyra "And as you know, I developed that plan to leave you with my healthier side and these twisted feelings would disappear."
                            neus_lyra "Obviously my methods were questionable."
                            scene two_bodies_mc_evening0_69 with dissolve
                            neus_lyra "But you accepted these feelings"
                            neus_lyra "Which made me very happy and well, I try to cause as few problems as possible so you don't regret your decision."
                            neus_lyra "Obviously, I want to slit that busty bitch’s throat for trying to get close to my boyfriend."
                            neus_lyra "But I try to be better."
                            scene two_bodies_mc_evening0_70 with dissolve
                            stop ambience fadeout 0.5
                            play music the_truth_is_in_the_dark fadein 1.0
                            neus_lyra "Although if you wanted me to admit my killer instinct."
                            scene two_bodies_mc_evening0_71 with dissolve                            
                            waitress "Would you like to order anything else?"(multiple=2)
                            neus_lyra "I admit I wanted to break that bitch's neck-"(multiple=2)
                            scene two_bodies_mc_evening0_72 with dissolve
                            stop music fadeout 1.0
                            play ambience people volume 0.2 fadeout 1.0
                            mc "Thank you very much, but we are about to leave, although it would be great if you could get me the recipe for dish 20."
                            waitress "*scared* U-Understood, I will ask the chef."
                            scene two_bodies_mc_evening0_73 with dissolve
                            neus_lyra "I'm sorry."                           
                            mc "Don't worry about it, in the end I was the one who provoked you."
                            scene two_bodies_mc_evening0_74 with dissolve
                            neus "That was refreshing."
                            scene two_bodies_mc_evening0_75 with dissolve
                            neus "I see you managed to behave yourself, more or less, while I was gone."
                            scene two_bodies_mc_evening0_76 with dissolve
                            neus "Ready to head out?"
                        "Pass":
                            scene two_bodies_mc_evening0_74 with dissolve
                            neus "That was refreshing."
                            scene two_bodies_mc_evening0_75 with dissolve
                            neus "I see you managed to behave yourself, more or less, while I was gone."
                            scene two_bodies_mc_evening0_76 with dissolve
                            neus "Ready to head out?"
                    scene two_bodies_mc_evening0_77 with w18
                    play ambience night_ambience volume 0.1 fadein 1.0
                    if incest_story:
                        neus "So, what should we do now brother?"
                    else:
                        neus "So, what should we do now?"
                    menu:
                        "Hotel":
                            scene two_bodies_mc_evening0_78 with w21
                            stop ambience
                            play char3 kissing1
                            neus_lyra "This place is nice"
                            neus "*Kisses*"
                            scene two_bodies_mc_evening0_79 with dissolve
                            neus "I want more kisses."
                            neus "More, more."
                            scene two_bodies_mc_evening0_80 with dissolve
                            if incest_story:
                                neus_lyra "I also want you to kiss me, brother."
                            else:
                                neus_lyra "I also want you to kiss me."
                            scene two_bodies_mc_evening0_81 with dissolve
                            neus_lyra "*Kisses*"
                            scene two_bodies_mc_evening0_82 with dissolve
                            neus "*Kisses*"
                            stop char3
                            scene two_bodies_mc_evening0_83 with dissolve
                            if incest_story:
                                neus_lyra_neus "I'm already very wet, I want you inside me, brother."
                            else:
                                neus_lyra_neus "I'm already very wet, I want you inside me."
                            menu:
                                "[neusname]":
                                    scene two_bodies_mc_evening0_84 with dissolve
                                    ""
                                    scene two_bodies_mc_evening0_85 with dissolve
                                    play  char3 sex6
                                    neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                                    ""
                                    menu:
                                        "Cum":
                                            pass
                                    stop char3
                                    play charM cum1
                                    scene two_bodies_mc_evening0_86 with hpunch
                                    if set_active_pregnancy and not(is_tb_pregnant_start):
                                        show screen tb_preegnancy_screen
                                    play char1 climax1
                                    neus "Uh!"
                                    scene two_bodies_mc_evening0_87 with dissolve
                                    if incest_story:
                                        neus_lyra "Brother, I also want you to fill me up."
                                    else:
                                        neus_lyra "I also want you to fill me up."
                                    scene two_bodies_mc_evening0_88 with dissolve
                                    play  char3 sex5
                                    neus_lyra "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                                    menu:
                                        "Cum":
                                            pass
                                    stop char3
                                    play charM cum1
                                    scene two_bodies_mc_evening0_89 with dissolve
                                    play char1 climax1
                                    neus_lyra "Uh!"
                                "[neusname_lyra]":
                                    scene two_bodies_mc_evening0_87 with dissolve
                                    ""
                                    scene two_bodies_mc_evening0_88 with dissolve
                                    play  char3 sex6
                                    neus_lyra "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                                    menu:
                                        "Cum":
                                            pass
                                    stop char3
                                    play charM cum1
                                    scene two_bodies_mc_evening0_89 with hpunch
                                    if set_active_pregnancy and not(is_tb_pregnant_start):
                                        show screen tb_preegnancy_screen
                                    play char1 climax1
                                    neus_lyra "Uh!"
                                    scene two_bodies_mc_evening0_84 with dissolve
                                    if incest_story:
                                        neus "Big brother... can you also give me a bit of love?"
                                    else:
                                        neus "Can you also give me a bit of love?"
                                    scene two_bodies_mc_evening0_85 with dissolve
                                    play  char3 sex5
                                    neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                                    menu:
                                        "Cum":
                                            pass
                                    stop char3
                                    play charM cum1
                                    scene two_bodies_mc_evening0_86 with dissolve
                                    play char1 climax1
                                    neus "Uh!"
                            scene two_bodies_mc_evening0_90 with dissolve
                            play char3 breathing1
                            menu:
                                "More":
                                    stop char3
                                    scene two_bodies_mc_evening0_91 with fadesex
                                    neus_lyra_neus "*lick suck*"
                                    scene two_bodies_mc_evening0_92 with dissolve
                                    play char3 deep_suck1
                                    neus "*Suck Suck*"
                                    neus "{e_heartbt2=cc0066}"
                                    scene two_bodies_mc_evening0_93 with dissolve
                                    neus_lyra "*Suck Suck*"
                                    neus_lyra "{e_heartbt2=760272}"
                                    scene two_bodies_mc_evening0_94 with dissolve
                                    play char3 sex5
                                    neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                                    neus_lyra "Yes, keep fucking my tight pussy."
                                    if not is_tb_pregnant:
                                        if incest_story:
                                            neus_lyra "Cum inside your little sister, I want to be impregnated by my big brother."
                                        else:
                                            neus_lyra "Cum inside, I want you to impregnate me."
                                    else:
                                        if incest_story:
                                            neus_lyra "Cum inside your little sister, I want to be full with my big brother's cum."
                                        else:
                                            neus_lyra "Cum inside, I want to be full with your cum."

                                    neus "Yes, I want it inside!"
                                    stop char3
                                    play charM cum1
                                    scene two_bodies_mc_evening0_95 with dissolve
                                    play char1 climax2
                                    neus "Uh!"
                                    if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start): 
                                        $ probability_of_pregnancy_bonus+=10
                                        "Chance of pregnancy increased by 10%%"
                                    stop char1 fadeout 1.0
                                    scene two_bodies_mc_evening0_96 with dissolve
                                    play char3 sex4
                                    neus_lyra "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                                    if incest_story:
                                        neus_lyra "Yes.. brother... keep fucking me hard."
                                    else:
                                        neus_lyra "Yes, keep fucking me hard."
                                    neus_lyra "Destroy me until my mind goes blank."
                                    neus_lyra "I'm cumming!"
                                    stop char3
                                    play charM cum1
                                    scene two_bodies_mc_evening0_97 with dissolve
                                    play char1 climax1
                                    neus_lyra "Uh!"
                                    if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start): 
                                        $ probability_of_pregnancy_bonus+=10
                                        "Chance of pregnancy increased by 10%%"
                                    scene two_bodies_mc_evening0_98 with dissolve
                                    play char3 breathing1
                                    play char1 french01
                                    neus_lyra_neus "*kiss*"
                                    menu:
                                        "More":
                                            stop char3
                                            scene two_bodies_mc_evening0_99 with dissolve
                                            neus "This feels so good..."
                                            neus "I can't think of anything else... my mind is overwhelmed with pleasure."
                                            scene two_bodies_mc_evening0_100 with dissolve
                                            if not is_tb_pregnant:
                                                if incest_story:
                                                    neus_lyra_neus "I just want to reproduce with my brother."
                                                else:
                                                    neus_lyra_neus "I just want to reproduce."
                                            else:
                                                if incest_story:
                                                    neus_lyra_neus "I just want to make love with my brother."
                                                else:
                                                    neus_lyra_neus "I just want to make love with you."
                                            neus_lyra "The room is so dirty."
                                            neus "It stinks of our body odors"
                                            scene two_bodies_mc_evening0_101 with dissolve
                                            play char3 double_sex3
                                            neus_lyra_neus "{bt=2}{=lust_style}ah ah ah ah{/bt}"
                                            neus_lyra_neus "{bt=2}{=lust_style}I'm cumming! {e_heartbt2=cc0066}{/bt}"
                                            stop char3
                                            play charM cum1
                                            scene two_bodies_mc_evening0_102 with dissolve
                                            play char1 double_climax2
                                            neus_lyra_neus "Uh!"
                                            neus_lyra_neus "{e_heartbt2=cc0066}"
                                            if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start): 
                                                $ probability_of_pregnancy_bonus+=20
                                                "Chance of pregnancy increased by 20%%"
                                            menu:
                                                "Make love":
                                                    stop char1 fadeout 1.0
                                                    play char3 breathing1 volume 0.5
                                                    scene two_bodies_mc_evening0_103 with dissolve
                                                    if incest_story:
                                                        mc "I'm going to make love to you all night, little sister."
                                                    else:
                                                        mc "I'm going to make love to you all night."
                                                    mc "Until your minds and bodies know how much I love you."
                                                    neus "That's unfair, just by whispering that you're making me cum."
                                                    scene two_bodies_mc_evening0_104 with w33
                                                    if incest_story:
                                                        neus_lyra "Brother, please, keep saying these words to me."
                                                    else:
                                                        neus_lyra "Please, keep saying these words to me."
                                                    neus_lyra "It makes me cum just by hearing them."
                                                    neus_lyra "Please, tell me more."
                                                    scene two_bodies_mc_evening0_105 with w9
                                                    mc "You're so cute and so hot."
                                                    mc "You've always been by my side, you're the only thing I need"
                                                    if incest_story:
                                                        mc "I love you, little sister."
                                                    else:
                                                        mc "I love you."
                                                    stop char3 fadeout 1.0
                                                    scene two_bodies_mc_evening0_106 with dissolve
                                                    play char1 double_climax2
                                                    neus_lyra_neus "{bt=2}{=lust_style}Uhhh, I'm cumming!{/bt}"
                                                    neus_lyra_neus "{bt=2}{=lust_style}I love you too, very much{/bt}"
                                                    ""
                                                    stop char1 fadeout 1.0
                                                    scene two_bodies_mc_evening0_107 with w9
                                                    if incest_story:
                                                        "You spend the night making love to your little sister."      
                                                    else:
                                                        "You spend the night making love."                                                   
                                                    scene black with dissolve
                                                    if set_active_pregnancy and not(probability_of_pregnancy==0) and not(is_tb_pregnant_start): 
                                                        $ probability_of_pregnancy_bonus+=30
                                                        "Chance of pregnancy increased by 30%%"
                                                    call tb_pregnancy_ramdom_check() from _call_tb_pregnancy_ramdom_check_4
                                                    ""
                                                    play ambience morning_sounds fadein 0.5
                                                    scene two_bodies_mc_evening0_108 with eyeopen
                                                    neus_lyra_neus "I can barely stand with how sore my legs are."
                                                    neus_lyra "But that was amazing."
                                                    neus "Yes."
                                                    scene black with dissolve
                                                    if incest_story:
                                                        "After a short car ride, you return home with your sister."
                                                    else:
                                                        "After a short car ride, you return home with [neusname] and [neusname_lyra]."
                                                "Stop":
                                                    stop char1 fadeout 1.0
                                                    scene black with dissolve
                                                    if incest_story:
                                                        "You and your little sister spend the night at the hotel, then head back home together."
                                                    else:
                                                        "You sleep with [neusname] and [neusname_lyra] at the hotel and then go back home with them."
                                        "Stop":
                                            stop char3 fadeout 1.0
                                            scene black with dissolve
                                            if incest_story:
                                                "You and your little sister spend the night at the hotel, then head back home together."
                                            else:
                                                "You sleep with [neusname] and [neusname_lyra] at the hotel and then go back home with them."
                                "Stop":
                                    stop char3 fadeout 1.0
                                    scene black with dissolve
                                    if incest_story:
                                        "You and your little sister spend the night at the hotel, then head back home together."
                                    else:
                                        "You sleep with [neusname] and [neusname_lyra] at the hotel, then go back home with them."
                        "Return home":
                            stop ambience fadeout 1.0
                            scene black with dissolve
                            if incest_story:
                                "After a somewhat long journey, you return home with your sister."
                            else:
                                "After a somewhat long journey, you return home with [neusname] and [neusname_lyra]."
                "No":
                    if incest_story:
                        "You enjoy the date with your little sister."
                    else:
                        "You enjoy the date with neus and lyra."
                    scene black with dissolve
                    "And after a somewhat long journey, you return home with them."
            jump two_bodies_sleeping_event
        "Leave":
            jump two_bodies_rooms
    jump two_bodies_mc_evening
label  two_bodies_mc_evening_outfit_cat:
    scene two_bodies_mc_evening0_15 with storyfx
    menu:
        "Regular outfit":
            scene two_bodies_mc_evening0_16 with dissolve
            neus_lyra_neus "Okey"
            $ is_two_bodies_outfit_cat=False
            jump two_bodies_mc_evening
        "Blowjob":
            scene two_bodies_mc_evening0_17 with w9
            neus_lyra "So you're finally going to feed your hungry kittens."
            scene two_bodies_mc_evening0_18 with fadesex
            play char3 double_suck1
            neus_lyra_neus "*Lick*"
            neus_lyra_neus "I'm very hungry."
            menu:
                "Fuck her throat":
                    scene two_bodies_mc_evening0_19 with fadesex
                    play char3 deep_suck1
                    neus_lyra "(This is so intense)"
                    if incest_story:
                        neus_lyra "(I'm going to receive my brother's milk directly in my stomach)"
                    else:
                        neus_lyra "(I'm going to receive his milk directly in my stomach)"
                    neus "(It's kind of hot to see how my throat is being fucked)"
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene two_bodies_mc_evening0_20 with dissolve
                    neus_lyra "{sc=4}{=lust_style}Uh!{/sc}"
                    play char1 gulp1
                    scene two_bodies_mc_evening0_21 with dissolve
                    neus_lyra "Gulp"
                    play char1 ahegao1
                    scene two_bodies_mc_evening0_22 with dissolve
                    neus_lyra "{bt=4}{=lust_style}Aaaaa{/bt}"
                    if incest_story:
                        neus_lyra "Thanks for the meal brother."
                    else:
                        neus_lyra "Thanks for the meal."
                    scene two_bodies_mc_evening0_23 with dissolve
                    neus "I hope you haven't forgotten that there's still a hungry little kitten waiting for her milk."
                    scene two_bodies_mc_evening0_24 with w17
                    play charM cum1
                    neus "{sc=4}{=lust_style}Uh!{/sc}"
                    scene two_bodies_mc_evening0_25 with dissolve                    
                    neus_lyra "*Lick*"(multiple=2)
                    play char1 lick01
                    neus "(That milk was delicious)"(multiple=2)                    
                "Cum":
                    stop char3
                    play charM cum1
                    scene two_bodies_mc_evening0_26 with dissolve
                    ""
                    scene two_bodies_mc_evening0_27 with dissolve
                    neus_lyra_neus "Thank you for feeding your hungry kittens."
            scene black with dissolve
            ""
        "Sex":
            $ probability_of_pregnancy_bonus=0
            scene two_bodies_mc_evening0_28 with dissolve
            if incest_story:
                neus "May I have the first turn, brother?"
            else:
                neus "May I have the first turn?"
            scene two_bodies_mc_evening0_29 with dissolve
            neus "My wet little pussy is in heat, and my primal instincts really want this inside me."
            scene two_bodies_mc_evening0_30 with dissolve
            play char1 penetration1
            neus "Uh!"
            scene two_bodies_mc_evening0_31 with fadesex
            play char3 sex2
            neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            neus "My uterus needed this."
            neus "I have an irresistible desire to mate."
            if not is_tb_pregnant:
                neus "And have many kittens."
            else:
                neus "Even though I am already impregnated with many kittens."
            mc "I'm glad you're honest, especially when you're not under any spell."
            scene two_bodies_mc_evening0_32 with dissolve
            if incest_story:
                neus "I don't know what you're talking about brother, obviously I'm under my own spell."
            else:
                neus "I don't know what you're talking about, obviously I'm under my own spell."
            neus "It's not like I use this as an excuse to say what I want."
            neus "And you better forget about having any thoughts like that."
            scene two_bodies_mc_evening0_31 with dissolve
            neus "Just focus on filling your in heat kitten's uterus with lots of milk"
            menu:
                "Cum":
                    pass 
            if set_active_pregnancy and not(is_tb_pregnant_start):           
                show screen tb_preegnancy_screen
            stop char3
            play charM cum1
            scene two_bodies_mc_evening0_33 with dissolve
            play char1 climax1
            neus "Uh!"
            if set_active_pregnancy and not(is_tb_pregnant_start):
                $ probability_of_pregnancy_bonus+=20
                if incest_story:
                    "You increase your sister's chance of getting pregnant by an additional 20%% by depositing a large amount of sperm in her uterus."
                else:
                    "You increase [neusname]'s chance of getting pregnant by an additional 20%% by depositing a large amount of sperm in her uterus."
            scene two_bodies_mc_evening0_34 with dissolve
            if not is_tb_pregnant:
                neus_lyra "This kitten is also in heat, I want to have many litters of kittens."
            else:
                neus_lyra "This kitten is also in heat, and wants her uterus filling with lots of milk."
            scene two_bodies_mc_evening0_35 with w33
            play char3 sex5
            neus_lyra "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            menu:
                "Cum":
                    pass            
            stop char3
            play charM cum1
            scene two_bodies_mc_evening0_36 with dissolve
            play char1 climax2
            neus_lyra "Nya!"
            menu:
                "More":
                    scene two_bodies_mc_evening0_38 with dissolve                    
                    if set_active_pregnancy and not(is_tb_pregnant_start):
                        $ probability_of_pregnancy_bonus+=20
                        "Chance of pregnancy increased by 20%%"
                    else:
                        ""
                "Stop":
                    pass
            scene two_bodies_mc_evening0_37 with dissolve
            neus_lyra_neus "My stomach is so full."
            play ambience morning_sounds fadeout 1.0 fadein 1.0 if_changed volume 1.0
            if incest_story:
                call tb_pregnancy_ramdom_check(_("I'm sure all my eggs are swimming in a large pool of my brother's milk while being fertilized."))
            else:          
                call tb_pregnancy_ramdom_check(_("I'm sure all my eggs are swimming in a large pool of milk while being fertilized.")) from _call_tb_pregnancy_ramdom_check_2 
            jump two_bodies_time_advances
        "Leave":
            jump two_bodies_rooms
    jump two_bodies_mc_evening_outfit_cat
label  two_bodies_mc_evening2:
    scene tb_evening_pregnant2_1 with storyfx
    menu:
        "Eating pussy":
            scene tb_evening_pregnant2_2 with dissolve
            neus "Eeee… mmm.. I think I'll reject-"
            scene tb_evening_pregnant2_3 with dissolve
            if incest_story:
                neus_lyra "I would love that, I want you to devour my pussy brother."
            else:
                neus_lyra "I would love that, I want you to devour my pussy."
            scene tb_evening_pregnant2_4 with dissolve
            neus "..."
            play char3 groan_music2
            pause 0.05
            play char2 groan_music2 loop
            scene tb_evening_pregnant2_5 with w9
            neus "Brother... Your fingers and your tongue"
            neus_lyra "They feel so good, I'm at my limit."
            scene tb_evening_pregnant2_6 with dissolve  
            stop char3
            stop char2
            play char1 double_climax1          
            neus_lyra_neus "I'm cumming {e_heartbt=FF0000}"
            stop char1 fadeout 2.0
            scene tb_evening_pregnant2_7 with dissolve
            play char3 breathing1
            neus_lyra "Uff, that was intense."
            scene tb_evening_pregnant2_8 with dissolve
            if incest_story:
                neus_lyra "Wait, wait, brother, I just came."
            else:
                neus_lyra "Wait, wait, I just came."
            mc "I still have to eat this pie."
            scene tb_evening_pregnant2_9 with dissolve
            play char2 groan_music loop #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            neus_lyra "{bt=2}{=lust_style}Mmm mmm mmm...{/bt}"
            neus_lyra "{e_heartbt2=FF0000}"
            stop char2
            stop char3
            scene tb_evening_pregnant2_10 with dissolve
            play char1 climax2
            neus_lyra "I'm cumming {e_heartbt=FF0000}"
            stop char1 fadeout 2.0
            scene tb_evening_pregnant2_11 with dissolve
            play char3 breathing1
            ""
            menu:
                "More":
                    play ambience night_ambience volume 0.1 fadeout 0.5
                    scene tb_evening_pregnant2_12 with dissolve
                    "You continue to devour their delicious pussies."
                    scene tb_evening_pregnant2_13 with w33
                    neus "How much time has passed, the sun has already set."
                    scene tb_evening_pregnant2_14 with dissolve
                    play char1 climax2
                    neus_lyra "I'm cumming {e_heartbt=FF0000}"
                    stop char1 fadeout 4.0
                    scene tb_evening_pregnant2_15 with dissolve
                    neus "I'm going to have some water…"
                    play sound whoosh1
                    scene tb_evening_pregnant2_16 with pushdo
                    play char2 groan_music2 loop
                    if incest_story:
                        neus "{bt=2}{=lust_style}Wait, wait, brother, just let me rest a while.{/bt}"
                    else:
                        neus "{bt=2}{=lust_style}Wait, wait, just let me rest a while.{/bt}"
                    neus_lyra "Although I like how affectionate you are and how good it feels."
                    neus_lyra "I think we should stop, if we continue I think I could lose my mind with pleasure."
                    menu:
                        "More":
                            scene tb_evening_pregnant2_17 with dissolve
                            neus "It's so unfair, just with your tongue and fingers you can give me so much pleasure."
                            if incest_story:
                                neus "Are you sure you're not using some kind of magic, brother?"
                                mc "No, no magic, just the motivation to eat my cute little sister's pussy"
                            else:
                                neus "Are you sure you're not using some kind of magic?"
                                mc "No, no magic, just the motivation to eat your cute little pussy"
                            stop char2 fadeout 2.0
                            stop char3 fadeout 2.0
                            stop music fadeout 5.0
                            scene black with dissolve
                            if incest_story:
                                "You spend all night giving pleasure to your little sister."
                            else:
                                "You spend all night giving pleasure to [neusname] and [neusname_lyra]."
                            jump two_bodies_sleeping_event
                        "Stop":
                            stop char2 fadeout 2.0
                            stop char3 fadeout 2.0
                            stop music fadeout 5.0
                            scene black with dissolve
                            "They clean themselves."
                            jump two_bodies_time_advances
                "Stop":
                    stop char3 fadeout 1.0
                    scene black with dissolve
                    "They clean themselves."
        "Blowjob":
            scene tb_evening_pregnant2_18 with dissolve
            if incest_story:
                neus "Okay brother."
            else:
                neus "Okay."
            scene tb_evening_pregnant2_19 with dissolve
            neus_lyra "*Lick*"
            scene tb_evening_pregnant2_20 with dissolve
            play char3 double_suck1
            neus_lyra_neus "*Lick suck*"
            neus_lyra_neus "Mmm."
            mc "As always, it feels very good."
            neus_lyra_neus "*Lick suck* {e_heartbt2=cc0066}."
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            play char1 groan1
            scene tb_evening_pregnant2_21 with dissolve
            neus_lyra_neus "Mmm."
            scene tb_evening_pregnant2_22 with dissolve
            play char1 gulp1
            neus_lyra "Gulp."
            scene tb_evening_pregnant2_23 with dissolve
            play char1 ahegao3
            neus_lyra "{bt=2}{=lust_style}Aaaaa{/bt}"
            scene tb_evening_pregnant2_24 with dissolve
            neus "*Lick*"
            scene black with dissolve
            if incest_story:
                "Your sister cleans your dick and then..."
            else:
                "[neusname] cleans your dick and then..."
            "They clean themselves."
        "Leave":
            jump two_bodies_rooms
    jump two_bodies_mc_evening2
label  two_bodies_mc_evening3:
    scene tb_evening_pregnant3_1 with storyfx
    menu:
        "Bellyjob":
            scene tb_evening_pregnant3_2 with dissolve
            if incest_story:
                neus_lyra_neus "Okay brother"
            else:
                neus_lyra_neus "Okay"
            scene tb_evening_pregnant3_3 with w33
            neus "Let's start moving"
            scene tb_evening_pregnant3_4 with fadesex
            play char3 handjob2
            ""
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_evening_pregnant3_5 with dissolve
            ""
            scene tb_evening_pregnant3_6 with dissolve
            neus_lyra_neus "Hehe"
            scene black with dissolve
            "They clean themselves"
        "Cat"(two_bodies_outfit_is_active_outfit):
            if not(is_view_intro_two_bodies_outfit_cat):
                $ is_view_intro_two_bodies_outfit_cat=True
                mc "Could you put on this outfit, please?"
                scene tb_evening_pregnant3_7 with dissolve
                if incest_story:
                    neus_lyra "I would love to brother"
                else:
                    neus_lyra "I would love to"
                scene tb_evening_pregnant3_8 with dissolve
                neus "This suit is a bit..."
            else:
                mc "Could you put that outfit on again?"
                scene tb_evening_pregnant3_8 with dissolve
                neus "I'm still not quite used to this."
            scene tb_evening_pregnant3_9 with dissolve
            if incest_story:
                neus_lyra "Hey brother, you know, this pregnant kitten is very horny."
            else:
                neus_lyra "Hey, you know, this pregnant kitten is very horny."
            scene tb_evening_pregnant3_10 with dissolve
            neus "I've been holding back a lot."
            scene tb_evening_pregnant3_11 with dissolve
            neus_lyra "I need you to give me lots of cuddles."
            menu:
                "Head pats":
                    scene tb_evening_pregnant3_12 with dissolve
                    "You gently caress their heads."
                    ""
                    scene tb_evening_pregnant3_13 with dissolve
                    neus_lyra "I wasn't referring to these kind of cuddles."
                    scene tb_evening_pregnant3_14 with dissolve
                    neus "Don't listen to her, these cuddles are great."
                    neus "Can you give me some more?"
                    scene tb_evening_pregnant3_12 with dissolve
                    ""
                    stop ambience fadeout 0.5
                    scene tb_evening_pregnant3_15 with w9
                    play music DarkestSoul_Schmidt volume 0.5
                    if incest_story:
                        neus_lyra "Enough games brother, I'm going to fuck you."
                    else:
                        neus_lyra "Enough games, I'm going to fuck you."
                    neus_lyra "This kitten is in heat and she's going to drain you dry."
                    stop music fadeout 1.0
                    play ambience morning_sounds fadein 0.5
                    scene tb_evening_pregnant3_17 with w33
                    play char1 penetration2
                    neus_lyra "Uh."
                "Sex":
                    scene tb_evening_pregnant3_16 with dissolve
                    if incest_story:
                        neus_lyra "I'm going to start brother."
                    else:
                        neus_lyra "I'm going to start."
                    scene tb_evening_pregnant3_17 with dissolve
                    play char1 penetration2
                    neus_lyra "Uh!"
            scene tb_evening_pregnant3_18 with dissolve
            play char3 sex6
            neus_lyra "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            neus_lyra "More, more, please, calm my state of heat."
            stop char3
            scene tb_evening_pregnant3_19 with dissolve
            if incest_story:
                neus "I'm sorry brother, but I can't hold back anymore, I also want to be pampered."
            else:
                neus "I'm sorry, but I can't hold back anymore, you could also pamper me."
            scene tb_evening_pregnant3_20 with dissolve
            play char3 double_sex1
            neus_lyra_neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"
            neus_lyra_neus "This feels so good."
            neus_lyra_neus "Not to mention that your dick and your tongue give so much pleasure."
            neus_lyra_neus "There's no way I can hold back."
            stop char3
            scene tb_evening_pregnant3_21 with dissolve
            play char1 double_climax3
            neus_lyra_neus "I'm cumming!"
            scene tb_evening_pregnant3_22 with dissolve
            neus_lyra_neus "Phew."
            mc "Well, I guess I should keep pampering my cute in heat little kittens."
            play ambience night_ambience volume 0.1 fadeout 1.0
            scene tb_evening_pregnant3_23 with fadesex
            if incest_story:
                neus_lyra "Brother, I'm not complaining, but just give me a few minutes break, I'm still sensitive."
            else:
                neus_lyra "I'm not complaining, but just give me a few minutes break, I'm still sensitive."
            scene tb_evening_pregnant3_24 with dissolve
            neus "Yeah, just 5 minutes, even 3 minutes would be enough."
            scene tb_evening_pregnant3_25 with dissolve
            "You spend the whole afternoon without stopping, calming the heat of your horny pregnant kittens."
            scene black with dissolve
            ""
            jump two_bodies_time_advances 
        "Leave":
            jump two_bodies_rooms
    jump two_bodies_mc_evening3
#----------------------------------------mc_night_room_quest----------------------------------------
label two_bodies_mc_night:
    if not(is_view_tb_chess):
        $ tb_choice_chess_win=random.choice([0,1])
        if tb_choice_chess_win==0:
            scene two_bodies_mc_night0_1 with storyfx
            neus "Checkmate"            
            scene two_bodies_mc_night0_2 with dissolve
            ""
        else:
            scene two_bodies_mc_night0_3 with storyfx
            neus_lyra "Checkmate"
            scene two_bodies_mc_night0_4 with dissolve
            ""
        $ is_view_tb_chess=True
        scene two_bodies_mc_night0_5 with w9
    else:
        scene two_bodies_mc_night0_5 with storyfx
    menu:
        "Sleep":
            if tb_choice_chess_win==0:
                scene two_bodies_mc_night0_6 with w33 
                neus "I'm so happy I won."
            else:
                scene two_bodies_mc_night0_7 with w33 
                neus_lyra "Nothing like enjoying your prize after having won."
            scene black with eyeclose
            ""           
            play ambience morning_sounds fadein 1.0
            scene two_bodies_mc_night0_8 with eyeopen
            if not(is_tb_pregnant_start) or is_tb_pregnant: 
                menu:
                    "Sleep in":
                        scene two_bodies_mc_night0_18 with w33
                        neus "Ready"
                        scene two_bodies_mc_night0_19 with dissolve
                        neus "How strange that he hasn't woken up yet"
                        neus "Maybe I should go wake him-"
                        scene two_bodies_mc_night0_20 with dissolve
                        neus_lyra "Don't worry, I'll go"
                        play sound whoosh1
                        scene two_bodies_mc_night0_21 with pushri
                        neus_lyra "Hehe"
                        play sound clothes
                        scene two_bodies_mc_night0_22 with dissolve
                        neus_lyra "*Lick suck*"
                        scene two_bodies_mc_night0_23 with circlefx
                        neus "She said she would wake you up 10 minutes ago, where is she?"
                        mc "Good morning sis"
                        scene two_bodies_mc_night0_24 with dissolve
                        neus "Good morning br…"
                        scene two_bodies_mc_night0_25 with dissolve
                        play char3 suck1
                        neus "So you were here"
                        menu:
                            "Ask her to join":
                                stop char3 fadeout 1.0
                                scene two_bodies_mc_night0_26 with dissolve
                                neus "Well, I guess there's no other way, I’m starving and breakfast is waiting."
                                scene two_bodies_mc_night0_27 with dissolve
                                neus_lyra "Oh, so it's just about breakfast then?"                           
                                neus "..."
                                scene two_bodies_mc_night0_28 with dissolve
                                neus "I also want to suck your dick"
                                scene two_bodies_mc_night0_29 with dissolve
                                if incest_story:
                                    neus "Would you give your little sister your delicious milk for breakfast?"
                                else:
                                    neus "Would you give your girlfriend your delicious milk for breakfast?"
                                mc "Well, if you ask me like that, I guess I can't refuse"
                                scene two_bodies_mc_night0_30 with dissolve
                                play char3 double_suck1
                                neus_lyra_neus "*Lick suck*"
                                menu:                    
                                    "Cum":
                                        pass
                                stop char3
                                play charM cum1
                                scene two_bodies_mc_night0_31 with dissolve
                                ""
                                scene two_bodies_mc_night0_32 with dissolve
                                if incest_story:
                                    neus_lyra_neus "Thank you for your milk, brother"
                                else:
                                    neus_lyra_neus "Thank you for your milk"
                                scene two_bodies_mc_night0_33 with dissolve
                                neus "I think we should go have breakfast now, before the food gets cold"
                                scene two_bodies_mc_night0_34 with w33
                                if incest_story:
                                    "You enjoy a good breakfast with your sister"
                                else:
                                    "You enjoy a good breakfast"
                                scene black with dissolve
                                ""
                            "Cum":
                                stop char3
                                play charM cum1
                                scene two_bodies_mc_night0_35 with dissolve
                                neus_lyra "Mmm"
                                scene black with dissolve
                                if incest_story:
                                    "After releasing a large load of semen in your sister's mouth, you headed to the kitchen for breakfast."
                                    scene two_bodies_mc_night0_34 with w33
                                    "You enjoy a good breakfast with your sister"
                                else:
                                    "After releasing a large load of semen in [neusname_lyra]'s mouth, you headed to the kitchen for breakfast."
                                    scene two_bodies_mc_night0_34 with w33
                                    "You enjoy a good breakfast"
                                scene black with dissolve
                                ""  
                        call two_bodies_sleeping_event_call(1) from _call_two_bodies_sleeping_event_call
                        jump two_bodies_rooms               
                    "Wake up":
                        pass      
            jump two_bodies_sleeping_event
        "Blowjob":
            scene two_bodies_mc_night0_9 with dissolve
            neus_lyra_neus "Heh"
            scene two_bodies_mc_night0_10 with dissolve
            play char1 ahegao2
            pause 0.05
            play char2 ahegao2
            neus_lyra_neus "Aaaa"
            menu:
                "[neusname]":
                    scene two_bodies_mc_night0_11 with dissolve
                    ""
                    scene two_bodies_mc_night0_12 with dissolve
                    play char3 deep_suck1
                    ""
                    if incest_story:
                        neus "(I love your milk brother, I want you to fill my stomach)"
                    else:
                        neus "(I love your milk, I want you to fill my stomach)"
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene two_bodies_mc_night0_13 with dissolve
                    neus "Mmm"
                    scene two_bodies_mc_night0_14 with w9
                    ""
                    scene two_bodies_mc_night0_15 with dissolve
                    play char3 deep_suck1
                    ""
                    neus_lyra "(My stomach is hungry)"
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene two_bodies_mc_night0_16 with dissolve
                    neus_lyra "Mmm"
                "[neusname_lyra]":
                    scene two_bodies_mc_night0_14 with dissolve
                    ""
                    scene two_bodies_mc_night0_15 with dissolve
                    play char3 deep_suck1
                    ""
                    neus_lyra "(My stomach is hungry)"
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene two_bodies_mc_night0_16 with dissolve
                    neus_lyra "Mmm"
                    scene two_bodies_mc_night0_11 with w9
                    ""
                    scene two_bodies_mc_night0_12 with dissolve
                    play char3 deep_suck1
                    ""
                    if incest_story:
                        neus "(I love your milk brother, I want you to fill my stomach)"
                    else:
                        neus "(I love your milk, I want you to fill my stomach)"
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene two_bodies_mc_night0_13 with dissolve
                    neus "Mmm"
            scene two_bodies_mc_night0_17 with dissolve
            neus_lyra_neus "{e_heartbt2=cc0066}"
            scene black with dissolve
            ""
        "Leave":
            jump two_bodies_rooms
    jump two_bodies_mc_night
label two_bodies_mc_night2:
    scene tb_night_pregnant2_1 with storyfx
    menu:
        "Sleep":
            scene tb_night_pregnant2_22 with w33
            ""
            scene black with eyeclose
            ""           
            play ambience morning_sounds fadein 1.0
            scene two_bodies_mc_night0_8 with eyeopen
            jump two_bodies_sleeping_event
        "Kiss":
            scene tb_night_pregnant2_2 with dissolve
            neus "{e_heartbt=cc0066}"
            scene tb_night_pregnant2_3 with dissolve
            play char3 kissing1
            neus "*Kissing*"
            neus "Mmm"
            neus "{e_heartbt=cc0066}"
            stop char3
            scene tb_night_pregnant2_4 with dissolve
            play char1 ahegao3
            neus "Aaaa"
            scene tb_night_pregnant2_5 with dissolve
            if incest_story:
                neus_lyra "I also want kisses brother"
            else:
                neus_lyra "I also want kisses"
            scene tb_night_pregnant2_6 with dissolve
            play char3 kissing1
            neus_lyra "Mmmmm..."
            neus_lyra "{e_heartbt2=cc0066}"
            stop char3
            scene tb_night_pregnant2_7 with dissolve
            neus_lyra "Ufff"
            if incest_story:
                mc "*Mocking tone* Do you like my kisses little sister?"
            else:
                mc "*Mocking tone* Do you like my kisses?"
            scene tb_night_pregnant2_8 with dissolve
            neus "Yes, I love them, I love your kisses"
            scene tb_night_pregnant2_9 with dissolve
            neus "and {sc=2}I DEMAND MORE RIGHT NOW!{/sc}"
            scene tb_night_pregnant2_10 with dissolve
            if incest_story:
                "You spend a good time kissing your little sister"
            else:
                "You spend a good time kissing [neusname] and [neusname_lyra]"
        "Anal":
            scene tb_night_pregnant2_11 with dissolve
            if incest_story:
                neus_lyra "I would love to brother"
            else:
                neus_lyra "I would love to"
            scene tb_night_pregnant2_12 with dissolve
            neus_lyra "I'm going to put it in now"
            scene tb_night_pregnant2_13 with dissolve
            play char1 penetration1
            neus_lyra "Uh!"
            scene tb_night_pregnant2_14 with dissolve
            play char3 sex6
            neus_lyra "I've missed this feeling"
            neus_lyra "{bt=2}{=lust_style}Ha ha ha{/bt}"
            neus "*Kiss kiss*"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1 
            scene tb_night_pregnant2_15 with dissolve
            play char1 climax1
            neus_lyra "{sc=2}{=lust_style}Uh!{/sc}"
            scene tb_night_pregnant2_16 with dissolve
            neus_lyra "Uff"
            scene tb_night_pregnant2_17 with dissolve
            if incest_story:
                neus "I want some too brother"
            else:
                neus "I want some too"
            scene tb_night_pregnant2_18 with dissolve
            play char1 penetration2
            neus "Uh!"
            scene tb_night_pregnant2_19 with dissolve
            play char3 sex6
            neus "{bt=2}{=lust_style}Ho ho ho{/bt}"
            neus "{e_heartbt2=cc0066}"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1 
            scene tb_night_pregnant2_20 with dissolve
            play char1 climax1
            neus "{sc=2}{=lust_style}UH!{/sc}"
            scene tb_night_pregnant2_21 with dissolve
            neus "My ass is so full of your milk"
            neus "it's overflowing"
            scene black with dissolve
            "They clean up"
        "Leave":
            jump two_bodies_rooms
    jump two_bodies_mc_night2
label two_bodies_mc_night3:
    scene tb_night_pregnant3_1 with storyfx
    menu:
        "Sleep":
            scene tb_night_pregnant3_2 with w33
            ""
            scene black with eyeclose
            ""           
            play ambience morning_sounds fadein 1.0
            scene two_bodies_mc_night0_8 with eyeopen
            jump two_bodies_sleeping_event
        "Footjob":
            scene tb_night_pregnant3_3 with dissolve
            neus_lyra_neus "Mmm..."
            scene tb_night_pregnant3_4 with dissolve
            ""
            scene tb_night_pregnant3_5 with dissolve
            play char3 handjob2
            ""
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_night_pregnant3_6 with dissolve
            ""
            scene tb_night_pregnant3_7 with dissolve
            ""
            scene black with dissolve
            "They clean themselves"
        "Thighjob":
            scene tb_night_pregnant3_8 with dissolve
            neus_lyra_neus "Hehehe"
            scene tb_night_pregnant3_9 with dissolve
            ""
            scene tb_night_pregnant3_10 with dissolve
            play char3 handjob2
            ""
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene tb_night_pregnant3_11 with dissolve
            neus_lyra_neus "{e_heartbt2=FF0000}"
            scene tb_night_pregnant3_12 with dissolve
            ""
            scene black with dissolve
            "They clean themselves"
        "Sex":
            scene tb_night_pregnant3_13 with dissolve
            neus_lyra_neus "{e_heartbt2=FF0000}"
            scene tb_night_pregnant3_14 with dissolve
            neus "I'm going to start now"
            scene tb_night_pregnant3_15 with dissolve
            play char3 double_sex3
            neus_lyra_neus "{bt=2}{=lust_style}Ha ha ha{/bt}"
            if incest_story:
                neus_lyra_neus "Brother, it feels so good"
            else:
                neus_lyra_neus "It feels so good"
            neus_lyra_neus "I can't stand it anymore"
            neus_lyra_neus "Feeling your dick and your tongue at the same time is too much..."
            scene tb_night_pregnant3_16 with dissolve
            neus_lyra_neus "{sc=2}{=lust_style}I'm cumming{/sc}"
            stop char3
            play charM cum1
            scene tb_night_pregnant3_17 with dissolve
            play char1 double_climax2
            neus_lyra_neus "{sc=2}{=lust_style}Uh!{/sc}"
            stop char1 fadeout 2.0
            scene tb_night_pregnant3_18 with dissolve
            neus_lyra "I desperately needed this"
            scene black with dissolve
            "They clean themselves"
        "Leave":
            jump two_bodies_rooms
    jump two_bodies_mc_night3
