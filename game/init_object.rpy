#Inventory
default  inventory = Inventory()
#default  item
default  item_book_magic = Item(_("{b}Spell Book:{/b} "), image = "icon_book_spell_%s", description = _("Contains sexual spells"))
default  item_tsundere_magazine = Item(_("{b}Magazine:{/b} "), image = "icon_tsundere_magazine_%s", description = _("Contains advice on how to deal with a Tsundere"))
default  key_room_neus = Item(_("{b}Key:{/b} "), image = "icon_key_neus_%s", description = _("[neusname]'s room key"))
default  key_room_attic = Item(_("{b}Key:{/b} "), image = "icon_key_attic_%s", description = _("Attic key"))
default  item_portrait_neus = Item(_("{b}Portrait:{/b} "), image = "icon_portrait_neus_%s", description = _("Portrait of [neusname]"))
default  item_newspaper_living = Item(_("{b}Newspaper:{/b} "), image = "icon_newspaper_living_%s", description = _("Tribute to the Fallen."))
#----------------------------mc---------------------------------
default  mc_photo0 = Item(image = "icon_old_photo0_%s",event_image="inventory/photo/mc_photo0.webp",level=0)
default  mc_photo1 = Item(image = "icon_old_photo1_%s",event_image="inventory/photo/mc_photo1.webp",level=1)
default  mc_photo2 = Item(image = "icon_old_photo2_%s",event_image="inventory/photo/mc_photo2.webp",level=2)
default  mc_photo3 = Item(image = "icon_old_photo3_%s",event_image="inventory/photo/mc_photo3.webp",level=3)
#----------------------------neus---------------------------------
default  neus_photo0 = Item(image = "icon_old_photo0_%s",event_image="inventory/photo/neus_photo0.webp",level=0)
default  neus_photo1 = Item(image = "icon_old_photo1_%s",event_image="inventory/photo/neus_photo1.webp",level=1)
default  neus_photo2 = Item(image = "icon_old_photo2_%s",event_image="inventory/photo/neus_photo2.webp",level=2)
default  neus_photo3 = Item(image = "icon_old_photo3_%s",event_image="inventory/photo/neus_photo3.webp",level=3)
#----------------------------bath---------------------------------
default  bath_photo0 = Item(image = "icon_old_photo0_%s",event_image="inventory/photo/bath_photo0.webp",level=0)
default  bath_photo1 = Item(image = "icon_old_photo1_%s",event_image="inventory/photo/bath_photo1.webp",level=1)
default  bath_photo2 = Item(image = "icon_old_photo2_%s",event_image="inventory/photo/bath_photo2.webp",level=2)
default  bath_photo3 = Item(image = "icon_old_photo3_%s",event_image="inventory/photo/bath_photo3.webp",level=3)
#----------------------------kitchen---------------------------------
default  kitchen_photo0 = Item(image = "icon_old_photo0_%s",event_image="inventory/photo/kitchen_photo0.webp",level=0)
default  kitchen_photo1 = Item(image = "icon_old_photo1_%s",event_image="inventory/photo/kitchen_photo1.webp",level=1)
default  kitchen_photo2 = Item(image = "icon_old_photo2_%s",event_image="inventory/photo/kitchen_photo2.webp",level=2)
default  kitchen_photo3 = Item(image = "icon_old_photo3_%s",event_image="inventory/photo/kitchen_photo3.webp",level=3)
#----------------------------living---------------------------------
default  living_photo0 = Item(image = "icon_old_photo0_%s",event_image="inventory/photo/living_photo0.webp",level=0)
default  living_photo1 = Item(image = "icon_old_photo1_%s",event_image="inventory/photo/living_photo1.webp",level=1)
default  living_photo2 = Item(image = "icon_old_photo2_%s",event_image="inventory/photo/living_photo2.webp",level=2)
default  living_photo3 = Item(image = "icon_old_photo3_%s",event_image="inventory/photo/living_photo3.webp",level=3)
#Rooms
default  select_room='mc'
default  mc_room = Room('mc','icon_mc_room_%s',_("My room"))
default  neus_room = Room('neus','icon_neus_room_%s',_("[neusname]'s room"))
default  bathroom_room = Room('bath','icon_bath_room_%s',_("Bathroom"))
default  kitchen_room = Room('kitchen','icon_kitchen_room_%s',_("Kitchen"))
default  living_room = Room('living','icon_living_room_%s',_("Living room"))
default  house = [mc_room,neus_room,bathroom_room,kitchen_room,living_room]

#Quest
#-----------Main-------------
default empty_quest=Quest()
default questMain_1 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}")
,0,"kitchen",0,"level0_0")
default questMain_2 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
,0,"neus",0,"level0_1")
default questMain_3 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
,0,"neus",0,"level0_2")
default questMain_4 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}")
,0,"kitchen",0,"level1_0")
default questMain_5 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}")
,0,"neus",2,"level1_2")
default questMain_6 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}")
,0,"neus",2,"level1_3")
default questMain_7 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} at {color=#cc0066}Noon{/color}")
,0,"neus",1,"level2_0")
default questMain_8 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
,0,"neus",0,"level2_1")
default questMain_9 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Evening{/color}")
,0,"kitchen",3,"level2_2")
default questMain_select=questMain_1

#-----------Side-------------
default  questSide_1 = Quest(_("Examine the mysterious book on your desk."),0)
default  questSide_2 = Quest(_("Learn the ''Touch'' spell"),0)
default  questSide_3 = Quest(_("Find the key to [neusname]'s room"),1,start=False)
default  questSide_4 = Quest(_("Find the key to the attic"),1,start=False)
default  questSide_5 = Quest(_("Go to the attic and confront her."),3)
default  questSide_6 = Quest(_("Go to [neusname]'s room and choose ''Another personality''"),3)
default  questSide_7 = Quest(_("''Split personalities'' or ''Don't split''"),3)
default  questListSide=[questSide_1,questSide_2,questSide_3,questSide_4,questSide_5,questSide_6,questSide_7]

#-----------Main_v2-------------
default quest_v2 = False

default questMain_v2_1 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color} and ask [neusname] out on a date")
,0,"kitchen",0,"level0_0a")
default questMain_v2_2 = Quest(_("Increase [neusname]'s lust to 3")
,0,"kitchen",0,"level0_0a")
default questMain_v2_3 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}")
,0,"kitchen",0,"level0_0")
default questMain_v2_4 = Quest(_("Increase [neusname]'s lust to 8")
,0)
default questMain_v2_5 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
,0,"neus",0,"level0_1")
default questMain_v2_6 = Quest(_("Increase [neusname]'s lust to 16")
,0)
default questMain_v2_7 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
,0,"neus",0,"level0_2")
default questMain_v2_8 = Quest(_("Increase [neusname]'s lust to 26")
,0)
default questMain_v2_9 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Morning{/color}")
,0,"kitchen",0,"level1_0")
default questMain_v2_10 = Quest(_("Increase [neusname]'s lust to 38")
,0)
default questMain_v2_11 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}")
,0,"neus",2,"level1_2")
default questMain_v2_12 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Afternoon{/color}")
,0,"neus",2,"level1_3")
default questMain_v2_13 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} at {color=#cc0066}Noon{/color}")
,0,"neus",1,"level2_0")
default questMain_v2_14 = Quest(_("Increase [neusname]'s lust to 64")
,0)
default questMain_v2_15 = Quest(_("Go to {color=#cc0066}[neusname]'s room{/color} in the {color=#cc0066}Morning{/color}")
,0,"neus",0,"level2_1")
default questMain_v2_16 = Quest(_("Go to the {color=#cc0066}kitchen{/color} in the {color=#cc0066}Evening{/color}")
,0,"kitchen",3,"level2_2")
default questMain_v2_select=questMain_v2_1

#-----------Side_v2-------------
default questSide_v2_1 = Quest(_("Examine the mysterious book on your desk."),0)
default questSide_v2_2 = Quest(_("Learn the ''Touch'' spell"),0)
default questSide_v2_3 = Quest(_("Use the ''Touch'' spell on [neusname]"),0)
default questSide_v2_4 = Quest(_("Find the key to [neusname]'s room"),1,start=False)
default questSide_v2_5 = Quest(_("Find the key to the attic"),1,start=False)
default questSide_v2_6 = Quest(_("Go to the attic and confront her."),3)
default questSide_v2_7 = Quest(_("Go to [neusname]'s room and choose ''Another personality''"),3)
default questSide_v2_8 = Quest(_("''Split personalities'' or ''Don't split''"),3)
default questListSide_v2 = [questSide_v2_1,questSide_v2_2,questSide_v2_3,questSide_v2_4,questSide_v2_5,questSide_v2_6,questSide_v2_7,questSide_v2_8]

#spell Level
default  spell_0_1=spell(_("Touch"),_("Has aphrodisiac effects, although it can also be used to give energy. (The more {color=#cc0066}relationship level{/color} you have, the more powerful ''Touch'' becomes.)"),"btn_spell_0_1_%s",0,0,questSide_2)
default  level_0=[spell_0_1]

default  spell_1_1=spell(_("Level up and down"),_("Adjusts the level of events in all rooms, increasing or decreasing it."),"btn_spell_1_1_%s",5,1,is_active=False)
default  level_1=[spell_1_1]

default  spell_2_1=spell(_("Pain is pleasure"),_("Turns pain into pleasure"),"btn_spell_2_1_%s",5,2)
default  spell_2_2=spell(_("Object creation"),_("Allows the creation of any object as long as a reference is available"),"btn_spell_2_2_%s",5,2)
default  level_2=[spell_2_1,spell_2_2]

default  spell_3_1=spell(_("Fertilization"),_("Allows you to set the fertilization rate to 100% or 0%."),"btn_spell_3_1_%s",5,3)
default  spell_3_2=spell(_("Personality"),_("Allows the separation of personalities or can make one predominate over another."),"btn_spell_3_2_%s",5,3,start=False)
default level_3=[spell_3_1,spell_3_2]
#tree
default tree=[level_0,level_1,level_2,level_3]
default select_spell=spell_0_1
#Spell for action
default spells_action=[spell_0_1]

# Diary
default diary_neus = [["",_("Missing pages"),"","",_("Missing pages"),"",_("The beginning")],
["",_("Missing pages"),"","",_("Missing pages"),"",_("Routines of the past")],
["",_("Missing pages"),"","",_("Missing pages"),"",_("The change")],
[_("{size=33}I finally finished university and decided to take a vacation since my episodes of unconsciousness became more frequent and prolonged."),
_("{size=33}[firstname] has been acting strange lately."),
"",
"",
"",
"",
_("The present")
]
]


# Diary Incest
default diary_neus_incest = [["",_("Missing pages"),"","",_("Missing pages"),"",_("The beginning")],
["",_("Missing pages"),"","",_("Missing pages"),"",_("Routines of the past")],
["",_("Missing pages"),"","",_("Missing pages"),"",_("The change")],
[_("{size=33}I finally finished university and decided to take a vacation since my episodes of unconsciousness became more frequent and prolonged."),
_("{size=33}My brother has been acting strange lately."),
"",
"",
"",
"",
_("The present")
]
]