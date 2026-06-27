default is_replay_level3_0=False
default is_view_personality2=False
default unlock_two_bodies=False
default unlock_milf=False
label level3_0:
    if _in_replay:
        if persistent.gallery_incest_story:
            $ incest_story = True
        if persistent.gallery_pregnancy_censored:    
            $ set_active_pregnancy = False
        $ firstname = persistent.gallery_firstname
        $ neusname = persistent.gallery_neusname
    if not(is_view_personality) or is_replay_level3_0:
        scene black with dissolve
        stop music fadeout 2.0 
        centered "{size=+40}You tell her about her other personality"                               
        scene neus3_p_0 with dissolve
        neus "I see."                
        neus "I'm sorry, I wasn't fully aware of my condition."               
        neus "Looking back, the signs were there, but I chose to ignore them."                
        neus "And I never told you because I was scared. I know that doesn’t excuse my actions." 
        scene neus3_p_1 with dissolve               
        neus "I understand if you want to distance yourself from me."
        scene neus3_p_2 with dissolve
        neus "You don't need to fulfill the promise you made to me."
        scene neus3_p_3 with dissolve
        play music atelier_and_cyber_world volume 0.2 fadeout 1.0
        mc "Who said I wanted to distance myself from you?"
        mc "I'll fulfill my promise even if you don't want me to."
        scene neus3_p_4 with dissolve
        if incest_story:
            mc "You're my adorable little sister, how could I not want you to be completely mine."
        else:
            mc "I want to make you completely mine."
        scene neus3_p_5 with dissolve
        neus "My condition really doesn't bother you?"
        neus "Knowing everything, you still want to be with me?"
        mc "Yes."
        scene neus3_p_6 with dissolve
        if incest_story:
            neus "*nervous laughter* Haha, I also want to be with you brother, but..."
        else:
            neus "*nervous laughter* Haha, I also want to be with you, but..."
        scene neus3_p_7 with dissolve
        neus "*whispering*{size=-15}I don't think it's fair for you to accept my obsessive sid-"
        scene neus3_p_8 with pushle
        play music lazy_night volume 0.5 fadeout 0.5
        neus_yan "Says the one who's been represses her feelings."
        neus_yan "That's not exactly healthy either."
        scene neus3_p_9 with pushri
        neus "!!?"
        scene neus3_p_10 with pushle
        neus_yan "I've always had the ability to take control."
        scene neus3_p_11 with dissolve
        if incest_story:
            neus_yan "My original plan was to disappear using the book, after becoming our brother's wife."
        else:
            neus_yan "My original plan was to disappear using the book, after becoming his wife."
        neus_yan "But I can't deny the possibility of being loved by him too."
        scene neus3_p_12 with pushri
        neus "Hmm, has my condition really reached this point?"
        scene neus3_p_8 with pushle
        neus_yan "I'm sorry, but I won't disappear until we fulfill our goal."                
        neus_yan "Although... there's another option."
        scene neus3_p_13 with fade
        neus_yan "If we had different bodies, we wouldn't suffer from multiple personalities."
        scene neus3_p_14 with snow1
        neus "{size=-15}I don't think it would work like that..."(multiple=2)
        neus_yan "Because we'd be separate individuals."(multiple=2)                
        scene neus3_p_15 with dissolve
        neus_yan "Haha, just kidding."
        scene neus3_p_16 with dissolve
        neus_yan "Or maybe not."  
        scene neus3_p_17 with dissolve              
        neus_yan "The book I gave you, its final spell can grant wishes."
        scene neus3_p_9 with pushri
        neus "*whispering* {size=-15}Then I'd become even weirder."
        scene neus3_p_8 with pushle
        neus_yan "Yes, but it's not necessary. Like I said, I'll disappear once we become his wife."
        mc "Assuming you separate your personalities, can you still get pregnant?"
        scene neus3_p_18 with snow1
        neus "Hmm?"(multiple=2)
        neus_yan "Yes."(multiple=2)
        scene neus3_p_19 with dissolve
        neus "Your smile scares me."(multiple=2)
        neus_yan "Oh, I see. Hehe."(multiple=2)
        $is_view_personality=True   
    if is_view_personality2 and not is_replay_level3_0:
        jump level3_0_div     
    $ is_replay_level3_0 = False
    scene neus3_p_20 with fade
    play music lazy_night volume 0.5 fadeout 0.5 if_changed    
    menu:                
        "Continue":                
            play music atelier_and_cyber_world volume 0.2 fadeout 0.4
            mc "Let's do it."
            scene level3_0_0 with dissolve
            neus "Huh! Really?"
            scene level3_0_1 with dissolve
            mc "Why not?"
            mc "Although, I might have gotten a little too excited."
            mc "This decision is yours to make."
            scene level3_0_2 with dissolve
            neus "Thank you... but what's with the sudden change in attitude?"
            scene level3_0_3 with dissolve
            mc "Well, whatever decision you make, I will be happy with."
            mc "If you decide to separate your personalities, having another [neusname] would be great."
            mc "And if you choose not to, learning to coexist with your other personality could be a good choice too."
            scene level3_0_4 with dissolve
            neus "Really? Is that what you think?"            
            mc "Hahaha, was I that obvious?"
            mc "Well, the idea of having a threesome, only with the person I love, is by far the option that excites me the most."
            if incest_story:
                mc "But there's something I want even more: to see my little sister happy, so I won't intervene."
            else:
                mc "But there's something I want even more: to see you happy, so I won't intervene."
            scene level3_0_5 with dissolve           
            neus_yan "{e_heartbt=FF0000}"(multiple=2)
            neus "...{e_heartbt=FF0000}"(multiple=2)
            scene level3_0_6 with dissolve
            neus "(Hmm, what should I do?)"
            $is_view_personality2=True
            if quest_v2:
                $ questSide_v2_7.completion = True
            else:
                $questSide_6.completion=True
            $is_change_quest = True 
            if not _in_replay:
                call notify_personalized(_("Side Quest updated"))          
            jump level3_0_div
        "Leave":
            scene level3_0_152 with dissolve
            neus "What!?"(multiple=2)
            neus_yan "I understand, I will hold onto the memories for now, until you decide."(multiple=2)   
            play sound magical1 volume 0.3 
            $renpy.end_replay()
            jump rooms

label level3_0_div:
    play music atelier_and_cyber_world volume 0.2 if_changed
    scene level3_0_6 with dissolve
    $ xsize_value = 750
    menu(screen="custom_choice_enhanced"):                
        "What is her decision regarding the personality split?"
        "Split personalities":
            play sound whoosh1
            scene level3_0_7 with pushle           
            neus_yan "Great, now we just need someone with a lot of energy to perform the spell."
            scene level3_0_8 with dissolve
            mc "Understood, leave it to me."
            scene level3_0_9 with dissolve
            neus_yan "The first step is to share my thoughts and memories with you, to intertwine them."
            scene level3_0_10 with pushri
            neus "Wait, {sc=2}what?!{/sc} I think I’m having second thoughts."
            scene level3_0_11 with dissolve
            mc "Come on, don't be a coward and back out at the last moment."
            scene level3_0_12 with pushle
            neus_yan "Well, let's begin."
            scene level3_0_12_1 with pushri
            neus "{sc=4}W-wait, I chang-{/sc}{w=1.0}{nw}" with hpunch
            play sound magical1 volume 0.3
            play music happy_memories fadeout 1.0
            scene level3_0_13 at gray_scale with snow1
            neus  "Could you stay a little longer, mom?"
            scene level3_0_14 at gray_scale with dissolve                   
            mom_n "I'm sorry, my dear."
            play music Kazuchi_2_23_am volume 0.3 fadeout 1.0
            scene level3_0_15 with w24
            if incest_story:
                neus "Mom and Dad were always too busy to celebrate moments like these, so I never thought I’d have a birthday like this..."
                scene level3_0_16 with dissolve
                neus "This is the best birthday ever thanks to you!"
                neus "I can’t wait to open my gift and see what you got me."
                scene level3_0_17 with dissolve
                neus "Are you sure you want to give me this? You know what it signifies, right?"
            else:
                neus "I know they're busy with work, but it wouldn’t hurt to take one day off—just once."
                scene level3_0_16 with dissolve
                neus "At least this time, I’m not alone. Maybe I can even hope for a nice gift."
                scene level3_0_17 with dissolve
                neus "Are you sure you want to give me this? You know what it signifies, right?"
            stop music fadeout 1.0
            scene level3_0_18 at gray_scale with fadesex
            play char1 whisper volume 0.3
            if incest_story:
                neus "*whispering* An overwhelming desire for your little sister washes over you, as you dream of building a large, loving family with her."
            else:
                neus "*whispering* You'll always be with [neusname], and you're going to have a big, big family with her."
            stop char1 fadeout 0.5
            scene level3_0_19  with dissolve
            if incest_story:
                mc "Hey sis, could you stop doing that?"
            else:
                mc "Hey, could you stop doing that?"
            play music Kazuchi_2_23_am volume 0.3 fadein 1.0
            scene level3_0_20  with dissolve
            neus "*Whistling* Doing what?"
            mc "... Never mind."
            scene level3_0_21 with pushu
            if incest_story:
                neus "(A new series is premiering today, I should invite my brother to watch it with me.)"
            else:
                neus "(A new series is premiering today, I should invite him to watch it with me.)"
            neus "(I hope he doesn't have plans, although he never does, so I can have him all to myself.)"
            scene level3_0_22 with pushri
            girl2 "Hey, do you want to come to the karaoke with us?"
            girl1 "Come on, it'll be fun."
            play music the_truth_is_in_the_dark fadein 1.0
            scene level3_0_23 with pushdo
            mc "No, thanks. I'm busy."(multiple=2)
            neus "{glitch}...{/glitch}"(multiple=2)
            scene level3_0_24 at gray_scale with pushle
            girl1 "I heard his family is rich."(multiple=2)
            neus "(No one is going to {glitch}{=lust_style}steal{/glitch} him from me...)"(multiple=2)
            scene level3_0_25 at gray_scale with dissolve
            girl2 "We can seduce him, turn him into our errand boy, and get him to buy us things, hahaha."(multiple=2)
            neus "(And the best way to avoid that is to {glitch}{=lust_style}cut the problem at the source{/glitch}.)"(multiple=2)
            scene level3_0_26 at gray_scale with dissolve
            if incest_story:
                girl3 "The only downside is that he's always hanging out with his little sister, you know the girl with the small breasts."(multiple=2)
            else:
                girl3 "The only downside is that he's always hanging out with that girl with small breasts."(multiple=2)
            neus "It's time to {glitch}{=lust_style}deflate{/glitch} those poorly inflated balloons."(multiple=2)
            girl2 "Yeah, every time we invite him somewhere, he rejects us. And the last time, he ignored us as if we were trash."
            scene level3_0_27 at gray_scale with dissolve
            neus "..."(multiple=2)
            girl1 "Exactly, he's so arrogant. If it weren’t for his money, we wouldn’t even waste our time talking to him."(multiple=2)
            girl3 "He should be grateful that girls like us, with such great attributes, even talk to him."
            stop music fadeout 1.0
            scene level3_0_28 with dissolve
            neus "Am I really going to do this...?"
            scene level3_0_29 with dissolve
            neus "No..."  
            scene level3_0_30 with dissolve                  
            neus "Y-you saw that too... {sc=4}right?{/sc}"
            mc "Yes"
            scene level3_0_31 with dissolve
            neus "{sc=2}C-Can you-{/sc}{w=1.0}{nw}"
            $ renpy.music.set_volume(0.1, channel='music')
            play music a_stray_cat_aimed_for_space fadeout 1.0
            scene level3_0_32 with dissolve
            mc "If you're worried that my feelings for you have changed, you don't need to. They haven't."
            mc "And in the end, you regretted it and didn't go through with it, right?"
            scene level3_0_32_1 with dissolve
            neus "Yes, {sc=4}but...{/sc}"
            scene level3_0_33 with dissolve
            mc "Shh, don't think about it—just let go."
            scene level3_0_34 with dissolve
            play char1 french02
            neus "Uhhh kiss"
            scene level3_0_35 with dissolve
            if incest_story:
                neus "Really, are you sure brother?"
            else:
                neus "Really, are you sure?"
            mc "Yes"
            scene level3_0_36 with dissolve
            neus "*Whispering*{bt=3}{size=-20}I love you{/bt}"
            scene level3_0_37 with dissolve
            mc "?"(multiple=2)
            neus "Can you allow me something?"(multiple=2)
            neus "I want to always be by your side..."
            scene level3_0_38 with dissolve
            mc "Could you repeat what you just said?"
            scene level3_0_39 with dissolve
            neus "I want to be... always by your side..."
            mc "The part before that"
            scene level3_0_40 with dissolve
            neus "{sc=2}I l-{/sc}"                    
            neus "(The more I hold back, the more my {color=#cc0066}chest hurts{/color})"
            neus "(He already knows {color=#cc0066}everything{/color}, I want to say it...)"
            $ renpy.music.set_volume(0.6,delay=3.5, channel='music')
            neus "(I want to {bt=2}{color=#cc0066}express{/color}{/bt} it)"
            scene level3_0_41 with dissolve
            neus "I want you to give me {bt=2}{=lust_style}lots of love{/bt}"
            scene level3_0_42 with dissolve
            neus "I want to give you every part of my being... and for you to {bt=2}{=lust_style}love every \npart of them{/bt}"
            scene level3_0_43 with dissolve
            neus_yan "{bt=3}{=lust_style}{glitch}I looooooooove you{/bt} {e_heartbt=FF0000}"(multiple=2)
            neus "{bt=3}{=lust_style}I love you{e_heartbt=FF0000}{/bt}"(multiple=2)
            scene level3_0_44 with dissolve
            mc "I love you too, and I love every part of you"
            scene level3_0_45 with dissolve
            play char1 short_kiss
            neus_yan "Kisssss"(multiple=2)
            neus "Kissssss"(multiple=2)
            $ renpy.music.set_volume(0.2,delay=1.5, channel='music')
            scene level3_0_46 with dissolve
            neus "I'm ready, let's do the division of personalities."
            stop music fadeout 1.0
            scene black with dissolve 
            centered "{size=+20}After the bonding, you perform the personality separation spell"   
            scene level3_0_47 with dissolve
            neus_yan "Yaaay! I finally have a body"
            $ renpy.music.set_volume(0.3,delay=1.5, channel='music')
            play music Trance_Steele fadeout 0.5
            scene level3_0_48 with dissolve
            if incest_story:
                neus_yan "Hey big brother{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5} Don't you want to take a little taste, of your little sister's new body?"
            else:
                neus_yan "Hey... Don't you want to take a little taste... of my new body?"
            neus_yan "Even though technically it's the same, hehe."
            scene level3_0_49 with dissolve
            neus "W-Wait, I-I want to go {size=-15}first"
            play music DarkestSoul_Schmidt volume 0.5 fadeout 1.0
            scene level3_0_50 with dissolve
            $ renpy.music.set_volume(0.6,delay=1.0, channel='music')
            neus_yan "Then let it be a {sc=4}{color=#cc0066}duel{/color}{sc}"
            stop music fadeout 1.0
            scene level3_0_51 with dissolve
            neus_yan "of rock-paper-scissors"  
            scene level3_0_51_1 with dissolve        
            $ renpy.music.set_volume(1.0,delay=1.0, channel='music')        
            ""
            scene level3_0_52 with dissolve 
            play music Trance_Steele fadeout 0.5 volume 0.5             
            neus "(Damn, why do I have such bad luck)"(multiple=2)
            neus_yan "Hehe, I guess I'll go first"(multiple=2)
            scene level3_0_53 with dissolve 
            neus_yan "But before we start, would you like to give me a name, so it's easier for you to identify us?"
            if persistent.gallery_lyra != "Lyra":
                $ neusname_lyra = renpy.input(_("What is the name you want to give her? (Default: Lyra)"), default=persistent.gallery_lyra, exclude='\\[{')
            else:
                $ neusname_lyra = renpy.input(_("What is the name you want to give her? (Default: Lyra)"), exclude='\\[{') 
            $ neusname_lyra = neusname_lyra.title()
            $ neusname_lyra = neusname_lyra.strip()
            if neusname_lyra == "":
                $ neusname_lyra = "Lyra"
            $ persistent.gallery_lyra = neusname_lyra
            scene level3_0_54 with dissolve
            if neusname_lyra.lower() == neusname.lower():                        
                neus_lyra "Hehe, really? I guess if it doesn't make it difficult for you to identify us, then it's fine"
            else:
                neus_lyra "Great! I love it"
            scene level3_0_55 with dissolve
            neus_lyra "So let's begin, but since it's my first time in this body"
            play sound clothes
            scene level3_0_56 with dissolve
            neus_lyra "It would be better if we moisten this great sword"
            play char1 short_kiss
            scene level3_0_57 with dissolve
            neus_lyra "Kiss"
            scene level3_0_58 with dissolve
            if incest_story:
                neus_lyra "It seems like our brother is very excited about taking my first time for the second time"
            else:
                neus_lyra "It seems like you're very excited about taking my first time for the second time"
            scene level3_0_59 with dissolve
            neus "Huh?"(multiple=2)
            neus_lyra "Lick lick"(multiple=2)
            scene level3_0_60 with dissolve
            neus "(My tongue feels strange, with a familiar texture)"
            neus "(Don't tell me)"
            scene level3_0_61 with dissolve
            neus "Hey, can you stop?"
            scene level3_0_62 with dissolve
            neus_lyra "Oh, are you feeling jealous?"
            scene level3_0_63 with dissolve
            neus "It's not that."
            scene level3_0_64 with dissolve
            neus_lyra "We are the same person, you know. I know you're jealous."
            neus_lyra "I wouldn't normally share this delicacy with anyone."
            neus_lyra "But since it's me, I think I can make an exception"
            mc "(I like where this is going)"
            scene level3_0_65 with dissolve
            neus_lyra "Come here."
            neus "I really didn't mean this-"
            play music SweetSax_Dellay volume 0.1 fadeout 1.5
            scene level3_0_66 with dissolve
            neus "(It's quite big)"
            scene level3_0_67 with dissolve
            neus_lyra "Hehe, I knew it."
            scene level3_0_67_1 with dissolve
            neus "(Salty)"(multiple=2)
            neus_lyra "(Delicious)"(multiple=2)
            play char3 double_suck1
            scene level3_0_68 with dissolve
            neus "Lick lick"
            neus_lyra "Lick lick"
            if incest_story:
                mc "(Having two of my sisters' tongues licking me feels so good)"
            else:
                mc "(Having two tongues licking me feels so good)"
            stop char3 fadeout 0.5
            scene level3_0_69 with dissolve
            neus_lyra "Well, it's time to take a good mouthful of this delicacy."
            scene level3_0_70 with dissolve
            neus_lyra "(It tastes so delicious)"
            play char3 suck4
            scene level3_0_71 with dissolve
            neus_lyra "Suck suck"
            if incest_story:
                neus_lyra "(Although this body has never tasted my brother's cock)"
            else:
                neus_lyra "(Although this body has never tasted this cock)"
            neus_lyra "(It's like the memories have transferred, and this body knows the exact places that make it feel the best)"
            neus_lyra "Suck suck slurp"
            scene level3_0_72 with dissolve
            if incest_story:
                neus "(The familiar sensation of my brother's cock is invading my mouth, I want some too...)"
            else:
                neus "(The familiar sensation of his cock is invading my mouth, I want some too...)"
            scene level3_0_71 with dissolve
            neus_lyra "(It's so delicious, I want to feel it deeper)"
            play char3 deep_suck1
            scene level3_0_73 with dissolve
            neus_lyra "(If I do this every day, this body will become addicted very easily)"
            if incest_story:
                neus_lyra "(And I'll always want to have my brother's cock in my mouth, I love it so much)"
            else:
                neus_lyra "(And I'll always want to have your cock in my mouth, I love it so much)"
            neus_lyra "suck slurp suck"
            scene level3_0_74 with flash
            stop char3
            play charM cum1
            neus_lyra "Ugh"
            scene level3_0_75 with dissolve
            ""
            play char1 gulp1
            scene level3_0_76 with dissolve
            neus_lyra "Ah"
            scene level3_0_77 with dissolve
            if incest_story:
                neus "Brother... I-I want some too"
            else:
                neus "I-I want some too"
            play char3 suck4
            scene level3_0_78 with fadesex
            neus "Suck suck"
            neus_lyra "I look so lascivious sucking your big cock"
            stop char3 fadeout 0.5
            scene level3_0_79 with dissolve
            neus_lyra "Although it feels better deeper"
            neus "(It's going so deep)"
            neus_lyra "Oh, I can feel it so deep"
            neus_lyra "(Interesting, if we physically touch, our connection intensifies)"
            play char3 deep_suck1
            scene level3_0_80 with dissolve
            neus "Mmm Mmmm"
            if incest_story:
                neus_lyra "Cum in your little sister's throat"
            else:
                neus_lyra "Cum in my throat"
            scene level3_0_81 with flash
            stop char3
            play charM cum1
            neus "Ugh"
            scene level3_0_81_1 with dissolve
            if incest_story:
                neus_lyra "Swallow all of our brother's cum, don't leave a drop."
            else:
                neus_lyra "Swallow all of his cum, don't leave a drop."
            play char1 gulp1
            neus "Gulp"
            stop music fadeout 1.0
            play ambience night_ambience volume 0.1
            scene level3_0_82 with dissolve
            neus_lyra "Okay, enough of the foreplay"
            scene level3_0_83 with dissolve
            neus "I want it inside."
            scene level3_0_84 with dissolve
            neus_lyra "This body wants to try it even though it's her first time."         
            scene level3_0_85 with dissolve
            neus "H-Hey, can you sto-"
            neus_lyra "Oh, I understand."
            scene level3_0_86 with dissolve
            neus_lyra "Let's share this sensation" 
            neus "Mmm?"                    
            scene level3_0_87 with dissolve
            play char1 double_penetration1 volume 2.0
            neus "{=lust_style}Ah!"(multiple=2)
            neus_lyra "{=lust_style}Ah!"(multiple=2)
            scene level3_0_88 with dissolve                    
            neus "*Nodding*"(multiple=2)
            neus_lyra "I'm going to start moving now."(multiple=2)
            play char3 double_sex1
            scene level3_0_89 with dissolve
            neus "{=lust_style}Ah ah ah ah"(multiple=2)
            neus_lyra "{=lust_style}Ah ah ah ah"(multiple=2)
            neus "(It's strange to feel this sensation again)"
            neus "{bt=2}{=lust_style}Ah ah ah ah{/bt}"(multiple=2)
            neus_lyra "(I seem like a pervert, but I don't care because I'm his pervert)"(multiple=2)
            neus "{bt=2}{=lust_style}Oh oh oh oh{/bt}"(multiple=2)            
            neus_lyra "This feels so good."(multiple=2)                    
            neus_lyra "(But...)" 
            scene level3_0_90 with dissolve
            stop char3 fadeout 0.5
            neus_lyra "(I want him deeper inside me.)"
            scene level3_0_91 with dissolve
            play char1 double_penetration2
            neus "Ummm"(multiple=2)
            neus_lyra "Mhmmm"(multiple=2)
            play char3 double_sex2
            scene level3_0_92 with dissolve
            neus "{bt=2}{=lust_style}Ah ah ah{/bt}"(multiple=2)
            neus_lyra  "{bt=2}{=lust_style}Ah ah ah{/bt}"(multiple=2)
            neus_lyra "(This is the sensation I was thinking about)"
            if incest_story:
                neus "(The feeling of being fucked by my brother's big cock feels so good)"
            else:
                neus "(The feeling of being fucked his big cock feels so good)"
            neus "(But at the same time, my belly feels so empty and it's starting to crave his cock a lot)"
            neus "(Please let it be my turn now, {sc=2}{=lust_style}quickly!{/sc})"
            stop char3
            scene level3_0_93 with dissolve
            play char1 double_climax3
            neus "{sc=2}{=lust_style}I'm cumming{/sc}"(multiple=2)
            neus_lyra "{sc=2}{=lust_style}I'm cumming{/sc}"(multiple=2)                   
            scene level3_0_94 with flash
            play charM cum1  
            play char1 double_climax1       
            if incest_story:
                neus_lyra "Yes, fill up your sister's little belly."
            else:                              
                neus_lyra "Yes, fill up my little belly."
            neus_lyra "Impregnate my body on the first time it tries your cock"  
            stop char1 fadeout 1.0                                 
            scene level3_0_95 with dissolve
            neus "Mmmm!"
            neus "(I want him to cum inside me too.)"
            play char3 breathing1
            scene level3_0_96 with dissolve
            neus_lyra "It feels so good to have my first orgasm in this body"
            scene level3_0_97 with dissolve
            neus "I can't take it anymore..."
            scene level3_0_98 with dissolve
            stop char3 fadeout 1.0
            neus "Be responsible, my belly feels lonely"
            scene level3_0_99 with dissolve
            neus "I-I want you to fill it with {bt=2}{=lust_style}lots of cum{/bt}"
            mc "Since when did you become such a pervert?"
            neus "Just shut up and put it inside me, {sc=2}please{/sc}."
            scene level3_0_100 with dissolve
            play char1 penetration4
            neus "Uhmm"                    
            mc "I'm going to start moving now."
            play char3 sex4
            scene level3_0_101 with dissolve
            neus "{=lust_style}Ha Ha Ha"
            neus "(I needed this {e_heartbt=FF0000})"
            if incest_story:
                neus "Brother, that feels so good."
            else:
                neus "That feels so good."
            stop char3 fadeout 0.5
            scene level3_0_102 with dissolve
            neus_lyra "Share some pleasure with me"
            play char3 double_sex3
            scene level3_0_102_1 with dissolve                    
            neus_lyra "{bt=2}{=lust_style}Ha Ha Ha{/bt}"
            neus "{bt=2}{=lust_style}Ha Ha Ha{/bt}"
            neus "I'm cumming for the second time from this magnificent sensation"
            scene level3_0_103 with dissolve  
            stop char3 
            play char1 double_climax3                  
            neus_lyra "I'm cumming"(multiple=2)
            neus "I'm cumming"(multiple=2)
            scene level3_0_104 with dissolve
            play char3 breathing1                    
            neus "(Finally, my belly has been filled and I no longer feel that emptiness)"
            scene level3_0_105 with dissolve                    
            neus "Ah"
            mc "Hey, could you repeat that phrase you said earlier?"
            scene level3_0_106 with dissolve                    
            neus "I don't know what you're talking about."    
            stop char3 fadeout 1.0
            stop ambience fadeout 1.0
            play music Trance_Steele volume 0.1                                       
            scene level3_0_107 with dissolve
            if incest_story:
                neus_lyra "Don't try to act like you don't know. We both know which phrase our brother is referring to."
            else:
                neus_lyra "Don't try to act like you don't know. We both know which phrase he's referring to."
            scene level3_0_108 with dissolve
            neus "... ?"
            scene level3_0_109 with dissolve
            neus_lyra "If you don't say it, I will."
            scene level3_0_110 with dissolve
            neus "..."
            scene level3_0_111 with dissolve
            neus_lyra "I guess I'll say it then."                    
            neus_lyra "{w=0.25}I {w=0.5}lo{w=0.75}-ve{w=1.0} y{w=1.25}-o{w=1.25}-{w=1.25}{nw}"
            scene level3_0_112 with dissolve
            play music TheGirlFromBrasil_Hauser volume 0.2 fadeout 1.0
            neus "{bt=4}{=lust_style}I love you.{/bt}"
            scene level3_0_113 with dissolve
            neus_lyra "Good girl."(multiple=2)
            neus "I find it very embarrassing to say, because I don't consider myself worthy of saying it."(multiple=2)
            scene level3_0_113_1 with dissolve
            neus "But still, I..."
            scene level3_0_114 with dissolve
            play char1 french01
            play char2 french03
            neus_lyra "I love you very much." (multiple=2)
            neus "I love you very much." (multiple=2)
            scene level3_0_115 with dissolve
            neus "To the point of being so obsessed that I created a personality based on the obsession I feel for you."
            neus "A personality that was capable of using hypnosis to make you mine."                    
            neus "If it's not too much to ask, while you cum inside me, I want you to tell me that you love me."
            mc "I love you."
            scene level3_0_116 with dissolve
            play charM cum1
            play char1 double_penetration1
            neus "Uhhhh"
            neus "I lhove yhou vhery mhuch thoo\n(I love you very much too)."
            scene level3_0_117 with dissolve
            neus_lyra "Huh, I feel so jealous of myself for receiving so much love."
            neus_lyra "Can you give me the same love you gave to her?"
            play char3 sex4
            scene level3_0_118 with dissolve
            neus_lyra "{bt=2}{=lust_style}Ha Ha Ha{/bt}"
            neus_lyra "I love you {e_heartbt=FF0000}, I love you {e_heartbt=FF0000}, I love you {e_heartbt=FF0000}."
            neus_lyra "I want to always be with you.{e_heartbt=FF0000}"
            neus_lyra "I want you to give me {bt=2}{color=#cc0066}lots{/color}{/bt} of {bt=2}{color=#cc0066}love every day{/color}{/bt}."
            scene level3_0_119 with dissolve
            stop char3 fadeout 0.5
            play charM cum1
            play char1 climax1
            neus_lyra "Ha"
            scene level3_0_120 with dissolve
            play char1 french01
            pause 0.2
            play char2 short_kiss
            if incest_story:
                neus_lyra "We love you brother {e_heartbt2=FF0000}."(multiple=2)
                neus "We love you brother {e_heartbt2=FF0000}."(multiple=2)
            else:
                neus_lyra "We love you {e_heartbt2=FF0000}."(multiple=2)
                neus "We love you {e_heartbt2=FF0000}."(multiple=2)
            scene black with dissolve
            stop music fadeout 2.0
            centered "{size=+30}The next day"
            play ambience morning_sounds fadein 0.5
            scene level3_0_121 with eyeopen
            neus "Last night was intense."
            neus "Hey, you know, last night I said some embarrassing things, you can forget about them."
            mc "Are you trying to say that what you said last night was a lie and that you don't love me?"
            scene level3_0_122 with dissolve
            neus "Damn, I wasn't trying to say that."
            neus "You're very ann-{w=1.0}{nw}"
            scene level3_0_123 with dissolve
            neus "I’m not handling this well, am I?"
            scene level3_0_124 with dissolve
            play sound clothes
            neus "What I said last night was very real. I-I love you a lot {e_heartbt=FF0000}."
            neus "It's just a bit difficult to get rid of those bad habits."
            neus "But I believe that, over time, I'll overcome this problem."
            scene level3_0_125 with dissolve                    
            neus "Although you should be careful not to give me too much love, or I'll end up like her, obsessed with you."
            scene level3_0_126 with dissolve
            neus_yan "lick lick"(multiple=2)
            mc "Well, I can't promise that. Most likely, you'll end up like [neusname_lyra] in the future."(multiple=2)
            mc "Although it would be a bit sad if in the future I couldn't tease you about not being able to express your emotions."
            scene level3_0_127 with dissolve
            play char3 suck4
            neus "So you're just a bully."
            neus "But setting that aside, I want our relationship to be based not only on sex."
            neus "I also want to-"
            scene level3_0_128 with dissolve
            stop char3 fadeout 0.5
            neus "Hey, can you stop making noise?"
            scene level3_0_127 with dissolve
            play char3 suck4
            neus "Well, the thing is, I want to have romantic moments."
            scene level3_0_129 with dissolve
            stop char3 fadeout 0.5
            neus_lyra "Ummm"(multiple=2)
            neus "And, oh, if you want, feel free to use it as your personal Onahole"(multiple=2)
            scene level3_0_130 with dissolve                    
            play charM cum1
            neus_lyra "{e_musical2=FFF}"(multiple=2)
            neus "(Damn, I forgot that when I touch it, it's like we become one entity again.)"(multiple=2)
            scene level3_0_131 with dissolve
            neus_lyra "You're so mean, you know?"
            neus_lyra "I want to have romantic moments too."
            scene level3_0_132 with dissolve
            neus_lyra "But I also think we should enjoy this big cock that's just for us."
            neus "..."
            scene level3_0_133 with dissolve
            stop ambience fadeout 0.5
            play music the_truth_is_in_the_dark fadein 2.0
            neus_lyra "And by the way, you better not cheat on us, because if you do, I’ll make you scream and not in the good way."
            scene level3_0_134 with pushri
            stop music fadeout 2.0
            play ambience morning_sounds fadein 2.0
            neus_lyra "Hehe, I'm just joking... or maybe I'm not."
            scene level3_0_134_0 with dissolve
            neus "I don't like the idea of making you scream, but if you cheat on us, I'll be really upset."
            mc "(Hmmm? For some reason, there's unjustified distrust towards me.)"
            mc "(And I believe that talking won't solve that.)"
            menu:
                mc "(The only solution that comes to my mind is ...)"
                "Do it":  
                    stop ambience fadeout 2.0
                    play char3 sex5                          
                    scene level3_0_135 with fadesex                            
                    neus_lyra "{bt=2}{=lust_style}Ha ha ha{/bt} {e_heartbt2=FF0000}"
                    neus_lyra "Yhes(Yes), give a lot of love to my {bt=2}{=lust_style}jealous vagina{/bt} {e_heartbt=FF0000}."
                    if incest_story:
                        neus_lyra "Give lots of love to the one responsible for you being obsessed with forming a {sc=2}big family with your sister.{/sc}"
                    else:
                        neus_lyra "Give lots of love to the one responsible for you being obsessed with forming a {sc=2}big family.{/sc}"
                    scene level3_0_136 with dissolve
                    mc "Does that mean you're going to take responsibility?"                            
                    neus_lyra "Yhes(Yes), you can use this body until there are no more eggs to fertilize."
                    scene level3_0_137 with dissolve
                    neus "(That looks very intense.)"
                    scene level3_0_138 with dissolve
                    neus "(But I better escape from here or I'll end up like a kitchen rag.)"
                    neus "(If my obsessive side wants to be his kitchen rag, good for her, but I don't want that.)"
                    scene level3_0_139 with dissolve
                    neus "Uhhh."(multiple=2)
                    neus_lyra "Lhet's share this mhagnifhicent plheashure.\n(Let's share this magnificent pleasure.)" (multiple=2)
                    scene level3_0_140 with dissolve
                    neus "{bt=2}{=lust_style}This feels so good{/bt} {e_heartbt=FF0000}."
                    scene level3_0_141 with dissolve
                    stop char3 fadeout 1.0
                    play char1 double_climax3
                    neus_lyra "{sc=2}I'm cumming{/sc}"(multiple=2)
                    neus "{sc=2}I'm cumming{/sc}"(multiple=2)
                    scene level3_0_142 with dissolve
                    play charM cum1
                    play char1 double_climax2
                    neus_lyra "{sc=2}Oh{/sc}"(multiple=2)
                    neus "{sc=2}Mmmm{/sc}"(multiple=2)
                    stop char1 fadeout 1.0
                    play char3 sex5 volume 0.3 fadein 1.0
                    scene black with dissolve
                    if incest_story:
                        neus "Please... brother, {sc=2}no more.{/sc}"
                    else:
                        neus "Please, {sc=2}no more.{/sc}"
                    neus "I understand how much you love me, and my mistrust is unfounded."
                    neus "But I can't take it anymore; my mind will break."
                    scene level3_0_143 with dissolve
                    neus "I don't want to end up like her."
                    scene black with dissolve
                    play charM slap_hard1 volume 3.0
                    neus "{sc=3}Ah.{/sc}"
                    $ renpy.music.set_volume(1.0, channel='char3')
                    scene level3_0_144 with dissolve
                    if incest_story:
                        neus "Please stop spanking my butt brother; it's all red now."  
                    else:
                        neus "Please stop spanking my butt; it's all red now."                            
                    neus "I won't be able to sit for weeks."
                    mc "It seems like you understand how much I love you."
                    scene level3_0_145 with dissolve                            
                    neus "Thanhk yhou.\n(Thank you.)"
                    scene level3_0_146 with dissolve
                    stop char3 fadeout 1.0
                    mc "But you know, I'm a big fan of the phrase ''If you start something, you have to finish it.''"
                    scene level3_0_147 with dissolve
                    mc "I'm going to give you so much love that you won't have time to think about anything else."
                    neus_lyra "{e_musical2=FFF}"(multiple=2)
                    neus "..."(multiple=2)
                    scene level3_0_147_1 with dissolve
                    if incest_story:
                        neus "Yes! Yes! Fill me up, fill my little belly with lots of your brotherly love."
                    else:
                        neus "Yes! Yes! Fill me up, fill my little belly with lots of love."
                    neus "Go deeper and I want you to kiss me a lot."
                    scene level3_0_147_2 with dissolve
                    mc "You really love my kisses, huh?"
                    scene level3_0_147_3 with dissolve
                    play char1 short_kiss
                    neus "Yes, I'm addicted to your kisses."
                    mc "(It seems like her mind broke a little)"
                    scene level3_0_147_4 with dissolve
                    if incest_story:
                        mc "(But it wouldn't hurt to enjoy my beautiful sisters a bit more.)"
                    else:
                        mc "(But it wouldn't hurt to enjoy my beautiful girlfriends a bit more.)"
                    scene black with dissolve   
                    play char1 double_climax1
                    neus_lyra "I'm cumming"(multiple=2)                          
                    neus "I'm cumming {sc=2}again{/sc}!"(multiple=2)    
                    stop char1 fadeout 0.5                                                
                    scene level3_0_148 with dissolve
                    mc "(I think maybe I went a bit overboard with my display of affection)."                            
                    mc "(It would probably be good to make a few small changes to the house, now that we have one more guest)."
                    if not quest_v2:
                        call addLust(30) from _call_addLust_11
                "Forget it":
                    stop ambience fadeout 1.0
                    scene black with dissolve
                    mc "(For now, I suppose I'll let it slide, but I can't forget there's a new member in the house, so a few small renovations wouldn't hurt.)"
            scene black with dissolve
            centered "{size=+45}During the renovations"
            play music Kazuchi_2_23_am volume 0.3 fadein 1.5
            scene level3_0_149 with dissolve
            neus_lyra "I hope this space is enough."(multiple=2)
            neus "(I hope these toys aren't dangerous.)"(multiple=2)
            scene level3_0_150 with dissolve
            neus "That was an exhausting job."
            scene level3_0_151 with dissolve
            neus_lyra "Well, with that, we've finished remodeling the last room."
            scene black with dissolve
            centered "{size=+60}{color=#cc0066}Phase {color=#cc0066}''Two bodies''"
            $ spell_3_1.is_active=True 
            $ probability_of_pregnancy=50
            $renpy.end_replay()
            if quest_v2 and not questSide_v2_8.completion:
                if questSide_v2_8.description == "''Split personalities'' or ''Don't split''":
                    $ questSide_v2_8.description = "''Don't split''"
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))    
                elif questSide_v2_8.description == "''Split personalities''":
                    $questSide_v2_8.completion=True
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))    
            elif not quest_v2 and not questSide_7.completion:
                if questSide_7.description == "''Split personalities'' or ''Don't split''":
                    $ questSide_7.description = "''Don't split''"
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))    
                elif questSide_7.description == "''Split personalities''":
                    $questSide_7.completion=True
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))      
            $unlock_two_bodies = True
            python:
                achievement.grant("Another_Personality")
                achievement.sync()   
            jump two_bodies_rooms                
        "Don't split (Ending?)":
            scene level3_0_152 with dissolve     
            stop music fadeout 1.0
            neus_yan "Well, I guess we'll be sticking to the original plan."
            scene level3_0_153 with dissolve
            mc "I don't think that's what your other personality meant."
            scene level3_0_154 with dissolve
            $ renpy.music.set_volume(0.1, channel='music')
            play music a_stray_cat_aimed_for_space
            neus "She's right... I think it's best if I get rid of these feelings."
            mc "..."
            scene level3_0_155 with dissolve
            neus "These feelings are wrong."            
            mc "And that bothers you?"
            scene level3_0_156 with dissolve
            neus "I could get very jealous at any moment and want to kill anyone who tries to steal you from me."
            mc "Hmm... I guess that would be bad."
            $ renpy.music.set_volume(0.3,delay=3.5, channel='music')
            scene level3_0_157 with dissolve
            mc "But it's already too late for me."
            if incest_story:
                mc "I love the side of you that struggles to express herself and the side that won’t stop until she gets what she wants—it reminds me of the little sister I grew up with."
            else:
                mc "I love the side of you that struggles to express herself and the side that won’t stop until she gets what she wants—it reminds me of the [neusname] I first met."
            mc "(Although, back then, she didn't reach this level.)"
            scene level3_0_158 with dissolve
            mc "Besides, if you're worried that you might lose control at some point, don't be. "
            mc "I'll give you so much love and attention that your mind will be completely consumed by pleasure—you won't be able to think about anything else."
            mc "So if the reason you want to get rid of these feelings is because of me, don't."
            scene level3_0_159 with dissolve
            mc "I want all of you—every part."
            $ renpy.music.set_volume(0.2,delay=1.5, channel='music')
            scene level3_0_160 with dissolve
            neus "Really?"
            mc "Yes."
            scene level3_0_161 with dissolve
            pause 1.5
            neus "I hope you won't regret this."
            if incest_story:
                neus "Because from now on, you'll officially have your obsessed sister as your {glitch}girlfriend-wife{/glitch}."
            else:
                neus "Because from now on, you'll officially have a {glitch}girlfriend-wife{/glitch} who's obsessed with you."
            neus "And I hope you'll give me lots of love, or I might end up doing something very bad."
            scene level3_0_162 with dissolve
            neus "Hehehe, just kidding."
            mc "That didn't sound like a joke to me, but-"
            play char1 french02
            scene level3_0_162_1 with dissolve            
            neus "Kiss"
            $ renpy.music.set_volume(0.05,delay=2.0, channel='music')
            scene level3_0_163 with fadesex
            play char3 sex4
            neus "{bt=2}{=lust_style}Ah ah ah{/bt}"
            if incest_story:
                neus "Yes, right there brother. That's the spot."
            else:
                neus "Yes, right there. That's the spot."
            neus "That feels so good."
            neus "(I want him to kiss me more.)"
            if incest_story:
                neus "(I can't help it, I'm addicted to my brother's kisses. I can't live without him.)"
            else:
                neus "(I can't help it, I'm a kiss addict. I can't live without him.)"
            scene level3_0_164 with fadesex
            play char3 sex5
            if incest_story:
                mc "I'm gonna fuck you so hard little sister, that you won't be able to think about anything else."
            else:
                mc "I'm gonna fuck you so hard, that you won't be able to think about anything else."
            neus "Yes, this feels so good."
            if incest_story:
                neus "Please pour all your baby-making seed into my womb brother."
            else:
                neus "Please pour all your baby-making seed into my womb."
            neus "I want you to drown all my eggs in your milk."
            mc "Yeah, I'm going to make sure you only have thoughts of being a mother."
            if incest_story:
                neus "Yes, do it brother, {glitch}cum inside{/glitch}"
            else:
                neus "Yes, do it, {glitch}cum inside{/glitch}"
            scene level3_0_165 with dissolve
            stop char3            
            play charM cum1
            play char1 climax1
            neus "Ha"  
            if incest_story:
                neus "I want more, please brother?"     
            else:
                neus "I want more, please?"                    
            scene level3_0_166 with dissolve  
            $ renpy.music.set_volume(0.2,delay=3.0, channel='music')
            mc "Let’s do this every day and build a big family together." 
            neus "{glitch}Yes{/glitch}"
            play char1 french02
            neus "Kiss"
            if set_active_pregnancy: 
                play music TheGirlFromBrasil_Hauser fadein 0.5 fadeout 1.0
                scene level3_0_167 with fadesex
                if incest_story:
                    neus "Hey brother, I don't look weird in this outfit, do I?"
                else:
                    neus "Hey, I don't look weird in this outfit, do I?"
                scene level3_0_168 with dissolve
                neus "This outfit is a bit provocative, don't you think?"
                scene level3_0_169 with dissolve
                neus "Plus, it puts my enormous belly on full display, making it even more embarrassing."
                scene level3_0_170 with dissolve
                mc "I love it; you look so cute, and I adore that lovely huge belly."
                if incest_story:
                    mc "I can't wait to shower you with love and affection, little sister."
                    scene level3_0_171 with dissolve
                    neus "Then what are you waiting for big brother?"
                else:
                    mc "I can't wait to shower you with love and affection."
                    scene level3_0_171 with dissolve
                    neus "Then what are you waiting for?"
                neus "All those words got me really hot."
                neus "I can't take it anymore."
                $ renpy.music.set_volume(0.05,delay=2.0, channel='music')
                scene level3_0_172 with fadesex
                play char3 sex6
                neus "{bt=2}{=lust_style}Oh oh oh{/bt}"
                neus "That feels so good, but my vagina itches for attention."
                neus "I want our son to be born already."
                scene level3_0_173 with dissolve
                if incest_story:
                    neus "So that my vagina can eat my brother's delicious cock again."
                else:
                    neus "So that my vagina can eat your delicious cock again."
                scene level3_0_172 with fadesex
                neus "But anal feels really good too."  
                neus "I suppose that's normal, we've only had anal sex for the last few months."
                neus "So my anus has perfectly molded to the shape of your cock."
                neus "{bt=2}{=lust_style}Ah ah ah{/bt}"
                scene level3_0_174 with dissolve
                stop char3
                play char1 climax1
                neus "{sc=2}I'm cumming{/sc}"
                scene level3_0_175 with dissolve
                play charM cum1
                play char1 climax2
                if incest_story:
                    neus "Ah brother {e_heartbt=FF0000}"  
                else:
                    neus "Ah {e_heartbt=FF0000}"                
                neus "My ass is filled with so much {bt=2}{=lust_style}cum{/bt}"
                neus "It feels so {bt=2}{=lust_style}good{/bt}"
                stop char1 fadeout 0.5
                $ renpy.music.set_volume(0.2,delay=3.0, channel='music')
                scene level3_0_176 with fadesex
                neus "That was intense."
                if incest_story:
                    mc "Hey sis, could you say that phrase I like to hear you say?"
                else:
                    mc "Hey, could you say that phrase I like to hear you say?"
                mc "I know it's hard for you, but could you sa-{w=2.5}{nw}"
                scene level3_0_177 with fadesex
                if incest_story:
                    neus "I love you brother."
                    mc "I love you too sister."
                else:
                    neus "I love you."
                    mc "I love you too."
                mc "Let's build a big, big family."
                scene level3_0_178 with dissolve
                play char1 short_kiss
                neus "{e_heartbt2=FF0000}"
            else:
                scene black with dissolve
                "{size=+8}{color=#ff0000}Pregnant sex censorship activated."
            scene black with dissolve                   
            centered "{size=+60}Ending ''Only One''{w}{size=+120}{color=#cc0066}?"
            if incest_story:
                mc "After turning my sister into my wife, I had many children with her."
            else:
                mc "After turning my childhood friend into my wife, I had many children with her."
            stop music fadeout 1.0
            centered "{size=+60}17 years later"
            play ambience morning_sounds fadein 1.0
            scene level3_0_179 with eyeopen
            if incest_story:
                neus "Good morning, brother."                     
                mc "Good morning, sister."  
            else:
                neus "Good morning, sweetheart."                    
                mc "Good morning, dear."
            scene level3_0_180 with dissolve
            neus "Did you sleep well, huh?"
            mc "Well, it's one of the few times the house has been so quiet."
            scene level3_0_181 with dissolve
            neus "Yes, it's relaxing, but it feels strange that the house is so quiet."
            scene level3_0_182 with dissolve
            if incest_story:
                neus "But I guess we should enjoy it, while the kids are at our auntie's."
            else:
                neus "But I guess we should enjoy it a bit while the kids are at my mother's."
            neus "I hope they don't give her too much trouble."
            scene level3_0_183 with dissolve
            neus "Well, I'm going to the kitchen to prepare breakfast."
            mc "Let me change clothes, and then I'll join you. It's a good opportunity to have a ''nice couple's moment''."
            scene level3_0_184 with dissolve
            if incest_story:
                neus "Hehe, okay big brother. I'll be waiting for you then."
            else:
                neus "Hehe, I understand. I'll be waiting for you then."
            scene black with dissolve
            centered "{size=+60}Phase {color=#cc0066}''MILF''"
            $ renpy.music.set_volume(1.0, channel='music')
            $renpy.end_replay()
            if quest_v2 and not questSide_v2_8.completion:
                if questSide_v2_8.description == "''Split personalities'' or ''Don't split''":
                    $ questSide_v2_8.description = "''Split personalities''"
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))    
                elif questSide_v2_8.description == "''Don't split''":
                    $questSide_v2_8.completion=True
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))    
            elif not quest_v2 and not questSide_7.completion:
                if questSide_7.description == "''Split personalities'' or ''Don't split''":
                    $ questSide_7.description = "''Split personalities''"
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))    
                elif questSide_7.description == "''Don't split''":
                    $questSide_7.completion=True
                    $is_change_quest = True
                    call notify_personalized(_("Side Quest updated"))      
            $unlock_milf = True
            python:
                achievement.grant("Only_One")
                achievement.sync()         
            jump milf_rooms
        "Postpone":
            scene level3_0_152 with dissolve
            neus "What!?"(multiple=2)
            neus_yan "I understand, I will hold onto the memories for now, until you decide"(multiple=2)  
            play sound magical1 volume 0.3 
            $renpy.end_replay()           
            jump rooms            
        