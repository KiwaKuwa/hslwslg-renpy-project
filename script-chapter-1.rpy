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
        $ fame =+ 1
        jump Chapter_1_OpeningCeremony

    "\"Straight to your classroom.\"":
        jump Chapter_1_NotOpeningCeremony
   
    
#Join opening ceremony
label Chapter_1_OpeningCeremony:
    n "\"You are arrived at the school main hall.\""
    n "\"You meet and have greeting with a lot of people.\""
    n "\"After the opening ceremony end.\""
    n "\"You go outside the school main hall and looking for classrooms list to check your classroom.\""
    me "(looking around)"
    n "\"You see a girl who stand alone at the corner.\""
    n "\"She looks at you.\""

#First greeting1
menu How_you_greeting:
    "\"Hi can I help you?\"":
        $ bond =+ 1
        $ fame =+ 1
        jump Greeting_with_her1
    
    "(...)":
        jump Nothing
    
#First greeting with little girl1   
label Greeting_with_her1:
    me "Hi err... can I help you."
    s "(........)"
    me "What is your name."
    s "...."
    me "(she look very shy.)"
    h "My name is Haruka."
    h "I want to check my classroom but there are a lot of people here."
    n "\"You look at her.\""
    me "(She is so tiny no wonder why she cannot do it by herself.)"
    me "Um... I haven't seen it yet."
    me "Let me see."
    n "\"You went in the crowd of students.\""
    me "(Carefully check the student list in each classroom.)"
    n "\"You found that you are in the same classroom.\"" 
    me "Oh! look like we are in the same classroom."
    h "Really!"
    h "Er... thankyou for helping me."
    h "You are really kind."
    
    return

#You just...
label Nothing:
    me "(........)"
    me "(She look very shy.)"
    me "Wait!" 
    n "\"She walk away.\""
    n "After that,"
    jump Chapter_1_NotOpeningCeremony

#Not join opening ceremony
label Chapter_1_NotOpeningCeremony:
    n "You walk stragiht the student list broad to check your classroom."
    me "(Checking..)"
    n "\"You walking to your classroom.\""

    return

#Bond >= 1
label Lovely_Route:
    n "\"After that,\""
    n "\"You walking with her to the classroom.\""
    n "\"While walking you have notice something.\""
    me "(Why she look unhappy all the time.)"
    me "(She look so nervous and not smile at all.)"

#Your Asking
menu Ask:
    "\"Are you ok?\"":
       $ bond =+ 2
       jump Lovely_Conversation
    "(Say nothing)":
       jump Silent

#Walking screen    
label Lovely_Conversation:
    n "\"She look at you with worried look.\""
    h "I worry if I unable to compatible with the other in the class."
    h "I alway avoid people and never have a close friend before."
    h "Everyone approached me by thinking to take advantage of me."
    h "I feel like I can't trust any people again."
    h "But something happended this day make me feel different."
    h "I think maybe I can trust someone again."
    me "Can I be your friend."
    me "Listen! I promise."
    me "I will never betrey you."
    me "Whatever anything happend."
    me "Then...."
    me "Pls"
    n "\"She start crying.\""
    n "\"But... it not come from sadness.\""
    n "\"She looking at you.\""
    n "\"Finally\""
    me "(She is smiling.)"
    h "Yes!"
      
    return
    
#Say nothings
label Silent:
    n "\"You thinking it not your ploblem or you just can't do any thing to make it better.\""
    me "(................................)"
    h "(................................)"
    n "\"We are not talking to each other until arrive the class.\""
   
    return

#Arrived at classroom
label ClassroomScreen:
    n "\"You comein the classroom.\""
    n "\"There are no people and you can choose any seat you want.\""
    n "\"You sit at seat which near the window to take a good view outside.\""
    
    return

#bond = 2
label WeRFriend:
    n "\"Her seat is next to you.\""
    n "\"The class is start.\""
    t "Hello everyone I'm the teacher who will take care of you."
    t "I think you all are new here."
    t "Let introduce your self in front of the class."
    n "\"Everyone were introduced themself.\""
    n "\"It time that Haruka have to introduce her self.\""


    n "\"She walk back to her seat.\""
    me "(She is sobing.)"
    n "\"You look at her.\""
    me "(I must do something.)"
    me "(....)"
    h "I'm did it badly."
    h "I'm worst."
    h "(Sobing)"
    me "It okay."
    me "It fine."
    me "I stay here beside you."

    return

#bond = 1
label Just_someone_you_Know:  
    n "\"Her seat is next to you.\""
    n "\"The class is start.\""
    t "Hello everyone I'm the teacher who will take care of you."
    t "I think you all are new here."
    t "Let introduce your self in front of the class."
    n "\"Everyone were introduced themself.\""
    n "\"It time that Haruka have to introduce her self.\""
  
    n "\"She walk back to her seat.\""
    me "(She is sobing.)"
    n "\"You look at her.\""
    me "(....)"
    h "I'm did it badly."
    h "I'm worst."
    h "(Sobing)"
    n "\"But nothing you can do.\""

    return

#bond = 0
label IDKAnythings:
    n "\"You waitng to the class to start.\""
    n "\"20 minutes later\""
    n "\"The class is start.\""
    t "Hello everyone I'm the teacher who will take care of you."
    t "I think you all are new here."
    t "Let introduce your self in front of the class."
    n "\"Everyone were introduced themself.\""
    n "You normally introduce yourself."
    n "Even it so noisy in this class."
    n "But the only thing you care is studing."
    n "You studing until the last subject."

    return
   