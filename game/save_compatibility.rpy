default game_version = 0
label rework_diary:
    # Diary
    $diary_neus[3] =[_("I finally finished university and decided to take a vacation since my episodes of unconsciousness became more frequent and prolonged."),
        _("[firstname] has been acting strange lately."),
        "",
        "",
        "",
        "",
        _("The present")
        ]
    if diary_neus[2][0]!="":
        $ diary_neus[2]=[_("Finally, I am of legal age, and I have been awarded a scholarship to study at a good university!"),
            _("To save money on rent, I will be moving in with [firstname]"),
            _("For now, I can only hide my feelings, so I started therapy to learn how to control them."),
            _("It has been two years of therapy, and I believe I have finally gotten rid of the feelings. Although lately, I have been experiencing episodes of losing consciousness."),
            _("Portraits and two strange books have started to appear in the attic, but for some reason, I can't get rid of them, as if something is preventing me from doing so."),
            "",
            _("The change")]
    if diary_neus[1][0]!="":
        $ diary_neus[1]=[_("I woke up enjoying the pleasant smell, then I headed to the kitchen and prepare breakfast."),
            _("As usual, we met up so we could go to school together."),
            _("When we were coming back from school, we split up because he had to buy underwear due to his going missing."),
            _("As always, I was pondering over my stagnant relationship while enjoying the scent of stolen sheets."),
            _("If he finds out, he will definitely {color=#f00}hate{/color} me."),
            _("I don't want him to distance himself from me. I need to let go of my obsession."),
            _("Routines of the past")]
    if questMain_5.completion:
        call page_4_2 from _call_page_4_2_1
    if questMain_6.completion:
        call page_4_3 from _call_page_4_3_1
    if questMain_7.completion:
        call page_4_4 from _call_page_4_4_1
    if questMain_9.completion:
        call page_4_5 from _call_page_4_5
    return

label after_load:    
    if  game_version < 0.9:                   
        stop music
        #Quest Main
        $questMain_1 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}")
                            ,0,"kitchen",0,"level0_0",completion=questMain_1.completion)
        $questMain_2 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
                            ,0,"neus",0,"level0_1",completion=questMain_2.completion)
        $questMain_3 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
                            ,0,"neus",0,"level0_2",completion=questMain_3.completion)
        $questMain_4 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}")
                            ,0,"kitchen",0,"level1_0",completion=questMain_4.completion)
        $questMain_5 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}")
                            ,0,"neus",2,"level1_2",completion=questMain_5.completion)
        $questMain_6 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}")
                            ,0,"neus",2,"level1_3",completion=questMain_6.completion)
        $questMain_7 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} at {color=#cc0066}Noon{/color}")
                            ,0,"neus",1,"level2_0",completion=questMain_7.completion)
        $questMain_8 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
                            ,0,"neus",0,"level2_1",completion=questMain_8.completion)                     
        if questMain_4.completion and not(questMain_5.completion):            
            $questMain_select=questMain_5
        if questMain_8.completion and relationship_level<=2:
            $questMain_select=questMain_8
        #Quest Side 
        $questSide_1 = Quest(_("Take the book from your room."),0,completion=questSide_1.completion)
        $questSide_2 = Quest(_("Activate ''Touch''"),0,completion=questSide_2.completion)         
        $questSide_4 = Quest(_("Take the attic key from the living room."),1,start=False,completion=questSide_4.completion)
        $questSide_5 = Quest(_("Go to the attic and confront her."),3,completion=is_neus_sec_dis)
        $questSide_6 = Quest(_("Go to [neusname]' room and choose ''Another personality''"),3,completion=questSide_6.completion)
        $questSide_7 = Quest(_("Split her personalities or not..."),3,completion=questSide_7.completion)
        $questListSide=[questSide_1,questSide_2,questSide_4,questSide_5,questSide_6,questSide_7]
        #Spell

        $spell_0_1=spell(_("Touch"),_("Has aphrodisiac effects, although it can also be used to give energy. (The more {color=#cc0066}relationship level{/color} you have, the more powerful ''Touch'' becomes.)"),"btn_spell_0_1_%s",0,0,questSide_2,is_active=spell_0_1.is_active)
        $level_0=[spell_0_1]
        $spell_1_1=spell(_("Level up and down"),_("Adjusts the level of events in all rooms, increasing or decreasing it."),"btn_spell_1_1_%s",5,1,is_active=True)
        $level_1=[spell_1_1]
        $spell_2_1=spell(_("Pain is pleasure"),_("Turn pain into pleasure"),"btn_spell_2_1_%s",5,2,is_active=spell_2_1.is_active)
        $spell_2_2=spell(_("Object creation"),_("Allows the creation of any object as long as a reference is available"),"btn_spell_2_2_%s",5,2,is_active=spell_2_2.is_active)
        $level_2=[spell_2_1,spell_2_2]    
        $spell_3_1=spell(_("Fertilization"),_("Allows you to set the fertilization rate to 100% or 0%."),"btn_spell_3_1_%s",5,3,is_active=spell_3_1.is_active)
        $spell_3_2=spell(_("Personality"),_("Allows the separation of personalities or can make one predominate over another."),"btn_spell_3_2_%s",5,3,start=False,is_active=spell_3_2.is_active)
        $level_3=[spell_3_1,spell_3_2]
        $tree=[level_0,level_1,level_2,level_3]
        $ probability_of_pregnancy = 50        
        call rework_diary from _call_rework_diary          
    $ game_version = myconfig.version


    
    if mod_version < 1.1:
        $ item_book_magic = Item(_("{b}Spell Book:{/b} "), image = "icon_book_spell_%s", description = _("Contains sexual spells"))
        $ item_tsundere_magazine = Item(_("{b}Magazine:{/b} "), image = "icon_tsundere_magazine_%s", description = _("Contains advice on how to deal with a Tsundere"))
        $ key_room_neus = Item(_("{b}Key:{/b} "), image = "icon_key_neus_%s", description = _("[neusname]'s room key"))
        $ key_room_attic = Item(_("{b}Key:{/b} "), image = "icon_key_attic_%s", description = _("Attic key"))
        $ item_portrait_neus = Item(_("{b}Portrait:{/b} "), image = "icon_portrait_neus_%s", description = _("Portrait of [neusname]"))
        $ item_newspaper_living = Item(_("{b}Newspaper:{/b} "), image = "icon_newspaper_living_%s", description = _("Tribute to the Fallen."))
        
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
        $ questSide_2.description = "Activate the ''Touch'' spell"
        $ questSide_3.description = "Find the key to [neusname]'s room"
        $ questSide_4.description = "Find the key to the attic"
        $ questSide_5.description = "Go to the attic and confront her."
        $ questSide_6.description = "Go to [neusname]'s room and choose ''Another personality''"
        $ questSide_7.description = "''Split personalities'' or ''Don't split''"

        $ spell_0_1.description = "Has aphrodisiac effects, although it can also be used to give energy. (The more {color=#cc0066}relationship level{/color} you have, the more powerful ''Touch'' becomes.)"
        $ spell_1_1.description = "Adjusts the level of events in all rooms, increasing or decreasing it."
        $ spell_2_1.description = "Turns pain into pleasure"
        $ spell_2_2.description = "Allows the creation of any object as long as a reference is available"
        $ spell_3_1.description = "Allows you to set the fertilization rate to 100% or 0%."
        $ spell_3_2.description = "Allows the separation of personalities or can make one predominate over another."

        $ mod_version = 1.1

    if mod_version < 1.2:
        $ index = difficulties.index(difficulty) if difficulty in difficulties else None
        $ difficulty = difficulties[index + 1] if index is not None and index + 1 < len(difficulties) else difficulty

        $ questSide_2.description = "Learn the ''Touch'' spell"
        $ questSide_v2_2.description = "Learn the ''Touch'' spell"

        if customer_name == "customer":
            $ customer_name = "dear ''customer''"

        if incest_story:
            $ persistent.gallery_incest_story = True
        if not set_active_pregnancy:
            $ persistent.gallery_pregnancy_censored = True

        $ persistent.gallery_firstname = firstname
        $ persistent.gallery_neusname = neusname
        $ persistent.gallery_lyra = neusname_lyra
        $ persistent.gallery_sylvia = neusname_sylvia
        $ persistent.gallery_customer_name = customer_name

        if not quest_v2 and unlock_milf and unlock_two_bodies:
            $ questSide_7.completion = True
            $ is_change_quest = True
            call notify_personalized(_("Side Quest updated")) 
        
        $ mod_version = 1.2
    return