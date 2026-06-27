image spanking_quit1:
    "spanking/spanking_quit1_%s.webp"%(outfit_spanking)
image spanking_quit2:
    Composite((1920,1080),
    (0,0),"spanking/spanking_quit2_%s_%s.webp"%(outfit_spanking,undress_spanking),
    (0,0),ConditionSwitch(
        "undress_spanking==0", Null(),
        "undress_spanking>=1",im.Alpha("spanking/mask/spanking_mask_quit2_%s_%s.webp"%(outfit_spanking,undress_spanking), (spanking_count/10))))

image spanking_quit3:
    Composite((1920,1080),
    (0,0),"spanking/spanking_quit3_%s_%s.webp"%(outfit_spanking,undress_spanking),
    (0,0),ConditionSwitch(
        "undress_spanking==0", Null(),
        "undress_spanking>=1",im.Alpha("spanking/mask/spanking_mask_quit3_%s_%s.webp"%(outfit_spanking,undress_spanking), (spanking_count/10))))
image spanking_quit4:
    "spanking/spanking_quit4_%s.webp"%(outfit_spanking)

image spanking_quit5:
    Composite((1920,1080),
    (0,0),"spanking/spanking_quit5_%s_%s.webp"%(outfit_spanking,undress_spanking),
    (0,0),ConditionSwitch(
        "undress_spanking==0", Null(),
        "undress_spanking>=1",im.Alpha("spanking/mask/spanking_mask_quit5_%s_%s.webp"%(outfit_spanking,undress_spanking), (spanking_count/10))))

image spanking_quit6:
    Composite((1920,1080),
    (0,0),"spanking/spanking_quit6_%s_%s.webp"%(outfit_spanking,undress_spanking),
    (0,0),ConditionSwitch(
        "undress_spanking==0", Null(),
        "undress_spanking>=1",im.Alpha("spanking/mask/spanking_mask_quit6_%s_%s.webp"%(outfit_spanking,undress_spanking), (spanking_count/10))))

image spanking_quit7:
    Composite((1920,1080),
    (0,0),"spanking/spanking_quit7_%s_%s.webp"%(outfit_spanking,undress_spanking),
    (0,0),ConditionSwitch(
        "undress_spanking==0", Null(),
        "undress_spanking>=1",im.Alpha("spanking/mask/spanking_mask_quit7_%s_%s.webp"%(outfit_spanking,undress_spanking), (spanking_count/10))))
image base_spanking:
    "spanking/spanking%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking)
    
image base_spanking_with_mask:
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))

image spanking_hard: 
    "spanking%s%s%s0_3_01"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_3_02"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_3_03"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_3_04"%(position_spanking,point_view_spanking,outfit_spanking)
    0.01
    "spanking%s%s%s0_3_05"%(position_spanking,point_view_spanking,outfit_spanking)
    0.01
    "spanking%s%s%s0_3_06"%(position_spanking,point_view_spanking,outfit_spanking)
    0.01
    "spanking%s%s%s0_3_07"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.01
    "spanking%s%s%s0_3_08"%(position_spanking,point_view_spanking,outfit_spanking)
    0.01
    "spanking%s%s%s0_3_09"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.01
    "spanking%s%s%s0_3_10"%(position_spanking,point_view_spanking,outfit_spanking)
    0.01
    "spanking%s%s%s0_3_11"%(position_spanking,point_view_spanking,outfit_spanking)
    0.01
    "spanking%s%s%s0_3_12"%(position_spanking,point_view_spanking,outfit_spanking)
    0.75
    "spanking%s%s%s0_3_11"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_3_10"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_3_09"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_3_08"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_3_07"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_3_06"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_3_05"%(position_spanking,point_view_spanking,outfit_spanking) 

image spanking_hard_with_mask: 
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_01.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_01.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_02.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_02.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_03.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_03.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_04.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_04.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_05.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_05.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_06.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_06.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_07.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_07.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_08.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_08.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_09.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_09.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_11.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_11.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.01
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_12.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_12.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.75
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_11.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_11.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_09.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_09.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_08.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_08.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_07.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_07.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_06.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_06.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_3_05.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_3_05.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    
#Normal
image spanking_normal: 
    "spanking%s%s%s0_1_1"%(position_spanking,point_view_spanking,outfit_spanking)
    0.02
    "spanking%s%s%s0_1_2"%(position_spanking,point_view_spanking,outfit_spanking)
    0.02
    "spanking%s%s%s0_1_3"%(position_spanking,point_view_spanking,outfit_spanking)
    0.02
    "spanking%s%s%s0_1_4"%(position_spanking,point_view_spanking,outfit_spanking)
    0.02
    "spanking%s%s%s0_1_5"%(position_spanking,point_view_spanking,outfit_spanking)
    0.02
    "spanking%s%s%s0_1_6"%(position_spanking,point_view_spanking,outfit_spanking)
    0.02
    "spanking%s%s%s0_1_7"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.02
    "spanking%s%s%s0_1_8"%(position_spanking,point_view_spanking,outfit_spanking)
    0.02
    "spanking%s%s%s0_1_9"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.02
    "spanking%s%s%s0_1_10"%(position_spanking,point_view_spanking,outfit_spanking)
    0.5
    "spanking%s%s%s0_1_9"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_8"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_7"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_6"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_5"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_4"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_3"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_2"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_1"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_0"%(position_spanking,point_view_spanking,outfit_spanking)

image spanking_normal_with_mask:   
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.02
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.5
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10))) 

#Slow spanking
image spanking_slow: 
    "spanking%s%s%s0_1_1"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_1_2"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_1_3"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_1_4"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_1_5"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_1_6"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_1_7"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.03
    "spanking%s%s%s0_1_8"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "spanking%s%s%s0_1_9"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.03
    "spanking%s%s%s0_1_10"%(position_spanking,point_view_spanking,outfit_spanking)
    0.4
    "spanking%s%s%s0_1_9"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_8"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_7"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_6"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_5"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_4"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_3"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_2"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_1"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "spanking%s%s%s0_1_0"%(position_spanking,point_view_spanking,outfit_spanking)

image spanking_slow_with_mask:   
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.4
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/spanking%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/spanking_mask%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10))) 


#Slow spanking
image spanking_massage: 
    "massage%s%s%s0_1_1"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "massage%s%s%s0_1_2"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "massage%s%s%s0_1_3"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "massage%s%s%s0_1_4"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "massage%s%s%s0_1_5"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "massage%s%s%s0_1_6"%(position_spanking,point_view_spanking,outfit_spanking)
    0.03
    "massage%s%s%s0_1_7"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.03  
    "massage%s%s%s0_1_8"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.03 
    "massage%s%s%s0_1_9"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.03  
    "massage%s%s%s0_1_10"%(position_spanking,point_view_spanking,outfit_spanking,)
    0.03  
    "massage%s%s%s0_1_9"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_8"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_7"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_6"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_5"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_4"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_3"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_2"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_1"%(position_spanking,point_view_spanking,outfit_spanking)
    0.04
    "massage%s%s%s0_1_0"%(position_spanking,point_view_spanking,outfit_spanking)
    0.1
    repeat
image spanking_massage_with_mask:   
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03   
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03 
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_10.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.03
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_9.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_8.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_7.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_6.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_5.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_4.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_3.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_2.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_1.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.04
    Composite((1920,1080),
    (0,0),"spanking/massage%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking),
    (0,0),im.Alpha("spanking/mask/massage_mask%s%s%s%s_1_0.webp"%(position_spanking,point_view_spanking,outfit_spanking,undress_spanking), (spanking_count/10)))
    0.1
    repeat