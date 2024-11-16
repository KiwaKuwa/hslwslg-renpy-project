#Characters
define s = ("Someone")
define a = ("Akemi")
define t = ("Teacher")
define p = ("Student president")

# The game starts here.
label start:

    $ bond = 0

    # Intro

    $ me = renpy.input("What is your name.")

    #Chapter 1 start
    call Chapter_1

    if bond == 2:
        call Lovely_Route
        call ClassroomScreen_R1
        call Afternoon_Break_R1            
    if bond == 0:
        call ClassroomScreen_R2
        call Afternoon_Break_R2
    if bond == 2:
        call After_School

return
