label splashscreen:
    if persistent.splashscreen_logo or persistent.splashscreen_warning:
        scene black    
    if persistent.splashscreen_logo:
        show CLLGames 
        pause 2.5    
        hide CLLGames    
    if persistent.splashscreen_warning:
        show text _("{color=#f00}{size=+40}WARNING{/size}{vspace=40}{/color}{size=+20}This game is intended for an adult audience.{vspace=40}If you are not considered of adult age in your country please exit this game.{/size}{vspace=40}{size=+20}All characters depicted in this game are fictional and over 18. Any resemblance to real people or events is accidental.{/size}") with dissolve
        ""
        hide text with dissolve   
    $ persistent.preferences_type = "main" 
    return

label splash_message(message="",time_pause=2.5):
    scene black with dissolve
    centered "{size=+60}[message!t]{/size}{w=[time_pause]}{nw}"
    return

label start: 
    $ mod_version = 1.2
    $persistent.main_menu_b=0
    $ game_version = myconfig.version       
    stop music fadeout 3      
    
    call screen game_settings

    if quest_v2:
        call quest_v2
    
    if incest_story:
        call incest_story

    if not set_active_pregnancy:
        $ gallery_pregnancy_censored = True

    if persistent.gallery_firstname != "Neron":
        $ firstname = renpy.input(_("What is your name? (Default: Neron)"), default=persistent.gallery_firstname, exclude='\\[{') 
    else:
        $ firstname = renpy.input(_("What is your name? (Default: Neron)"), exclude='\\[{') 
    $ firstname = firstname.title()
    $ firstname = firstname.strip()   
    if firstname == "":
        $ firstname = "Neron"   
    $ persistent.gallery_firstname = firstname
    scene neus_name with dissolve
    if persistent.gallery_neusname != "Neus":
        $ neusname = renpy.input(_("What is your [friend_sister]'s name? (Default: Neus)"), default=persistent.gallery_neusname, exclude='\\[{') 
    else:
        $ neusname = renpy.input(_("What is your [friend_sister]'s name? (Default: Neus)"), exclude='\\[{') 
    $ neusname = neusname.title()
    $ neusname = neusname.strip()
    if neusname == "":
        $ neusname = "Neus"
    $ persistent.gallery_neusname = neusname
    jump introduction    
    return

init python:
    def next_preset():
        global difficulty, jigsaw_difficulty, fifteen_difficulty, selected_mode, cheat_minigame, solve_label

        # Find current preset if it matches any difficulty, else default to the first one
        current_idx = 0
        for i, d in enumerate(difficulties):
            if selected_mode == "Jigsaw & Fifteen" and jigsaw_difficulty == d and fifteen_difficulty == d:
                current_idx = i
                break

        # Move to next preset
        next_idx = (current_idx + 1) % len(difficulties)
        difficulty = difficulties[next_idx]

        # Apply preset to both puzzle types
        jigsaw_difficulty = difficulty
        fifteen_difficulty = difficulty

        # Always set puzzle type to both
        selected_mode = "Jigsaw & Fifteen"

        # Always set solve puzzle button to disabled
        cheat_minigame = False
        solve_label = "Disabled"

    def next_mode():
        global selected_mode
        idx = modes.index(selected_mode)
        idx = (idx + 1) % len(modes)
        selected_mode = modes[idx]

    def next_jigsaw():
        global jigsaw_difficulty
        idx = difficulties.index(jigsaw_difficulty)
        idx = (idx + 1) % len(difficulties)
        jigsaw_difficulty = difficulties[idx]

    def next_fifteen():
        global fifteen_difficulty
        idx = difficulties.index(fifteen_difficulty)
        idx = (idx + 1) % len(difficulties)
        fifteen_difficulty = difficulties[idx]

    def game_settings_true():
        global game_settings_var
        game_settings_var = True
    def game_settings_false():
        global game_settings_var
        game_settings_var = False

screen game_settings():
    modal True  # Prevents clicking outside the menu

    frame:
        align (0.5, 0.5)
        padding (30, 30)
        background "#222222"

        vbox:
            xalign 0.5
            
            text "Game Settings" size 50 color "#ffffff" xalign 0.5
            
            # Mini-game difficulty setting
            text "Puzzle settings:" size 38 color "#cc0066"
            text "Control which puzzles appear throughout the game and set their difficulty." size 20 color "#aaaaaa"
            # textbutton "[difficulty] ([selected_mode])" action Show("difficulty_settings")
            # Determine label for mini-game button
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
            textbutton "[puzzle_label]" action [Show("difficulty_settings"), Hide("game_settings"), Function(game_settings_true)]

            null height 20

            # Expanded Quest Line
            text "Expanded Quest Line:" size 38 color "#cc0066"
            text "Add additional quests that require increasing her lust through sandbox elements to\nprogress. This setting can't be changed later." size 20 color "#aaaaaa"
            if quest_v2:
                textbutton "Enabled" text_size 40:
                    action SetVariable("quest_v2", not quest_v2)
            else:
                textbutton "Disabled" text_size 40:
                    action SetVariable("quest_v2", not quest_v2)

            null height 20

            # Incest Story Mode
            text "Incest Story:" size 38 color "#cc0066"
            text "Makes her your sister, with minor story adjustments to accommodate this. This setting\ncan't be changed later." size 20 color "#aaaaaa"
            if incest_story:
                textbutton "Enabled" text_size 40:
                    action SetVariable("incest_story", not incest_story)
            else:
                textbutton "Disabled" text_size 40:
                    action SetVariable("incest_story", not incest_story)

            null height 20

            # Pregnancy Content Option
            text "Pregnancy Content:" size 38 color "#cc0066"
            text "Disabling this will only censor the sex scenes where she is pregnant, it won't prevent her\nfrom getting pregnant." size 20 color "#aaaaaa"
            if set_active_pregnancy:
                textbutton "Enabled" text_size 40:
                    action SetVariable("set_active_pregnancy", not set_active_pregnancy)
            else:
                textbutton "Disabled" text_size 40:
                    action SetVariable("set_active_pregnancy", not set_active_pregnancy)

            null height 20

            # Confirm Button
            textbutton "Confirm" action Return() xalign 0.5

screen difficulty_settings():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        background "#222222"
        vbox:

            # Preset Difficulty
            text "Difficulty Preset:" size 38 color "#cc0066"
            text "Cycle through difficulty presets; Normal matches the base game settings,\nwith minor difficulty increases for outfit puzzles." size 20 color "#aaaaaa"
            # Determine label
            $ matched_preset = None
            for d in difficulties:
                if selected_mode == "Jigsaw & Fifteen" and jigsaw_difficulty == d and fifteen_difficulty == d:
                    $ matched_preset = d
                    break

            # Display button
            if matched_preset:
                textbutton "[matched_preset]" action Function(next_preset)
            else:
                textbutton "Custom" action Function(next_preset)
            
            null height 20

            # Puzzle Type
            text "Puzzle Type:" size 38 color "#cc0066"
            text "Select which puzzle types are active." size 20 color "#aaaaaa"
            textbutton "[selected_mode]" action Function(next_mode)

            null height 20

            # Jigsaw Difficulty
            text "Jigsaw Difficulty:" size 38 color "#cc0066"
            text "Adjust difficulty for Jigsaw puzzles independently of preset." size 20 color "#aaaaaa"
            if selected_mode in ["Jigsaw", "Jigsaw & Fifteen"]:
                textbutton "[jigsaw_difficulty]" action Function(next_jigsaw)
            else:
                textbutton "[jigsaw_difficulty]"

            null height 20

            # Fifteen Difficulty
            text "Fifteen Difficulty:" size 38 color "#cc0066"
            text "Adjust difficulty for Fifteen puzzles independently of preset." size 20 color "#aaaaaa"
            if selected_mode in ["Fifteen", "Jigsaw & Fifteen"]:
                textbutton "[fifteen_difficulty]" action Function(next_fifteen)
            else:
                textbutton "[fifteen_difficulty]"

            null height 20

            # Solve Button
            text "Solve Puzzle Button:" size 38 color "#cc0066"
            text "Add a button to puzzles which allows you to instantly solve them.\nAlternatively, you can disable all puzzles by changing 'Puzzle Type' to 'None'." size 20 color "#aaaaaa"
            
            if cheat_minigame:
                $ solve_label = "Enabled"
            else:
                $ solve_label = "Disabled"

            if selected_mode != "None":
                textbutton "[solve_label]" action SetVariable("cheat_minigame", not cheat_minigame)
            else:
                textbutton "[solve_label]"

            null height 20

            # Done button
            if not game_settings_var:
                textbutton "Confirm" action Jump("rooms") xalign 0.5
            else:
                textbutton "Confirm" action [Hide("difficulty_settings"), Show("game_settings"), Function(game_settings_false)] xalign 0.5
                


label incest_story:
    $ neus_title=_("Sister")
    $ momname = "Mom"
    $ friend_sister = "sister"
    $ persistent.gallery_incest_story = True
    if quest_v2: # Quest v2 descriptions
        $ questMain_v2_1.description = "Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color} and ask your sister out on a date"
        $ questMain_v2_2.description = "Increase your sister's lust to 3"
        $ questMain_v2_3.description = "Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_v2_4.description = "Increase your sister's lust to 8"
        $ questMain_v2_5.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_v2_6.description = "Increase your sister's lust to 16"
        $ questMain_v2_7.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_v2_8.description = "Increase your sister's lust to 26"
        $ questMain_v2_9.description = "Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_v2_10.description = "Increase your sister's lust to 38"
        $ questMain_v2_11.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}"
        $ questMain_v2_12.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}"
        $ questMain_v2_13.description = "Go to {color=#cc0066}[neusname]'s room{/color} at {color=#cc0066}Noon{/color}"
        $ questMain_v2_14.description = "Increase your sister's lust to 64"
        $ questMain_v2_15.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_v2_16.description = "Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Evening{/color}"
        $ questSide_v2_1.description = "Examine the mysterious book on your desk."
        $ questSide_v2_2.description = "Learn the ''Touch'' spell"
        $ questSide_v2_3.description = "Use the ''Touch'' spell on your sister"
        $ questSide_v2_4.description = "Find the key to [neusname]'s room"
        $ questSide_v2_5.description = "Find the key to the attic"
        $ questSide_v2_6.description = "Go to the attic and confront her."
        $ questSide_v2_7.description = "Go to [neusname]'s room and choose ''Another personality''"
        $ questSide_v2_8.description = "''Split personalities'' or ''Don't split''"
    else:        # Quest v1 descriptions
        $ questMain_1.description = "Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_2.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_3.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_4.description = "Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_5.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}"
        $ questMain_6.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}"
        $ questMain_7.description = "Go to {color=#cc0066}[neusname]'s room{/color} at {color=#cc0066}Noon{/color}"
        $ questMain_8.description = "Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}"
        $ questMain_9.description = "Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Evening{/color}"
        $ questSide_1.description = "Examine the mysterious book on your desk."
        $ questSide_2.description = "Learn the ''Touch'' spell"
        $ questSide_3.description = "Find the key to [neusname]'s room"
        $ questSide_4.description = "Find the key to the attic"
        $ questSide_5.description = "Go to the attic and confront her."
        $ questSide_6.description = "Go to [neusname]'s room and choose ''Another personality''"
        $ questSide_7.description = "''Split personalities'' or ''Don't split''"
    return

label quest_v2:
    $ spell_0_1.quest = questSide_v2_2
    return