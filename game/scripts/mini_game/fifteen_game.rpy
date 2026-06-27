init -1 python:  # negative priority ensures it runs after basic Ren'Py modules
    def solve_fifteen():
        """
        Put every tile into its solved position and mark the puzzle solved.
        Safe to call from the screen action list for any fifteen puzzle instance.
        """
        try:
            # tiles_list is created by the running puzzle; mutate it into solved state.
            for t in tiles_list:
                t["tile_value"] = t["tile_number"] + 1

            # Mark solved in the Ren'Py store so screen/labels pick it up immediately.
            fifteen_is_solved = True

        except Exception:
            # Fail silently if tiles_list / variables aren't present.
            return


##### The game screen.
screen fifteen_scr:
    
    ##### Timer.
    if timer_on:
        timer 1.0 action If(fifteen_timer > 0, [SetVariable("fifteen_timer", fifteen_timer-1), Return("smth")], Return("time_is_up") ) repeat True
        text "{size=+30}"+ str(fifteen_timer) xalign 0.1 ypos 30
    
    ##### Game field.
    frame:
        xalign 0.5 yalign 0.5
        background Solid("#ccc")
        grid grid_width grid_height spacing 0:
            for every_tile in tiles_list:
                if every_tile["tile_value"] == empty_tile_value and not fifteen_is_solved:
                    null
                else:
                    button:                       
                        left_padding 0 right_padding 0 top_padding 0 bottom_padding 0
                        left_margin 0 right_margin 0 top_margin 0 bottom_margin 0
                        add im.Crop(chosen_img,((every_tile["tile_value"]-1)%grid_width*tile_width,
                                        (every_tile["tile_value"]-1)//grid_width*tile_height,
                                        tile_width,
                                        tile_height))
                        #
                        #####               
                        action [ If (every_tile["tile_number"] not in top_row,
                                    true = If(tiles_list[every_tile["tile_number"]-grid_width]["tile_value"] == empty_tile_value,
                                        true = [SetDict( tiles_list[every_tile["tile_number"]-grid_width], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                        false = None),
                                    false = None),
                                    If (every_tile["tile_number"] not in bottom_row,
                                    true = If (tiles_list[min(len(tiles_list)-1, every_tile["tile_number"]+grid_width)]["tile_value"] == empty_tile_value,
                                        true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+grid_width))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                        false = None),
                                    false = None),
                                    If (every_tile["tile_number"] not in left_column,
                                    true = If (tiles_list[every_tile["tile_number"]-1]["tile_value"] == empty_tile_value,
                                        true = [SetDict(tiles_list[every_tile["tile_number"]-1], "tile_value", every_tile["tile_value"]),SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                        false = None),
                                    false = None),
                                    If (every_tile["tile_number"] not in right_column,
                                    true = If (tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))]["tile_value"] == empty_tile_value,
                                        true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                        false = None),
                                    false = None), Return("smth")
                                ]

    ##### A button that will let player quit the game (especially useful if there will be no timer to finish the game).
    if not fifteen_is_solved:
        textbutton _("{size=+30}Shuffle") action Jump("shuffle_tiles") xalign 0.1 ypos 10
    if cheat_minigame:
        textbutton _("{size=+30}Solve") action [ Function(solve_fifteen), Return("smth") ] xalign 0.75 ypos 10
    textbutton _("{size=+30}Quit") action Jump("quit_fifteen_game") xalign 0.9 ypos 10
    
    ##### A button that will show the whole image, should be used only if game uses images (not numbers).
    textbutton _("{size=+30}Show/hide image") action If(renpy.get_screen("full_image"), Hide("full_image"), Show("full_image") ) xalign 0.5 ypos 10

label shuffle_tiles:
    $ shuffle_moves = grid_width * grid_height * int((grid_width + grid_height) * 1.00)
    jump tiles_shuffle


##### Screen that contains an image to show (not useful in classic fifteen game).
#

screen full_image:
    if chosen_img != "rooms/mc/lvl0/book_magic_3.webp":
        add chosen_img xalign 0.5 yalign 0.5 at pic_trans
    else:
        add chosen_img xalign 0.5 yalign 0.5 at fade_in

transform pic_trans:
    alpha 0.0 zoom 0.7
    on show:
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 0.6 zoom 1.2
            linear 0.4 zoom 1.0
    on hide:
        linear 0.5 alpha 0.0
        
transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0
    
#
#####


label fifteen_game:    
    # Next 4 lines are used to set an image to solve (could be deleted for clasic fifteen game).
    # It is recommended that all images will be smaller than screen size.
    $ chosen_img = im.Scale(chosen_img, 1500, 844)
    $ chosen_img_width= 1500
    $ chosen_img_height = 844
    $ tile_width = chosen_img_width/grid_width
    $ tile_height = chosen_img_height/grid_height
    #

    # Some useful calculations:
    $ top_row = []
    python:
        for i in range(0, grid_width):
            top_row.append(i)
    $ bottom_row = []
    python:
        for i in range(0, grid_width):
            bottom_row.append((grid_width*(grid_height-1)+i))
    $ left_column = []
    python:
        for i in range(0, grid_height):
            left_column.append(grid_width*i)
    $ right_column = []
    python:
        for i in range(0, grid_height):
            right_column.append(grid_width*(i+1)-1)

    
    # Let's set the game field - all the tiles are on their places.
    $ tiles_list = []
    python:
        for i in range (0, grid_height):
            for j in range (0, grid_width):
                tiles_list.append({"tile_number":(i*grid_width+j),"tile_value":(i*grid_width+(j+1))})
    $ empty_tile_value = grid_width*grid_height    
    # Some variables:
    # will let us control if the missed tile should be shown
    $ fifteen_is_solved = False
    # sets the timer to make game more difficult
    $ fifteen_timer = 100
    # will let us control the timer
    $ timer_on = False
    
    # This will show the game screen.
    show screen fifteen_scr 

    $ shuffle_moves = grid_width * grid_height * int((grid_width + grid_height) * 1.00)
    label tiles_shuffle:
        if shuffle_moves >0:
            python:
                possible_moves_list = []
                for j in tiles_list:
                    if j["tile_value"] == empty_tile_value:
                        if j["tile_number"] not in top_row:
                            possible_moves_list.append("top")
                        if j["tile_number"] not in bottom_row:
                            possible_moves_list.append("bottom")
                        if j["tile_number"] not in left_column:
                            possible_moves_list.append("left")
                        if j["tile_number"] not in right_column:
                            possible_moves_list.append("right")
                        move_tile = renpy.random.choice(possible_moves_list)
                        if move_tile == "top":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-grid_width]["tile_value"]
                            tiles_list[j["tile_number"]-grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "bottom":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+grid_width]["tile_value"]
                            tiles_list[j["tile_number"]+grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "left":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-1]["tile_value"]
                            tiles_list[j["tile_number"]-1]["tile_value"] = empty_tile_value
                        elif move_tile == "right":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+1]["tile_value"]
                            tiles_list[j["tile_number"]+1]["tile_value"] = empty_tile_value
                        shuffle_moves -= 1
                        #renpy.pause(0.1)           # If used pause should be not so long.
                        renpy.jump("tiles_shuffle")
                
    # Now we can start the timer.
    $ timer_on = False
    
    # The game loop.
    label fifteen_game_loop:
        $ result = ui.interact()
        $ fifteen_timer = fifteen_timer
        if result == "time_is_up":
            jump fifteen_lose
        python:
            for j in tiles_list:
                if j["tile_value"]-1 != j["tile_number"]: # will continue the game if at least one tile is not in its place
                    renpy.jump("fifteen_game_loop")
        jump fifteen_win

label fifteen_win:
    # This will turn off the timer.
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)
    
    # This will show the missed tile in its place.
    $ fifteen_is_solved = True    
    ""
    hide screen fifteen_scr
    hide screen full_image
    return

label fifteen_lose:
    $ timer_on = False
    $ renpy.pause(0.1, hard = True)
    $ renpy.pause(0.1, hard = True)
    "To slow... Try again."
    hide screen fifteen_scr
    jump fifteen_game

label quit_fifteen_game:
    hide screen fifteen_scr
    hide screen full_image
    "Enough for now..."
    if phase_selected == "normal":
        jump rooms
    elif phase_selected == "milf":
        jump milf_rooms
    elif phase_selected == "two_bodies":
        jump two_bodies_rooms
    elif phase_selected == "nym":
        jump nym_rooms
    else:
        jump rooms