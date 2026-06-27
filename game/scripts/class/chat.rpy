init python:
    class Msg:
        def __init__(self, who, text, replies=None, condition=None, actions=None, picture=None):
           
            if who not in ["mc", "npc"]:
                renpy.error("Function <Msg.__init__>: The <who> argument must be 'mc' or 'npc' (Current value: {})".format(who))
            else:
                self.who = who

            self.text = text

           
            if replies is None:
                self.replies = []
            else:
                if isinstance(replies, list):
                    self.replies = replies
                else:
                    self.replies = [ replies ]
            
            self.condition = condition
            
            if actions is None:
                self.actions = []
            else:
                if isinstance(actions, list):
                    self.actions = actions
                else:
                    self.actions = [ actions ]
            self.picture = picture

        def is_valid(self):
            if self.condition is None:
                return True
            else:
                return eval(self.condition)

    def chat_next_step(step):
        current_step = step        
        msg = current_chat[step]        
        store.chat_history.append(step)
        if len(msg.actions) > 0:            
            for act in msg.actions:
                exec(act)
        store.chat_step = step   
    def next_who():
        rep = current_chat[chat_step].replies
        if rep:
            return current_chat[rep[0]].who
        else:
            return "end"


    def phone_point(var, value=1):
       
        setattr(store, var, getattr(store, var) + value)


default chat_history = []
default current_chat = None
default chat_step = None
default chat_yadj = None


label chat(chat):
    $ current_chat = chat
    $ chat_history = []
    $ chat_step = None
    $ chat_yadj = ui.adjustment()

    $ chat_next_step("0")

    play sound notificationphone2

    show screen chat with dissolve

    jump chat_loop


label chat_loop:
    if next_who() == "mc":
        
        call screen chat_answers()

        
        $ chat_yadj.value = float('inf')

    elif next_who() == "npc":
        
        show screen chat_is_typing()
        pause 0.7
        hide screen chat_is_typing
        play sound notificationphone        
        $ chat_next_step( [ rep for rep in current_chat[chat_step].replies if current_chat[rep].is_valid() ][0] )

        if next_who() == "npc":            
            pause 0.5

        elif next_who() == "mc":            
            pause 0.5

    else:        
        call screen chat_end()
        hide screen chat with dis08
        return
    jump chat_loop

transform phone_pic():
    on show:
        zoom 0.0
        linear 0.2 zoom 1.0

    on hide:
        zoom 1.0
        linear 0.1 zoom 0.0
screen show_pic(pic):
    modal True
    
    imagebutton:
        idle Null(width=1920, height=1080)
        action Hide("show_pic")

    frame:
        style "empty"
        align (0.5, 0.5)

        at phone_pic

        imagebutton:
            keysym "game_menu"
            idle pic
            action Hide("show_pic")


transform answers_dissolve:
    alpha 0.0
    linear 0.3 alpha 1.0


screen chat_answers():
    vbox:
        at answers_dissolve
        xalign 0.99
        yalign 0.5
        spacing 15

        for key, msg in [ (key, current_chat[key]) for key in current_chat[chat_step].replies ]:
            if msg.is_valid():
                vbox:
                    button:
                        padding (0, 0, 0, 0)
                        action [ Function(chat_next_step, step=key), Return() ]

                        frame:
                            xsize 380
                            padding (10, 10, 10, 10)
                            background Frame("chat_mc_background",17,17,17,17)

                            vbox:
                                xalign 0.5

                                text _(msg.text):
                                    style "chat_button_text"
                                    xalign 0.5

                                if msg.picture is not None:
                                    #
                                    # Display a picture in the message
                                    #
                                    add Transform(msg.picture, zoom=0.2) xalign 0.5
transform message_popup:
    alpha 0.0
    yoffset 50
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0


screen chat():
    style_prefix "chat"    
    add current_chat["background"]

    frame:
        style "empty"        
        background Frame("chat_background_messages", 60, 60, 60, 60)
        xysize (1120, 930)
        ypos 50
        xalign 0.5

        viewport yadjustment chat_yadj:
            pos (60, 150)
            xsize 1000
            ymaximum 740
            mousewheel True
            draggable True

            vbox:
                xsize 1000
                spacing 10

                for msg in [ current_chat[key] for key in chat_history]:

                    if len(msg.text) > 0:
                        vbox:
                            at message_popup
                            if msg.who == "mc":                                
                                xalign 1.0

                            frame:
                                yalign 0.5
                                padding (25, 32, 25, 25)
                                if msg.who == "npc":                                    
                                    background Frame("chat_npc_background",17,17,17,17)
                                else:                                    
                                    background Frame("chat_mc_background",17,17,17,17)

                                vbox:
                                    xminimum 500
                                    xmaximum 707
                                    text msg.text
                                    if msg.picture is not None:                                        
                                        imagebutton:
                                            xalign 0.5
                                            idle Transform(msg.picture, zoom=0.2)
                                            hover Transform(msg.picture, zoom=0.2, matrixcolor=BrightnessMatrix(0.2))
                                            action Show("show_pic", pic=msg.picture)
                            if msg.who == "npc":
                                add "chat_npc_background_tip"
                            else:
                                add "chat_mc_background_tip" xalign 1.0
    add current_chat["thumbnail"] xalign 0.5


screen chat_is_typing():
    frame:
        style "empty"
        xsize 1030
        pos (85, 990)

        has hbox:
            xalign 0.5

        # \u25cf = unicode character "black circle"
        text "\u25cf " at delayed_blink(0.0, 0.8) style "chat_npc_is_typing_dot"
        text "\u25cf " at delayed_blink(0.2, 0.8) style "chat_npc_is_typing_dot"
        text "\u25cf " at delayed_blink(0.4, 0.8) style "chat_npc_is_typing_dot"
        text renpy.substitute(_("[npc_name!ti] is typing..."), scope={ "npc_name" : current_chat["npc"]}) style "chat_npc_is_typing"


screen chat_end():    
    textbutton _("Click to end the chat"):
        style "chat_exit_button"
        keysym "game_menu"
        anchor (0.5,0.5)
        pos (0.5, 0.9)
        action [ Return() ]


style chat_text:
    color "#000000"
    size 30
    xalign 0.5

style chat_button_text:
    font gui.text_font
    idle_color "#000000"
    hover_color "#ffffff"
    size 30

style chat_npc_is_typing_dot:
    yoffset -6
    color "#ffffff"
    size 26
    font "DejaVuSans.ttf"

style chat_npc_is_typing:
    color "#ffffff"
    size 31
    italic True

style chat_exit_button:
    align (0.5, 0.95)
    xanchor 0.5

style chat_exit_button_text:
    size 50
    idle_color "#ffffff"
    hover_color "#ffffff"
    idle_outlines [ (11, "#0000"), (1, "#000000") ]
    hover_outlines [(4, "#cc0066"),
                    (3, "#cc0066d6"),
                    (2, "#cc0066cf"),
                    (1 ,"#cc006690"),
                ]
define lyra_chat1 = {
    "background" : "nym_day_17",
    "thumbnail" : "chat_lyra_1",
    "npc" : "Lyra",
    "0" : Msg("npc", _("I'm very hot."), "1", picture="nym_day_17_1"),
    "1" : Msg("npc", _("I need someone to cool me down."),["2a", "2b"]),
    "2a" : Msg("mc", _("On my way."), "2"),
    "2" : Msg("npc", _("{image=images/buttons/chat/e_fire.png}{image=images/buttons/chat/e_fire.png}{image=images/buttons/chat/e_fire.png}"),actions="store.nym_chat_toilet_go=True"),
    "2b" : Msg("mc", _("I think I'll pass this time."), "3"),
    "3" : Msg("npc", _("Okay, I understand. We'll be back soon."),actions="store.nym_chat_toilet_go=False"),    
    }