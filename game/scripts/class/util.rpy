init python:
    def unlock_gallery():
        for i in range(0,len(nameByIDscene_main_quest)):
            renpy.mark_label_seen(nameByIDscene_main_quest[i][1])     
    def moving_camera(trans, st, at):
        x, y = renpy.display.draw.get_mouse_pos()
        trans.xoffset = (x - config.screen_width / 2) * .05
        trans.yoffset = (y - config.screen_height / 2) * .05
        return 0          
    
    