#Characters
define n = ("Narrator")
define s = ("Someone")
define h = ("Hazuka")
define t = ("Teacher")

# The game starts here.
label start:
    $ bond = 0
    $ fame = 0

    # Intro
    n "\"Hello! welcome to our game.\""
    n "\"I am the developer of this game.\""
    n "\"I hope you will get back some good experiance.\""
    n "\"In this game you are high school student at the start of the lesson.\""
    n "\"Good luck have fun.\""
    $ me = renpy.input("What is your name.")

    #Chapter 1 start
    call Chapter_1

    if bond == 1:
        call Lovely_Route

    call ClassroomScreen

    if bond == 2: 
        call WeRFriend

    if bond == 1:
        call Just_someone_you_Know

    if bond == 0:
        call IDKAnythings
        

return
