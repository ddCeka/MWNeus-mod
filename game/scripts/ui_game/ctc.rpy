screen ctc(arg=None):

    zorder 100

    hbox:
        xalign 0.0
        yalign 0.96
        spacing 10

        text "{icon=icon-chevrons-down}" at ctc_animation: 
            outlines [ (persistent.text_outline,gui.accent_color) ]         
            size 40  
            color gui.text_color

        text _("Click to continue"):
            outlines [ (persistent.text_outline,gui.accent_color) ]
            font gui.interface_text_font
            size gui.notify_text_size
            xalign 0.0
            yalign 0.96
            color gui.text_color

