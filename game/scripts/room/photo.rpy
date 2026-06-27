#----------------------------mc---------------------------------
screen mc_photo:     
    if time < 4:
        if not(mc_photo0.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", mc_photo0),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 775,590
        if relationship_level>=1 and not(mc_photo1.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", mc_photo1),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 200,800
        if relationship_level>=2 and not(mc_photo2.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", mc_photo2),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 300,750
        if relationship_level>=3 and not(mc_photo3.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", mc_photo3),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1400,600   
    else:
        if not(mc_photo0.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", mc_photo0),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 775,590
        if relationship_level>=1 and not(mc_photo1.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", mc_photo1),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 200,800
        if relationship_level>=2 and not(mc_photo2.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", mc_photo2),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 300,750
        if relationship_level>=3 and not(mc_photo3.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", mc_photo3),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1400,600   

#----------------------------neus---------------------------------
screen neus_photo:
    if time < 4:
        if not(neus_photo0.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", neus_photo0),Jump("call_puzzle")
                tooltip _("Photo")
                pos 400,600
        if relationship_level>=1 and not(neus_photo1.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", neus_photo1),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1800,820
        if relationship_level>=2 and not(neus_photo2.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", neus_photo2),Jump("call_puzzle")
                tooltip _("Photo")
                pos 200,600
        if relationship_level>=3 and not(neus_photo3.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", neus_photo3),Jump("call_puzzle")
                tooltip _("Photo")
                pos 950,500
    else:
        if not(neus_photo0.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", neus_photo0),Jump("call_puzzle")
                tooltip _("Photo")
                pos 400,600
        if relationship_level>=1 and not(neus_photo1.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", neus_photo1),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1800,820
        if relationship_level>=2 and not(neus_photo2.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", neus_photo2),Jump("call_puzzle")
                tooltip _("Photo")
                pos 200,600
        if relationship_level>=3 and not(neus_photo3.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", neus_photo3),Jump("call_puzzle")
                tooltip _("Photo")
                pos 950,500

#----------------------------bath---------------------------------
screen bath_photo:
    if time < 4:
        if not(bath_photo0.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", bath_photo0),Jump("call_puzzle")
                tooltip _("Photo")
                pos 400,520
        if relationship_level>=1 and not(bath_photo1.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", bath_photo1),Jump("call_puzzle")
                tooltip _("Photo")
                pos 1700,600
        if relationship_level>=2 and not(bath_photo2.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", bath_photo2),Jump("call_puzzle")
                tooltip _("Photo")
                pos 1300,550
        if relationship_level>=3 and not(bath_photo3.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", bath_photo3),Jump("call_puzzle")
                tooltip _("Photo")
                pos 1000,600
    else:
        if not(bath_photo0.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", bath_photo0),Jump("call_puzzle")
                tooltip _("Photo")
                pos 400,520
        if relationship_level>=1 and not(bath_photo1.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", bath_photo1),Jump("call_puzzle")
                tooltip _("Photo")
                pos 1700,600
        if relationship_level>=2 and not(bath_photo2.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", bath_photo2),Jump("call_puzzle")
                tooltip _("Photo")
                pos 1300,550
        if relationship_level>=3 and not(bath_photo3.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", bath_photo3),Jump("call_puzzle")
                tooltip _("Photo")
                pos 1000,600

#----------------------------kitchen---------------------------------
screen kitchen_photo:
    if time < 4:
        if not(kitchen_photo0.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo0),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1250,620
        if relationship_level>=1 and not(kitchen_photo1.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo1),Jump("call_puzzle")
                tooltip _("Photo")
                pos 250,750
        if relationship_level>=2 and not(kitchen_photo2.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo2),Jump("call_puzzle")
                tooltip _("Photo")
                pos 500,500
        if relationship_level>=3 and not(kitchen_photo3.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo3),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 700,700
    else:
        if not(kitchen_photo0.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo0),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1250,620
        if relationship_level>=1 and not(kitchen_photo1.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo1),Jump("call_puzzle")
                tooltip _("Photo")
                pos 250,750
        if relationship_level>=2 and not(kitchen_photo2.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo2),Jump("call_puzzle")
                tooltip _("Photo")
                pos 500,500
        if relationship_level>=3 and not(kitchen_photo3.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", kitchen_photo3),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 700,700

#----------------------------living---------------------------------
screen living_photo:
    if time < 4:
        if not(living_photo0.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", living_photo0),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 110,430
        if relationship_level>=1 and not(living_photo1.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", living_photo1),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 500,650
        if relationship_level>=2 and not(living_photo2.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", living_photo2),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 600,350
        if relationship_level>=3 and not(living_photo3.is_view):
            imagebutton:
                auto "btn_old_photo_%s"     
                action SetVariable("select_photo", living_photo3),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1800,700
    else:
        if not(living_photo0.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", living_photo0),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 110,430
        if relationship_level>=1 and not(living_photo1.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", living_photo1),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 500,650
        if relationship_level>=2 and not(living_photo2.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", living_photo2),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 600,350
        if relationship_level>=3 and not(living_photo3.is_view):
            imagebutton:
                auto "btn_night_old_photo_%s"     
                action SetVariable("select_photo", living_photo3),Jump("call_fifteen_game")
                tooltip _("Photo")
                pos 1800,700


label call_fifteen_game:  

    if selected_mode != "None":
        if selected_mode == "Jigsaw": 
            jump call_puzzle

        show expression "old_photo%s"%select_photo.level at left
        menu:
            "Challenges you to a puzzle"
            "Accept":
                scene black
                centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start  
                scene bg_puzzle
                $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(select_photo.level, fifteen_grid_sizes["Normal"][0])
                $ chosen_img = select_photo.event_image                           
                call fifteen_game from _call_fifteen_game_1
            # "Skip mini-game." if cheat_minigame:
            #     pass
            "Back":
                jump rooms
        hide old_photo
    else:
        $ chosen_img = im.Image(select_photo.event_image)

        show screen full_image
        ""
        scene black
        hide screen full_image


    $ inventory.add_item(select_photo)     
    $ photo_count += 1
    call splash_message(_("The photo has been added to your inventory.")) from _call_splash_message_10
    jump rooms

label call_puzzle:

    if selected_mode != "None":
        if selected_mode == "Fifteen": 
            jump call_fifteen_game

        show expression "old_photo%s"%select_photo.level at left
        menu:
            "Challenges you to a puzzle"
            "Accept":
                scene black
                centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start    
                # Get the grid dimensions based on the current difficulty level and stage
                $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(select_photo.level, puzzle_grid_sizes["Normal"][0])
                $ chosen_img = select_photo.event_image            
                # and call puzzle label
                call puzzle from _call_puzzle
            # "Skip mini-game." if cheat_minigame:
            #     pass
            "Back":
                jump rooms
        hide old_photo
    else:
        $ chosen_img = im.Image(select_photo.event_image)

        show screen full_image
        ""
        scene black
        hide screen full_image

    $ inventory.add_item(select_photo)    
    $ photo_count += 1
    call splash_message(_("The photo has been added to your inventory.")) from _call_splash_message_11
    jump rooms

label kitchen3_minigame:    

    if selected_mode != "None":
        show  old_photo_s at left

        if selected_mode != "Jigsaw": 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start  
                    scene bg_puzzle
                    $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(4, fifteen_grid_sizes["Normal"][0])
                    $ chosen_img = "inventory/photo/kitchen3_outfit_photo.webp"                         
                    call fifteen_game from _call_fifteen_game_2 
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump rooms
        else: 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start  
                    scene bg_puzzle
                    $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(4, puzzle_grid_sizes["Normal"][0])
                    $ chosen_img = "inventory/photo/kitchen3_outfit_photo.webp"                         
                    call puzzle
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump rooms
        hide old_photo_s         

    $ outfit_photo_count += 1
    $ kitchen3_is_active_outfit = True
    scene kitchen3_outfit_photo with dissolve
    if spell_2_2.is_active:
        centered "{size=+30}New outfits have been unlocked for [neusname], they can be used in the kitchen."
    else:
        centered "{size=+30}New outfits have been unlocked for [neusname], but {color=#cc0066}you need to learn the ''Object creation'' spell to materialize them.{/color}"  
        # menu:
        #     "Do you want to learn the ''Object creation'' spell?"
        #     "Yes":
        #         $ spell_2_2.is_active = True
        #     "No":
        #         pass                
    jump rooms

label living_room3_minigame:    

    if selected_mode != "None":
        show  old_photo_s at left

        if selected_mode != "Jigsaw": 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start  
                    scene bg_puzzle
                    $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(4, fifteen_grid_sizes["Normal"][0])        
                    $ chosen_img = "inventory/photo/living_room3_outfit_photo.webp"                         
                    call fifteen_game from _call_fifteen_game_3 
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump rooms
        else:
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start  
                    scene bg_puzzle
                    $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(4, puzzle_grid_sizes["Normal"][0])    
                    $ chosen_img = "inventory/photo/living_room3_outfit_photo.webp"                         
                    call puzzle
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump rooms
        hide old_photo_s   

    $ outfit_photo_count += 1
    $ living_room3_is_active_outfit = True
    scene living_room3_outfit_photo with dissolve
    if spell_2_2.is_active:
        centered "{size=+30}New outfits have unlocked for [neusname], they can be used in the Living room."
    else:
        centered "{size=+30}New outfits have been unlocked for [neusname], but {color=#cc0066}you need to learn the ''Object creation'' spell to materialize them.{/color}"  
        # menu:
        #     "Do you want to learn the ''Object creation'' spell?"
        #     "Yes":
        #         $ spell_2_2.is_active = True
        #     "No":
        #         pass                
    jump rooms

label neus3_minigame:    
    if selected_mode != "None":
        show  old_photo_s at left

        if selected_mode != "Jigsaw": 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start  
                    scene bg_puzzle
                    $ grid_width, grid_height = fifteen_grid_sizes.get(difficulty, {}).get(4, fifteen_grid_sizes["Normal"][0])       
                    $ chosen_img = "inventory/photo/neus3_outfit_photo.webp"                         
                    call fifteen_game from _call_fifteen_game_4 
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump rooms
        else: 
            menu:
                "Challenges you to a puzzle"
                "Accept":
                    scene black
                    centered "{size=+30}Loading data ...{nw}" # nw-tag is necessary for puzzle to actually start  
                    scene bg_puzzle
                    $ grid_width, grid_height = puzzle_grid_sizes.get(difficulty, {}).get(4, puzzle_grid_sizes["Normal"][0])         
                    $ chosen_img = "inventory/photo/neus3_outfit_photo.webp"                         
                    call puzzle
                # "Skip mini-game." if cheat_minigame:
                #     pass
                "Back":
                    jump rooms
        hide old_photo_s      

    $ outfit_photo_count += 1
    $ neus3_is_active_outfit = True
    scene neus3_outfit_photo with dissolve
    if spell_2_2.is_active:
        centered "{size=+30}New outfits have been unlocked for [neusname], they can be used in [neusname]'s room."
    else:
        centered "{size=+30}New outfits have been unlocked for [neusname], but {color=#cc0066}you need to learn the ''Object creation'' spell to materialize them.{/color}"  
        # menu:
        #     "Do you want to learn the ''Object creation'' spell?"
        #     "Yes":
        #         $ spell_2_2.is_active = True
        #     "No":
        #         pass                
    jump rooms