
screen quests_all:   
    default auxIncest=0
    default auxSide=0
    vbox:        
        spacing 30
        ysize 545
        vbox:
            xsize 640
            label _('{color=#cc0066}{size=+10}{b}Main quests{/b}') 
            if quest_v2:
                if questMain_v2_select.place=="" and questMain_v2_16.completion:
                    text _("Go to [neusname]'s room and choose your ending or...")
                else:
                    text _(str(questMain_v2_select.description))
            if not quest_v2:
                if questMain_select.place=="" and questMain_9.completion:
                    text _("Go to [neusname]'s room and choose your ending or...")              
                else:
                    text _(str(questMain_select.description))
        vbox:
            xsize 640
            label _('{color=#0b2ecb}{size=+10}{b}Side quests{/b}')
            if quest_v2:
                for q in questListSide_v2:
                    if not(q.completion) and q.level<=relationship_level and auxSide<1 and q.start:
                        $auxSide+=1
                        text _(str(q.description))  
            elif not quest_v2:
                for q in questListSide:
                    if not(q.completion) and q.level<=relationship_level and auxSide<1 and q.start:
                        $auxSide+=1
                        text _(str(q.description))             
            if  auxSide==0 and relationship_level<3:
                text _("Advance in the main quest.")           
            elif auxSide==0:
                text _("All the side quests have been completed for this phase.")   
           
    vbox:
        xsize 640
        spacing 10
        text _('{b}Photo:{/b} {color=#cc0066}[photo_count]{/color}/20')
        text _('{b}Outfit photo:{/b} {color=#cc0066}[outfit_photo_count]{/color}/3')       
        text _('{b}Secrets:{/b} {color=#cc0066}[secret_point]{/color}/[total_secrets]')
        if is_view_attic:
            text _("{b}[neusname]'s Diary Page:{/b} {color=#cc0066}[pages_diary_neus]{/color}/[total_pages]") 
        text "{b}Endings Obtained:{/b} {color=#cc0066}[endings_obtained_count]{/color}/[total_endings]"
