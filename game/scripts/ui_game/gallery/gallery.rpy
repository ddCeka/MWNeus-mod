 #Gallery
define nameByIDscene_main_quest = [
["story/intro/intro_2.webp","introduction","introduction"],
["story/level0/level0_0_10.webp","level0_0","level0_0"],   
["story/level0/level0_1_10.webp","level0_1","level0_1"],
["story/level0/level0_2_15.webp","level0_2","level0_2"],
["story/level1/level1_0_5.webp","level1_0","level1_0"],
["story/level1/level1_1_3.webp","level1_1","level1_1"],
["story/level1/level1_2_6.webp","level1_2","level1_2"],
["story/level1/level1_3_6.webp","level1_3","level1_3"],
["story/level2/level2_0_11.webp","level2_0","level2_0"],
["story/level2/level2_1_10.webp","level2_1","level2_1"],
["story/level2/level2_2_0.webp","level2_2","level2_2"],
["story/endings/end_nor1_21.webp","ending_normal1","ending_normal1"]]
define nameByIDscene_secret = [
    ["story/extra/extra0_15.webp","confrontation","confrontation"],
    ["rooms/neus/lvl3/neus3_p_20.webp","level3_0","level3_0"],
    ["rooms/milf/milf_true_ending15.webp","milf_true_ending","milf_true_ending"],
    ["rooms/tb/mc/tb_end_15.webp","tb_ending_event","tb_ending_event"],
    ["rooms/tb/mc/tb_p3_0.webp","two_bodies_personality3","two_bodies_personality3"],
    ["rooms/nym/nym_end_1.webp","nym_ending","nym_ending"]]
screen gallery_replay():
    default gallery_type = "main_quest"
    tag menu
    use game_menu(_("Gallery"), scroll="viewport"):
        style_prefix "help"
        hbox:
            if any(not renpy.seen_label(scene[1]) for scene in nameByIDscene_main_quest):
                imagebutton: 
                    auto "btn_lock_%s"               
                    action Confirm("Are you sure? This will unlock everything \nin \"Main quest\" Gallery.", Function(unlock_gallery))
                    at Transform(zoom=0.6, ypos=18)
            textbutton _("{size=+20}Main quest") action SetScreenVariable("gallery_type", "main_quest")            
            textbutton _("{size=+20}Secret") action SetScreenVariable("gallery_type", "secret")
            null width 580
            textbutton _("{size=+20}Settings") action SetScreenVariable("gallery_type", "settings")

        if gallery_type == "main_quest":
            use main_quest_gallery(nameByIDscene_main_quest,gallery_type)        
        elif gallery_type == "secret":
            use main_quest_gallery(nameByIDscene_secret,gallery_type)
        elif gallery_type == "settings":
            use gallery_settings()
                         
screen main_quest_gallery(nameByIDscene_aux,gallery_type):
    vbox:
        spacing 20    
        vpgrid:
            cols 3
            spacing 30  
            allow_underfull True     
            for sce in nameByIDscene_aux:
                $ evt = sce[1]
                $ jump_evt = sce[2]                   
                if renpy.seen_label(evt):
                    $ event_image = im.Scale(sce[0], 400, 225)
                    imagebutton:
                        idle im.Grayscale(event_image)
                        hover event_image
                        action Replay(jump_evt,locked=False)
                else:
                    $ event_image = im.Scale("gallery/none.png",  400, 225)
                    imagebutton:
                        idle event_image
                        hover event_image
                        action NullAction()

screen gallery_settings():
    hbox:
        vbox:
            xsize 1070
            ysize 400          
            
        vbox:
            if persistent.gallery_incest_story:
                $ persistent.incest_label = "Enabled"
                $ persistent.gallery_friend_sister = "sister"
            else:
                $ persistent.incest_label = "Disabled"
                $ persistent.gallery_friend_sister = "childhood friend"

            if persistent.gallery_pregnancy_censored:
                $ persistent.pregnancy_label = "Enabled"
            else:
                $ persistent.pregnancy_label = "Disabled"

            text "Incest Story:" size 38 color "#cc0066"
            textbutton "[persistent.incest_label]" action SetVariable("persistent.gallery_incest_story", not persistent.gallery_incest_story)
            
            text "Censor Pregnancy:" size 38 color "#cc0066"
            textbutton "[persistent.pregnancy_label]" action SetVariable("persistent.gallery_pregnancy_censored", not persistent.gallery_pregnancy_censored)

            text "MC Name:" size 38 color "#cc0066"
            textbutton "[persistent.gallery_firstname]" action Show("enter_name", target=FieldInputValue(persistent, "gallery_firstname"), prompt="What is your name? (Default: Neron)")

            text "Neus Name:" size 38 color "#cc0066"
            textbutton "[persistent.gallery_neusname]" action Show("enter_name", target=FieldInputValue(persistent, "gallery_neusname"), prompt="What is your [persistent.gallery_friend_sister]'s name? (Default: Neus)")
            
            if renpy.seen_label("two_bodies_rooms"):
                text "Lyra Name:" size 38 color "#cc0066"
                textbutton "[persistent.gallery_lyra]" action Show("enter_name", target=FieldInputValue(persistent, "gallery_lyra"), prompt="What is the name of your [persistent.gallery_friend_sister]'s\nsecond personality? (Default: Lyra)")

            if renpy.seen_label("nym_rooms"):
                text "Sylvia Name:" size 38 color "#cc0066"
                textbutton "[persistent.gallery_sylvia]" action Show("enter_name", target=FieldInputValue(persistent, "gallery_sylvia"), prompt="What is the name of your [persistent.gallery_friend_sister]'s\nthird personality? (Default: Sylvia)")

screen enter_name(target, prompt):
    modal True
    frame:
        background "#0008"
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        vbox:
            spacing 20
            text prompt size 40 color "#fff"
            input value target length 20 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'"
            if target.get_text().strip() != "":
                textbutton "OK" action Hide("enter_name")
            else:
                textbutton "OK"
            
            key "K_RETURN" action If(target.get_text().strip() != "", Hide("enter_name"), NullAction())
