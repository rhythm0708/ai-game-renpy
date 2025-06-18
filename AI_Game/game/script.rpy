# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define MC = Character("You", color="#70C3FF")
define boss = Character("Bob", color="#43469D")
define HR = Character("Karim", color="#1AD87A")
define PR = Character("Madison", color="#FFDD1B")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

#Scenario 1 - Chapter 1
    "You’re sitting at your desk in front of a mass of spreadsheets when your boss approaches you with a laptop in hand."

    boss "Hey, so we’ve been looking at trends in AI and we see that a lot of major companies are incorporating it."
    boss "Apparently it can speed up workflow and help the company save costs—it sounds like exactly what the company needs right now!"
    boss "We’re thinking of doing a trial on it in our hiring system. It seems like the safest place to start with this kind of thing."
    boss "So we need your help."
    boss "Here, this is what Karim, the head of HR, showed me this morning."

    MC "My first decision. Do I:"

menu:

        "Encourage immediate company-wide deployment of the AI software":
            jump scenario1a

        "Use AI to recommend and filter resumés, but have staff look over any that are flagged or rejected":
            jump scenario1b

        "Keep human screening for now, and pilot AI in low-risk, supporting roles":
            jump scenario1c

label scenario1a:
    MC "Let’s rip the band aid off—this will maximize cost savings, and we’ll eventually need it anyway"
    jump scenario1d

label scenario1b:
    MC "Adding a human touch might make the transition softer and preserve trust"
    jump scenario1d

label scenario1c:
    MC "This might not save much money in the short-term, but it's a cautious approach"
    jump scenario1d

label scenario1d:
    MC "How does that sound?"


    # This ends the game.

    return
