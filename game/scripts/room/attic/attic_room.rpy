default is_view_attic = False
default is_view_hypnosis_book = False
label attic_room_entrance:
    if(is_view_attic):       
        jump attic_room
    scene attic1_0
    menu:
        "Enter the attic."(key_room_attic.is_view):
            scene attic1_1 with dissolve
            "" 
            scene attic1_2 with dissolve           
            mc "Finally got in the attic..."  
            $is_view_attic = True  
            $secret_point += 1
            python:
                achievement.grant("Attic")
                achievement.sync()
            jump attic_room 
        "Break the door":
            mc "I don't want to have to repair the door later. I need the key"
        "Leave":
            jump rooms 
    jump attic_room_entrance  

label attic_room:      
    scene expression "attic%s_3"%relationship_level   
    call screen ui_attic

screen ui_attic:    
    imagebutton:
        auto "btn_hypnosis_book_%s" 
        focus_mask True           
        action Jump("hypnosis_book")
        tooltip _("Hypnosis Book")
    
    imagebutton:
        auto "btn_diary_neus_%s" 
        focus_mask True           
        action Show("ui_diary_neus")
        tooltip _("Diary")        
    if incest_story:
        if diary_neus_incest[2][0]=="":
            imagebutton:
                auto "btn_page2_diary_%s" 
                focus_mask True           
                action Jump("page_2_incest")
                tooltip _("Page?")
                at event_animation_page
        if diary_neus_incest[1][0]=="" and relationship_level>=2:
            imagebutton:
                auto "btn_page1_diary_%s" 
                focus_mask True           
                action Jump("page_1_incest")
                tooltip _("Page?")
                at event_animation_page
        if diary_neus_incest[0][0]=="" and relationship_level>=3:
            imagebutton:
                auto "btn_page0_diary_%s" 
                focus_mask True           
                action Jump("page_0_incest")
                tooltip _("Page?")
                at event_animation_page
    else:
        if diary_neus[2][0]=="":
            imagebutton:
                auto "btn_page2_diary_%s" 
                focus_mask True           
                action Jump("page_2")
                tooltip _("Page?")
                at event_animation_page
        if diary_neus[1][0]=="" and relationship_level>=2:
            imagebutton:
                auto "btn_page1_diary_%s" 
                focus_mask True           
                action Jump("page_1")
                tooltip _("Page?")
                at event_animation_page
        if diary_neus[0][0]=="" and relationship_level>=3:
            imagebutton:
                auto "btn_page0_diary_%s" 
                focus_mask True           
                action Jump("page_0")
                tooltip _("Page?")
                at event_animation_page
    imagebutton:
            auto "icon_neus_room_%s"       
            tooltip _("%s's room")%neusname
            action Jump("rooms")
            xpos 50
            ypos 830    
    imagebutton:
        auto "btn_event_%s"                   
        tooltip _("Confrontation") 
        xpos 350
        ypos 400      
        action  Jump("confrontation_event")
        at event_animation_ending
    use screen_tooltip

label hypnosis_book:
    scene attic1_4 with dissolve
    if not(is_view_hypnosis_book):
        "You find a hypnosis book, but it rejects you."
        scene attic1_4_0 with dissolve
        mc "Apparently it already has an owner."
        scene attic1_4 with dissolve   
        mc "Mmm... "        
        $is_view_hypnosis_book = True   
    else:
        mc "..."  
    jump attic_room

screen ui_diary_neus:
    tag menu
    default page = total_pages
    imagebutton:
        idle "gui/overlay/confirm.png"
        action [Hide("ui_diary_neus"), Jump("attic_room")]
    add "diary_neus_screen" xalign 0.5
    $ current_diary = diary_neus_incest if incest_story else diary_neus
    grid 2 1:
        allow_underfull True
        xalign 0.5
        yalign 0.5
        spacing 150
        vbox:   
            ypos -10
            xpos 50         
            xsize 600
            ysize 800                           
            text current_diary[page][0]:
                outlines [(2, "#000")]
                justify True                
                xsize 500
                font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                        If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                        "fonts/Alkatra-Regular.ttf")) 
                size 35
            text current_diary[page][1]:
                outlines [(2, "#000")]
                justify True
                xsize 400                             
                xalign 1.0
                font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                        If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                        "fonts/Alkatra-Regular.ttf"))
                size 35
            text current_diary[page][2]:
                xsize 500
                justify True               
                outlines [(2, "#000")] 
                font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                        If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                        "fonts/Alkatra-Regular.ttf"))
                size 35
        vbox: 
            ypos -10
            xpos -10         
            xsize 600
            ysize 800 
            text current_diary[page][3]: 
                outlines [(2, "#000")]                
                xsize 500  
                justify True              
                xalign 1.0
                font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                        If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                        "fonts/Alkatra-Regular.ttf"))
                size 35
            text current_diary[page][4]:
                xsize 400
                justify True                
                outlines [(2, "#000")]
                font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                        If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                        "fonts/Alkatra-Regular.ttf"))
                size 35
            text current_diary[page][5]: 
                outlines [(2, "#000")]
                xsize 500 
                justify True               
                xalign 1.0
                font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                        If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                        "fonts/Alkatra-Regular.ttf"))
                size 35
    text _("%s") % (page + (page * 1) + 1):
        size 60
        xalign 0.15 
        yalign 0.9  
        font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                "fonts/Alkatra-Regular.ttf"))
        outlines [(2, "#000")]  
    text current_diary[page][6]:
        size 60
        color "#e7c9d8"
        xalign 0.5 
        yalign 0.88  
        font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                "fonts/Alkatra-Regular.ttf"))
        outlines [(2, "#000")]  
    text _("%s") % (page + (page * 1) + 2):
        size 60
        xalign 0.855 
        yalign 0.9  
        font If(_preferences.language == "chinese_simplified", "fonts/NotoSerifSC-Regular.ttf", 
                If(_preferences.language == "russian", "fonts/RobotoCondensed-Regular.ttf", 
                "fonts/Alkatra-Regular.ttf"))
        outlines [(2, "#000")]
    if len(current_diary) > (page + 1):
        imagebutton:
            auto "btn_arrow_right_%s"     
            tooltip _("right")
            yalign .5
            xalign 0.85
            action Play("sound", audio.page_turn), SetScreenVariable("page", page + 1)
    if page > 0:
        imagebutton:
            auto "btn_arrow_left_%s"     
            tooltip _("left")
            yalign .5
            xalign 0.16
            action Play("sound", audio.page_turn), SetScreenVariable("page", page - 1)

label page_0:
    scene attic1_5 with dissolve
    "You found pages 1 and 2 of [neusname]' diary. ''The beginning''"
    "You can read the pages in the attic journal."
    $ diary_neus[0]=[ _("{size=33}Today, I met a very somber boy who apparently lost his parents."),
    _("{size=33}It's been two years since we met, and it's truly pleasant to spend time with him."),
    _("{size=33}Today was my 15th birthday, and he gave me a beautiful ring. He is so sweet.. I want to rape him {e_heart=FF0000}."),
    _("{size=33}Despite having a strange hairstyle, recently, many busty bitches have been approaching him."),
    _("{size=33}{color=#f00}Death to big tits, death to big tits, death to big tits, death to big tits, death to big tits..."),
    _("{size=33}{color=#f00}Death to thieving bitches, death to thieving bitches, death to thieving bitches..."),
    _("The beginning")]
    $secret_point+=1
    $pages_diary_neus+=1
    jump attic_room
label page_1:
    scene attic1_5 with dissolve
    "You found pages 3 and 4 of [neusname]' diary. ''Routines of the past''"
    "You can read the pages in the attic journal."
    $ diary_neus[1]=[_("{size=33}I woke up savoring the familiar, comforting scent around me, then I headed to the kitchen to prepare breakfast."),
    _("{size=33}As usual, we met up so we could go to school together."),
    _("{size=33}When we were coming back from school, we split up because he had to buy underwear due to his going missing."),
    _("{size=33}As always, I was pondering over my stagnant relationship while enjoying the scent of stolen sheets."),
    _("{size=33}If he finds out, he will definitely {color=#f00}hate{/color} me."),
    _("{size=33}I don't want him to distance himself from me. I need to let go of my obsession."),
    _("Routines of the past")]
    $secret_point+=1
    $pages_diary_neus+=1
    jump attic_room
label page_2:
    scene attic1_5 with dissolve
    "You found pages 5 and 6 of [neusname]' diary. ''The change''"
    "You can read the pages in the attic journal."
    $ diary_neus[2]=[_("{size=33}Finally, I am of legal age, and I have been awarded a scholarship to study at a good university!"),
    _("{size=33}To save money on rent, I will be moving in with [firstname]."),
    _("{size=33}For now, I can only hide my feelings, so I started therapy to learn how to control them."),
    _("{size=33}It has been two years of therapy, and I believe I have finally gotten rid of the feelings. Although lately, I have been experiencing episodes of losing consciousness."),
    _("{size=33}Portraits and two strange books have started to appear in the attic, but for some reason, I can't get rid of them, as if something is preventing me from doing so."),
    "",
    _("The change")]
    $secret_point+=1
    $pages_diary_neus+=1
    jump attic_room

label page_4_2:
    $diary_neus[3][2]=_("{size=33}He almost took my virginity. Why is he so aggressive? I don't hate the idea, but I think we should take things slower.")
    return

label page_4_3:
    $diary_neus[3][3]=_("{size=33}That was painful, I hated it.")
    return

label page_4_4:
    $diary_neus[3][4]=_("{size=33}We officially started dating, not that I'm excited...")
    return
label page_4_5:
    $diary_neus[3][5]=_("{size=33}I'm trash, and to make matters worse, I'm very happy...")
    return
label confrontation_event:
    scene extra0_0
    # if diary_neus[0][0]=="":
    #     scene extra0_0
    # else:
    #     scene extra0_1
    if not is_neus_sec_dis:
        show screen requirements_menu
    menu:
        #"{b}Requirements{/b}:\n[neusname]'s Diary Pages: {color=#cc0066}[pages_diary_neus]{/color}/[total_pages], Hypnosis Book: {color=#cc0066}[is_view_hypnosis_book]{/color}, Spell Book: {color=#cc0066}[item_book_magic.is_view]{/color} and Relationship Level: {color=#cc0066}[relationship_level]{/color}/3"
        "Confront"((pages_diary_neus>=total_pages) and (is_view_hypnosis_book) and (item_book_magic.is_view) and (spell_0_1.is_active) and (relationship_level>=3)):
            hide screen requirements_menu
            if not(is_neus_sec_dis):
                jump confrontation
            else:
                jump confrontation_menu
        "Confront intro" if (is_neus_sec_dis):
            hide screen requirements_menu
            jump confrontation
        "Leave":
            hide screen requirements_menu
            jump attic_room

screen requirements_menu():
    # Requirements text at a custom position
    vbox:
        xalign 0.916
        yalign 0.89
        text "{b}Requirements{/b}:" size 50
        null height 5
        text "[neusname]'s Diary Pages: {color=#cc0066}[pages_diary_neus]{/color}/[total_pages]"size 36
        text "Hypnosis Book: {color=#cc0066}[is_view_hypnosis_book]{/color}" size 36
        text "Spell Book: {color=#cc0066}[item_book_magic.is_view]{/color}" size 36
        text "Touch spell: {color=#cc0066}[spell_0_1.is_active]{/color}" size 36
        text "Relationship Level: {color=#cc0066}[relationship_level]{/color}/3" size 36


label page_0_incest:
    scene attic1_5 with dissolve
    "You found pages 1 and 2 of [neusname]' diary. ''The beginning''"
    "You can read the pages in the attic journal."
    $ diary_neus_incest[0]=[ _("{size=33}It's been so hard to sleep since mom and dad died, luckily my big brother has been letting me sleep with him, I feel so safe in his arms."),
    _("{size=33}Two years have past, and it's still hard, but at least I have my brother. I truly love spending time with him."),
    _("{size=33}Today was my 15th birthday, and he gave me a beautiful ring. He is so sweet.. I want to rape him {e_heart=FF0000}."),
    _("{size=33}Despite having a strange hairstyle, recently, many busty bitches have been approaching him."),
    _("{size=33}{color=#f00}Death to big tits, death to big tits, death to big tits, death to big tits, death to big tits..."),
    _("{size=33}{color=#f00}Death to thieving bitches, death to thieving bitches, death to thieving bitches..."),
    _("The beginning")]
    $secret_point+=1
    $pages_diary_neus+=1
    jump attic_room
label page_1_incest:
    scene attic1_5 with dissolve
    "You found pages 3 and 4 of [neusname]' diary. ''Routines of the past''"
    "You can read the pages in the attic journal."
    $ diary_neus_incest[1]=[_("{size=33}I woke up savoring the familiar, comforting scent around me, then I headed to the kitchen to prepare breakfast."),
    _("{size=33}As usual, we headed to school together."),
    _("{size=33}On our way back from school, we parted ways because he had to buy new underwear after his went missing."),
    _("{size=33}As always, I was pondering over our stagnant relationship while enjoying the comforting scent of his stolen sheets."),
    _("{size=33}If he finds out, he will definitely {color=#f00}hate{/color} me."),
    _("{size=33}I don't want him to distance himself from me, he's all I've got left. I need to let go of my obsession."),
    _("Routines of the past")]
    $secret_point+=1
    $pages_diary_neus+=1
    jump attic_room
label page_2_incest:
    scene attic1_5 with dissolve
    "You found pages 5 and 6 of [neusname]' diary. ''The change''"
    "You can read the pages in the attic journal."
    $ diary_neus_incest[2]=[_("{size=33}Today he moved out, and it really hurts. I feel so empty inside without him, like a part of me is missing."),
    _("{size=33}Finally, I am of legal age, and I have been awarded a scholarship to study at a good university!"),
    _("{size=33}The thought of being away from my brother any longer was unbearable, so I chose a university near him as an excuse to move in with him."),
    _("{size=33}Today, I started therapy to help me control my feelings. I can't risk losing him again."),
    _("{size=33}After two years of therapy, I believe I have finally gotten rid of the feelings. Although lately, I have been experiencing episodes of losing consciousness."),
    _("{size=33}Portraits and two strange books have started to appear in the attic, but for some reason, I can't get rid of them, as if something is preventing me from doing so."),
    _("The change")]
    $secret_point+=1
    $pages_diary_neus+=1
    jump attic_room

label page_4_2_incest:
    $diary_neus_incest[3][2]=_("{size=33}He almost took my virginity. Why is he so aggressive? I did't hate the idea, but he's my brother.")
    return

label page_4_3_incest:
    $diary_neus_incest[3][3]=_("{size=33}That was painful, I hated it.")
    return

label page_4_4_incest:
    $diary_neus_incest[3][4]=_("{size=33}We officially started dating, not that I'm excited...")
    return
label page_4_5_incest:
    $diary_neus_incest[3][5]=_("{size=33}I'm trash, and to make matters worse, I'm very happy...")
    return