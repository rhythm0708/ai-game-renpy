# Characters.
define mc = Character("You", color="#70C3FF")
define boss = Character("Bob", color="#43469D")
define hr = Character("Karim", color="#1AD87A")
define pr = Character("Madison", color="#FFDD1B")

default company_name = "Fintek"

label start:
    scene bg room
    jump exposition

label exposition:
    "This is {color=#f00}[company_name]{/color}"

    # show company backdrop

    "[company_name] was once a thriving company, but it has been on a downward trajectory since 2015."

    "After a bad investment in {color=#f00}CorgiCoin{/color}, customers started losing trust and sales have been declining year-over-year."

    "The company is desperately in search of a strategic leader to guide them in the right direction and win back customers."

    "That's where you come in."

    # show main character

    "You are a tech consultant for {color=#f00}TechRight{/color} hired to overhaul the company’s competitive strategy."

    "You’re relatively new, but you think you have what it takes to turn this company around and win back customers."

    "That’s what it says on your business card anyway."

    # flash business card

    jump scenario1

label scenario1:
    # scene office with fade

    "It's your first day on the job."

    "You’re sitting at your desk in front of a mass of spreadsheets when your boss approaches you with a laptop in hand."

    show boss neutral at center with moveinright

    boss "Hey, so we’ve been looking at trends in AI and we see that a lot of major companies are beginning to incorporate it."

    boss "Apparently it can speed up workflow and help the company save costs—it sounds like exactly what we need right now!"

    boss "We’re thinking of doing a trial on it in our hiring system. It seems like the safest place to start with this kind of thing."
    
    boss "Here. This is what Karim, the head of HR, showed me this morning."

    # computer screen with AI screening program

    "{i}Your boss opens their laptop and gestures to the screen. On it, you see the familiar upload boxes, percentages, and CAPTCHAs of an A.I software{/i}"

    "It’s an AI resumé-screening program. It scans resumé and cover letters for specific requirements and keywords, and returns a score for each candidate."

    "You’re the tech consultant, so, what do you think? We need your guidance on how we can most effectively implement this AI tool."

    menu:
        mc "My first decision. Do I:"

        "Encourage immediate company-wide deployment of the AI software":
            mc "Let’s rip the band aid off—this will maximize cost savings, and we’ll eventually need it anyway"
            jump scenario2

        "Use AI to recommend and filter resumés, but have staff look over any that are flagged or rejected":
            mc "Adding a human touch might make the transition softer and preserve trust"
            jump scenario2

        "Keep human screening for now, and pilot AI in low-risk, supporting roles":
            mc "This might not save much money in the short-term, but it's a cautious approach"
            jump scenario2

label scenario2:
    "{i}You’re sitting at your desk when a man walks up to you. They flash a smile and wave.{/i}"

# This ends the game.

return
