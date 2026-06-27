image hallway0_2= DynamicAnimation(
["rooms/hallway/lvl0/hallway0_2_0.webp",
"rooms/hallway/lvl0/hallway0_2_1.webp", 
"rooms/hallway/lvl0/hallway0_2_2.webp",
"rooms/hallway/lvl0/hallway0_2_3.webp",
"rooms/hallway/lvl0/hallway0_2_4.webp"],time_start=0,random_delay=0)

label bath_hallway: 
    scene hallway0_0   
    call rooms_music
    show screen bath_spell    
    menu:
        "Knock on the door":
            hide screen spell_screen
            play sound door_knock volume 0.5
            jump expression "bath_knock%s"%bath_event_lvl
        "Peek":  
            hide screen spell_screen
            jump expression "bath_peek%s"%bath_event_lvl
        "Back": 
            $select_room ="mc"                               
            jump rooms
    jump bath_hallway
    
#----------------------------Level 0---------------------------------
label bath_peek0:
    stop music fadeout 0.5
    play ambience shower2 volume 0.5
    scene hallway0_2  with peekfx
    "You peek through the keyhole..."
    mc "(Her ass is flawless...)"
    mc "(Just a little longer… and I might see her perfect tits.)"
    $ xsize_value = 500
    menu(screen="custom_choice_enhanced"):
        "Wait":
            pass
        "Leave":
            stop ambience
            jump bath_hallway
    "You wait a bit longer while you continue peeking through the keyhole" 
    ""
    stop ambience fadeout 0.5
    scene hallway0_3 with peekfx
    ""
    scene black
    "You return to your room quietly" 
    if quest_v2:
        call addLust(1)
    $select_room ="mc" 
    jump time_advances      
    jump bath_hallway

label bath_knock0:
    neus "I'm in here."   
    jump bath_hallway

#----------------------------Level 1---------------------------------
label bath_peek1:    
    stop music fadeout 0.5
    play ambience shower2 volume 0.5
    scene hallway0_2  with peekfx
    "You peek through the keyhole"   
    ""  
    stop ambience
    jump bath_hallway

label bath_knock1:   
    neus "I'm in here, I'll be out soon" 
    stop music fadeout 1.0
    call splash_message(_("Moments later")) from _call_splash_message_7
    scene hallway1_0 with dissolve
    neus "You can go in now"
    scene hallway1_1 with dissolve
    if incest_story:
        neus "Hey, what are you doing brother?"
        scene hallway1_2 with dissolve
        neus "You are such a pervert"
    else:
        neus "Hey, what are you doing?"
        scene hallway1_2 with dissolve
        neus "You are a fucking monkey"
    play char1 french01
    scene hallway1_3 with dissolve
    neus "Guuu"
    scene hallway1_4 with dissolve
    neus "{sc=3}Haa{/sc}"
    scene hallway1_5 with dissolve
    neus "({sc=3}...{/sc})"
    scene black with dissolve
    "You take a shower"
    $ neus_left_room = True
    if quest_v2:
        call addLust(2)
    jump time_advances