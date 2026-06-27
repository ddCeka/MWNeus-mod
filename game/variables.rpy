#Modded
default persistent.splashscreen_language = True
default persistent.splashscreen_logo = True
default persistent.splashscreen_warning = True
default persistent.ScreenMode = "Window"
default mod_version = 1.0
default phase_selected = "normal"
default incest_story = False
default persistent.gallery_incest_story = False
default persistent.gallery_pregnancy_censored = False
default friend_sister = "childhood friend"
default persistent.gallery_friend_sister = "childhood friend"
default persistent.incest_label = "Disabled"
default persistent.pregnancy_label = "Disabled"
default neus_lust_label = ""
default kitchen_room3_is_view_talk_movie = False
default customer_name = "dear ''customer''"
default persistent.gallery_customer_name = "dear ''customer''"
default date_ask = False
default menu_text = ""
define total_pages = 3
define total_secrets = 4
default sleep_blowjob = False
default sleep_action = False
default is_sex = 0
default quest_screen = "quests"
default is_change_quest_screen = False
default xsize_value = 650
default cheat_minigame = True
default endings_obtained_count = 0
define total_endings = 6
default ending_1_obtained = False
default ending_2_obtained = False
default ending_3_obtained = False
default ending_4_obtained = False
default ending_5_obtained = False
default ending_6_obtained = False

default game_settings_var = False

default selected_mode = "None"
default modes = ["Jigsaw & Fifteen", "Jigsaw", "Fifteen", "None"]

default difficulty = "Normal"
default jigsaw_difficulty = "Normal"
default fifteen_difficulty = "Normal"
default difficulties = ["Easy", "Normal", "Hard", "Expert"]


define fifteen_grid_sizes = {
    "Easy": {
        0: (2, 2),  # Stage 0 grid size for easy
        1: (2, 2),  # Stage 1 grid size for easy
        2: (2, 2),  # Stage 2 grid size for easy
        3: (2, 2),  # Stage 3 grid size for easy
        4: (3, 2),  # Stage 4 grid size for easy
    },
    "Normal": {
        0: (2, 2),  # Stage 0 grid size for easy
        1: (2, 2),  # Stage 1 grid size for easy
        2: (3, 2),  # Stage 2 grid size for easy
        3: (3, 2),  # Stage 3 grid size for easy
        4: (4, 3),  # Stage 4 grid size for easy
    },
    "Hard": {
        0: (3, 2),  # Stage 0 grid size for normal
        1: (4, 3),  # Stage 1 grid size for normal
        2: (5, 4),  # Stage 2 grid size for normal
        3: (6, 5),  # Stage 3 grid size for normal
        4: (7, 6),  # Stage 4 grid size for normal
    },
    "Expert": {
        0: (5, 4),  # Stage 0 grid size for hard
        1: (6, 5),  # Stage 1 grid size for hard
        2: (7, 6),  # Stage 2 grid size for hard
        3: (8, 7),  # Stage 3 grid size for hard
        4: (9, 8),  # Stage 4 grid size for hard
    }
}

define puzzle_grid_sizes = {
    "Easy": {
        0: (3, 2),  # Stage 0 grid size for easy
        1: (3, 2),  # Stage 1 grid size for easy
        2: (3, 2),  # Stage 2 grid size for easy
        3: (3, 2),  # Stage 3 grid size for easy
        4: (4, 3),  # Stage 4 grid size for easy
    },
    "Normal": {
        0: (3, 2),  # Stage 0 grid size for easy
        1: (3, 2),  # Stage 1 grid size for easy
        2: (4, 3),  # Stage 2 grid size for easy
        3: (4, 3),  # Stage 3 grid size for easy
        4: (5, 4),  # Stage 4 grid size for easy
    },
    "Hard": {
        0: (4, 3),  # Stage 0 grid size for normal
        1: (5, 4),  # Stage 1 grid size for normal
        2: (6, 5),  # Stage 2 grid size for normal
        3: (7, 6),  # Stage 3 grid size for normal
        4: (8, 7),  # Stage 4 grid size for normal
    },
    "Expert": {
        0: (6, 5),  # Stage 0 grid size for hard
        1: (7, 6),  # Stage 1 grid size for hard
        2: (8, 7),  # Stage 2 grid size for hard
        3: (9, 8),  # Stage 3 grid size for hard
        4: (10, 9),  # Stage 4 grid size for hard
    }
}

#Global
define available_endings=6
default time = 0
default time_name = 0
default N_state=0
#Puzzle
default view_puzzle_book = False
default is_view_tv=False
#Routine
default neus_routine = ["kitchen","living","bath","neus","neus"]
define neus_states=[_("Normal"),_("Tired"),_("Hot"),_("Pregnant")]
#P points
default neus_love_real=100
default neus_love_hide='???'
default neus_lust=0
default neus_obsession=100 
default neus_obsession_name='???:'
default is_neus_sec_dis=False 
default neus_age=22  
default days_to_final_obsession=0
default neus_is_evading=False
default set_active_pregnancy=True
default probability_of_pregnancy_init_random=50
default probability_of_pregnancy=50
default probability_of_pregnancy_bonus=0
default probability_of_pregnancy_aux=0
default probability_of_pregnancy_random=0
#Especial
default neus_title=_("Childhood friends")
#Relationship
default relationship_level=0
#spell
default secret_point=0
default pages_diary_neus=0
default photo_count=0
default outfit_photo_count=0
#Event
default kitchen_event_lvl = 0
default bath_event_lvl = 0
default living_event_lvl = 0
default neus_event_lvl = 0
default mc_event_lvl = 0
default is_change_quest = False
default is_change_tree_skill=True
#Event State
default is_touch=0
default is_kiss=0
default is_peek=0
default is_handjob=0
default is_titjob=0
default is_footjob=0
default is_blowjob=0
default is_sexpussy=0
default is_sexanal=0
default is_wake_up_neus=False
default tiredness_level=0
#Event lvl
default lvl_event_date_sr=0
default lvl_event_fear=0
default lvl_event_fear_aux=0
default lvl_neus3_out_event_anal=0
#Photo
default select_photo = ""
#Steam
define is_steam_version=False
init python:
    achievement.register("Attic") # Enter the attic
    achievement.register("Girlfriend") # neus is girlfriend (end of level 2, after first sex)
    achievement.register("Secret") # Confront neus about secret
    achievement.register("Another_Personality") # Two bodies phase unlocked
    achievement.register("Another_Personality_Again") # Nymphomania phase unlocked
    achievement.register("Only_One") # Milf phase unlocked

    # Endings
    achievement.register("Normal_Ending") # normal ending
    achievement.register("True_Ending_1") # Milf ending
    achievement.register("True_Ending_2") # Two bodies ending
    achievement.register("End") # Nymphomania ending
    
    achievement.register("Obsession_Ending") # 2nd personality ending
    achievement.register("No_Escape") # 2nd personality non consenting ending 