
image CLLGames = Movie(play="images/animation/CLLGames.webm",loop=False)
image main_menu_b = ConditionSwitch(
         "persistent.main_menu_b==0", Movie(play="gui/main_menu0.webm",loop=True),
         "persistent.main_menu_b==1", "gui/main_menu1.webp",
         "persistent.main_menu_b==2", "gui/main_menu2.webp",
         "persistent.main_menu_b==3", Movie(play="gui/main_menu3.webm",loop=True),
         "persistent.main_menu_b==4", Movie(play="gui/main_menu4.webm",loop=True),
         "persistent.main_menu_b==5", "gui/main_menu5.webp",
         "persistent.main_menu_b==6", "gui/main_menu6.webp",)
#Story
image level0_2_17 = Movie(play="images/animation/level0_2_17.webm",start_image="images/animation/start_image/level0_2_17.webp")
image level0_2_19 = Movie(play="images/animation/level0_2_19.webm",start_image="images/animation/start_image/level0_2_17.webp")
#Level 1
image level1_1_11 = Movie(play="images/animation/level1_1_11.webm",start_image="images/animation/start_image/level1_1_11.webp")
image level1_1_12 = Movie(play="images/animation/level1_1_12.webm",start_image="images/animation/start_image/level1_1_11.webp")
image level1_1_13 = Movie(play="images/animation/level1_1_13.webm",start_image="images/animation/start_image/level1_1_13.webp")
image level1_2_14 = Movie(play="images/animation/level1_2_14.webm",start_image="images/animation/start_image/level1_2_14.webp")
image level1_2_17 = Movie(play="images/animation/level1_2_17.webm",start_image="images/animation/start_image/level1_2_17.webp")
image level1_3_11 = Movie(play="images/animation/level1_3_11.webm",start_image="images/animation/start_image/level1_3_11.webp")
image level1_3_15 = Movie(play="images/animation/level1_3_15.webm",start_image="images/animation/start_image/level1_3_15_0.webp",
loop=False, image="images/animation/start_image/level1_3_15_1.webp")
image level1_3_17 = Movie(play="images/animation/level1_3_17.webm",start_image="images/animation/start_image/level1_3_17.webp")
image level1_3_18 = Movie(play="images/animation/level1_3_18.webm",start_image="images/animation/start_image/level1_3_18.webp")
#Level 2
image level2_0_16 = Movie(play="images/animation/level2_0_16.webm",start_image="images/animation/start_image/level2_0_16_0.webp",
loop=False, image="images/animation/start_image/level2_0_16_1.webp")
image level2_0_18 = Movie(play="images/animation/level2_0_18.webm",start_image="images/animation/start_image/level2_0_18.webp")
image level2_0_20 = Movie(play="images/animation/level2_0_20.webm",start_image="images/animation/start_image/level2_0_20.webp")
image level2_2_10 = Movie(play="images/animation/level2_2_10.webm",start_image="images/animation/start_image/level2_2_10.webp")
image level2_2_11 = Movie(play="images/animation/level2_2_11.webm",start_image="images/animation/start_image/level2_2_11.webp")
image level2_2_23 = Movie(play="images/animation/level2_2_23.webm",start_image="images/animation/start_image/level2_2_23.webp")
image level2_2_26 = Movie(play="images/animation/level2_2_26.webm",start_image="images/animation/start_image/level2_2_26.webp")
image level2_2_31 = Movie(play="images/animation/level2_2_31.webm",start_image="images/animation/start_image/level2_2_31.webp")

image level2_2_49 = Movie(play="images/animation/level2_2_49.webm",start_image="images/animation/start_image/level2_2_49.webp")
image level2_2_51 = Movie(play="images/animation/level2_2_51.webm",start_image="images/animation/start_image/level2_2_51_0.webp",
loop=False, image="images/animation/start_image/level2_2_51_1.webp")
image level2_2_52 = Movie(play="images/animation/level2_2_52.webm",start_image="images/animation/start_image/level2_2_52.webp")
image level2_2_54 = Movie(play="images/animation/level2_2_54.webm",start_image="images/animation/start_image/level2_2_54.webp")
image level2_2_55 = Movie(play="images/animation/level2_2_55.webm",start_image="images/animation/start_image/level2_2_55_0.webp",
loop=False, image="images/animation/start_image/level2_2_55_1.webp")
image level2_2_58 = Movie(play="images/animation/level2_2_58.webm",start_image="images/animation/start_image/level2_2_58.webp")
#Level 3
image level3_0_47 = Movie(play="images/animation/level3_0_47.webm",start_image="images/animation/start_image/level3_0_47.webp")
image level3_0_68 = Movie(play="images/animation/level3_0_68.webm",start_image="images/animation/start_image/level3_0_68.webp")
image level3_0_71 = Movie(play="images/animation/level3_0_71.webm",start_image="images/animation/start_image/level3_0_71.webp")
image level3_0_73 = Movie(play="images/animation/level3_0_73.webm",start_image="images/animation/start_image/level3_0_73.webp")
image level3_0_78 = Movie(play="images/animation/level3_0_78.webm",start_image="images/animation/start_image/level3_0_78.webp")
image level3_0_79 = Movie(play="images/animation/level3_0_79.webm",start_image="images/animation/start_image/level3_0_79_0.webp",
loop=False, image="images/animation/start_image/level3_0_79_1.webp")
image level3_0_80 = Movie(play="images/animation/level3_0_80.webm",start_image="images/animation/start_image/level3_0_79_0.webp")
image level3_0_89 = Movie(play="images/animation/level3_0_89.webm",start_image="images/animation/start_image/level3_0_89.webp")
image level3_0_91 = Movie(play="images/animation/level3_0_91.webm",start_image="images/animation/start_image/level3_0_91_0.webp",
loop=False, image="images/animation/start_image/level3_0_91_1.webp")
image level3_0_92 = Movie(play="images/animation/level3_0_92.webm",start_image="images/animation/start_image/level3_0_91_0.webp")
image level3_0_101 = Movie(play="images/animation/level3_0_101.webm",start_image="images/animation/start_image/level3_0_101.webp")
image level3_0_102_1 = Movie(play="images/animation/level3_0_102_1.webm",start_image="images/animation/start_image/level3_0_102_1.webp")
image level3_0_118 = Movie(play="images/animation/level3_0_118.webm",start_image="images/animation/start_image/level3_0_118.webp")
image level3_0_127 = Movie(play="images/animation/level3_0_127.webm",start_image="images/animation/start_image/level3_0_127.webp")
image level3_0_135 = Movie(play="images/animation/level3_0_135.webm",start_image="images/animation/start_image/level3_0_135.webp")

image level3_0_161 = Movie(play="images/animation/level3_0_161.webm",start_image="images/animation/start_image/level3_0_161_0.webp",
loop=False, image="images/animation/start_image/level3_0_161_1.webp")
image level3_0_163 = Movie(play="images/animation/level3_0_163.webm",start_image="images/animation/start_image/level3_0_163.webp")
image level3_0_164 = Movie(play="images/animation/level3_0_164.webm",start_image="images/animation/start_image/level3_0_164.webp")
image level3_0_172 = Movie(play="images/animation/level3_0_172.webm",start_image="images/animation/start_image/level3_0_172.webp")

#Endings 1
image end_nor1_27 = Movie(play="images/animation/end_nor1_27.webm",start_image="images/animation/start_image/end_nor1_27.webp")
#Endings 2
image end_obs1_6 = Movie(play="images/animation/end_obs1_6.webm",start_image="images/animation/start_image/end_obs1_6.webp")
image end_obs1_9 = Movie(play="images/animation/end_obs1_9.webm",start_image="images/animation/start_image/end_obs1_9_0.webp",
loop=False, image="images/animation/start_image/end_obs1_9_1.webp")
image end_obs1_10 = Movie(play="images/animation/end_obs1_10.webm",start_image="images/animation/start_image/end_obs1_10.webp")
image end_obs1_11 = Movie(play="images/animation/end_obs1_11.webm",start_image="images/animation/start_image/end_obs1_11.webp")
image end_obs1_12 = Movie(play="images/animation/end_obs1_12.webm",start_image="images/animation/start_image/end_obs1_12.webp")
image end_obs1_28 = Movie(play="images/animation/end_obs1_28.webm",start_image="images/animation/start_image/end_obs1_28.webp")
#Endings 3
image end_obs2_6 = Movie(play="images/animation/end_obs2_6.webm",start_image="images/animation/start_image/end_obs2_6.webp")
image end_obs2_7 = Movie(play="images/animation/end_obs2_7.webm",start_image="images/animation/start_image/end_obs2_7.webp")
image end_obs2_8 = Movie(play="images/animation/end_obs2_8.webm",start_image="images/animation/start_image/end_obs2_8.webp")
#event room
#Kitchen
image kitchen1_26 = Movie(play="images/animation/kitchen1_26.webm",start_image="images/animation/start_image/kitchen1_26.webp")
image kitchen2_1_intro1 = Movie(play="images/animation/kitchen2_1_intro1.webm",start_image="images/animation/start_image/kitchen2_1_intro1.webp")
image kitchen2_1_intro3 = Movie(play="images/animation/kitchen2_1_intro3.webm",start_image="images/animation/start_image/kitchen2_1_intro3.webp")
image kitchen2_1_intro9 = Movie(play="images/animation/kitchen2_1_intro9.webm",start_image="images/animation/start_image/kitchen2_1_intro9.webp")
image kitchen2_8 = Movie(play="images/animation/kitchen2_8.webm",start_image="images/animation/start_image/kitchen2_8.webp")
image kitchen2_22 = Movie(play="images/animation/kitchen2_22.webm",start_image="images/animation/start_image/kitchen2_22.webp")
image kitchen2_29 = Movie(play="images/animation/kitchen2_29.webm",start_image="images/animation/start_image/kitchen2_29.webp")
image kitchen2_33 = Movie(play="images/animation/kitchen2_33.webm",start_image="images/animation/start_image/kitchen2_33.webp")
image kitchen2_39 = Movie(play="images/animation/kitchen2_39.webm",start_image="images/animation/start_image/kitchen2_39.webp")
image kitchen2_43 = Movie(play="images/animation/kitchen2_43.webm",start_image="images/animation/start_image/kitchen2_43.webp")
image kitchen3_b_9 = Movie(play="images/animation/kitchen3_b_9.webm",start_image="images/animation/start_image/kitchen3_b_9.webp")
image kitchen3_b_10 = Movie(play="images/animation/kitchen3_b_10.webm",start_image="images/animation/start_image/kitchen3_b_10.webp")
image kitchen3_out1_5 = Movie(play="images/animation/kitchen3_out1_5.webm",start_image="images/animation/start_image/kitchen3_out1_5.webp")
image kitchen3_out1_in_6 = Movie(play="images/animation/kitchen3_out1_in_6.webm",start_image="images/animation/start_image/kitchen3_out1_in_6.webp")
image kitchen3_out1_in_8 = Movie(play="images/animation/kitchen3_out1_in_8.webm",start_image="images/animation/start_image/kitchen3_out1_in_8_0.webp",
loop=False, image="images/animation/start_image/kitchen3_out1_in_8_1.webp")
image kitchen3_out1_in_9 = Movie(play="images/animation/kitchen3_out1_in_9.webm",start_image="images/animation/start_image/kitchen3_out1_in_8_0.webp")
image kitchen3_out1_16 = Movie(play="images/animation/kitchen3_out1_16.webm",start_image="images/animation/start_image/kitchen3_out1_16.webp")
image kitchen3_3 = Movie(play="images/animation/kitchen3_3.webm",start_image="images/animation/start_image/kitchen3_3.webp")
image kitchen3_11 = Movie(play="images/animation/kitchen3_11.webm",start_image="images/animation/start_image/kitchen3_11.webp")
image kitchen3_12 = Movie(play="images/animation/kitchen3_12.webm",start_image="images/animation/start_image/kitchen3_12.webp")
image kitchen3_out2_7 = Movie(play="images/animation/kitchen3_out2_7.webm",start_image="images/animation/start_image/kitchen3_out2_7.webp")
image kitchen3_out2_13 = Movie(play="images/animation/kitchen3_out2_13.webm",start_image="images/animation/start_image/kitchen3_out2_13.webp")
image kitchen3_out2_30 = Movie(play="images/animation/kitchen3_out2_30.webm",start_image="images/animation/start_image/kitchen3_out2_30.webp")
image kitchen3_out2_40 = Movie(play="images/animation/kitchen3_out2_40.webm",start_image="images/animation/start_image/kitchen3_out2_40.webp")
image kitchen3_t_29 = Movie(play="images/animation/kitchen3_t_29.webm",start_image="images/animation/start_image/kitchen3_t_29.webp")
image kitchen3_t_46 = Movie(play="images/animation/kitchen3_t_46.webm",start_image="images/animation/start_image/kitchen3_t_46.webp")
image kitchen3_t_48 = Movie(play="images/animation/kitchen3_t_48.webm",start_image="images/animation/start_image/kitchen3_t_48.webp")
image kitchen3_t_51 = Movie(play="images/animation/kitchen3_t_51.webm",start_image="images/animation/start_image/kitchen3_t_51.webp")
#Living room
image living1_10 = Movie(play="images/animation/living1_10.webm",start_image="images/animation/start_image/living1_10.webp")
image living1_25 = Movie(play="images/animation/living1_25.webm",start_image="images/animation/start_image/living1_25.webp")
image living2_10 = Movie(play="images/animation/living2_10.webm",start_image="images/animation/start_image/living2_10.webp")
image living2_24 = Movie(play="images/animation/living2_24.webm",start_image="images/animation/start_image/living2_24.webp")
image living2_25 = Movie(play="images/animation/living2_25.webm",start_image="images/animation/start_image/living2_25.webp")
image living2_26 = Movie(play="images/animation/living2_26.webm",start_image="images/animation/start_image/living2_26.webp")
image living2_32 = Movie(play="images/animation/living2_32.webm",start_image="images/animation/start_image/living2_32.webp")
image living2_38 = Movie(play="images/animation/living2_38.webm",start_image="images/animation/start_image/living2_38.webp")
image living2_42 = Movie(play="images/animation/living2_42.webm",start_image="images/animation/start_image/living2_42.webp")
image living3_t_21 = Movie(play="images/animation/living3_t_21.webm",start_image="images/animation/start_image/living3_t_21.webp")
image living_room3_out1_6 = Movie(play="images/animation/living_room3_out1_6.webm",start_image="images/animation/start_image/living_room3_out1_6.webp")
image living3_11 = Movie(play="images/animation/living3_11.webm",start_image="images/animation/start_image/living3_11.webp")
image living_room3_out1_17 = Movie(play="images/animation/living_room3_out1_17.webm",start_image="images/animation/start_image/living_room3_out1_17.webp")
image living3_20 = Movie(play="images/animation/living3_20.webm",start_image="images/animation/start_image/living3_20.webp")
image living3_29 = Movie(play="images/animation/living3_29.webm",start_image="images/animation/start_image/living3_29.webp")
image living_room3_out2_10 = Movie(play="images/animation/living_room3_out2_10.webm",start_image="images/animation/start_image/living_room3_out2_10.webp")
image living_room3_out2_18 = Movie(play="images/animation/living_room3_out2_18.webm",start_image="images/animation/start_image/living_room3_out2_18.webp")
image living_room3_out2_19 = Movie(play="images/animation/living_room3_out2_19.webm",start_image="images/animation/start_image/living_room3_out2_18.webp")
#Bathroom
image bath2_1 = Movie(play="images/animation/bath2_1.webm",start_image="images/animation/start_image/bath2_1.webp")
image bath2_7 = Movie(play="images/animation/bath2_7.webm",start_image="images/animation/start_image/bath2_7.webp")
image bath2_14_0 = Movie(play="images/animation/bath2_14_0.webm",start_image="images/animation/start_image/bath2_14_0.webp")
image bath2_14_1 = Movie(play="images/animation/bath2_14_1.webm",start_image="images/animation/start_image/bath2_14_1.webp")
image bath3_1 = Movie(play="images/animation/bath3_1.webm",start_image="images/animation/start_image/bath3_1.webp")
image bath3_1 = Movie(play="images/animation/bath3_1.webm",start_image="images/animation/start_image/bath3_1.webp")
image bath3_9 = Movie(play="images/animation/bath3_9.webm",start_image="images/animation/start_image/bath3_9.webp")
image bath3_10 = Movie(play="images/animation/bath3_10.webm",start_image="images/animation/start_image/bath3_10_0.webp",
loop=False, image="images/animation/start_image/bath3_10_1.webp")
image bath3_11 = Movie(play="images/animation/bath3_11.webm",start_image="images/animation/start_image/bath3_10_0.webp")
image bath3_21 = Movie(play="images/animation/bath3_21.webm",start_image="images/animation/start_image/bath3_21.webp")
image bath3_30 = Movie(play="images/animation/bath3_30.webm",start_image="images/animation/start_image/bath3_30.webp")
image bath3_31 = Movie(play="images/animation/bath3_31.webm",start_image="images/animation/start_image/bath3_31_0.webp",
loop=False, image="images/animation/start_image/bath3_31_1.webp")
image bath3_32 = Movie(play="images/animation/bath3_32.webm",start_image="images/animation/start_image/bath3_31_0.webp")
#Neus
image neus1_17 = Movie(play="images/animation/neus1_17.webm",start_image="images/animation/start_image/neus1_17.webp")
image neus1_28 = Movie(play="images/animation/neus1_28.webm",start_image="images/animation/start_image/neus1_28.webp")
image neus1_33 = Movie(play="images/animation/neus1_33.webm",start_image="images/animation/start_image/neus1_33.webp")
image neus2_13 = Movie(play="images/animation/neus2_13.webm",start_image="images/animation/start_image/neus2_13.webp")
image neus2_18 = Movie(play="images/animation/neus2_18.webm",start_image="images/animation/start_image/neus2_18.webp")
image neus2_28 = Movie(play="images/animation/neus2_28.webm",start_image="images/animation/start_image/neus2_28.webp")
image neus2_35 = Movie(play="images/animation/neus2_35.webm",start_image="images/animation/start_image/neus2_35.webp")
image neus2_43 = Movie(play="images/animation/neus2_43.webm",start_image="images/animation/start_image/neus2_43.webp")
image neus2_55 = Movie(play="images/animation/neus2_55.webm",start_image="images/animation/start_image/neus2_55.webp")
image neus2_58 = Movie(play="images/animation/neus2_58.webm",start_image="images/animation/start_image/neus2_58.webp")
image neus2_60 = Movie(play="images/animation/neus2_60.webm",start_image="images/animation/start_image/neus2_60.webp")
image neus2_64 = Movie(play="images/animation/neus2_64.webm",start_image="images/animation/start_image/neus2_64.webp")
image neus2_66 = Movie(play="images/animation/neus2_66.webm",start_image="images/animation/start_image/neus2_66.webp")
image neus3_er_23 = Movie(play="images/animation/neus3_er_23.webm",start_image="images/animation/start_image/neus3_er_23.webp")
image neus3_er_29 = Movie(play="images/animation/neus3_er_29.webm",start_image="images/animation/start_image/neus3_er_29.webp")
image neus3_er_35 = Movie(play="images/animation/neus3_er_35.webm",start_image="images/animation/start_image/neus3_er_35.webp")
image neus3_er2_0 = Movie(play="images/animation/neus3_er2_0.webm",start_image="images/animation/start_image/neus3_er2_0.webp")
image neus3_out1_5 = Movie(play="images/animation/neus3_out1_5.webm",start_image="images/animation/start_image/neus3_out1_5.webp")
image neus3_out1_15 = Movie(play="images/animation/neus3_out1_15.webm",start_image="images/animation/start_image/neus3_out1_15.webp")
image neus3_out1_20 = Movie(play="images/animation/neus3_out1_20.webm",start_image="images/animation/start_image/neus3_out1_20.webp")
image neus3_out2_7 = Movie(play="images/animation/neus3_out2_7.webm",start_image="images/animation/start_image/neus3_out2_7.webp")
image neus3_out2_13 = Movie(play="images/animation/neus3_out2_13.webm",start_image="images/animation/start_image/neus3_out2_13.webp")
image neus3_out2_15 = Movie(play="images/animation/neus3_out2_15.webm",start_image="images/animation/start_image/neus3_out2_15.webp")

image neus3_7 = Movie(play="images/animation/neus3_7.webm",start_image="images/animation/start_image/neus3_7.webp")
image neus3_8 = Movie(play="images/animation/neus3_8.webm",start_image="images/animation/start_image/neus3_8.webp")
image neus3_15 = Movie(play="images/animation/neus3_15.webm",start_image="images/animation/start_image/neus3_15.webp")
image neus3_24 = Movie(play="images/animation/neus3_24.webm",start_image="images/animation/start_image/neus3_24.webp")
image neus3_night9 = Movie(play="images/animation/neus3_night9.webm",start_image="images/animation/start_image/neus3_night9.webp")
image neus3_night29 = Movie(play="images/animation/neus3_night29.webm",start_image="images/animation/start_image/neus3_night29.webp")
image neus3_sleep6 = Movie(play="images/animation/neus3_sleep6.webm",start_image="images/animation/start_image/neus3_sleep6.webp")
#mc
image mc3_w_5 = Movie(play="images/animation/mc3_w_5.webm",start_image="images/animation/start_image/mc3_w_5.webp")
image mc3_w_6 = Movie(play="images/animation/mc3_w_6.webm",start_image="images/animation/start_image/mc3_w_5.webp")
image mc3_f_13 = Movie(play="images/animation/mc3_f_13.webm",start_image="images/animation/start_image/mc3_f_13.webp")
image mc3_f_25 = Movie(play="images/animation/mc3_f_25.webm",start_image="images/animation/start_image/mc3_f_25.webp")
#TB
image tb_p3_27 = Movie(play="images/animation/tb_p3_27.webm",start_image="images/animation/start_image/tb_p3_27.webp")
image tb_p3_31 = Movie(play="images/animation/tb_p3_31.webm",start_image="images/animation/start_image/tb_p3_31.webp")
image tb_p3_34 = Movie(play="images/animation/tb_p3_34.webm",start_image="images/animation/start_image/tb_p3_34.webp")
image tb_p3_37 = Movie(play="images/animation/tb_p3_37.webm",start_image="images/animation/start_image/tb_p3_37.webp")
image tb_p3_61 = Movie(play="images/animation/tb_p3_61.webm",start_image="images/animation/start_image/tb_p3_61.webp")
image tb_p3_62 = Movie(play="images/animation/tb_p3_62.webm",start_image="images/animation/start_image/tb_p3_62.webp")
image tb_p3_68 = Movie(play="images/animation/tb_p3_68.webm",start_image="images/animation/start_image/tb_p3_68.webp")
image tb_p3_69 = Movie(play="images/animation/tb_p3_69.webm",start_image="images/animation/start_image/tb_p3_69.webp")
image tb_p3_98 = Movie(play="images/animation/tb_p3_98.webm",start_image="images/animation/start_image/tb_p3_98.webp")
image tb_p3_101 = Movie(play="images/animation/tb_p3_101.webm",start_image="images/animation/start_image/tb_p3_101.webp")
image tb_p3_103 = Movie(play="images/animation/tb_p3_103.webm",start_image="images/animation/start_image/tb_p3_103.webp")

image two_bodies_kitchen0_12 = Movie(play="images/animation/two_bodies_kitchen0_12.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_12.webp")
image two_bodies_kitchen0_20 = Movie(play="images/animation/two_bodies_kitchen0_20.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_20.webp")
image two_bodies_kitchen0_26 = Movie(play="images/animation/two_bodies_kitchen0_26.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_26.webp")
image two_bodies_kitchen0_27 = Movie(play="images/animation/two_bodies_kitchen0_27.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_27.webp")
image two_bodies_kitchen0_32 = Movie(play="images/animation/two_bodies_kitchen0_32.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_32.webp")
image two_bodies_kitchen0_35 = Movie(play="images/animation/two_bodies_kitchen0_35.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_35.webp")
image two_bodies_kitchen0_41 = Movie(play="images/animation/two_bodies_kitchen0_41.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_41.webp")
image two_bodies_kitchen0_44 = Movie(play="images/animation/two_bodies_kitchen0_44.webm",
                                    start_image="images/animation/start_image/two_bodies_kitchen0_44.webp")
image tb_kitchen_pregnant2_10 = Movie(play="images/animation/tb_kitchen_pregnant2_10.webm",
                                    start_image="images/animation/start_image/tb_kitchen_pregnant2_10.webp")     
image tb_kitchen_pregnant2_14 = Movie(play="images/animation/tb_kitchen_pregnant2_14.webm",
                                    start_image="images/animation/start_image/tb_kitchen_pregnant2_14.webp")
image tb_kitchen_pregnant2_19 = Movie(play="images/animation/tb_kitchen_pregnant2_19.webm",
                                    start_image="images/animation/start_image/tb_kitchen_pregnant2_19.webp")
image tb_kitchen_pregnant3_14 = Movie(play="images/animation/tb_kitchen_pregnant3_14.webm",
                                    start_image="images/animation/start_image/tb_kitchen_pregnant3_14.webp")
image tb_kitchen_pregnant3_17 = Movie(play="images/animation/tb_kitchen_pregnant3_17.webm",
                                    start_image="images/animation/start_image/tb_kitchen_pregnant3_17.webp")
 
image two_bodies_bath0_5 = Movie(play="images/animation/two_bodies_bath0_5.webm",
                                    start_image="images/animation/start_image/two_bodies_bath0_5.webp")
image two_bodies_bath0_8 = Movie(play="images/animation/two_bodies_bath0_8.webm",
                                    start_image="images/animation/start_image/two_bodies_bath0_8.webp")
image two_bodies_bath0_13 = Movie(play="images/animation/two_bodies_bath0_13.webm",
                                    start_image="images/animation/start_image/two_bodies_bath0_13.webp")
image two_bodies_bath0_18 = Movie(play="images/animation/two_bodies_bath0_18.webm",
                                    start_image="images/animation/start_image/two_bodies_bath0_18.webp")
image tb_bath_pregnant2_6 = Movie(play="images/animation/tb_bath_pregnant2_6.webm",
                                    start_image="images/animation/start_image/tb_bath_pregnant2_6.webp")
image tb_bath_pregnant2_9 = Movie(play="images/animation/tb_bath_pregnant2_9.webm",
                                    start_image="images/animation/start_image/tb_bath_pregnant2_9.webp")        
image tb_bath_pregnant3_5 = Movie(play="images/animation/tb_bath_pregnant3_5.webm",
                                    start_image="images/animation/start_image/tb_bath_pregnant3_5.webp") 
image tb_bath_pregnant3_10 = Movie(play="images/animation/tb_bath_pregnant3_10.webm",
                                    start_image="images/animation/start_image/tb_bath_pregnant3_10.webp") 


image two_bodies_mc_evening0_18 = Movie(play="images/animation/two_bodies_mc_evening0_18.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_18.webp")
image two_bodies_mc_evening0_19 = Movie(play="images/animation/two_bodies_mc_evening0_19.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_19.webp")
image two_bodies_mc_evening0_31 = Movie(play="images/animation/two_bodies_mc_evening0_31.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_31.webp")
image two_bodies_mc_evening0_32 = Movie(play="images/animation/two_bodies_mc_evening0_32.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_32.webp")
image two_bodies_mc_evening0_35 = Movie(play="images/animation/two_bodies_mc_evening0_35.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_35.webp")
image two_bodies_mc_evening0_45 = Movie(play="images/animation/two_bodies_mc_evening0_45.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_45.webp")
image two_bodies_mc_evening0_46 = Movie(play="images/animation/two_bodies_mc_evening0_46.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_46.webp")
image two_bodies_mc_evening0_49 = Movie(play="images/animation/two_bodies_mc_evening0_49.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_49.webp")
image two_bodies_mc_evening0_85 = Movie(play="images/animation/two_bodies_mc_evening0_85.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_85.webp")
image two_bodies_mc_evening0_88 = Movie(play="images/animation/two_bodies_mc_evening0_88.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_88.webp")
image two_bodies_mc_evening0_92 = Movie(play="images/animation/two_bodies_mc_evening0_92.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_92.webp")
image two_bodies_mc_evening0_93 = Movie(play="images/animation/two_bodies_mc_evening0_93.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_93.webp")
image two_bodies_mc_evening0_94 = Movie(play="images/animation/two_bodies_mc_evening0_94.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_94.webp")
image two_bodies_mc_evening0_96 = Movie(play="images/animation/two_bodies_mc_evening0_96.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_96.webp")
image two_bodies_mc_evening0_101 = Movie(play="images/animation/two_bodies_mc_evening0_101.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_101.webp")                              
image two_bodies_mc_evening0_121 = Movie(play="images/animation/two_bodies_mc_evening0_121.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_121.webp")  
image two_bodies_mc_evening0_129 = Movie(play="images/animation/two_bodies_mc_evening0_129.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_129.webp")  
image two_bodies_mc_evening0_133 = Movie(play="images/animation/two_bodies_mc_evening0_133.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_evening0_133.webp")
image tb_evening_pregnant2_5 = Movie(play="images/animation/tb_evening_pregnant2_5.webm",
                                    start_image="images/animation/start_image/tb_evening_pregnant2_5.webp")   
image tb_evening_pregnant2_9 = Movie(play="images/animation/tb_evening_pregnant2_9.webm",
                                    start_image="images/animation/start_image/tb_evening_pregnant2_9.webp")  
image tb_evening_pregnant2_20 = Movie(play="images/animation/tb_evening_pregnant2_20.webm",
                                    start_image="images/animation/start_image/tb_evening_pregnant2_20.webp") 
image tb_evening_pregnant3_4 = Movie(play="images/animation/tb_evening_pregnant3_4.webm",
                                    start_image="images/animation/start_image/tb_evening_pregnant3_4.webp") 
image tb_evening_pregnant3_12 = Movie(play="images/animation/tb_evening_pregnant3_12.webm",
                                    start_image="images/animation/start_image/tb_evening_pregnant3_12.webp") 
image tb_evening_pregnant3_18 = Movie(play="images/animation/tb_evening_pregnant3_18.webm",
                                    start_image="images/animation/start_image/tb_evening_pregnant3_18.webp") 
image tb_evening_pregnant3_20 = Movie(play="images/animation/tb_evening_pregnant3_20.webm",
                                    start_image="images/animation/start_image/tb_evening_pregnant3_20.webp")
image two_bodies_mc_night0_12 = Movie(play="images/animation/two_bodies_mc_night0_12.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_night0_12.webp")
image two_bodies_mc_night0_15 = Movie(play="images/animation/two_bodies_mc_night0_15.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_night0_15.webp")
image two_bodies_mc_night0_25 = Movie(play="images/animation/two_bodies_mc_night0_25.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_night0_25.webp")
image two_bodies_mc_night0_30 = Movie(play="images/animation/two_bodies_mc_night0_30.webm",
                                    start_image="images/animation/start_image/two_bodies_mc_night0_30.webp")
image tb_night_pregnant2_3 = Movie(play="images/animation/tb_night_pregnant2_3.webm",
                                    start_image="images/animation/start_image/tb_night_pregnant2_3.webp")
image tb_night_pregnant2_6 = Movie(play="images/animation/tb_night_pregnant2_6.webm",
                                    start_image="images/animation/start_image/tb_night_pregnant2_6.webp")
image tb_night_pregnant2_14 = Movie(play="images/animation/tb_night_pregnant2_14.webm",
                                    start_image="images/animation/start_image/tb_night_pregnant2_14.webp")
image tb_night_pregnant2_19 = Movie(play="images/animation/tb_night_pregnant2_19.webm",
                                    start_image="images/animation/start_image/tb_night_pregnant2_19.webp")
image tb_night_pregnant3_5 = Movie(play="images/animation/tb_night_pregnant3_5.webm",
                                    start_image="images/animation/start_image/tb_night_pregnant3_5.webp")
image tb_night_pregnant3_10 = Movie(play="images/animation/tb_night_pregnant3_10.webm",
                                    start_image="images/animation/start_image/tb_night_pregnant3_10.webp")
image tb_night_pregnant3_15 = Movie(play="images/animation/tb_night_pregnant3_15.webm",
                                    start_image="images/animation/start_image/tb_night_pregnant3_15.webp")
image tb_end_7 = Movie(play="images/animation/tb_end_7.webm",
                                    start_image="images/animation/start_image/tb_end_7.webp")
image tb_end_18 = Movie(play="images/animation/tb_end_18.webm",
                                    start_image="images/animation/start_image/tb_end_18.webp")
image tb_end_21 = Movie(play="images/animation/tb_end_21.webm",
                                    start_image="images/animation/start_image/tb_end_21.webp")

#Milf
image milf_event_kitchen0_0 = Movie(play="images/animation/milf_event_kitchen0_0.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen0_0.webp")
image milf_event_kitchen0_5 = Movie(play="images/animation/milf_event_kitchen0_5.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen0_5.webp")
image milf_event_kitchen0_8 = Movie(play="images/animation/milf_event_kitchen0_8.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen0_8.webp")
image milf_event_kitchen1_0 = Movie(play="images/animation/milf_event_kitchen1_0.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen1_0.webp")
image milf_event_kitchen1_1 = Movie(play="images/animation/milf_event_kitchen1_1.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen1_1.webp")
image milf_event_kitchen_pregnant2_9 = Movie(play="images/animation/milf_event_kitchen_pregnant2_9.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen_pregnant2_9.webp")
image milf_event_kitchen_pregnant2_10 = Movie(play="images/animation/milf_event_kitchen_pregnant2_10.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen_pregnant2_10.webp")
image milf_event_kitchen_pregnant3_5 = Movie(play="images/animation/milf_event_kitchen_pregnant3_5.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen_pregnant3_5.webp")
image milf_event_kitchen_pregnant3_6 = Movie(play="images/animation/milf_event_kitchen_pregnant3_6.webm",
                                    start_image="images/animation/start_image/milf_event_kitchen_pregnant3_6.webp")
                                    
image milf_event_bath0_6 = Movie(play="images/animation/milf_event_bath0_6.webm",
                                    start_image="images/animation/start_image/milf_event_bath0_6.webp")
image milf_event_bath1_0 = Movie(play="images/animation/milf_event_bath1_0.webm",
                                    start_image="images/animation/start_image/milf_event_bath1_0.webp")
image milf_event_bath1_1 = Movie(play="images/animation/milf_event_bath1_1.webm",
                                    start_image="images/animation/start_image/milf_event_bath1_1.webp")
image milf_event_bath_pregnant2_0 = Movie(play="images/animation/milf_event_bath_pregnant2_0.webm",
                                    start_image="images/animation/start_image/milf_event_bath_pregnant2_0.webp")
image milf_event_bath_pregnant2_1 = Movie(play="images/animation/milf_event_bath_pregnant2_1.webm",
                                    start_image="images/animation/start_image/milf_event_bath_pregnant2_1.webp")
image milf_event_bath_pregnant3_0 = Movie(play="images/animation/milf_event_bath_pregnant3_0.webm",
                                    start_image="images/animation/start_image/milf_event_bath_pregnant3_0.webp")

image milf_event_mc_eve0_6 = Movie(play="images/animation/milf_event_mc_eve0_6.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve0_6.webp")
image milf_event_mc_eve0_15 = Movie(play="images/animation/milf_event_mc_eve0_15.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve0_15.webp")
image milf_event_mc_eve_pregnant2_11 = Movie(play="images/animation/milf_event_mc_eve_pregnant2_11.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant2_11.webp")
image milf_event_mc_eve_pregnant2_12 = Movie(play="images/animation/milf_event_mc_eve_pregnant2_12.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant2_12.webp")
image milf_event_mc_eve_pregnant2_19 = Movie(play="images/animation/milf_event_mc_eve_pregnant2_19.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant2_19.webp")
image milf_event_mc_eve_pregnant3_4 = Movie(play="images/animation/milf_event_mc_eve_pregnant3_4.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant3_4.webp")
image milf_event_mc_eve_pregnant3_9 = Movie(play="images/animation/milf_event_mc_eve_pregnant3_9.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant3_9.webp")
image milf_event_mc_eve_pregnant3_14 = Movie(play="images/animation/milf_event_mc_eve_pregnant3_14.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant3_14.webp")
image milf_event_mc_eve_pregnant3_outfit_cow_9 = Movie(play="images/animation/milf_event_mc_eve_pregnant3_outfit_cow_9.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant3_outfit_cow_9.webp")
image milf_event_mc_eve_pregnant3_outfit_cow_18 = Movie(play="images/animation/milf_event_mc_eve_pregnant3_outfit_cow_18.webm",
                                    start_image="images/animation/start_image/milf_event_mc_eve_pregnant3_outfit_cow_18.webp")

image milf_event_mc_night0_6 = Movie(play="images/animation/milf_event_mc_night0_6.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night0_6.webp")
image milf_event_mc_night0_7 = Movie(play="images/animation/milf_event_mc_night0_7.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night0_7.webp")
image milf_event_mc_night0_16 = Movie(play="images/animation/milf_event_mc_night0_16.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night0_16.webp")
image milf_event_mc_night0_17 = Movie(play="images/animation/milf_event_mc_night0_17.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night0_17.webp")
image milf_event_mc_night2_5 = Movie(play="images/animation/milf_event_mc_night2_5.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night2_5.webp")
image milf_event_mc_night2_13 = Movie(play="images/animation/milf_event_mc_night2_13.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night2_13.webp")
image milf_event_mc_night3_4 = Movie(play="images/animation/milf_event_mc_night3_4.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night3_4.webp")
image milf_event_mc_night3_8 = Movie(play="images/animation/milf_event_mc_night3_8.webm",
                                    start_image="images/animation/start_image/milf_event_mc_night3_8.webp")

#Nym
image nym_day_4 = Movie(play="images/animation/nym_day_4.webm",start_image="images/animation/start_image/nym_day_4.webp")
image nym_day_28 = Movie(play="images/animation/nym_day_28.webm",start_image="images/animation/start_image/nym_day_28.webp")
image nym_day_32 = Movie(play="images/animation/nym_day_32.webm",start_image="images/animation/start_image/nym_day_32.webp")
image nym_day_51 = Movie(play="images/animation/nym_day_51.webm",start_image="images/animation/start_image/nym_day_51.webp")
image nym_day_52 = Movie(play="images/animation/nym_day_52.webm",start_image="images/animation/start_image/nym_day_52.webp")
image nym_day_60 = Movie(play="images/animation/nym_day_60.webm",start_image="images/animation/start_image/nym_day_60.webp")
image nym_day_74 = Movie(play="images/animation/nym_day_74.webm",start_image="images/animation/start_image/nym_day_74.webp")
image nym_day_94 = Movie(play="images/animation/nym_day_94.webm",start_image="images/animation/start_image/nym_day_94.webp")
image nym_day_102 = Movie(play="images/animation/nym_day_102.webm",start_image="images/animation/start_image/nym_day_102.webp")
image nym_day_108 = Movie(play="images/animation/nym_day_108.webm",start_image="images/animation/start_image/nym_day_108.webp")
image nym_day_113 = Movie(play="images/animation/nym_day_113.webm",start_image="images/animation/start_image/nym_day_113.webp")
image nym_day_117 = Movie(play="images/animation/nym_day_117.webm",start_image="images/animation/start_image/nym_day_117.webp")

image nym_night_8 = Movie(play="images/animation/nym_night_8.webm",start_image="images/animation/start_image/nym_night_8.webp")
image nym_night_13 = Movie(play="images/animation/nym_night_13.webm",start_image="images/animation/start_image/nym_night_13.webp")
image nym_night_19 = Movie(play="images/animation/nym_night_19.webm",start_image="images/animation/start_image/nym_night_19.webp")
image nym_night_33 = Movie(play="images/animation/nym_night_33.webm",start_image="images/animation/start_image/nym_night_33.webp")
image nym_night_41 = Movie(play="images/animation/nym_night_41.webm",start_image="images/animation/start_image/nym_night_41.webp")
image nym_night_46 = Movie(play="images/animation/nym_night_46.webm",start_image="images/animation/start_image/nym_night_46.webp")

image nym_end_5 = Movie(play="images/animation/nym_end_5.webm",start_image="images/animation/start_image/nym_end_5.webp")
image nym_end_22 = Movie(play="images/animation/nym_end_22.webm",start_image="images/animation/start_image/nym_end_22.webp")
image nym_end_26 = Movie(play="images/animation/nym_end_26.webm",start_image="images/animation/start_image/nym_end_26.webp")