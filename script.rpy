#Characters
define me = ("Me")
define n = ("Narrator")

# The game starts here.
label start:
    $bond_big_sister = 0
    $bond_young_sister = 0
    $fame = 0

    # Intro
    n "\"Hello! welcome to our game.\""
    n "\"I am the developer of this game.\""
    n "\"I hope you will get back some good experiance.\""
    n "\"In this game you are high school student at the start of the lesson\""
    n "\"Good luck have fun.\""
    jump Chapter_1

#Chapter 1
label Chapter_1:
    # First scene
    n "\"You just getting up in the morning.\""
    me "what time is it?"
    n "\"you looking to the alarmclock.\""
    # Insert alarmclock
    n "\"Look like you have 45 minutes before you're getting late.\""
    n "\"You dressing up and preparing to school.\""
    #Main character cutscreen 
    me "(I hope my first day gonna be ok.)"
    n "\"You decide walking to school. (Your school is 143 Meters from your home.)\""
    n "\"You are arrived at school.\""
    me "(I heard it has opening ceremony.)"
    me "(Should I go join.)"

#Opening Ceremony
menu Opening_Ceremony:
    "\"Attend to opening ceremony.\"":
        $fame =+ 1
        jump Chapter_1_OpeningCeremony

    "\"Straight to your classroom.\"":
        jump Chapter_1_NotOpeningCeremony

#Join opening ceremony
label Chapter_1_OpeningCeremony:
    n "\"You are arrived at the school main hall.\""
    n "\"You meet and have greeting with a lot of people.\""
    me "(looking around)"
    n "\"You see a girl who stand alone at the corner\""

#Not join opening ceremony
label Chapter_1_NotOpeningCeremony:


    return
