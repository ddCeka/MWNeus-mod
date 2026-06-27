default is_stundere_magazine=False
screen mc_room_quest:    
    imagebutton:
        auto "btn_tv_event_%s" 
        pos   225, 230        
        tooltip _("Puzzle settings")
        action Jump ("mc_room_pc")
    if not(item_book_magic.is_view):
        if time < 4:
            imagebutton:
                auto "btn_book_spell_%s" 
                focus_mask True           
                action Jump("book_magic")   
                tooltip _("Spell Book")    
        else:
            imagebutton:
                auto "btn_night_book_spell_%s" 
                focus_mask True           
                action Jump("book_magic")   
                tooltip _("Spell Book")  
    if quest_v2 and not(questMain_v2_3.completion):
        if time < 4:
            imagebutton:
                auto "btn_hentai_magazine_%s" 
                focus_mask True           
                action Jump("hentai_magazine")
                tooltip _("Hentai manga")
        else:
            imagebutton:
                auto "btn_night_hentai_magazine_%s" 
                focus_mask True           
                action Jump("hentai_magazine")
                tooltip _("Hentai manga")
    elif not quest_v2 and not(questMain_1.completion):
        if time < 4:
            imagebutton:
                auto "btn_hentai_magazine_%s" 
                focus_mask True           
                action Jump("hentai_magazine")
                tooltip _("Hentai manga")
        else:
            imagebutton:
                auto "btn_night_hentai_magazine_%s" 
                focus_mask True           
                action Jump("hentai_magazine")
                tooltip _("Hentai manga")
    if not(is_stundere_magazine):
        if time < 4:
            imagebutton:
                auto "btn_stundere_magazine_%s" 
                focus_mask True           
                action Jump("stundere_magazine")
                tooltip _("Magazine")
        else:
            imagebutton:
                auto "btn_night_stundere_magazine_%s" 
                focus_mask True           
                action Jump("stundere_magazine")
                tooltip _("Magazine")
    if not(item_portrait_neus.is_view):
        if time < 4:
            imagebutton:
                auto "btn_portrait_neus_%s" 
                focus_mask True           
                action Jump("portrait_neus")   
                tooltip _("Portrait of [neusname]")
        else:
            imagebutton:
                auto "btn_night_portrait_neus_%s" 
                focus_mask True           
                action Jump("portrait_neus")   
                tooltip _("Portrait of [neusname]")
    imagebutton:
        auto "btn_bed_event_%s"       
        action Jump ("mc_bed")
        tooltip _("Sleep")
        xpos 1300
        ypos 450
        
label mc_bed:
    scene bg_mc_room_night    
    menu:        
        "Sleep":
            jump expression "sleeping_event%s"%mc_event_lvl
        "Back":
            jump rooms

#----------------------------Level 0---------------------------------
default night_1 = False
default whisper_vol = 0.1
default hypnosis_alpha = 0.334
label sleeping_event0:  
    scene mc_room_sleep_close with dissolve
    scene black with eyeclose 
    if not night_1:
        $days_to_final_obsession+=1    
    else:
        $night_1=False     
    if (quest_v2 and questMain_v2_2.completion and not questMain_v2_3.completion):           
        stop music
        scene bg_hypnosis with dissolve  
        play sound magical1 volume 0.1
        play char1 whisper volume 0.3
        pause 0.5   
        centered "{size=+40}You want to take [neusname] on a date to the new amusement park, You want to take [neusname] on a date to the new amusement park, You want to take [neusname] on a date to the new amusement park ...{w=8.0}{nw}"
        scene black with dissolve
        stop char1 fadeout 1.0
        pause 1.0
        scene mc_room_sleep_open with eyeopen
        mc "..." 
        scene black with dissolve
        "With a quiet, gentle pull, the whispers guide your footsteps, leading you toward the [questMain_v2_select.place]." 
        jump expression questMain_v2_select.label_event
    elif not quest_v2 and not questMain_9.completion and days_to_final_obsession>=3:        
        stop music          
        scene bg_hypnosis with dissolve  
        play sound magical1 volume 0.1
        play char1 whisper volume 0.3
        pause 0.5
        if incest_story:
            centered "{size=+40}You want a son with your sister. You want a son with your sister. You want a son with your sister. You want a son with your sister. You want a son with your sister. You want a son with your sister...{w=8.0}{nw}" 
        else:
            centered "{size=+40}You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]...{w=8.0}{nw}"
        scene black with dissolve
        stop char1 fadeout 1.0
        pause 1.0
        scene mc_room_sleep_open with eyeopen
        mc "..." 
        scene black with dissolve
        if questMain_select.place=="neus":
            "With a quiet, gentle pull, the whispers guide your footsteps, drawing you closer to [neusname]'s room."
        else:
            "With a quiet, gentle pull, the whispers guide your footsteps, leading you toward the [questMain_select.place]."           
        jump expression questMain_select.label_event    
    elif relationship_level < 3 and days_to_final_obsession > 0:
        stop music
        if days_to_final_obsession == 1:
            $ whisper_vol = 0.05
            $ hypnosis_alpha = 0.25
        elif days_to_final_obsession == 2:
            $ whisper_vol = 0.15
            $ hypnosis_alpha = 0.5
        play char1 whisper volume whisper_vol
        pause 1.0
        show bg_hypnosis at Transform(alpha=hypnosis_alpha) with dissolve
        pause 7.0
        scene black with dissolve
        stop char1 fadeout 1.0
        pause 1.0
    scene mc_room_sleep_open with eyeopen   
    jump next_day
    
#----------------------------Level 1---------------------------------
label sleeping_event1:  
    stop music fadeout 1.0
    scene mc_room_sleep_close with dissolve
    scene black with eyeclose
    $days_to_final_obsession+=1       
    if not quest_v2 and not questMain_9.completion and days_to_final_obsession>=3:  
        scene bg_hypnosis with dissolve  
        play sound magical1 volume 0.1
        play char1 whisper volume 0.3
        pause 0.5
        if incest_story:
            centered "{size=+40}You want a son with your sister. You want a son with your sister. You want a son with your sister. You want a son with your sister. You want a son with your sister. You want a son with your sister...{w=8.0}{nw}" 
        else:
            centered "{size=+40}You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]. You want a son with [neusname]...{w=8.0}{nw}" 
        scene black with dissolve
        stop char1 fadeout 1.0
        pause 1.0
        scene mc_room_sleep_open with eyeopen
        mc "..." 
        scene black with dissolve
        if questMain_select.place=="neus":
            "With a quiet, gentle pull, the whispers guide your footsteps, drawing you closer to [neusname]'s room."
        else:
            "With a quiet, gentle pull, the whispers guide your footsteps, leading you toward the [questMain_select.place]."               
        jump expression questMain_select.label_event 
    elif relationship_level < 3 and days_to_final_obsession > 0:
        if days_to_final_obsession == 1:
            $ whisper_vol = 0.05
            $ hypnosis_alpha = 0.25
        elif days_to_final_obsession == 2:
            $ whisper_vol = 0.15
            $ hypnosis_alpha = 0.5
        play char1 whisper volume whisper_vol
        pause 1.0
        show bg_hypnosis at Transform(alpha=hypnosis_alpha) with dissolve
        pause 7.0
        scene black with dissolve
        stop char1 fadeout 1.0
        pause 1.0
        
    if is_wake_up_neus:
        play ambience morning_sounds fadein 1.0
        scene mc1_0 with eyeopen
        if incest_story:
            neus "Good morning, brother"
            scene mc1_1 with dissolve
            mc "Good morning"
        else:
            neus "Good morning, [firstname]"
            scene mc1_1 with dissolve
            mc "Good morning, [neusname]"
        stop ambience fadeout 1.0
        if not quest_v2: 
            $is_stundere_magazine = True   
        $is_wake_up_neus=False   
    else:
        scene mc_room_sleep_open with eyeopen
    jump next_day

#----------------------------Level 2---------------------------------
label sleeping_event2:
    stop music fadeout 1.0
    scene mc_room_sleep_close with dissolve
    scene black with eyeclose  
    if not night_1:
        $days_to_final_obsession+=1    
    else:
        $night_1=False
    if not quest_v2 and not questMain_9.completion and days_to_final_obsession>=3:
        scene bg_hypnosis with dissolve  
        play sound magical1 volume 0.1
        play char1 whisper volume 0.3
        pause 0.5 
        if incest_story:
            centered "{size=+40}You only love your sister. You only love your sister. You only love your sister. You only love your sister. You only love your sister. You only love your sister. You only love your sister...{w=8.0}{nw}" 
        else:
            centered "{size=+40}You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]. You only love [neusname]...{w=8.0}{nw}" 
        scene black with dissolve
        stop char1 fadeout 1.0
        pause 1.0
        scene mc_room_sleep_open with eyeopen
        mc "..." 
        scene black with dissolve
        if questMain_select.place=="neus":
            "With a quiet, gentle pull, the whispers guide your footsteps, drawing you closer to [neusname]'s room."
        else:
            "With a quiet, gentle pull, the whispers guide your footsteps, leading you toward the [questMain_select.place]."                   
        jump expression questMain_select.label_event  
    elif relationship_level < 3 and days_to_final_obsession > 0:
        if days_to_final_obsession == 1:
            $ whisper_vol = 0.05
            $ hypnosis_alpha = 0.25
        elif days_to_final_obsession == 2:
            $ whisper_vol = 0.15
            $ hypnosis_alpha = 0.5
        play char1 whisper volume whisper_vol
        pause 1.0
        show bg_hypnosis at Transform(alpha=hypnosis_alpha) with dissolve
        pause 7.0
        scene black with dissolve
        stop char1 fadeout 1.0
        pause 1.0
       
    if is_wake_up_neus and not(neus_is_evading):
        play ambience morning_sounds fadein 1.0
        scene mc2_0 with eyeopen
        if incest_story:
            neus "Brother, wake up"
        else:
            neus "Hey, wake up"
        scene black with dissolve 
        "She moves the sheets around"
        scene mc2_1 with dissolve
        neus "He's always so energetic" 
        scene mc2_2 with dissolve
        neus "I can't believe I got this thing inside me, although it did cause me a lot of pain."
        if incest_story:
            mc "Good morning little sister, are you having fun?"
            scene mc2_3 with dissolve
            neus "Ugh, G ... Good morning brother"
        else:
            mc "Good morning, are you having fun?"
            scene mc2_3 with dissolve
            neus "Ugh, G ... Good morning"
        scene black with dissolve
        neus "I... I'm leaving"
        stop ambience fadeout 1.0
        if incest_story:
            "Your sister leaves with a red face"
        else:
            "[neusname] leaves with a red face"
        if not quest_v2: 
            $is_stundere_magazine = True   
        $is_wake_up_neus=False    
    else:        
        scene mc_room_sleep_open with eyeopen     
    $N_state=0
    jump next_day
#----------------------------Level 3---------------------------------
label sleeping_event3:
    stop music fadeout 1.0
    scene mc_room_sleep_close with dissolve
    scene black with eyeclose     
    $N_state=0  
    if lvl_event_fear_aux==1:
        play ambience night_ambience volume 0.1
        scene mc3_f_0 with fadesex
        if incest_story:
            neus "Hey brother, are you still awake?"
        else:
            neus "Hey, are you still awake?"
        scene mc3_f_1 with dissolve
        neus "C-Can I sleep with you tonight?"
        menu:
            "Sure":
                if lvl_event_fear!=2:
                    $lvl_event_fear=1
                scene mc3_f_2 with dissolve
                neus "Really? Thank you!"
                scene black with dissolve
                if incest_story:
                    "Your little sister climbs into bed with you."
                    scene mc3_f_3 with dissolve
                    neus "H-Hey brother, can I hug you?"
                else:
                    "She climbs into bed with you."
                    scene mc3_f_3 with dissolve
                    neus "H-Hey, can I hug you?"
                mc "Of course you can, you seem really scared."
                scene mc3_f_4 with dissolve
                neus "Maybe a little... it's your fault, you made me watch that movie."
                scene mc3_f_5 with dissolve
                neus "And by the way, why do you always bother me about my breasts?"
                neus "Do you really like big boobs that much?"
                scene mc3_f_6 with dissolve
                mc "I never claimed that, and besides, it's fun to see how much it affects you."
                scene mc3_f_5 with dissolve
                neus "It's not fun for me. It's like if I mocked your weird haircut."
                scene mc3_f_6 with dissolve
                mc "I thought you liked it... that's why I always get it."
                scene mc3_f_7 with dissolve
                neus "Ah! Yes, yes, your haircut is cool."
                scene mc3_f_8 with dissolve
                mc "(Maybe I should change my hairstyle.)"(multiple=2)
                neus "*Yawning* I'm so tired."(multiple=2)
                scene mc3_f_9 with dissolve
                if incest_story:
                    neus "We better go to sleep brother."
                else:
                    neus "We better go to sleep."
                stop ambience fadeout 0.5
                call splash_message(_("Midnight")) from _call_splash_message_51 
                play ambience night_ambience volume 0.1
                scene mc3_f_10 with dissolve               
                neus "*Mumbling in her sleep* My breasts aren't small, they're average, I swear."               
                menu:
                    "Help her sleep {e_heartbt=FF0000}":
                        scene mc3_f_11 with fadesex
                        ""
                        scene mc3_f_12 with dissolve
                        play char1 penetration4
                        neus "Ah"
                        scene mc3_f_13 with dissolve
                        play char3 sex2
                        neus "{bt=2}{=lust_style}ah ah ah{/bt}"
                        if incest_story:
                            neus "*Mumbling in her sleep* Don't be so rude to me, brother."  
                        else:
                            neus "*Mumbling in her sleep* Don't be so rude to me, [firstname]."                        
                        stop char3
                        play charM cum1 
                        scene mc3_f_14 with dissolve
                        play char1 climax1
                        neus "Ohh."
                        scene mc3_f_15 with dissolve 
                        neus "*Mumbling in her sleep*So hot." 
                        stop ambience fadeout 0.5
                        call splash_message(_("The next day")) from _call_splash_message_52
                        play ambience morning_sounds fadein 1.0
                        scene mc3_f_15_0 with dissolve  
                        neus "G..(My stomach feels very warm)"
                        scene mc3_f_15_1 with dissolve
                        neus "..."    
                        stop ambience fadeout 1.0
                        scene black with dissolve
                        if incest_story:
                            "When you wake up, your sister is already gone." 
                        else:
                            "When you wake up, [neusname] is already gone." 
                        $ neus_left_room = True
                        call addLust(4) from _call_addLust_7             
                    "Hug her":
                        scene mc3_f_16 with dissolve
                        if incest_story:
                            "Your little sister was sleep-talking for a while, but after a tight hug, she calmed down."
                        else:
                            "She was sleep-talking for a while, but after a tight hug, she calmed down."
                        stop ambience fadeout 0.5
                        call splash_message(_("The next day")) from _call_splash_message_53
                        play ambience morning_sounds fadein 1.0
                        scene mc3_f_16_1 with dissolve
                        neus "(It's been a while since I slept that well.)"
                        scene mc3_f_16_2 with dissolve
                        if incest_story:
                            neus "Mmm... good morning brother... thank you for letting me sleep with you."
                        else:
                            neus "Mmm... good morning... thank you for letting me sleep with you."
                        scene mc3_f_16_3 with dissolve
                        neus "I have some things to do, so I'll leave you."
                        stop ambience fadeout 1.0
                        scene black with dissolve
                        "She leaves your room."
            "No":
                scene mc3_f_17 with dissolve
                neus "Oh... Okay, I guess you want to be alone."
                neus "Have a good sleep, g-goodnight."
                stop ambience fadeout 0.5
                scene black with dissolve
                "She leaves your room."
    if lvl_event_fear_aux==2:
        $lvl_event_fear=2
        play ambience night_ambience volume 0.1
        scene mc3_f_18 with fadesex
        if incest_story:
            neus "Hey brother, can I sleep with you again?"
        else:
            neus "Hey, can I sleep with you again?"
        mc "Sure, and I think we should sleep together from now on"
        scene mc3_f_19 with dissolve
        neus "No way. If I sleep with you, there’s zero chance I’ll get any good sleep."
        scene mc3_f_20 with dissolve
        neus "Now be quiet, keeper of questionable movies, and be a good pillow"
        scene mc3_f_21 with dissolve
        if incest_story:
            mc "(I can feel my sister's small warm breasts)"(multiple=2)       
        else:
            mc "(I can feel her small warm breasts)"(multiple=2)
        neus "(Cuddling up against his chest is so relaxing)"(multiple=2)       
        menu:  
            "Convince her to sleep with you":
                scene mc3_f_22 with dissolve
                neus "!?"
                if incest_story:
                    neus "Brother, what are you doing?"
                else:
                    neus "What are you doing?"
                scene mc3_f_23 with dissolve
                mc "Showing you the advantages of sleeping together."
                neus "There's no need for you to do this-"
                scene mc3_f_24 with dissolve
                play char1 penetration4
                neus "Ah!"
                mc "I'll start."
                scene mc3_f_25 with dissolve
                play char3 sex2
                neus "{bt=1}{=lust_style}Ah Ah ah ...{/bt}"
                if incest_story:
                    mc "So little sister, what do you say?"
                else:
                    mc "So, what do you say?"
                neus "N-No."
                scene mc3_f_26 with dissolve
                stop char3
                play charM cum1
                neus "Ah"
                mc "I understand, but we have all night to change your mind."         
                stop ambience fadeout 0.5
                call splash_message(_("The next day")) from _call_splash_message_54
                play ambience morning_sounds fadein 1.0
                scene mc3_f_27 with dissolve
                mc "So?"
                neus "{size=-10}Noooo{/size} (if I agree, I'll end up like this {bt=2}{=lust_style}every day {/bt} {e_heartbt=FF0000})."
                scene mc3_f_28 with dissolve
                neus "(My legs are trembling)."
                mc "Need some help?"
                scene mc3_f_29 with dissolve
                neus "{size=-10}I can manage{/size} (It's difficult to walk)."
                stop ambience fadeout 1.0
                scene black with dissolve
                "She leaves the room."
                $ neus_left_room = True
                call addLust(5) from _call_addLust_8 
            "Be a pillow":
                stop ambience fadeout 0.5
                scene black with dissolve
                if incest_story:
                    "When you wake up, your sister is already gone."      
                else:
                    "When you wake up, [neusname] is already gone."        
    $lvl_event_fear_aux=0
    if is_wake_up_neus:
        play ambience morning_sounds fadein 2.0
        scene mc3_w_0 with fadesex    
        if incest_story:
            neus "Good morning brother!"
        else:    
            neus "Good morning!"
        scene mc3_w_1 with dissolve
        neus "Hey, don't pretend to be asleep."
        scene mc3_w_2 with dissolve
        neus "Hmm... I see that your friend is very energetic..."
        neus "(I've heard that the best way to wake up is with a blowj-)"
        scene black with dissolve 
        if incest_story:
            "Your sister removes the sheets that were covering you."
        else:
            "She removes the sheets that were covering you."
        scene mc3_w_3 with dissolve
        neus "(No, I'm not that kind of perverted person, but... I am his girlfriend, so...)"
        scene mc3_w_4 with dissolve
        neus "(It's not like I want to try it)"
        scene black with dissolve
        neus "Aaaa"
        play char3 suck2       
        neus "*sucking, sucking*"        
        scene mc3_w_5 with dissolve        
        mc "Mmm..."
        if incest_story:
            mc "Good morning, sister."     
        else:
            mc "Good morning, [neusname]."        
        neus "Go..od mo.. rning."
        mc "It's impolite to talk with your mouth full, you know?"
        scene mc3_w_6 with dissolve
        play char3 suck3
        neus "Mmm *sucking, sucking*"
        mc "(Mmm... I'm deep in her throat)"
        neus "*suck, suck* aah aah"
        menu:
            "Cum":
                pass        
        stop char3        
        play charM cum1
        scene mc3_w_7 with flash2
        neus "Uhhh"
        scene mc3_w_8 with dissolve
        if incest_story:
            neus "G-Good morning brother"
        else:
            neus "G-Good morning"
        stop ambience fadeout 1.0
        scene black with dissolve
        "She leaves your room."
        if not quest_v2: 
            $is_stundere_magazine = True   
        $is_wake_up_neus=False
        $ neus_left_room = True
        call addLust(3)
    else:
        scene mc_room_sleep_open with eyeopen
    jump next_day
#----------------------------object---------------------------------
default tutorial_text = ""
default tutorial_complete = False
default persistent.tutorial_complete = False
default tutorial_skip = False
label book_magic:
    if not(view_puzzle_book):
        scene book_magic_0 with spellfx
        "You notice a book lying on your desk, one that you’re sure wasn’t there before... as if it had mysteriously appeared overnight."        
        "As you take a closer look, you recognize what kind of book it is." 
        scene book_magic_0_1 with pixellate
        "It’s a well-known book among wizarding couples."       
        scene book_magic_1 with dissolve
        "It has the power to deepen a relationship, making it more intimate and exciting."
        "There is a legend that says the final spell fulfills the greatest desire of each person in the relationship."
        "Still, you can’t help but think a book on hypnosis would be much more useful."
        "Despite your doubts, you sense that this book is exactly what you need."
        if selected_mode != "None":
            "Before you start thinking of ways this book could help you get closer to her..." 
        $view_puzzle_book = True
    scene book_magic_1 with dissolve
    
    if selected_mode != "None":

        if selected_mode != "Jigsaw": 
            menu:
                "The book challenges you to a puzzle."
                "Accept":
                    scene bg_puzzle
                    $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(0, fifteen_grid_sizes["Normal"][0])  
                    $ chosen_img = "rooms/mc/lvl0/book_magic_3.webp"
                    call fifteen_game from _call_fifteen_game
                # "Skip mini-game." if cheat_minigame:
                #     pass      
        else: 
            menu:
                "The book challenges you to a puzzle."
                "Accept":
                    scene bg_puzzle
                    $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(0, puzzle_grid_sizes["Normal"][0])    
                    $ chosen_img = "rooms/mc/lvl0/book_magic_3.webp"
                    call puzzle
                # "Skip mini-game." if cheat_minigame:
                #     pass     
            show screen full_image
            "" 
            hide screen full_image 
    scene book_magic_2 with dissolve  
    if selected_mode != "None":
        "You solved the puzzle"   
    $ inventory.add_item(item_book_magic)   
    if quest_v2:
        $ questSide_v2_1.completion = True  
    else:  
        $ questSide_1.completion = True    
    "You notice something written in the book: ''Obtain the last spells.''"
    call splash_message(_("You have unlocked the spell tree")) from _call_splash_message_20
    call notify_personalized(_("Side Quest updated"))
    $is_change_quest = True   
    if persistent.tutorial_complete:
        menu:
            "Would you like to see the spell book tutorial"
            "Play tutorial":
                $ tutorial_skip = False
            "Skip tutorial":
                $ tutorial_skip = True
    if not tutorial_skip:
        call rooms_background
        $ tutorial_text = "Before you can use spells, you need to learn them.\nTo do this, click the \"Quests\" button at the top-left."
        show screen popup_text("[tutorial_text]")
        call screen tutorial_ui
    
    #scene book_magic_4 at blur2 with dissolve  
    #centered"{size=+30}{color=#cc0066}To use the spells, you have to learn them."    
    #scene book_magic_5 at blur2  with dissolve
    #centered "{size=+30}{color=#cc0066}The more you progress in your relationship with [neusname], the more spells you will unlock."   
    #$ inventory.add_item(item_book_magic)       
    call notify_personalized(_("Side Quest updated")) from _call_notify_personalized
    $is_change_quest = True   
    jump rooms

label book_magic_end:
    call notify_personalized(_("Side Quest updated"))
    $is_change_quest = True   
    jump rooms

screen tutorial_ui:   
    $ time_name = times_of_day[time]         
    hbox:
        xpos 5
        ypos 5
        spacing 5         
        imagebutton: 
            auto 'btn_gear_%s'
            tooltip _("Settings")
        imagebutton: 
            auto 'btn_backpack_%s'
            tooltip _("Backpack")
        vbox:
            spacing -48
            imagebutton:
                auto 'btn_neus_%s'
                action SetVariable("is_change_quest",False), Function(is_quest_change_screen, False), SetVariable("tutorial_text", "Now select the spell book button in the top left."), Jump("tutorial_is_tree_spell_stats_quests")   
                tooltip _("Quests")
                               
            if is_change_quest: 
                text _("{icon=icon-info}"):
                        color "#fff"
                        size 48 
                        outlines [ (3,gui.accent_color) ] 
                        xalign 0.5
                        ypos 16                                                        
                        at text_animation_alpha 
        if quest_v2:
            if (questSide_v2_8.completion) or (questSide_v2_8.description=="''Don't split''") or (questSide_v2_8.description=="''Split personalities''"):
                vbox:
                    spacing -48
                    imagebutton:
                        auto 'btn_phase_change_%s'
                        action SetVariable("is_change_phase",False),Jump("phase_change")   
                        tooltip _("Phase change")
                                    
                    if is_change_phase: 
                        text _("{icon=icon-info}"):
                                color "#fff"
                                size 48 
                                outlines [ (3,gui.accent_color) ] 
                                xalign 0.5
                                ypos 16                                                        
                                at text_animation_alpha  
        else: 
            if (questSide_7.completion) or (questSide_7.description == "''Split personalities''") or (questSide_7.description == "''Don't split''"):
                vbox:
                    spacing -48
                    imagebutton:
                        auto 'btn_phase_change_%s'
                        action SetVariable("is_change_phase",False),Jump("phase_change")   
                        tooltip _("Phase change")
                                    
                    if is_change_phase: 
                        text _("{icon=icon-info}"):
                                color "#fff"
                                size 48 
                                outlines [ (3,gui.accent_color) ] 
                                xalign 0.5
                                ypos 16                                                        
                                at text_animation_alpha     
        imagebutton: 
            auto 'btn_clock_%s'                                    
            tooltip _("Advance time")

    use tutorial_house_room   
    text _("{size=60}{color=#cc0066}[time_name!t]{/size}")  xalign 0.99 outlines [ (3,"#000") ]
    use screen_tooltip

screen tutorial_house_room(): 
    hbox:
        xalign 0.5
        ypos 830
        spacing 15
        for i in xrange(0,len(house)): 
            vbox:
                spacing -96                
                hbox:
                    spacing -64                                                                  
                    imagebutton:
                            auto house[i].icon                    
                            selected_idle house[i].icon % 'hover'
                            tooltip house[i].tooltip 
                    if house[i].name==neus_routine[time]:
                        if quest_v2:
                            if not(time==questMain_v2_select.time_event) or questMain_v2_select.place=="":
                                imagebutton:
                                    idle "icon_neus_routine"
                                    yalign 1.0
                        else:
                            if not(time==questMain_select.time_event) or questMain_select.place=="":
                                imagebutton:
                                    idle "icon_neus_routine"
                                    yalign 1.0

label tutorial_is_tree_spell_stats_quests:
    if time < 4:         
        scene expression 'bg/bg_[select_room]_room_day.webp'
    if time >= 4:        
        scene expression 'bg/bg_[select_room]_room_night.webp'
    call screen tutorial_is_tree_spell_stats_quests
    jump is_tree_spell_stats_quests

screen tutorial_is_tree_spell_stats_quests():

    default select_option = quest_screen

    if relationship_level==2:
        default outfit_sprite=  "neus_casual%s_%s"%(relationship_level,N_state)
    else: 
        default outfit_sprite=  "neus_casual%s_0"%relationship_level
    default isback = False          
    add "images/treespell/tree_spell_stats_quests_back.png"  
    add particles_sprite                 
    hbox:
        spacing 50                       
        vbox:
            xsize 680                                
            xpos 70
            ypos 15
            spacing 20
            hbox:                     
                spacing 10    
                vbox:       
                    spacing -86    
                    if select_option == "quests":
                        imagebutton:
                            auto 'btn_quest_%s'                   
                            selected_idle 'btn_quest_hover'
                            action [SetScreenVariable(
                                        name='select_option', 
                                        value="quests"
                                        ), Function(is_quest_change_screen, False), Function(is_quest_change, False)] 
                    else:
                        imagebutton:
                            auto 'btn_quest_%s'                   
                            selected_idle 'btn_quest_hover'
                    if quest_v2:
                        if is_change_quest_screen and questSide_v2_2.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                    else:
                        if is_change_quest_screen and questSide_2.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                vbox:
                    spacing -83      
                    if quest_v2:
                        imagebutton:                         
                            auto 'btn_tree_spell_%s'                        
                            selected_idle 'btn_tree_spell_hover'
                            insensitive "btn_lock_idle"
                            sensitive questSide_v2_1.completion
                            action [SetScreenVariable(
                                    name='select_option', 
                                    value="tree_spell"
                                    ),Function(btn_tree_spell),
                                    SetVariable("tutorial_text", "test")]
                    else:               
                        imagebutton:                         
                            auto 'btn_tree_spell_%s'                        
                            selected_idle 'btn_tree_spell_hover'
                            insensitive "btn_lock_idle"
                            sensitive questSide_1.completion
                            action [SetScreenVariable(
                                    name='select_option', 
                                    value="tree_spell"
                                    ),Function(btn_tree_spell),
                                    SetVariable("tutorial_text", "Finally, with the spell selected, press \"Learn\"")]
                    if quest_v2:
                        if is_change_tree_skill and questSide_v2_1.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                    else:
                        if is_change_tree_skill and questSide_1.completion: 
                            text "{icon=icon-info}":
                                color "#fff"
                                size 64 
                                outlines [ (3,"#d5303e")] 
                                xalign 0.5 
                                ypos 0                                                                                                       
                                at text_animation_alpha 
                imagebutton:                         
                    auto 'btn_config_%s'                        
                    selected_idle 'btn_config_hover'

                if tutorial_complete:
                    imagebutton:
                        xpos 254
                        auto 'btn_close_%s'                                      
                        action [Function(quest_screen_quests), Hide("popup_text"), Jump("book_magic_end")]
                else:          
                    imagebutton:
                        xpos 254
                        auto 'btn_close_%s'                                      
            if select_option=="tree_spell":                    
                use tutorial_tree_spell
            elif select_option=="quests":
                use quests_all   
                          
        # middle  
        vbox:              
            xsize 600                                                                       
            add outfit_sprite ypos 40                            
        #Left             
        use neus_stats        
    
    #outfit back
    imagebutton: 
        xpos 1750 
        ypos 930                            
        auto 'btn_turn_around_%s'        
        selected_idle 'btn_turn_around_hover'

screen tutorial_tree_spell:         
    vpgrid:
        cols 1
        spacing 30  
        ypos -10
        ysize 550        
        allow_underfull True  
        scrollbars "vertical"
        draggable True
        mousewheel True
        for i in range(0,len(tree)):
            vbox:
                xsize 635 
                spacing 20  
                label _('{color=#FFFFFF}Level [i]') xalign 0.5  
                hbox: 
                    spacing 20
                    xalign 0.5                    
                    for j in range(0,len(tree[i])):
                        if tree[i][j].name == "Touch":
                            if tree[i][j].is_active:
                                imagebutton:
                                    idle tree[i][j].image % 'active'
                                    hover tree[i][j].image % 'hover'
                                    selected_idle tree[i][j].image % 'hover'
                                    insensitive "btn_lock_idle"
                                    sensitive i <=relationship_level
                                    action SetVariable("select_spell",tree[i][j])                                                                                                           
                            else:
                                imagebutton:
                                    auto tree[i][j].image                                    
                                    selected_idle tree[i][j].image % 'hover' 
                                    insensitive "btn_lock_idle"
                                    sensitive i <=relationship_level and tree[i][j].start              
                                    action SetVariable("select_spell", tree[i][j])    
                        else:     
                            if tree[i][j].is_active:
                                if i > relationship_level:
                                    imagebutton:
                                        idle tree[i][j].image % 'active'
                                        hover tree[i][j].image % 'hover'
                                        selected_idle tree[i][j].image % 'hover'
                                        insensitive "btn_lock_idle"
                                        sensitive i <=relationship_level    
                                else:
                                    imagebutton:
                                        idle tree[i][j].image % 'active'
                                        hover tree[i][j].image % 'hover'
                                        selected_idle tree[i][j].image % 'hover'
                                        sensitive i <=relationship_level                                                                                                        
                            else:
                                if i > relationship_level:
                                    imagebutton:
                                        auto tree[i][j].image                                    
                                        selected_idle tree[i][j].image % 'hover' 
                                        insensitive "btn_lock_idle"
                                        sensitive i <=relationship_level and tree[i][j].start       
                                else:
                                    imagebutton:
                                        auto tree[i][j].image                                    
                                        selected_idle tree[i][j].image % 'hover' 
                                        sensitive i <=relationship_level and tree[i][j].start                    
    use tutorial_modal_confirmation

screen tutorial_modal_confirmation:
    vbox:        
        xsize 630 
        spacing 5
        text _("[select_spell.name!tq]") xalign 0.5
        text str(select_spell.description):
            xalign 0.5
            size 35
          
        if select_spell.is_active:
            pass
        else:     
            if select_spell.name == "Touch":
                textbutton _("{size=+15}{b}Learn"):
                    text_color "#cc0066"
                    text_hover_color "#fff"
                    ypos -10
                    xalign 0.5
                    action [
                        SetField(select_spell, "is_active", True),
                        If(select_spell.quest != "", [
                            SetField(select_spell.quest, "completion", True),
                            Function(quest_screen_spells),
                            SetVariable("tutorial_text", "You will unlock more spells as you progress " + neusname + "'s relationship.\nClose the spell tree by pressing the \"X\" button at the top."),
                            SetVariable("tutorial_complete", True),
                            SetVariable("persistent.tutorial_complete", True)
                            # Function(is_quest_change, True),
                            # Function(is_quest_change_screen, True),
                            #Call("notify_personalized", _("Side Quest updated"))
                        ])
                    ]
                    at text_animation_alpha
            else:
                textbutton _("{size=+15}{b}Learn"):
                    text_color "#cc0066"
                    text_hover_color "#fff"
                    ypos -10
                    xalign 0.5
                    at text_animation_alpha

screen popup_text(message):
    zorder 100
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            background Solid("#000000C0")
            padding (30, 20)
            text "{color=#cc0066}" + message + "{/color}" xalign 0.5 yalign 0.5 textalign 0.5

label hentai_magazine:
    scene bg_hentai_magazine with dissolve
       
    "Hentai manga"
    jump rooms

label stundere_magazine:
    scene bg_stundere_magazine with dissolve
    "A magazine titled ''How to deal with your Tsundere''"

    jump rooms

label portrait_neus:
    scene mc0_0 with dissolve
    if incest_story:
        "A portrait of your sister"
    else:
        "A portrait of [neusname]"    
    $ inventory.add_item(item_portrait_neus)
    jump rooms
        
screen mc_room_pc_screen:
    modal True  # Prevents clicking outside the menu

    frame:
        align (0.5, 0.5)
        padding (30, 30)
        background "#222222"

        vbox:
            xalign 0.5
            
            # Mini-game difficulty buttons
            text "Puzzle settings:" size 38 color "#cc0066"
            text "Control which puzzles appear throughout the game\nand set their difficulty." size 20 color "#aaaaaa"
            $ puzzle_label = None

            if selected_mode == "None":
                $ puzzle_label = "Puzzles disabled"
            else:
                $ puzzle_label = None
                for d in difficulties:
                    if selected_mode == "Jigsaw & Fifteen":
                        if jigsaw_difficulty == d and fifteen_difficulty == d:
                            $ puzzle_label = f"{jigsaw_difficulty} ({selected_mode})"
                        elif jigsaw_difficulty != fifteen_difficulty:
                            $ puzzle_label = f"{jigsaw_difficulty} / {fifteen_difficulty} ({selected_mode})"
                    elif selected_mode == "Jigsaw" and jigsaw_difficulty == d:
                        $ puzzle_label = f"{d} ({selected_mode})"
                        break
                    elif selected_mode == "Fifteen" and fifteen_difficulty == d:
                        $ puzzle_label = f"{d} ({selected_mode})"
                        break

                if puzzle_label is None:
                    $ puzzle_label = f"Custom ({selected_mode})"

            # Display button
            textbutton "[puzzle_label]" action Show("difficulty_settings")
            
            null height 20

            # Mini-game cheat buttons
            # text "Skip mini-game button:" size 38 color "#cc0066"
            # if cheat_minigame:
            #     textbutton "Enabled" text_size 40 action SetVariable("cheat_minigame", False)
            # else:
            #     textbutton "Disabled" text_size 40 action SetVariable("cheat_minigame", True)
            # text "Adds a ''Skip mini-game'' button before each mini-game\nwhich allows you to skip it." size 20 color "#aaaaaa"

            # Exit button
            textbutton "Exit" text_size 40 action Jump("rooms") xalign 0.5
            key "K_ESCAPE" action Jump("rooms")

label mc_room_pc:
    call screen difficulty_settings
    return