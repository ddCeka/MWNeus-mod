default neus_room_unlocked = False
default unlock_enter = "Unlock and enter"
label neus_hallway:
    if time == 4 and neus_event_lvl == 0:
        show screen neus_spell
    else:
        hide screen spell_screen
    if time == 4:
        stop music fadeout 0.5
    scene hallway0_1     
    menu:
        "Knock on the door" if (neus_event_lvl == 0) or (neus_event_lvl == 1 and time == 3 and not is_view_key_room_neus) or (neus_event_lvl == 1 and time == 4 and not key_room_neus.is_view):
            hide screen spell_screen
            play sound door_knock volume 0.5
            if time == 4:
                jump expression "neus_knock_sleep%s"%neus_event_lvl
            else:
                jump expression "neus_knock%s"%neus_event_lvl
        "[unlock_enter]" (key_room_neus.is_view) if neus_event_lvl == 1:
            jump expression "neus_enter%s"%neus_event_lvl
        "Peek":
            hide screen spell_screen
            if time == 4:
                jump expression "neus_peek_sleep%s"%neus_event_lvl
            else:
                jump expression "neus_peek%s"%neus_event_lvl
        "Back": 
            $select_room ="mc"                             
            jump rooms
    jump neus_hallway
#----------------------------Level 0---------------------------------
label neus_peek_sleep0:
    scene hallway0_4 with peekfx
    "You peek through the keyhole"
    jump neus_hallway
label neus_knock_sleep0:
    "She does not answer"
    jump neus_hallway
label neus_peek0:
    scene hallway0_5 with peekfx
    "You peek through the keyhole"
    jump neus_hallway
label neus_knock0:
    neus "You can come in"
    scene hallway0_1 at zoom_animation
    "You enter her room"
    jump expression "neus%s"%neus_event_lvl
#----------------------------Level 1---------------------------------
label neus_peek_sleep1:
    scene hallway1_7 with peekfx
    "You peek through the keyhole"
    jump neus_hallway
label neus_knock_sleep1:    
    "She does not answer"          
    jump neus_hallway
label neus_peek1:
    scene hallway1_6  with peekfx
    "You peek through the keyhole"
    jump neus_hallway
label neus_knock1:
    neus "Come in"
    scene hallway0_1 at zoom_animation
    "You enter her room"
    jump expression "neus%s"%neus_event_lvl
label neus_enter1:
    scene hallway0_1 at zoom_animation
    if not is_view_key_room_neus:
        "You unlock the door and enter her room"
    else:
        "You enter her room"
    $ neus_room_unlocked = True
    jump rooms