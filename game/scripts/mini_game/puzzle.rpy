init python:
    def solve_jigsaw():
        """
        Snap every piece into its correct location and mark them placed.
        Safe to call from the jigsaw screen action list.
        """
        try:
            # Ensure required variables exist
            gw = int(grid_width)
            gh = int(grid_height)

            for i in range(gw):
                for j in range(gh):
                    # correct position for piece (i,j)
                    correct_x = int(i * active_area_size * x_scale_index) + puzzle_field_offset
                    correct_y = int(j * active_area_size * y_scale_index) + puzzle_field_offset

                    # update the piecelist position so the piece appears in the right place
                    piecelist[i, j] = [ correct_x, correct_y ]

                    # mark it placed
                    placedlist[i, j] = True

            # Optionally play a sound
            # renpy.music.play("audio/sfx/puzzle_hit.ogg", channel="sound")

        except Exception:
            # Fail silently if called at the wrong time; nothing breaks.
            return


# define sets the values that won't be changed in game
# default sets the values that will be changed in game
default grid_width = 3
default grid_height = 3
define puzzle_field_size = (650*2)
define puzzle_field_offset = 120
define puzzle_piece_size = (450*2)
define grip_size = (75*2)
define active_area_size = puzzle_piece_size - (grip_size * 2)
image puzzle_background = "inventory/photo/puzz_imgs/bg_puzzle.jpg"
init python:    
    def piece_dragged(drags, drop):        
        if not drop:
            return     
        p_x = drags[0].drag_name.split("-")[0]
        p_y = drags[0].drag_name.split("-")[1]
        t_x = drop.drag_name.split("-")[0]
        t_y = drop.drag_name.split("-")[1]        
        a = []
        a.append(drop.drag_joined)
        a.append((drags[0], 3, 3))
        drop.drag_joined(a)
        
        if p_x == t_x and p_y == t_y:
            # comment next line if you don't need sound
            renpy.music.play("audio/sfx/puzzle_hit.ogg", channel="sound")            
            my_x = int(int(p_x)*active_area_size*x_scale_index)-int(grip_size*x_scale_index)+puzzle_field_offset
            my_y = int(int(p_y)*active_area_size*y_scale_index)-int(grip_size*y_scale_index)+puzzle_field_offset
            drags[0].snap(my_x,my_y, delay=0.1)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True

            for i in range(0, grid_width):
                for j in range(0, grid_height):
                    if placedlist[i,j] == False:
                        return
            return True
        return

    
screen jigsaw:    
    key "rollback" action [[]]
    key "rollforward" action [[]]    
    add im.Scale("inventory/photo/puzz_imgs/_puzzle_field.png", img_width, img_height) pos(puzzle_field_offset, puzzle_field_offset) 
    ##### A button that will let player quit the game (especially useful if there will be no timer to finish the game).
        
    draggroup:
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s"%(i,j)
                $ my_x = i*int(active_area_size*x_scale_index)+puzzle_field_offset
                $ my_y = j*int(active_area_size*y_scale_index)+puzzle_field_offset
                drag:
                    drag_name name
                    child im.Scale("inventory/photo/puzz_imgs/_blank_space.png", int(active_area_size*x_scale_index), int(active_area_size*y_scale_index) )
                    draggable False
                    xpos my_x ypos my_y           
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s-%s-piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    #droppable False
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]
    textbutton _("{size=+30}Quit") action Jump("quit_puzzle") xalign 0.5 ypos 10
    if cheat_minigame:
        textbutton _("{size=+30}Solve") action [ Function(solve_jigsaw), Return() ] xalign 0.3 ypos 10
label puzzle:
    #####################################################################################################
    #
    python:        
        img_width, img_height = renpy.image_size(chosen_img)       
        
        # scales down an image to fit the puzzle_field_size
        if img_width >= img_height and img_width > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_width), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)            
        elif img_height >= img_width and img_height > puzzle_field_size:
            img_scale_down_index = round( (1.00 * puzzle_field_size / img_height), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)            
        else:
            img_to_play = chosen_img        
        x_scale_index = round( (1.00 * (img_width/grid_width)/active_area_size), 6)
        y_scale_index = round( (1.00 * (img_height/grid_height)/active_area_size), 6)        
        
        mainimage = im.Composite((int(img_width+(grip_size*2)*x_scale_index), int(img_height+(grip_size*2)*y_scale_index)),(int(grip_size*x_scale_index), int(grip_size*y_scale_index)), img_to_play)
        # some calculations
        top_row = []
        for i in range (0, grid_width):
            top_row.append(i)
            
        bottom_row = []
        for i in range (0, grid_width):
            bottom_row.append(grid_width*(grid_height-1)+i)
            
        left_column = []
        for i in range (0, grid_height):
            left_column.append(grid_width*i)
            
        right_column = []
        for i in range (0, grid_height):
            right_column.append(grid_width*i + (grid_width-1) )        
        
        # randomly makes the shape of each puzzle piece
        # (starts from top row, fills it in from left to right, then - next row)
        jigsaw_grid = []
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                jigsaw_grid.append([9,9,9,9])   # [top, right, bottom, left]
                
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                if grid_width*i+j not in top_row:
                    if jigsaw_grid[grid_width*(i-1)+j][2] == 1:
                        jigsaw_grid[grid_width*i+j][0] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][0] = 1
                else:
                    jigsaw_grid[grid_width*i+j][0] = 0
                    
                if grid_width*i+j not in right_column:
                    jigsaw_grid[grid_width*i+j][1] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][1] = 0
                    
                if grid_width*i+j not in bottom_row:
                    jigsaw_grid[grid_width*i+j][2] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][2] = 0
                    
                if grid_width*i+j not in left_column:
                    if jigsaw_grid[grid_width*i+j-1][1] == 1:
                        jigsaw_grid[grid_width*i+j][3] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][3] = 1
                else:
                    jigsaw_grid[grid_width*i+j][3] = 0                    
        
        # makes description for each puzzle piece
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        testlist = dict()
        
        for i in range(0,grid_width):
            for j in range (0,grid_height):
                piecelist[i,j] = [int(renpy.random.randint(0, int(config.screen_width * 0.9 - puzzle_field_size))+puzzle_field_size), int(renpy.random.randint(0, int(config.screen_height * 0.8)))]
                
                temp_img = im.Crop(mainimage, int(i*active_area_size*x_scale_index), int(j*active_area_size*y_scale_index), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))
        
        # makes puzzle piece image using its shape description and tile pieces
        # (will rotate them to form top, right, bottom and left sides of puzzle piece)
                imagelist[i,j] = im.Composite(
        (int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("inventory/photo/puzz_imgs/_00%s.png"%(jigsaw_grid[grid_width*j+i][0]), 0, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("inventory/photo/puzz_imgs/_00%s.png"%(jigsaw_grid[grid_width*j+i][1]), 270, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("inventory/photo/puzz_imgs/_00%s.png"%(jigsaw_grid[grid_width*j+i][2]), 180, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("inventory/photo/puzz_imgs/_00%s.png"%(jigsaw_grid[grid_width*j+i][3]), 90, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)))
        )
                placedlist[i,j] = False
    #
    #####################################################################################################
    show puzzle_background as puzzle_bg
    call screen jigsaw
    jump win
    
label win:
    if chosen_img != "rooms/mc/lvl0/book_magic_3.webp":
        show black as puzzle_bg
        show expression chosen_img as win_img at truecenter with dissolve
        ""
        hide puzzle_bg
    return # end of puzzle (return to game)
label quit_puzzle:
    "Enough for now..."
    hide puzzle_bg
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