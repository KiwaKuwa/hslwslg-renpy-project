#Chapter 1
label Chapter_1:

    scene bedroom_bg
    with fade

    # First scene bedroom
    "You just getting up in the morning."

    me "what time is it?"

    "you looking to the alarmclock."
    
    "Look like you have 45 minutes before you're getting late."

    "You look out the window it a shinyday outside."

    "You grab your smartphone to check the mail and twitter."

    "You dressing up and preparing to school."
    
    me "(I hope my first day gonna be ok.)"

    scene apartment_bg
    with fade

    "You come out of your apartment."

    "You decide walking to school. (Your school is 143 Meters from your home.)"

    scene footpath_bg
    with fade

    # outside scene while walking
    "While you walking you have seen a lot of people."

    "The people that you never met before."

    "They all live with a smile and depend on each other."

    "Walk passed a lot of places that you never went in."

    "You have seen a lot of students who exited about school and talking to eachother."

    "But it only you who walking alone."

    "Now you feel more lonely."

    "In the peaceful world."

    "There are somethings missing."

    "You just hope this day to be a good they for you to change yourself."

    # bakery scene
    "You stop at the bakery to get some bread for breakfast."

    # melon bread picture
    "You got the melon bread."

    "It look so tasty and you can't wait to try it."

    "You walk along the footpath."

    "Thinking of yourself and sign." 

    #30 minutes later
    "You are arrived at school."

    scene schoolpark_bg
    with fade

    "You sit on the bench and having breakfast."

    "You don't know what to do."

    "Then you playing your smartphone and listen to the music."

    "There are a lot of people you never met before."

    "You think you should get to know the other people."

    "You meet and have greeting with a lot of people."

    "You think maybe you can find some friends here."

    "You sit on the seat and looking around."

    "Now you looking for a classroom broad to check your classroom."

    me "(looking around)"

    "You see a girl who stand alone at the corner."

    show akemi at center
    with dissolve

    "She looks at you."

#First greeting1
menu How_you_greeting:
    "\"Hi can I help you?\"":
        $ bond =+ 2
        jump Greeting_with_her
    
    "(...)":
        jump Nothing
    
#First greeting with little girl
label Greeting_with_her:

    me "Hi err... can I help you."

    s "(........)"

    me "What is your name."

    s "...."

    me "(she look very shy.)"

    a "My name is Hazuka Akemi."

    a "I want to check my classroom but there are a lot of people here."

    a "I can't see anythings."

    a "Can you help me checking."

    a "My studentID is 1001."

    "You look at her."

    me "(She is so tiny no wonder why she cannot do it by herself.)"

    me "Yes, sure!"

    me "I haven't seen it yet."

    hide akemi

    me "Let me see."

    "You went in the crowd of students."

    me "(Carefully check the student list in each classroom.)"

    "You found that you are in the same classroom." 

    me "Oh! look like we are in the same classroom."

    show akemi at center
    with dissolve

    a "Really!?"
    
    me "Do you wanna walk with me I'll go to the classroom."

    a "Yes.."

    a "Er... thankyou for helping me."

    me "No problem"

    return

#You just...
label Nothing:

    me "(........)"

    me "(She look very shy.)"
   
    me "Wait!" 

    hide akemi
    
    "She walk away."
    
    "After that,"
    
    "You walk stragiht the classroom broad to check your classroom."
    
    me "(Checking..)"

    "You walking to your classroom."

    return

#Bond = 2
label Lovely_Route:
    
    "Before you walk to your classroom."

    "You have a conversation with her."

    me "Why did you come to this school?"

    a "Because it not too far from my home."

    a "How about you?"

    me "Me too it just about 140 meters from my home."

    me "I always walk to school." 

    "You don't know what to say next."

    "You look at her."

    me "(Why she look unhappy all the time.)"

    me "(She look so nervous.)"

    me "(Look like she doesn't fine.)"

    me "Are you ok?"

    me "Your expression doesn't look good."

    me "You can tell me maybe I can help you."

    "She look at you with worried look."

    a "I worry if I unable to compatible with the other in the class."

    a "I can't back when some people talked to me."

    a "When I was in the middle school I didn't have anyone to talk to except my parents."

    me "Oh I sorry to hear that."

    me "But did you know."

    me "I think if it ok that we can be friend."

    a "So that mean you want to be friend with me."

    me "Yes"

    me "It fine right."

    a "It fine if you can accept me."

    me "Sure!"

    me "I don't have any problem with that."

    return
    
#Arrived at classroom
label ClassroomScreen_R1:

    scene classroom_bg
    with fade

    "You come in the classroom."

    "There are nobody here." 

    "Then you can choose any seat you want."

    "You sit at seat which near the window to take a good view outside."

    "Her seat is next to you."

    "Teacher comein the class."

    t "Hello everyone I'm the teacher who will take care of you."

    t "I think you all are new here."

    t "Let introduce your self in front of the class."

    "Everyone were introduced themself."

    "You can't remember all of them but there are some of them you have met before in the ceremony."

    "It time that Akemi have to introduce her self."

    show akemi 
    with dissolve

    a "Hello m-my name is Hazuka Akemi."

    a "N-Nice to meet you."

    hide akemi

    "She walk back to her seat."

    "Other people looking at her and laughing."

    "You wonder why they laughing at her cause she just shuttering."

    "You look at her."

    me "(She is sobing.)"

    me "(I must do something.)"

    me "(....)"

    me "It okay you did nothing wrong."

    show akemi
    with dissolve

    a "I did it badly."

    a "I'm worst."

    a "(Sobing)"

    me "It okay."

    me "Everyone just doesn't understand you."

    me "It fine."

    me "You just try to improve and get better next time."

    me "Don't pay attenion to them."  

    a "Thank you."

    a "You make me feel a bit better."

    hide akemi

    me "Now you have to pay attention to class."

    me "(I think she so emotional.)"

    me "(Of course she used to be lonely for a while.)"

    "The class is starting."

    "After that you just pay attention to the lesson as usual."   

    "You especially attentive to studying with some subject like Math."

    "That because you have to get more scores for studing at university in the future."

    return

label ClassroomScreen_R2:

    scene classroom_bg 
    with fade

    "You comein the classroom."

    "There are nobody here." 

    "Then you can choose any seat you want."

    "You sit at seat which near the window to take a good view outside."

    "There are a girl who come in the class."

    me "(I remember I met her before at the hall.)"

    "She sit on the seat next to you."

    me "Hi"

    me "My name is ..."

    me "Nice to meet you."

    show akemi
    with dissolve

    a "Er...."

    a "My name is Akemi."

    a "N..Nice to meet you."

    hide akemi

    "After that we don't to eachother anymore."

    "Now everyone is at the class."

    "Teacher comein the class."

    t "Hello everyone I'm the teacher who will take care of you."

    t "I think you all are new here."

    t "Let introduce your self in front of the class."

    "Everyone were introduced themself."

    "You can't remember all of them but there are some of them you have met before in the ceremony."

    "It time that Akemi have to introduce her self."

    show akemi
    with dissolve

    a "Hello m-my name is Hazuka Akemi"

    a "N-Nice to meet you."

    hide akemi

    "She walk back to her seat."

    "Other people looking at her and laughing."

    "You wonder why they laughing at her cause she just shuttering."

    "You try to not look at her."

    "Because you don't want to embrass her."

    "The class is starting."

    "After that you just pay attention to the lesson as usual."   

    "You especially attentive to studying with some subject like Math."

    "That because you have to get more scores for studing at university in the future."

    return

label Afternoon_Break_R1:

    "You had studied Math and Physic."

    me "Studied Math and Physic make me so tired."

    me "Finaly it time for lunch."
    
    "You walk to the canteen."

    scene canteen_bg   
    with fade 

    "You see a lot of dishes."

    me "(But what I gonna get for lunch.)"

    me "Curry is sound great."

    "You got curry for your meal."

    "You looking for the seat and saw that Akemi having meal alone."

    show akemi
    with dissolve

    me "Excuse me can I take that seat."

    a "Er..."

    a "Sure."

    "You take that seat and having your lunch."

    "We don't talking to eachother and pay attention to the meal."

    "You look at her."

    me "(She is so cute...)"

    me "(How this girl doesn't has any friend.)"

    "She stop eating."

    a "What on my face ?"

    me "Er... Nothing!."

    me "Look like you enjoy your food very much."

    a "Yes, it so delicous."

    a "........."

    a "Thank you to sat with me."

    me "(She is very cute.)"

    me "(My heart gonna jump off.)"

    "Your face turn to red."

    a "Are you listening ?"

    a "What wrong."

    a "Are you get cold?"

    me "I'm fine!"

    me "About that"

    me "You don't have to thank me."

    me "I just want to do it."

    hide akemi

    return

label Afternoon_Break_R2:

    $ bond =+ 2

    "You had studied Math and Physic."

    me "Studied Math and Physic make me so tired."

    me "Finaly it time for lunch."

    "You walk to the canteen."

    scene canteen_bg
    with fade

    "You see a lot of dishes."

    me "(But what I gonna get for lunch.)"

    me "Curry is sound great."

    "You got curry for your meal."

    "You looking for the seat and saw that Akemi having meal alone."

    show akemi 
    with dissolve 

    me "Excuse me can I take that seat."

    a "Er..."

    a "Sure."

    "You take that seat and having your lunch."

    "We don't talking to eachother and pay attention to the meal."

    me "You know"

    me "About your introduction."

    me "It okay."

    me "Everyone just doesn't understand you."

    me "It fine."

    me "You just try to improve and get better next time."

    me "Don't pay attenion to them who laughed at you."

    "She don't talk back."

    "But she just smile a little."

    me "(She is so cute.)"

    me "..."

    me "I finished my meal."

    me "I gotta go."

    me "See ya!"

    a "Wait...."

    a "Thank you!"

    a "You make me feel a bit better."

    hide akemi

    "After said that she ran away."

    return

label After_School:
 
    scene classroom_bg
    with fade

    "You walk back to the classroom."

    "You preparing yourself and pay attention to the afternoon class."

    "2 hours later."

    me "Finaly the class is done."

    me "(Where is Akemi?)"

    me "(She left classroom so quickly.)"

    "You left the school."

    scene footpath_bg 
    with fade

    "On the way to your home."

    "You see Aoi walking following the path."

    me "Hey Akemi"

    "You call her quietly."

    show akemi
    with dissolve

    a "Eh!"

    "She was trembled."

    me "Sorry"

    me "Did I scare you?"

    me "I think we walk to the same direction."

    me "Would it be okay, if we walked together?"

    a "Yeah it fine."

    a "I think...."

    "We walking together and now you arrive at your apartment."

    scene apartment_bg 
    with fade

    me "See you later Bye!"

    a "Wait...."

    hide akemi

    "You say bye to Akemi and walk in the lobby."

    "You walk to the sceond floor."

    "Now you are in front of your room."

    show akemi 
    with dissolve

    me "???"

    a "!??"

    me "Are we in same apartment...?"

    return
    