#transform
transform Brightness0_2_a:
    easeout  0.4 matrixcolor BrightnessMatrix(0.2)
transform gray_blur15:
    blur 15.0
    matrixcolor SaturationMatrix(0)
transform gray_blur5:
    blur 7.0
    matrixcolor SaturationMatrix(0)
transform blur2:
    blur 2.0    

transform red_zoom1: 
    matrixcolor TintMatrix("#ffffff")
    zoom 1.0 
    parallel:  
        linear 3.0 matrixcolor TintMatrix("#ff0000")    
    parallel:
        linear 3.0 zoom 1.2 
transform red_zoom2: 
    xalign 0.5
    yalign 0.5
    matrixcolor TintMatrix("#ffffff")
    zoom 1.0 
    parallel:  
        linear 3.0 matrixcolor TintMatrix("#ff0000")    
    parallel:
        linear 3.0 zoom 1.2   
transform zoom_moven1: 
    zoom 1.6
    yalign 0.5 
    xalign 0.5    
    linear 2.5 yalign 0.1
    parallel:        
        linear 1.0 xalign 0.5
    parallel:
        linear 1.0 zoom 1.0
        

transform Brightness0_a:
    easeout  0.4 matrixcolor BrightnessMatrix(0)
transform Brightness0:
    matrixcolor BrightnessMatrix(0)
transform gray_scale: # smooth transition to grayscale
    matrixcolor SaturationMatrix(0)   
transform rotate_15: # rotate 15 degrees
    ycenter 0.5
    xcenter 0.5
    zoom 0.95
    rotate 15.0
transform rotate_15_degrees : # rotate -15 degrees
    ycenter 0.5
    xcenter 0.5
    zoom 0.95
    rotate -15.0
transform zoom_1_5:
    zoom 1.5   
transform zoom_animation:
    xalign 0.5
    yalign 0.5
    parallel:
        linear 0.5 zoom 1.5
    parallel:
        linear 0.5 blur 6.0  
    

#animation
transform text_animation_alpha:
    parallel:
        linear 0.4 alpha 0.8
        linear 0.4 alpha 1.0
        repeat
    parallel:        
        ease 0.4 yzoom 1.035        
        ease 0.4 yzoom 1.0
        repeat
transform event_animation_ending:
    parallel:        
        ease 0.4 yzoom 1.035        
        ease 0.4 yzoom 1.0
        repeat
    parallel:
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0.85        
        repeat
transform event_animation_page:
    parallel:        
        ease 0.4 yzoom 1.0015       
        ease 0.4 yzoom 1.0
        repeat
    parallel:
        linear 0.4 alpha 1.0
        linear 0.4 alpha 0.85        
        repeat   
transform PopUpFade:   
    on show:        
        xalign 1.2     
        linear 0.35 xalign 1.0
    on hide:
        linear .5 alpha 0.0
transform ctc_animation:
    parallel:
        alpha .5
        linear 1.0 alpha .9
        linear 1.0 alpha .5
        repeat
    parallel:
        linear 0.3 yoffset 0
        linear 0.3 yoffset 10
        linear 0.3 yoffset 0
        linear 0.3 yoffset -10
        repeat

style lust_style:
    color gui.accent_color   
    
transform parallax():
    perspective True
    subpixel True
    function moving_camera