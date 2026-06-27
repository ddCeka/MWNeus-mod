#Variables
init python:    
    position_spanking=0
    point_view_spanking=0
    outfit_spanking=0
    undress_spanking=0            
    spanking_count=0
default spanking_level=0
default is_action_spanking=2
default is_massage_or_spank=0
default max_spanking_pain = 2
default max_spanking_pleasure = 2
default spanking_force=0
default spanking_pain=0    
default spanking_pleasure=0    
default massage_type=0
default spanking_active=True 
default is_view_spanking=False 
label spanking_start:
    $is_action_spanking=2
    $spanking_force=0
    $spanking_pain=0    
    $spanking_pleasure=0
    $spanking_count=0
    $undress_spanking=0 
    $is_massage_or_spank=0
    stop music fadeout 1.0   
    if undress_spanking>=1:
        scene base_spanking_with_mask with dissolve
    else:
        scene base_spanking with dissolve          
    jump spanking
label spanking: 
    if spanking_count>=5:
        play char3 breathing1 if_changed
    else:
        stop char3 fadeout 1.0
    show screen spanking
    $ spanking_active=True
    pause
screen screen_tooltip_spanking:
    $ tooltip = GetTooltip(last=False)    
    if tooltip:                                
        text _("[tooltip!tq]"):
            xalign 0.99
            ypos 250
            size 60
            outlines [ (2,"#000") ]           
            
screen spanking: 
    imagebutton:
        idle Solid("#00000000")
        sensitive spanking_active
        action SetVariable("spanking_active",False),Jump("spanking_action%s"%is_massage_or_spank)   
    
    if spanking_pleasure==(spanking_level+1)*2 and spanking_level<2:
        textbutton __("{size=+40}{b}Next Level"):
                text_outlines [ (2,gui.accent_color) ]  
                sensitive spanking_active       
                action SetVariable("spanking_active",False),Jump("spanking_quit")
                ypos 10
                xalign 0.5
                at text_animation_alpha
    else:
        textbutton __("{size=+40}{b}Finish"):
            text_outlines [ (2,"#000") ]  
            sensitive spanking_active       
            action SetVariable("spanking_active",False),Jump("spanking_quit")
            ypos 10
            xalign 0.5
    if spanking_level>=1:
        textbutton __("{size=+10}{b}Reset Bruises %s/11")%spanking_count:
                text_outlines [ (2,"#000") ]  
                sensitive spanking_active  
                selected False     
                action SetVariable("spanking_count",0),Jump("change_state")
                yalign 0.93
                xalign 0.99
    vbox:
        xpos 10
        ypos 10                           
        text __("Level: %s/2")%spanking_level:
            outlines [ (4, gui.accent_color) ]
            size 60
            xalign 0.5
        if spanking_level<2:
            text __("Next level: %s/{color=#cc0066}%s{/color} pleasure")%(spanking_pleasure,(spanking_level+1)*2):
                outlines [ (2,"#000") ] 
                xalign 0.5 
        if not(spell_0_1.is_active):
            text __("Requirements:"):
                xalign 0.5
                outlines [ (2.3,"#000") ]
                color "#cc0066"
                size 45     
            text __("''{color=#cc0066}Touch{/color}'' spell"):
                outlines [ (2,"#000") ] 
                xalign 0.5
        elif spanking_level>=1 and relationship_level<=1:
            text __("Requirements:"):
                xalign 0.5
                outlines [ (2.3,"#000") ]
                color "#cc0066"
                size 45     
            text __("Relationship level {color=#cc0066}2{/color}"):
                outlines [ (2,"#000") ] 
                xalign 0.5
        elif not(spell_2_1.is_active) and spanking_level>=1 and relationship_level>=2:
            text __("Requirements:"):
                xalign 0.5
                outlines [ (2.3,"#000") ]
                color "#cc0066"
                size 45     
            text __("''{color=#cc0066}Pain is pleasure{/color}'' spell"):
                outlines [ (2,"#000") ] 
                xalign 0.5
        vbox:                    
            spacing 10 
            vbox:  
                text __("Pleasure: %s/%s") % (spanking_pleasure, max_spanking_pleasure) outlines [ (2,"#000") ] xalign 0.5     
                bar:            
                    value spanking_pleasure 
                    range max_spanking_pleasure 
                    xsize 400            
                    right_bar "#ffffff"  
                    left_bar "#cc0066"
            vbox: 
                text __("Pain: %s/%s") % (spanking_pain, max_spanking_pain) outlines [ (2,"#000") ] xalign 0.5   
                bar:            
                    value spanking_pain 
                    range max_spanking_pain
                    xsize 400            
                    right_bar "#ffffffff"  
                    left_bar "#000"                        
         
    #Action 
    vbox: 
        ypos 10
        xalign 0.99
        #subscreen        
        if is_action_spanking==1:
            hbox:
                xalign 0.5
                spacing 10
                textbutton _("{size=+15}Pants"):
                    text_outlines [ (2,"#000") ]
                    sensitive spanking_active and spanking_level>=1
                    action SetVariable("undress_spanking", 0),Jump("change_state")
                textbutton _("{size=+15}Panties"):
                    text_outlines [ (2,"#000") ]
                    sensitive spanking_active and spanking_level>=1
                    action SetVariable("undress_spanking", 1),Jump("change_state")
                textbutton _("{size=+15}Naked"):
                    text_outlines [ (2,"#000") ]
                    sensitive spanking_active and spanking_level>=2
                    action SetVariable("undress_spanking", 2),Jump("change_state")
        if is_action_spanking==2:
            hbox:                
                xalign 0.5
                spacing 10
                textbutton _("{size=+15}Touch"):
                    tooltip If(spanking_level>=2,_("+1 Pleasure, -1 Pain"),_("+1 Pleasure(max 3), -1 Pain"))
                    text_outlines [ (2,"#000") ]
                    sensitive spanking_active and spell_0_1.is_active
                    action SetVariable("massage_type", 1)
                textbutton _("{size=+15}Normal"):
                    tooltip _("+1 Pleasure(max 1)")
                    text_outlines [ (2,"#000") ]
                    sensitive spanking_active
                    action SetVariable("massage_type", 0)
        if is_action_spanking==3:        
            hbox:                
                xalign 0.5
                spacing 10
                textbutton _("{size=+15}Hard"):
                    text_outlines [ (2,"#000") ]
                    tooltip If(spanking_level>=2,_("+0 Pain"),If(spell_2_1.is_active,_("+1 Pain"),_("+2 Pain")))
                    sensitive spanking_active
                    action SetVariable("spanking_force", 2)
                textbutton _("{size=+15}Normal"):
                    text_outlines [ (2,"#000") ]
                    tooltip If(spanking_level>=2,_("+1 Pleasure"),If(spell_2_1.is_active,_("+0 Pain"),_("+1 Pain")))
                    sensitive spanking_active
                    action SetVariable("spanking_force", 1)
                textbutton _("{size=+15}Soft"):
                    text_outlines [ (2,"#000") ] 
                    tooltip If(spanking_level>=2,_("+2 Pleasure"),If(spell_2_1.is_active,_("+1 Pleasure"),_("+0 Pain")))
                    sensitive spanking_active               
                    action SetVariable("spanking_force", 0)           
        hbox:            
            spacing 10            
            xalign 1.0                       
            imagebutton:
                auto "btn_undress_spanking_%s"
                selected_idle "btn_undress_spanking_hover"
                tooltip _("Undress")
                insensitive im.Grayscale("buttons/btn_undress_spanking_idle.png")
                sensitive spanking_active
                action SetVariable("is_action_spanking", 1)
            imagebutton:
                auto "btn_massage_%s"
                selected_idle "btn_massage_hover"
                tooltip _("Massage")
                insensitive im.Grayscale("buttons/btn_massage_idle.png")
                sensitive spanking_active
                action [SetVariable("is_action_spanking", 2),Function(is_massage)]
            imagebutton:
                auto "btn_spank_%s" 
                selected_idle "btn_spank_hover" 
                insensitive im.Grayscale("buttons/btn_spank_idle.png") 
                sensitive spanking_active         
                tooltip _("Spank")
                action [SetVariable("is_action_spanking", 3),Function(is_spank)]                  
    use screen_tooltip_spanking

init python:
    def is_massage():
        renpy.store.is_massage_or_spank = 0
    def is_spank():
        renpy.store.is_massage_or_spank = 1


label change_state:    
    scene black with dissolve       
    if undress_spanking>=1:
        scene base_spanking_with_mask with dissolve
    else:
        scene base_spanking with dissolve 
    jump spanking

label spanking_action0:
    if spanking_pleasure< max_spanking_pleasure:
        if massage_type==0 and spanking_pleasure<1:            
            $spanking_pleasure+=1
        if massage_type==1 and spanking_pleasure<3:                       
            $spanking_pleasure+=1
        if spanking_level>=2:
            $spanking_pleasure+=1
    if undress_spanking>=1:
        scene spanking_massage_with_mask
    else:          
        scene spanking_massage
    if massage_type==0:
        if spanking_level>=2:
            neus "{e_heartbt=FF0000}"
        else:         
            neus "Hm...(That feels weird)"
    elif massage_type==1:
        if spanking_pain>0:
            $spanking_pain-=1 
        play sound magical1 volume 0.3
        play char1 penetration4   
        if spanking_level>=2:
            neus "{e_heartbt2=FF0000}"
        else:           
            neus "Oh...(That feels good..)"        
    jump spanking

label spanking_action1:    
    if spanking_pain<max_spanking_pain:
        if spanking_force==0:  
            if undress_spanking>=1:
                scene spanking_slow_with_mask
            else:          
                scene spanking_slow
            if spanking_count<=10:
                $spanking_count+=1
            play charM slap_slow1
            if spanking_level>=2:
                neus "(That feels good, I {color=#cc0066}want{/color} you to {color=#cc0066}spank{/color} me {color=#cc0066}more{/color}.)"
                $spanking_pleasure+=2
            else:
                if spell_2_1.is_active:
                    if spanking_pleasure< max_spanking_pleasure:
                        $spanking_pleasure+=1 
                    play char1 groan_slow1
                    neus "Hmm...(That feels good)"
                else:
                    neus "..."
        elif spanking_force==1:
            if undress_spanking>=1:
                scene spanking_normal_with_mask
            else:
                scene spanking_normal
            play charM slap1 
            if spanking_level>=2:                
                neus "{e_heartbt2=FF0000}"
                $spanking_pleasure+=1
            else:           
                if not(spell_2_1.is_active):
                    $spanking_pain+=1                
                    neus "Ouch!"
                else:
                    play char1 groan_normal1
                    neus "Hmm..."
                if spanking_count<=10:
                    $spanking_count+=2                         
        elif spanking_force==2:
            if undress_spanking>=1:
                scene spanking_hard_with_mask
            else:
                scene spanking_hard
            play charM slap_hard1           
            if spanking_count<=10:
                $spanking_count+=3
            if spanking_level>=2:
                neus "(That hurt a little, but it also {color=#cc0066}feels good{/color}.)"
            else:
                if not(spell_2_1.is_active):
                    $spanking_pain+=2
                    play char1 groan_hard1
                    neus "That hurts"
                else:
                    $spanking_pain+=1
                    play char1 groan_hard1
                    neus "Ouch!"                
    if spanking_count>=7:
        $spanking_pain+=1
    if spanking_pain>=max_spanking_pain:
        if spanking_level>=2:
            neus "Can we stop... {e_heartbt=FF0000} my butt hurts a little..."            
        else:
            neus "Stop it!"       
        jump spanking_quit      
    jump spanking

label spanking_quit:
    hide screen spanking
    scene black with dissolve    
    if spanking_level<2 and spanking_pleasure>=(spanking_level+1)*2:
        $spanking_level+=1
        if spanking_level==1:
            scene spanking_quit1 with dissolve
            neus "(That was annoying, although the massage was somewhat g ...)"
        elif spanking_level==2:
            scene spanking_quit2 with dissolve
            neus "(W-Why does it feel good when he spanks me? Am I a masochist or something?)" 
            scene spanking_quit3 with dissolve           
            neus "(No, he must have used some kind of magic, that must be it.)"
        $max_spanking_pain+=(2*spanking_level)
        $max_spanking_pleasure+=(2*spanking_level)        
        call splash_message(_("Spanking level +1")) from _call_splash_message_19 
    else:
        if spanking_level==0:
            scene spanking_quit4 with dissolve
            if spanking_pain>=2:
                neus "That hurt"
            else:
                neus "(That felt weird.)"
        elif spanking_level==1:
            scene spanking_quit5 with dissolve
            if spanking_pain>=3:
                neus "That hurt"
            else:
                neus "(That felt w ...)"
        elif spanking_level==2:
            if spanking_pleasure>=8:
                scene spanking_quit7 with dissolve
                neus "Ah... "            
            else:
                scene spanking_quit6 with dissolve
                neus "..."    
    jump time_advances 