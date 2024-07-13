# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = ("Me")
define n = ("Narrator")

# The game starts here.

label start:
    $bonds = 0

    # Intro
    n "\"Hello! welcome to our game.\""
    n "\"I am the developer of this game.\""
    n "\"We all hope you will get back some good experiance.\""
    n "\"In this game you are high school student at the start of the lesson\""
    n "\"Good luck have fun.\""
    jump Chapter_1

label Chapter_1:
    # First scene
    n "\"You just getting up in the morning.\""
    me "what time is it?"
    n "\"you look the alarmclock.\""
    

    return
