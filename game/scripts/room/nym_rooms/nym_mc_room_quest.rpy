image nym_day_1 = DynamicAnimation(
["rooms/nym/nym_day_1_0.webp",
"rooms/nym/nym_day_1_1.webp",
"rooms/nym/nym_day_1_2.webp",])
image nym_day_89 = DynamicAnimation(
["rooms/nym/nym_day_89_0.webp",
"rooms/nym/nym_day_89_1.webp",
"rooms/nym/nym_day_89_2.webp",])
image nym_day_128 = DynamicAnimation(
["rooms/nym/nym_day_128_0.webp",
"rooms/nym/nym_day_128_1.webp",
"rooms/nym/nym_day_128_2.webp",])
image nym_day_130 = DynamicAnimation(
["rooms/nym/nym_day_130_0.webp",
"rooms/nym/nym_day_130_1.webp",
"rooms/nym/nym_day_130_2.webp",])
image nym_night_2 = DynamicAnimation(
["rooms/nym/nym_night_2_0.webp",
"rooms/nym/nym_night_2_1.webp",
"rooms/nym/nym_night_2_2.webp",])
image nym_night_3 = DynamicAnimation(
["rooms/nym/nym_night_3_0.webp",
"rooms/nym/nym_night_3_1.webp",
"rooms/nym/nym_night_3_2.webp",])
default nym_chat_toilet_go=False
default is_view_nym_beach_sylvia=False
default is_view_nym_beach_lyra=False
default is_view_nym_beach_neus=False
#----------------------------day----------------------------
label nym_event_day_control:
    scene nym_day_1 with storyfx
    menu:
        "Assjob":
            scene nym_day_2 with dissolve
            neus "Ok"
            scene nym_day_3 with dissolve
            ly_ne_syl "Let's get started"
            scene nym_day_4 with dissolve
            play char3 handjob2
            if incest_story:
                mc "Receiving a triple assjob from my little sister is great"
            else:
                mc "Receiving a triple assjob is great"
            ly_ne_syl "{sc=2}{=lust_style}Hehehe{/sc} {e_heartbt2=FF0000}"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene nym_day_5 with dissolve
            ""
            scene nym_day_6 with dissolve
            if incest_story:
                ly_syl "Brother, you let out so much milk"
            else:
                ly_syl "You let out so much milk"
            scene black with dissolve
            "They clean themselves"
        "Casual day out":
            scene nym_day_7 with dissolve
            if incest_story:
                ly_ne_syl "I would love to brother."
            else:
                ly_ne_syl "I would love to."
            scene nym_day_8 with dissolve
            neus "As always, I love this place."
            neus_lyra "The desserts are so rich."
            neus_sylvia "Delicious!"
            scene nym_day_9 with dissolve
            waitress "Would you like anything else?"
            scene nym_day_10 with dissolve
            neus "Please give me menu item 1."(multiple=3)
            neus_lyra "Menu item 2 and 4 please."(multiple=3)
            neus_sylvia "Please menu item 5."(multiple=3)
            scene nym_day_11 with dissolve
            ly_ne_syl "Uff, so good."
            scene nym_day_12 with dissolve
            neus_lyra "I'm going to the bathroom for a bit."
            scene nym_day_13 with dissolve
            neus_sylvia "I also need to go."
            scene nym_day_14 with dissolve
            mc "[neusname], do you also need to go to the bathroom?"
            scene nym_day_15 with dissolve
            neus "Eh... no, I'm fine... in fact I want to have some more dessert."
            scene nym_day_16 with dissolve
            neus "Please give me menu item 1."
            "You receive a message."
            scene nym_day_17 with dissolve
            call chat(lyra_chat1) from _call_chat
            if nym_chat_toilet_go:
                mc "I'm going to the bathroom for a bit."
                scene nym_day_18 with dissolve
                neus "Mmm... okay."
                scene nym_day_19 with dissolve
                if incest_story:
                    neus_lyra "Brother, It's about time, can you help me cool down this heat."
                else:
                    neus_lyra "It's about time, can you help me cool down this heat."
                scene nym_day_20 with dissolve
                neus_sylvia "Although I'm not sure that using that hot rod will help."
                scene nym_day_21 with dissolve
                neus_lyra "Maybe my heat and your hotness will cool me off or I burn up in the attempt."
                scene nym_day_22 with dissolve
                waitress "Here is your dessert."
                play sound magical1 volume 0.3
                scene nym_day_23 with dissolve
                neus "Thank you-"
                scene nym_day_24 with dissolve
                play char1 double_penetration1
                ly_ne_syl "Uh!"
                waitress "Miss, are you okay?"
                scene nym_day_25 with dissolve
                neus_sylvia "Being able to share this pleasure and multiply it by 3 is great."
                scene nym_day_26 with dissolve
                neus_lyra "Yea... I almost climax just by having it inside."
                scene nym_day_27 with dissolve
                neus "Yes, I'm fine, don't worry. You can go."
                waitress "Excuse the question, but it's rare to see 3 people almost identical, you're triplets, right?"
                neus "Yes."
                scene nym_day_28 with dissolve
                play char3 double_sex3
                ly_ne_syl "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"(multiple=2)
                waitress "Wow, that's great, I know some twins but they're not as identical as you."(multiple=2)
                waitress "And even more rare that they share taste, especially in men... that guy is your boyfriend, right?"
                neus "{bt=2}{=lust_style}YShes.{/bt}"
                ly_ne_syl "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"(multiple=2)
                waitress "Wow, that's incredible, don't you feel jealous.. or being triplets you don't mind sharing the same man?"(multiple=2)
                neus "Well, there's no-"
                stop char3
                play charM cum1
                scene nym_day_29 with dissolve
                ly_ne_syl "{sc=2}{=lust_style}I'm cumming{/sc} {e_heartbt=FF0000}"
                play char1 double_climax1
                scene nym_day_30 with dissolve
                waitress "Miss, are you really okay?"
                neus "{size=-10}Yes. {e_heartbt2=FF0000}"
                scene nym_day_31 with dissolve
                waitress "Are you sure you don't need me to call someone-"
                scene nym_day_30 with dissolve
                manager "Hey, rookie, you have more than one customer who needs to be served."
                waitress "I'm coming right now, boss, sorry."
                waitress "If you'll excuse me, I have to leave, if you need help with something you can just call me."
                neus "Thank you for your kindness"
                scene nym_day_32 with dissolve
                play char3 double_sex3
                ly_ne_syl "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"
                if incest_story:
                    neus_sylvia "Please, fill me up brother."
                else:
                    neus_sylvia "Please, fill me up."
                neus_sylvia "Use me as if I were your exclusive sperm bank."
                neus_sylvia "Fill my uterus , until it overflows."
                neus_sylvia "*Panting* I'm g-gonna cum again..."
                stop char3
                play charM cum1
                scene nym_day_33 with dissolve
                play char1 double_climax1
                ly_ne_syl "{sc=2}{=lust_style}Uh!{/sc}"
                stop char1 fadeout 1.0
                scene nym_day_34 with dissolve
                play ambience night_ambience fadeout 0.5 volume 0.1
                neus_lyra "That was great."
                neus_sylvia "We'll have to come here again some time."
                mc "*Teasing tone* Is something wrong, [neusname]?"
                scene nym_day_35 with dissolve
                neus "I hope you take care of me next... I can't take it any longer."
                scene black with dissolve
                if incest_story:
                    "You spend the whole night with your sister in a hotel and the next morning you return home with them."
                else:
                    "You spend the whole night with [neusname], [neusname_lyra] and [neusname_sylvia] in a hotel."
                scene night_transition with dissolve
                play ambience morning_sounds fadein 0.5
                scene day_transition with wiperight
                ""
                $ nym_time=0
                $ nym_tired=True
                jump nym_rooms
            else:
                scene nym_day_18 with dissolve
                neus "What did I write to you?"
                scene nym_day_17 with dissolve
                mc "They're coming out of the bathroom right now."
                scene nym_day_18 with dissolve
                neus "Mmm... okay."
                scene nym_day_36 with dissolve
                neus_lyra "That was great."
                neus_sylvia "We have to come here again."
                scene black with dissolve
                "You all go home."
                jump nym_time_advances
        "Let's go to the beach":
            scene nym_day_37 with dissolve
            if incest_story:
                neus_sylvia "I would love to brother, it's been a long time since we last went to the beach."
            else:
                neus_sylvia "I would love to, it's been a long time since we last went to the beach."
            scene nym_day_38 with dissolve
            neus_lyra "Which bikini should I wear?"
            play ambience bathtub volume 0.1
            scene nym_day_39 with dissolve
            neus "I haven't been here in a long time."
            scene nym_day_40 with dissolve
            neus_lyra "Although this part of the beach is small, it has the advantage of not being visited by many people."
            scene nym_day_41 with dissolve
            neus "And as we are not in a holiday season, it is rare to find people here."
            scene nym_day_42 with dissolve
            neus_sylvia "We have it all to ourselves."
            scene nym_day_43 with dissolve
            neus "I'm going to take a walk along the shore."
            neus_sylvia "I want to get some sun."
            neus_lyra "I want to go in the water for a while."
            $ is_view_nym_beach_sylvia=False
            $ is_view_nym_beach_lyra=False
            $ is_view_nym_beach_neus=False
            jump nym_ui_beach
        "Outfit"(nym_outfit_is_active_outfit):
            if not(is_view_intro_nym_outfit):
                $ is_view_intro_nym_outfit=True
                scene nym_day_79 with dissolve
                neus "Do you have something for me... Hmm... a gift, eh?"
                scene nym_day_80 with w9
                if incest_story:
                    neus "Brother, I wasn't expecting this kind of gift."
                else:
                    neus "I wasn't expecting this kind of gift."
                scene nym_day_81 with dissolve
                neus_lyra "''This kitty wants to take all your milk.''"
                scene nym_day_82 with dissolve
                neus_sylvia "''I'm going to squeeze you until you're out of cream.''"
                scene nym_day_83 with dissolve
                mc "You all really got into character, huh?"
                scene nym_day_84 with dissolve
                neus_sylvia "Thanks, although I think it's all because my outfit goes perfectly with my personality."
                scene nym_day_85 with dissolve
                neus "Well I think mine doesn't match me at all."
                scene nym_day_86 with dissolve
                play sound magical1 volume 0.3
                ly_syl "{font=fonts/Alkatra-Regular.ttf}Touch{/font}"
                scene nym_day_87 with leafwipe
                neus "I'm going to squeeze out all your ''carrot'' juice."  
            else:
                scene nym_day_88 with dissolve
                ly_ne_syl "Okey"
            $ is_nym_outfit=True
            jump nym_event_day_control_outfit
        "Leave":
            jump nym_rooms
    jump nym_event_day_control
label nym_event_day_control_tired:
    play char3 breathing1 volume 0.5
    scene nym_day_128 with storyfx
    menu:
        "Talk":
            scene nym_day_129 with dissolve
            if incest_story:
                neus "I'm sorry brother, but I'm a bit tired from last night."
            else:
                neus "I'm sorry, but I'm a bit tired from last night."
            neus "It's a little hard for me to move my legs."            
        "Use ''Touch''":
            scene black with dissolve
            stop char3 fadeout 0.5
            play sound magical1 volume 0.3
            "You use ''Touch'' to give them a bit of energy."
            if incest_story:
                neus "Thank you brother, I feel very energized."
            else:
                neus "Thank you, I feel very energized."
            $ nym_tired=False
            jump nym_rooms
        "Leave":
            stop char3 fadeout 0.5
            jump nym_rooms
    jump nym_event_day_control_tired

label nym_event_day_control_outfit:
    scene nym_day_89 with storyfx
    menu:
        "Regular outfit":
            scene nym_day_90 with dissolve
            ""
            scene nym_day_91 with dissolve
            neus "Okey"
            $ is_nym_outfit=False
            jump nym_event_day_control
        "Blowjob":
            scene nym_day_92 with dissolve
            neus "{e_heartbt2=FF0000}"
            scene nym_day_93 with dissolve
            play char1 short_kiss
            neus "*Kiss*"
            stop char1 fadeout 2.0
            scene nym_day_94 with fadesex
            play char3 deep_suck1
            neus "*Suck lick*"
            if incest_story:
                neus_sylvia "Do you like your sister's little mouth?"
            else:
                neus_sylvia "Do you like her little mouth?"
            neus_lyra "It's made to be used by your carrot"
            neus_sylvia "You can cum at any time in her throat"
            neus_lyra "You can use it as if it were a vessel for your carrot juice."
            neus "*Suck lick*"
            menu:
                "Cum":
                    pass
            stop char3
            play charM cum1
            scene nym_day_95 with hpunch
            ly_ne_syl "UH!"
            scene nym_day_96 with dissolve
            play char1 gulp1
            neus "Gulp"
            scene nym_day_97 with dissolve
            play char1 ahegao1
            neus "{bt=2}{=lust_style}Ahhhh{/bt}"
            stop char1 fadeout 2.0
            scene black with dissolve
            "She cleans herself."
        "Sex":
            scene nym_day_98 with dissolve
            ly_ne_syl "Hehe {e_heartbt2=FF0000}"
            scene nym_day_99 with dissolve
            if incest_story:
                neus "This bunny is hungry for her brother's carrot"
            else:
                neus "This bunny is hungry for your carrot"
            scene nym_day_100 with dissolve
            play char1 penetration1
            neus "Uh!"
            scene nym_day_101 with dissolve
            neus "Hehe, my pussy ate your carrot to the base"
            scene nym_day_102 with fadesex
            play char3 sex6
            neus "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"
            ly_syl "*Lick, suck*"
            if incest_story:
                neus "I want all your carrot juice brother"
            else:
                neus "I want all your carrot juice"
            neus "I want you to flood my uterus"
            scene nym_day_103 with dissolve
            neus "I'm cumming!"
            stop char3
            play charM cum1
            scene nym_day_104 with hpunch
            play char1 climax2
            neus "Uh!"
            stop char1 fadeout 2.0
            scene nym_day_105 with dissolve
            neus "Uf!"
            scene nym_day_106 with dissolve
            neus_lyra "I hope you haven't forgotten that you have to feed this kitten"
            scene nym_day_107 with dissolve
            play char1 penetration2
            neus_lyra "UH!"
            scene nym_day_108 with dissolve
            play char3 sex7
            if incest_story:
                neus_lyra "Brother, you have to give me a lot of milk so that I can be healthy and well fed kitten"
            else:
                neus_lyra "You have to give me a lot of milk so that I can be healthy and well fed"
            neus_lyra "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"
            neus_lyra "{e_heartbt2=FF0000}"
            scene nym_day_109 with dissolve
            neus_lyra "I'm cumming!"
            stop char3
            play charM cum1
            scene nym_day_110 with hpunch
            play char1 climax2
            neus_lyra "Uh!"
            stop char1 fadeout 2.0
            scene nym_day_111 with dissolve
            ""
            scene nym_day_112 with dissolve
            if incest_story:
                neus_sylvia "Tonight you will not be able to rest… we are going to squeeze you until you are dry, brother"
            else:
                neus_sylvia "Tonight you will not be able to rest… we are going to squeeze you until you are dry"
            scene nym_day_113 with dissolve
            play char3 sex6
            neus_sylvia "{bt=2}{=lust_style}Oh oh oh oh.{/bt}"
            neus_sylvia "{e_heartbt2=FF0000}"
            scene nym_day_114 with dissolve
            ly_ne_syl "I'm cumming"
            stop char3
            play charM cum1
            scene nym_day_115 with hpunch
            play char1 double_climax1
            ly_ne_syl "Uh!"
            scene nym_day_116 with dissolve
            play char3 breathing1
            ly_ne_syl "{e_heartbt2=FF0000}"
            stop char1 fadeout 2.0
            play ambience night_ambience fadeout 1.0 fadein 0.5 volume 0.1
            scene nym_day_117 with fadesex
            play char2 sex4 loop
            neus_sylvia "{bt=2}{=lust_style}Ah ah ah ah.{/bt}"
            if incest_story:
                neus_sylvia "*Panting* Hey, brother, I know I said that I wouldn't let you rest tonight"
            else:
                neus_sylvia "*Panting* Hey, I know I said that I wouldn't let you rest tonight"
            neus_sylvia "*Panting* But, don't you think it would be good to take a few minutes break?"
            neus_lyra_neus "*Panting* it feels so good {e_heartbt2=FF0000}"
            neus_sylvia "*Panting* Just a few minutes, my ass and pussy are already full and are overflowing"
            neus_sylvia "*Panting* And if it continues like this I won't be able to avoid…"
            scene nym_day_118 with dissolve
            ly_ne_syl "{sc=2}I'M CUMMING!{/sc}"
            stop char2
            play charM cum1
            scene nym_day_119 with hpunch
            play char1 double_climax1
            ly_ne_syl "{sc=2}AAAAAAAAAAAGGHHHHHHHH...{/sc}"
            stop char1 fadeout 2.0
            $ renpy.music.set_volume(0.3,channel='char3')
            play char3 breathing2
            scene nym_day_120 with dissolve
            ""
            menu:
                "More":
                    $ renpy.music.set_volume(0.6,delay=1.0,channel='char3')
                    scene nym_day_121 with dissolve
                    neus "*Panting* My mind is blank and I can only feel pleasure"
                    neus "*Panting* Those two surrendered to pleasure long ago"
                    scene nym_day_122 with dissolve
                    $ renpy.music.set_volume(1.0,delay=1.0,channel='char3')
                    play char1 groan1
                    ly_syl "{e_heartbt2=FF0000}"
                    scene nym_day_123 with dissolve
                    play char2 double_penetration1
                    $ renpy.music.set_volume(0.6,delay=1.0,channel='char3')
                    neus_sylvia "*Panting* I want more, more..."
                    if incest_story:
                        neus_lyra "*Panting* Don't take them out so fast brother... {e_heartbt2=FF0000}"
                    else:
                        neus_lyra "*Panting* Don't take them out so fast... {e_heartbt2=FF0000}"
                    scene nym_day_124 with hpunch
                    play char1 double_climax2
                    play char2 double_climax2
                    stop char3 fadeout 1.0
                    ly_ne_syl"{sc=2}AHH! AHH! AHH! AGHH! AAAGGHHH!!!!{/sc}"
                    stop char1 fadeout 3.0
                    stop char2 fadeout 3.0
                    scene nym_day_125 with fadesex
                    play char2 kissing1 volume 2.0 loop
                    $ renpy.music.set_volume(0.2,delay=1.0,channel='char3')
                    play char3 breathing2
                    neus_lyra "{bt=2}{=lust_style}*Kiss* *Sip* Mooooore.. Mooooore....{/bt}"
                    "You spend the whole night flooding their uteruses until they overflow and equally fuck their asses"
                    stop char3 fadeout 1.0
                    stop char2 fadeout 3.0
                    stop char3 fadeout 2.0
                    scene black with dissolve
                    ""
                    scene night_transition with dissolve
                    play ambience morning_sounds fadein 0.5
                    scene day_transition with wiperight
                    ""
                    $ renpy.music.set_volume(1.0,delay=1.0,channel='char3')
                    $ nym_time=0
                    $ nym_tired=True
                    jump nym_rooms
                "No":
                    stop char3 fadeout 2.0
                    scene black with dissolve
                    "You take the suggestion and let them rest"
                    $ renpy.music.set_volume(1.0,delay=1.0,channel='char3')
                    jump nym_time_advances
        "Leave":
            jump nym_rooms
    jump nym_event_day_control_outfit
label nym_event_day_control_outfit_tired:
    play char3 breathing1 volume 0.5
    scene nym_day_130 with storyfx
    menu:
        "Talk":
            scene nym_day_131 with dissolve
            if incest_story:
                neus "I'm sorry brother, but I'm a bit tired from last night."
            else:
                neus "I'm sorry, but I'm a bit tired from last night."
            neus "It's a little hard for me to move my legs."                        
        "Use ''Touch''":
            scene black with dissolve
            play sound magical1 volume 0.3
            stop char3 fadeout 0.5
            "You use ''Touch'' to give them a bit of energy."
            if incest_story:
                neus "Thank you brother, I feel very energized."
            else:
                neus "Thank you, I feel very energized."
            $ nym_tired=False
            jump nym_rooms
        "Leave":
            stop char3 fadeout 0.5
            jump nym_rooms
    jump nym_event_day_control_outfit_tired

label nym_ui_beach:
    scene nym_day_44 with dissolve
    call screen nym_ui_beach
screen nym_ui_beach:
    if not(is_view_nym_beach_sylvia):
        imagebutton:
            auto "nym_beach_sylvia0_%s"
            focus_mask True
            tooltip "%s"%neusname_sylvia
            action Jump("nym_beach_sylvia")
    else:
        imagebutton:
            auto "nym_beach_sylvia1_%s"
            focus_mask True
            tooltip "%s"%neusname_sylvia
            action Jump("nym_beach_sylvia")
    if not(is_view_nym_beach_lyra):
        imagebutton:
            auto "nym_beach_lyra0_%s"
            focus_mask True
            tooltip "%s"%neusname_lyra
            action Jump("nym_beach_lyra")
    else:
        imagebutton:
            auto "nym_beach_lyra1_%s"
            focus_mask True
            tooltip "%s"%neusname_lyra
            action Jump("nym_beach_lyra")
    if is_view_nym_beach_sylvia and is_view_nym_beach_lyra:
        imagebutton:
            auto "nym_beach_neus1_%s"
            focus_mask True
            tooltip "%s"%neusname
            action Jump("nym_beach_neus")
    else:
        imagebutton:
            auto "nym_beach_neus0_%s"
            focus_mask True
            tooltip "%s"%neusname
            action Jump("nym_beach_neus")

    textbutton _("{size=+100}{b}Finish"):
        style "chat_exit_button"
        anchor (0.5,0.5)
        pos (0.84, 0.87)
        action Jump("nym_beach_finish")

label nym_beach_sylvia:
    if not(is_view_nym_beach_sylvia):
        $ is_view_nym_beach_sylvia=True
        scene nym_day_45 with dissolve
        if incest_story:
            neus_sylvia "Hey brother, could you put some sunscreen on me?"
        else:
            neus_sylvia "Hey, could you put some sunscreen on me?"
        scene nym_day_46 with dissolve
        "Carefully, you apply the sunscreen to her skin."
        scene nym_day_47 with dissolve
        neus_sylvia "Thank you, although I think you put too much on me."
        if incest_story:
            mc "Maybe... but you look really good like this, sister."
        else:
            mc "Maybe... but you look really good like this."
        scene nym_day_48 with dissolve
        neus_sylvia "Hmm... as compensation, I could ask you for another favor."
        scene nym_day_49 with dissolve
        neus_sylvia "I want you to bathe my womb like you did with the sunscreen."
        scene nym_day_50 with dissolve
        play char1 penetration2
        neus_sylvia "Uh!"
        scene nym_day_51 with dissolve
        play char3 sex6
        neus_sylvia "{bt=2}{=lust_style}Ha ha ha ha{/bt}"
        neus_sylvia "This feels so good"
        neus_sylvia "My legs are shaking, but I can't stop moving."
        play char3 sex7
        scene nym_day_52 with dissolve
        neus_sylvia "{bt=2}{=lust_style}YES. YES. YES. YES.{/bt}"
        if incest_story:
            neus_sylvia "Please, keep fucking me brother."
        else:
            neus_sylvia "Please, keep fucking me."
        neus_sylvia "I-I can't take it anymore."
        scene nym_day_53 with dissolve
        neus_sylvia "I'm cumming..."
        stop char3
        play charM cum1
        scene nym_day_54 with dissolve
        play char1 climax2
        neus_sylvia "{sc=2}Umgggg!{/sc}"
        stop char1 fadeout 1.5
        scene nym_day_55 with dissolve
        neus_sylvia "Phew, that was great, even though my legs are very tired and it's hard for me to move them."
        if incest_story:
            "You withdraw and let your sister rest."
        else:
            "You withdraw and let [neusname_sylvia] rest."
    else:
        scene nym_day_47 with dissolve
        if incest_story:
            neus_sylvia "Hey brother, I'm sorry but I'm still tired."
        else:
            neus_sylvia "Hey, I'm sorry but I'm still tired."
    jump nym_ui_beach
label nym_beach_lyra:
    if not(is_view_nym_beach_lyra):
        $ is_view_nym_beach_lyra=True
        scene nym_day_56 with dissolve
        neus_lyra "Feeling the waves is very relaxing."
        if incest_story:
            neus_lyra "Do you want to join me to go a little deeper into the ocean brother?"
        else:
            neus_lyra "Do you want to join me to go a little deeper into the ocean?"
        scene nym_day_57 with dissolve
        neus_lyra "Ever since I touched the sea, I've had a fantasy."
        scene nym_day_58 with dissolve
        if incest_story:
            neus_lyra "Brother... I want to make love here... I want you to fill me."
        else:
            neus_lyra "I want to make love here... I want you to fill me."
        scene nym_day_59 with dissolve
        play char1 penetration2
        neus_lyra "Uh."
        scene nym_day_60 with dissolve
        play char3 sex6
        neus_lyra "{bt=2}{=lust_style}Ha ha ha ha{/bt}"
        neus_lyra "Doing it while listening to the waves is exciting."
        neus_lyra "I can't take it anymore."
        scene nym_day_61 with dissolve
        neus_lyra "I'm cumming... {e_heartbt2=FF0000}"
        stop char3
        play charM cum1
        scene nym_day_62 with dissolve
        play char1 climax1
        neus_lyra "{sc=2}Uhhhh!{/sc}"
        stop char1 fadeout 1.5
        scene nym_day_63 with dissolve
        neus_lyra "Doing it in the sea was, as expected, very relaxing."
        if incest_story:
            "You walk away and let your sister enjoy the waves."
        else:
            "You walk away and let [neusname_lyra] enjoy the waves."
    else:
        scene nym_day_63 with dissolve
        neus_lyra "Feeling the waves after making love is even more relaxing."
        if incest_story:
            neus_lyra "I'm sorry brother, but I'm not available right now... I need to rest for a while."
        else:
            neus_lyra "I'm sorry, but I'm not available right now... I need to rest for a while."
    jump nym_ui_beach
label nym_beach_neus:
    scene nym_day_64 with dissolve
    if not(is_view_nym_beach_neus):
        if incest_story:
            neus "Hey brother, do you want to accompany me for a walk along the seashore?"
        else:
            neus "Hey, do you want to accompany me for a walk along the seashore?"
    else:
        if incest_story:
            neus "Hey brother, do you want to accompany me for a walk along the seashore again?"
        else:
            neus "Hey, do you want to accompany me for a walk along the seashore again?"
    scene nym_day_65 with dissolve
    menu:
        "Yes":
            if is_view_nym_beach_sylvia and is_view_nym_beach_lyra:
                scene nym_day_66 with dissolve
                ""
                scene nym_day_67 with dissolve
                if incest_story:
                    "Your little sister pushes you against a tree."
                else:
                    "[neusname] pushes you against a tree."
                scene nym_day_68 with dissolve
                neus "Hey, it's unfair that you've been with my other parts but not with me."
                neus "I also want to receive a little love."
                scene nym_day_69 with dissolve
                mc "*Teasing tone* Hmm...  Are you that needy?"
                scene nym_day_70 with dissolve
                if incest_story:
                    neus "Eh!... what's wrong with that brother? I'm your girlfriend, right?"
                else:
                    neus "Eh!... what's wrong with that? I'm your girlfriend, right?"
                neus "Not to mention that you should treat my parts equally."
                scene nym_day_71 with dissolve
                neus "Therefore, it's your obligation to give me the same treatment you gave them."
                scene nym_day_72 with dissolve
                mc "I understand."
                scene nym_day_73 with dissolve
                play char1 penetration1
                neus "UH!"
                scene nym_day_74 with dissolve
                play char3 sex6
                if incest_story:
                    neus "Yes, brother, this feeling feels a thousand times better."
                else:
                    neus "Yes, this feeling feels a thousand times better."
                neus "You know how unbearable it is to feel that I have you inside because of the bond I have with them."
                neus "But knowing that my vagina is empty."
                neus "Feeling that I receive a creampie, but my uterus is not full of your semen."
                neus "It's unbearable."
                neus "Please, I want you to fill me  "
                stop char3
                play charM cum1
                scene nym_day_75 with dissolve
                play char1 climax2
                neus "Ugghhh!"
                stop char1 fadeout 2.0
                scene nym_day_76 with dissolve
                neus "Uff, I desperately needed this."
                scene nym_day_77 with dissolve
                if incest_story:
                    "You carry your little sister back and leave her under the umbrella."
                else:
                    "You carry [neusname] and leave her under the umbrella."
                jump nym_beach_finish
            else:
                scene nym_day_66 with dissolve
                if not(is_view_nym_beach_neus):
                    $ is_view_nym_beach_neus=True
                    if incest_story:
                        "You take a relaxing walk along the seashore with your sister."
                    else:
                        "You take a relaxing walk along the seashore with [neusname]."
                else:
                    if incest_story:
                        "You take a relaxing walk along the seashore with your sister again."
                    else:
                        "You take a relaxing walk along the seashore with [neusname] again."
        "No":
            scene nym_day_64 with dissolve
            neus "I understand, but if you change your mind I will always be available."
    jump nym_ui_beach

label nym_beach_finish:
    scene black with dissolve
    "You enjoy your time at the beach until it's time to go home."
    jump nym_time_advances
#----------------------------night----------------------------
label nym_event_night_control:
    scene nym_night_2 with storyfx
    menu:
        "Sleep":
            scene nym_night_4 with fadesex
            ""
            scene black with eyeclose
            ""
            play ambience morning_sounds fadein 1.0
            scene two_bodies_mc_night0_8 with eyeopen
            ""
            jump nym_sleeping_event
        "Blowjob":
            scene nym_night_5 with dissolve
            neus "Well, I guess it can't be helped, hehe."
            scene nym_night_6 with w33
            ly_ne_syl "*Kiss*"
            scene nym_night_7 with dissolve
            ly_ne_syl "*Lick*"
            scene nym_night_8 with fadesex
            play char3 double_suck1
            neus "*Suck suck*"
            neus_sylvia "*Lick*"
            neus_lyra "*Kiss*"
            if incest_story:
                mc "Your sucking, licking, and kisses on my dick, feels so good little sister."
            else:
                mc "Your sucking, licking, and kisses on my dick, feels so good."
            ly_ne_syl "{e_heartbt2=FF0000}"
            menu:
                "Cum":
                    stop char3
                    play charM cum1
                    scene nym_night_9 with hpunch
                    neus "Mmmm!"
                    scene nym_night_10 with dissolve
                    play char1 gulp1
                    neus "*Gulp*"
                    play char1 ahegao1
                    scene nym_night_11 with dissolve
                    neus "Ahhhhhhhhh"
                    stop char1 fadeout 1.5
                    scene nym_night_12 with dissolve
                    ly_syl "*Lick*"
                "Blowjob and {b}rimjob{/b}":
                    scene nym_night_13 with fadesex
                    neus_lyra "*Suck suck*"
                    neus "*Kiss*"
                    neus_sylvia "*Lick*"
                    menu:
                        "Cum":
                            pass
                    stop char3
                    play charM cum1
                    scene nym_night_14 with hpunch
                    neus_lyra "Mmmm!"
                    scene nym_night_15 with dissolve
                    play char1 gulp1
                    neus_lyra "*Gulp*"
                    play char1 ahegao1
                    scene nym_night_16 with dissolve
                    neus_lyra "Ahhhhhhhhhh"
                    stop char1 fadeout 1.5
            scene black with dissolve
            "They clean themselves"
        "Cunnilingus":
            scene nym_night_17 with dissolve
            neus "EH..."
            scene nym_night_18 with dissolve
            ly_syl "I would love that."
            scene nym_night_19 with fadesex
            play char3 groan_music
            neus "*Panting* uhhhh…"
            if incest_story:
                neus_sylvia "*Panting* Yes, yes, brother, I love how you move your tongue."
                neus_lyra "You touch all the right places."
                neus "Don't lick my clitoris too much brother, it's very sensitive."
            else:
                neus_sylvia "*Panting* Yes, yes, I love how you move your tongue."
                neus_lyra "You touch all the right places."
                neus "Don't lick my clitoris too much, it's very sensitive."
            neus "I'm about to..."
            stop char3
            scene nym_night_20 with dissolve
            play char1 groan1
            neus "I'm going to cum."
            scene nym_night_21 with hpunch
            play char1 double_climax1
            ly_ne_syl "{bt=2}{=lust_style}Mmmmm…{/bt}"
            stop char1 fadeout 2.0
            play char3 breathing1
            scene nym_night_22 with dissolve
            "{i}You spend a good time devouring their wet pussies.{/i}"
            scene nym_night_23 with dissolve
            "{i}You lick their clitoris and make them cum many times.{i}"
            scene nym_night_24 with dissolve
            neus_sylvia "Ufff, I can't take anymore."
            menu:
                "More":
                    scene nym_night_25 with dissolve
                    if incest_story:
                        "{i}You spend the whole night tasting your sister's pussies and making them climax.{i}"
                    else:
                        "{i}You spend the whole night tasting their pussies and making them climax.{i}"
                    scene nym_night_26 with dissolve
                    ly_ne_syl "*Panting*{e_heartbt2=FF0000}"
                    scene nym_night_27 with dissolve
                    "{i}When they couldn't take anymore, you used ''touch'' to give them a little energy.{i}"
                    scene nym_night_28 with dissolve
                    "{i}And continued to blank their minds with pleasure.{i}"
                    stop char3 fadeout 2.0 #!!!!!!!!!!!!!!!! I added
                    scene black with dissolve
                    ""
                    scene night_transition with dissolve
                    play ambience morning_sounds fadein 0.5
                    scene day_transition with wiperight
                    ""
                    $ nym_time=0
                    $ nym_tired=True
                    jump nym_rooms
                "Stop":
                    stop char3 fadeout 2.0
                    scene black with dissolve
                    play sound magical1 volume 0.3
                    "{i}You use ''Touch'' to give them a little energy to recover.{i}"
        "Sex":
            scene nym_night_29 with dissolve
            ly_ne_syl "{e_heartbt2=FF0000}"
            scene black with dissolve
            if incest_story:
                neus_sylvia "Could you give us a moment brother, we need to change."
            else:
                neus_sylvia "Could you give us a moment, we need to change."
            neus_lyra "We won't take long."
            neus "This piece of clothing is somewhat exhibitionist."
            scene nym_night_30 with w9
            if incest_story:
                neus  "Brother.. we are ready."
            else:
                neus  "Well, we are ready."
            scene nym_night_31 with w33
            ""
            scene nym_night_32 with dissolve
            play char1 double_penetration1
            ly_ne_syl "UH!"
            scene nym_night_33 with fadesex
            play char3 double_sex3
            ly_ne_syl "{bt=2}{=lust_style}Oh oh oh{/bt}"
            neus "As always, this is very pleasurable."
            neus_lyra "Pleasure itself is great."
            neus "But for it to be multiplied by three is wonderful…"
            neus "I'm about to climax."
            stop char3
            play charM cum1
            scene nym_night_34 with hpunch
            play char1 double_climax1
            ly_ne_syl "{sc=2}*Orgasming* AAAAAAaaghhhhhhhhgh...{/sc}"
            stop char1 fadeout 2.0
            play char3 breathing1
            scene nym_night_35 with dissolve
            neus "*Panting* OH MY GOD"
            neus "*Panting* I am so satisfied, I felt like I came 3 times in a row."
            stop char3 fadeout 2.0
            scene nym_night_36 with dissolve
            if incest_story:
                neus_sylvia "Please brother, I want more."
            else:
                neus_sylvia "Please, I want more."
            menu:
                "More":
                    scene nym_night_39 with fadesex
                    ""
                    scene nym_night_40 with dissolve
                    play char1 penetration2
                    neus_sylvia "UH!"
                    scene nym_night_41 with fadesex
                    play char3 sex7
                    neus_sylvia "{bt=2}{=lust_style}Oh oh oh{/bt}"
                    if incest_story:
                        neus_sylvia "Yes, yes, give lots of kisses to your sister's uterus!"
                    else:
                        neus_sylvia "Yes, yes, give lots of kisses to my uterus!"
                    neus_sylvia "Oh God, this is so pleasurable!"
                    if incest_story:
                        neus_sylvia "I love how you drill my pussy and my uterus brother!"
                        neus_sylvia "My uterus has no escape, it wants to drink all your incest baby juice."
                    else:
                        neus_sylvia "I love how you drill my pussy and my uterus!"
                        neus_sylvia "My uterus has no escape, it wants to drink all your baby juice."
                    neus_sylvia "{sc=1}I CAN'T TAKE IT ANYMORE!{/sc}"
                    scene nym_night_42 with dissolve
                    neus_sylvia "{sc=3}{=lust_style}I'M CUMMING...{/sc}{w=1.0}{nw}"
                    stop char3
                    play charM cum1
                    scene nym_night_43 with hpunch
                    play char1 climax2
                    neus_sylvia "{sc=2}{=lust_style}*Orgasming* AAAAAAaaghhhhhhhhgh...{/sc}"
                    stop char1 fadeout 2.0
                    scene nym_night_44 with w9
                    play char3 breathing1
                    ""
                    stop char3 fadeout 2.0
                    scene nym_night_45 with dissolve
                    play char1 penetration3
                    neus_lyra "{sc=2}Mmmm!{/sc}"
                    scene nym_night_46 with fadesex
                    play char3 sex5
                    neus_lyra "{bt=2}{=lust_style}Ah Ah Ah{/bt}"
                    if incest_story:
                        neus_lyra "{bt=2}{=lust_style}I love it brother{/bt}"
                    else:
                        neus_lyra "{bt=2}{=lust_style}I love it{/bt}"
                    neus_lyra "It's so pleasurable I can't stand it anymore"
                    neus_lyra "I'm about to reach {bt=2}{=lust_style}climax{/bt}"
                    stop char3
                    play charM cum1
                    scene nym_night_47 with hpunch
                    play char1 climax2
                    neus_lyra "{sc=2}*Orgasming*{=lust_style} Mmmmmmmm...{/sc}"
                    stop char1 fadeout 2.0
                    play char3 breathing1
                    scene nym_night_48 with dissolve
                    ""
                    scene nym_night_49 with w33
                    "You kept filling their pussies as if there was no tomorrow."
                    scene nym_night_50 with dissolve
                    if incest_story:
                        neus_sylvia "Brother, it feels so good, please, keep spanking my ass."(multiple=2)
                    else:
                        neus_sylvia "It feels so good, please, keep spanking my ass."(multiple=2)
                    "You gave them many slaps on their big asses."(multiple=2)
                    neus "My buttocks are very red."
                    scene nym_night_51 with dissolve
                    "The room was filled with obscene smells."
                    scene nym_night_52 with dissolve
                    "They climaxed several times."
                    scene nym_night_53 with dissolve
                    neus_sylvia "This fheels so ghood, although I would lhike to try shomething.\n(This feels so good, although I would like to try something.)"
                    if incest_story:
                        neus_sylvia "Would yhou do it fhor me, please bhrother?\n(Would you do it for me, please brother?)"
                    else:
                        neus_sylvia "Would yhou do it fhor me, please?\n(Would you do it for me, please?)"
                    menu:
                        "Accept offer (BDSM)":
                            scene black with dissolve
                            stop char3 fadeout 3.0
                            "You wait a moment while they put on a mask and handcuffs."
                            neus "I can't see anything with this."
                            neus_lyra "I like these handcuffs."
                            scene nym_night_54 with w39
                            if incest_story:
                                neus_sylvia "I always wanted to know what it would feel like to be tied up and dominated, by my big brother, while I can't see anything."
                            else:
                                neus_sylvia "I always wanted to know what it would feel like to be tied up and dominated while I can't see anything."
                            scene nym_night_55 with dissolve
                            neus_sylvia "Could you fulfill this fetish for me?"
                            scene nym_night_56 with dissolve
                            play char3 kissing1 volume 2.0
                            "While you kiss them, you give little taps to their bellies, indicating that their uteruses should be ready to receive you."
                            stop char3 fadeout 4.0
                            scene nym_night_57 with w39
                            neus "This is too much, not being able to see anything, feeling that you are fucking me, but knowing that my vagina is empty, it feels good but it is very uncomfortable. I also want you to fill me."
                            scene nym_night_58 with w9
                            play char3 breathing1
                            "You fill their vaginas even more."
                            neus "My uterus is so full, the semen is coming out."
                            ly_syl "{e_heartbt2=FF0000}"
                            scene nym_night_59 with w33
                            "You handcuff [neusname_sylvia] to the pole"
                            scene nym_night_60 with dissolve
                            if incest_story:
                                neus_sylvia "Could you spank me brother?"
                            else:
                                neus_sylvia "Could you spank me?"
                            mc "Hmm… I don't feel like it at the moment, but if you ask me in a more appropriate way, I might consider it."
                            scene nym_night_61 with dissolve
                            neus_sylvia "Master, could you spank my masochist ass?"
                            menu:
                                "Slap":
                                    pass
                            play charM slap_hard1
                            scene nym_night_62 with hpunch
                            play char1 groan_hard1
                            neus_sylvia "Uh!"
                            stop char1 fadeout 1.5
                            scene nym_night_63 with dissolve
                            neus_sylvia "Spank me more."
                            mc "Hmm… I think it's better to leave it there."
                            scene nym_night_64 with dissolve
                            neus_sylvia "Master, please, keep spanking my buttocks, leave them so red that I can't sit for days."
                            play charM slap_hard1
                            scene nym_night_65 with hpunch
                            play char1 penetration1
                            neus_sylvia "{e_heartbt=FF0000}"(multiple=2)
                            mc "I suppose if you ask like that, I think I have no choice."(multiple=2)
                            scene black with dissolve
                            "You spank her ass until it turns a deep red."
                            play char3 breathing2 fadein 2.0
                            scene nym_night_66 with w9
                            neus_sylvia "{e_heartbt2=FF0000}"
                            neus_sylvia "My {bt=2}{=lust_style}bhutthocks{/bt} is {bt=2}{=lust_style}rhed hoht{/bt}.\n(My buttocks is red hot.)"
                            neus_sylvia "{bt=2}{=lust_style}Plhease mhaster{/bt}, chontinue {bt=2}{=lust_style}sphanking{/bt} mhy {bt=2}{=lust_style}mashochhistic ahss{/bt}.\n(Please master, continue spanking my masochistic ass.)"
                            scene nym_night_67 with w39
                            "You spend the whole night pleasuring them and filling their uteruses."
                        "Do not accept offer":
                            scene nym_night_68 with w39
                            if incest_story:
                                "You spend the whole night pleasuring your sister and filling their uteruses."
                            else:
                                "You spend the whole night pleasuring them and filling their uteruses."
                    stop char3 fadeout 2.0
                    scene black with dissolve
                    ""
                    scene night_transition with dissolve
                    play ambience morning_sounds fadein 0.5
                    scene day_transition with wiperight
                    ""
                    $ nym_time=0
                    $ nym_tired=True
                    jump nym_rooms
                "Stop":
                    scene nym_night_37 with dissolve
                    neus_sylvia "I understand."
                    scene nym_night_38 with dissolve
                    neus "T-Thank you."
                    scene black with dissolve
                    "They clean themselves"
        "Leave":
            jump nym_rooms
    jump nym_event_night_control
label nym_event_night_control_tired:
    play char3 breathing1 volume 0.5
    scene nym_night_3 with storyfx
    menu:
        "Sleep":
            stop char3 fadeout 1.0
            scene nym_night_4 with fadesex
            ""
            scene black with eyeclose
            ""
            play ambience morning_sounds fadein 1.0
            scene two_bodies_mc_night0_8 with eyeopen
            ""
            jump nym_sleeping_event
        "Use ''Touch''":
            stop char3 fadeout 0.5
            scene black with dissolve
            play sound magical1 volume 0.3
            "You use ''Touch'' to give them a bit of energy."
            if incest_story:
                neus "Thank you brother, I feel very energized."
            else:
                neus "Thank you, I feel very energized."
            $ nym_tired=False
            jump nym_rooms
        "Leave":
            stop char3 fadeout 0.5
            jump nym_rooms
    jump nym_event_night_control_tired
#----------------------------End----------------------------
label menu_nym_ending:
    menu:
        "Ending":
            jump nym_ending
        "Leave":
            jump nym_rooms
label nym_ending:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        if persistent.gallery_pregnancy_censored:    
            $ set_active_pregnancy = False
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
        $ neusname_lyra = persistent.gallery_lyra   
        $ neusname_sylvia = persistent.gallery_sylvia
    stop ambience fadeout 1.0
    play music a_stray_cat_aimed_for_space volume 0.5 fadein 2.0
    scene tb_end_0 with w39
    "They became your wives"
    $ renpy.music.set_volume(0.2,delay=2.5,channel='music')
    scene nym_end_0 with w9
    if incest_story:
        ly_ne_syl "Brother, we're ready"
    else:
        ly_ne_syl "Honey, we're ready"
    $ renpy.music.set_volume(0.02,delay=2.5,channel='music')
    scene nym_end_1 with dissolve
    play char3 kissing1
    pause 0.05
    play char2 kissing1 loop
    neus "*Kiss*"(multiple=2)
    neus_lyra "*Lick*"(multiple=2)
    neus_sylvia "*Suck*"
    stop char3
    stop char2
    scene nym_end_2 with dissolve
    if incest_story:
        neus_sylvia "Big brother, I can't take it anymore, I'm already very wet"
    else:
        neus_sylvia "I can't take it anymore honey, I'm already very wet"
    scene nym_end_3 with w9
    ""
    scene nym_end_4 with dissolve
    play char1 double_penetration1
    ly_ne_syl "{bt=2}{=lust_style}Uhmmm.{/bt}"
    scene nym_end_5 with dissolve
    play char3 threesome_sex2
    ly_ne_syl "{bt=2}{=lust_style}Ha ha ha.{/bt}"
    neus "This feels so {bt=2}{=lust_style}good{/bt}."
    neus_sylvia "My womb wants you to fill it up."
    neus_lyra "As I am now your wife, I have the obligation to receive all your baby juice."
    if incest_story:
        ly_ne_syl "So please big brother, {bt=2}{=lust_style}impregnate{/bt} your wives' {bt=2}{=lust_style}womb{/bt}."
    else:
        ly_ne_syl "So please, {bt=2}{=lust_style}impregnate{/bt} your wives' {bt=2}{=lust_style}womb{/bt}."
    menu:
        "Cum":
            pass
    stop char3
    play charM cum1
    scene nym_end_6 with hpunch
    play char1 double_climax2
    ly_ne_syl "{sc=2}Uh!{/sc}"
    stop char1 fadeout 3.0
    $ renpy.music.set_volume(0.3,channel='char3')
    play char3 breathing1
    scene nym_end_7 with dissolve
    ly_ne_syl  "{e_heartbt2=FF0000}"
    scene nym_end_8 with w39
    ""
    $ renpy.music.set_volume(1.0,channel='char3')
    scene nym_end_9 with wiperight
    ly_ne_syl "{sc=2}*Orgasming* Ugggggh!{/sc}"
    scene nym_end_10 with wipeleft
    ly_ne_syl "{e_heartbt2=FF0000}"
    neus_lyra "With everything you filled me with, I am one hundred percent sure that I am already pregnant."
    play char3 breathing2 fadein 1.5
    scene nym_end_11 with dissolve
    neus "My head is blank, I know I should not ask for more."
    neus "But I want you to use me as your personal onahole. I want to be your onahole wife."
    mc "*Mocking tone* Really?"
    scene nym_end_12 with dissolve
    if incest_story:
        neus "What's wrong big brother? Did you forget that those degenerates are also me."
    else:
        neus "What's wrong? You forget that those degenerates are also me."
    neus "And at this point, I don't care. I just want you to give me lots of love."
    scene nym_end_13 with w39
    neus "Yes yes yes, fill me up."
    scene nym_end_14 with w33
    ly_ne_syl "{e_heartbt2=FF0000}"
    if set_active_pregnancy:
        "After that night, it was inevitable that they would become pregnant."
        stop char3 fadeout 2.5
        scene black with cw39
        ""
        $ renpy.music.set_volume(0.2,delay=2.5,channel='music')
        scene nym_end_15 with w39
        neus "My belly grew very fast, although I suppose that's normal."
        scene nym_end_16 with dissolve
        neus "What really bothers me is this outfit, it's a bit weird."
        scene nym_end_17 with dissolve
        neus_sylvia "I would say it is very suitable for our situation."
        scene nym_end_18 with dissolve
        neus_lyra "With this you could say that we are officially dairy cows."
        scene nym_end_19 with dissolve
        neus_lyra "Although I think the level of milk production will not be the same for all."
        neus "…"
        scene nym_end_20 with dissolve
        neus_sylvia "*Mocking tone* Let's start... and you can use my big breasts."
        $ renpy.music.set_volume(0.02,delay=2.5,channel='music')
        scene nym_end_21 with w21
        neus_sylvia "Now my breasts can hug your cock very well."
        scene nym_end_22 with fadesex
        play char3 handjob2
        neus_lyra_neus "*Kiss*"
        if incest_story:
            neus_sylvia "How do my fat little titties feel big brother?"
        else:
            neus_sylvia "How do my fat little titties feel?"
        mc  "Uff, Great."
        neus_sylvia "Hehe"
        menu:
            "Cum":
                pass
        stop char3
        play charM cum1
        scene nym_end_23 with hpunch
        ""
        scene nym_end_24 with w33
        neus_sylvia "I can't take it anymore... I want to feel you inside me."
        scene nym_end_25 with dissolve
        play char1 penetration1
        neus_sylvia "{sc=2}UH!{/sc}"
        scene nym_end_26 with fadesex
        play char3 sex7
        neus_sylvia "I needed this so much."
        neus_sylvia "Since we couldn't have vaginal sex often, because of my situation."
        neus_sylvia "We had to resort to using my back hole"
        neus_sylvia "And now I think I've become addicted to anal sex."
        if incest_story:
            neus_sylvia "I want you to fill me up to the brim brother."
        else:
            neus_sylvia "I want you to fill me up to the brim."
        menu:
            "Cum":
                pass
        stop char3
        play charM cum1
        scene nym_end_27 with hpunch
        play char1 climax2
        neus_sylvia "{bt=2}{=lust_style}Mmmm!{/bt}"
        stop char1 fadeout 3.0
        scene nym_end_28 with w33
        play char3 breathing1
        play char2 kissing1 loop
        neus "I love this."
        neus "Although I think there is room for improvement... you could whisper in my ear how much you love me."
        menu:
            "Whisper in her ear":
                pass
            "Joke":
                mc "I'm sorry, I didn't hear you well, could you repeat that?"
                stop char2 fadeout 1.5
                scene nym_end_29 with dissolve
                neus "Here we go again, I know you heard me well."
                neus "Although I think I know what you're up to... you want me to say it first, right?"
                neus "I guess that's fair."
                scene nym_end_30 with dissolve
                neus "{bt=2}{=lust_style}I love you. I love you. I love you.{/bt}"
                scene nym_end_31 with dissolve
                neus "Okay, I've said it... can I get my reward now?"
        stop char2 fadeout 1.5
        scene nym_end_32 with dissolve
        mc "I love you."
        scene nym_end_33 with dissolve
        play char1 groan1
        if incest_story:
            neus "(Just hearing those words from my brother made me {color=#cc0066}very happy{/color} and I almost reached {color=#cc0066}climax{/color}.)"
        else:
            neus "(Just hearing those words made me {color=#cc0066}very happy{/color} and I almost reached {color=#cc0066}climax{/color}.)"
        neus "(Damn, I'm so obviously obsessed.)"
        neus "(Although at this point I don't care anymore, I just {color=#cc0066}want{/color} to be {color=#cc0066}myself{/color} without {color=#cc0066}holding back{/color}.)"
        stop char3 fadeout 2.0
        scene black with dissolve
    else:
        scene black with cw39
        stop char3 fadeout 2.0
        "{size=+8}{color=#ff0000}Pregnant sex censorship activated."
    $ renpy.music.set_volume(1.0,delay=2.5,channel='music')
    "You had lots of good times with them."
    scene nym_end_34 with dissolve
    "Some quite {color=#cc0066}peculiar{/color}."
    scene nym_end_35 with dissolve
    "But all were fun."
    python:
        achievement.grant("End")
        achievement.sync()
    if not ending_6_obtained:
        $ endings_obtained_count += 1
        $ ending_6_obtained = True
    centered "{color=#cc0066}{size=+500}END"
    scene black with snow1
    "You have obtained {color=#cc0066}Ending 6{/color} out of {color=#cc0066}[available_endings] possible endings{/color}."
    $ renpy.end_replay()
    $ persistent.main_menu_b=6
    jump nym_ending_ending
label nym_ending_ending:
    scene black
    menu(screen="custom_choice_long"):
        "Continue":
            jump nym_rooms
        "Main Menu":
            menu(screen="custom_choice_long"):
                "Are you sure you want to go to the main menu?"
                "Yes":
                    $ MainMenu(confirm=False)()
                "No":
                    jump nym_ending_ending