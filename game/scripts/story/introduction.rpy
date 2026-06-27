image intro_0:
    "story/intro/intro_0_0.webp" 
    pause 0.3    
    "story/intro/intro_0_1.webp" with Dissolve(0.5)

label introduction:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    call splash_message(_("SEVERAL YEARS AGO")) from _call_splash_message_29 
    play music happy_memories volume 0.2 fadeout 1.0       
    scene intro_past_0 with snow1
    if incest_story:
        neus "Through the years we've grown up together, you’ve been the one constant in my life and I’m so happy to have you in it, brother."  
    else:
        neus "Through the years we've spent together, you've become someone I hold close in my heart, someone who truly matters to me."
    scene intro_past_1 with dissolve
    neus "I wanted to ask if you ..."   
    stop music fadeout .5    
    scene intro_0 with storyfx    
    play sound hit_table  
    neus "I'm hungry. Hurry up!" with vpunch 
    scene intro_1 with dissolve
    mc "I'm coming."
    play music our_daytime volume 0.2 fadeout 1.0
    scene intro_2 with w33
    neus "That wasn't bad."        
    mc "So, did you graduate from university?"
    scene intro_3 with dissolve         
    neus "Yes!"    
    mc "That's great! So, what are your plans now?"  
    scene intro_4 with dissolve       
    neus "I'm planning to take a short vacation.. go to the beach, buy some new clothes, and finish watching a few shows."    
    mc "So, nothing important then?"
    scene intro_5 with dissolve 
    neus "I also want to find a boyfriend... (and some money)."
    neus "You should find a girlfriend too."   
    mc "So, you're free? I could really use your help around the house."
    scene intro_6 with dissolve 
    neus "Are you even listening? Do you really think I’m going to waste my time on chores?"   
    scene intro_7 with w33
    neus "Hmph... I will remember this."    
    stop music fadeout 2.0
    scene intro_8 with w39
    mc "Finally, that's over. Meetings are so boring." 
    mc "I should take a vacation." 
    play sound phone_ring 
    pause 1.5
    scene intro_9 with dissolve
    mc "Who could this be?"  
    ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
    mc "Hello?" with dissolve
    play sound magical1 volume 0.3 
    play char3 whisper volume 0.3  
    pause 1.0
    scene intro_9_hypnosis with peekfx
    mc ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
    stop char3 fadeout 1.0
    call splash_message(_("5 min later")) from _call_splash_message_3 
    stop music fadeout 2.0
    scene intro_10 with peekfx
    if incest_story:
        mc "How annoying, mom wants a grandchild."    
    else:
        mc "How annoying, my mother wants a grandchild."    
    mc "Besides, I don't even have a girlfriend or a candidate for the..."
    scene intro_3 at gray_scale with pixellate
    neus "I want to find a boyfriend." 
    if incest_story:
        mc "(No, that wouldn't be right, she’s my sister) {w=1.0}.{w=1.0}.{w=1.0}."
        mc "(Although, I’ve always had feelings for her that go beyond just a sibling love. We were very close when we were younger.)"
    else:
        mc "(I've known her for 10 years. We used to be really close.)"     

    mc "(But over time, she started pulling away, things became more challenging between us, and it got harder to connect with her.)"
    scene bg_mc_room_night with dissolve
    mc "Hmm..."
    mc "(Still, the idea of having children with her feels really good, like there's an undeniable pull inside me drawing me closer to her) {w=1.0}.{w=1.0}.{w=1.0}."

    "The challenge ahead lingers on your mind, keeping you awake a little longer."
    $renpy.end_replay() 
    call notify_personalized(_("Main Quest updated")) from _call_notify_personalized_1  
    $is_change_quest = True        
    $night_1=True           
    jump expression "sleeping_event%s"%mc_event_lvl
