screen notify_personalized(message):    
    zorder 100
    style_prefix "notify_personalized"      
    frame at PopUpFade:               
        text _("[message!tq]") text_align 0.5

    timer 3.5 action Hide('notify_personalized')

style notify_personalized_frame is empty
style notify_personalized_text is gui_text

style notify_personalized_frame:
    ypos 100 
    xalign 1.0      
    background Frame("gui/notify.png", Borders(64, 8,24,8), tile=gui.frame_tile)
    padding Borders(64, 8,24,8).padding

label notify_personalized(message):
    play sound notification volume 0.3
    show screen notify_personalized(message) 
    return

