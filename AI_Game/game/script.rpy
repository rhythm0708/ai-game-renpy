# Characters.
define mc = Character("You", color="#70C3FF")
define boss = Character("Boss", color="#43469D")
define hr = Character("Karim", color="#1AD87A")
define pr = Character("Madison", color="#FFDD1B")

default company_name = "{color=#297E89}Fintek{/color}"
default crypto_coin = "{color=#1AD87A}CorgiCoin{/color}"

# Stats.
default people_score = 50
default process_score = 50
default tech_score = 50
default policy_score = 50
default impact_score = 50

default company_money = 250

# HUD.
screen money_hud():
    tag overlay
    zorder 10

    frame:
        xalign 1.0
        yalign 0.0
        padding (20, 10)
        background "#0008"

        hbox:
            spacing 10
            image "images/UI/icon money.png" zoom 0.05
            text "Money: $ [company_money]k" size 24 color "#fff"
default hover_text = ""

# Transforms.
transform bobble:
    yoffset 0
    linear 0.2 yoffset 25
    linear 0.2 yoffset 0
    linear 0.2 yoffset 25
    linear 0.2 yoffset 0
    linear 0.2 yoffset 25
    linear 0.2 yoffset 0

init python:
    style.window.padding = (10, 10, 10, 10)

label start:
    scene smoke
    show screen money_hud
    play music "audio/office theme.mp3"
    $ renpy.music.set_volume(0.15, channel='music')
    jump exposition

label exposition:
    "This is [company_name]."

    show fintek with dissolve

    "[company_name] was once a thriving company, but it's been on a downward trajectory since 2015."

    "After a bad investment in [crypto_coin], customers started losing trust and sales have been declining year-over-year."

    "The company is desperately in search of a strategic leader to guide them in the right direction and win back customers."

    "That's where you come in."

    hide fintek with dissolve
    # fix timing
    show silhouette with dissolve

    "You are a tech consultant from {color=#f00}TechRight{/color} hired to overhaul the company’s competitive strategy."

    "You’re relatively new, but you think you have what it takes to turn this company around."

    show business card with dissolve

    "That’s what it says on your business card anyway."

    "For some reason when we printed it, only the name was smudged out. I'll have to fix that."

    hide business card with dissolve

    "{color=#f00}{i}NOTE: Conserve your money! If you run low on money by the end of the simulation, the company will go out of business. Make decisions carefully!{/color}{/i}"

    hide silhouette with dissolve
    jump scenario1

label scenario1:
    scene office with fade

    "It's your first day on the job."

    "{i}You’re sitting at your desk in front of a mass of spreadsheets when your boss approaches you with a laptop in hand.{/i}"

    show boss neutral at center with moveinright 

    boss "Hey, so we’ve been looking at trends in AI and we see that a lot of major companies are beginning to incorporate it."

    show boss neutral at bobble

    boss "Apparently it can speed up workflow and help the company save costs. It sounds like exactly what we need right now!"

    show boss neutral at bobble

    boss "We’re thinking of doing a trial on it in our hiring system. It seems like the safest place to start with this kind of thing."

    show boss neutral at bobble

    boss "Here. This is what Karim, the head of HR, showed me this morning."

    # computer screen with AI screening program

    "{i}Your boss opens their laptop and gestures to the screen. On it, you see the familiar upload boxes, percentages, and CAPTCHAs of an A.I software.{/i}"

    show boss neutral at bobble

    boss "It’s an AI resumé-screening program. It scans resumé and cover letters for requirements and keywords, and returns a score for each candidate."

    show boss neutral at bobble

    boss "You’re a tech consultant, what do you think? We need your guidance on how to best implement this tool."

    show screen decision_menu_1

    "How should the company implement its AI hiring tool?"
    

screen decision_menu_1():
    modal True

    frame:
        # background None
        background "#303030b2"
        xfill True
        yfill True
        xalign 0.5
        yalign 0.3
        padding (40, 30)
        has vbox:
            spacing 25
            xalign 0.5
            yalign 0.3

        vbox:
            spacing 15
            xalign 0.5
            yalign 0.2

            textbutton "Encourage immediate company-wide deployment of the AI software.":
                text_color "#333333"
                background "#CCCCCCCC"
                padding (25, 20)
                xsize 900
                hover_background "#AAAAAACC" 
                action Jump("choice_1a")

                hovered SetVariable("hover_text", "{i}This will maximize cost savings, and we’ll eventually need it anyway (+$100k){/i}")
                unhovered SetVariable("hover_text", "")
            
            null height 10

            textbutton "Use AI to recommend and filter resumés, but have staff look over any that are flagged or rejected.":
                text_color "#333333"
                background "#cccccccc"
                padding (25, 20)
                xsize 900
                hover_background "#AAAAAACC" 
                action Jump("choice_1b")

                hovered SetVariable("hover_text", "{i}Adding a human touch might make the transition softer and preserve trust{/i} (-$30k)")
                unhovered SetVariable("hover_text", "")

            null height 10

            textbutton "Keep human screening for now, and pilot AI in low-risk, supporting roles.":
                text_color "#333333"
                background "#CCCCCCCC"
                padding (25, 20)
                xsize 900
                hover_background "#AAAAAACC" 
                action Jump("choice_1c")

                hovered SetVariable("hover_text", "{i}This might not save much money in the short-term, but it's a cautious approach{/i} (-$150k)")
                unhovered SetVariable("hover_text", "")

        null height 20

        text hover_text size 24 color "#CCCCCC" xalign 0.5 italic True

label choice_1a:
    $ process_score += 20
    $ people_score -= 10
    $ impact_score -= 10
    $ company_money += 100

    hide screen decision_menu_1
    "{i}You encourage the boss to immediately deploy the AI tool and fix problems as they come up.{/i}"
    mc "Don't let your company fall behind your competitors."
    "{i}Your boss nods. He leaves to give instructions to the rest of the staff.{/i}"

    hide boss with moveoutleft
    jump scenario2

label choice_1b:
    $ process_score += 10
    $ people_score += 10
    $ company_money -= 30

    hide screen decision_menu_1
    mc "It's a good idea to keep employees part of the process, especially during the early stages."
    mc "It reduces liability if things come up, and backlash from the public from cutting jobs."
    "{i}Your boss nods, scribbling notes onto a notepad.{/i}"
    "{i}He leaves to inform the rest of the staff.{/i}"

    hide boss with moveoutleft
    jump scenario2

label choice_1c:
    $ process_score -= 10
    $ tech_score -= 10
    $ people_score += 10
    $ company_money -= 150

    hide screen decision_menu_1
    mc "AI is still a burgeoning technology. We shouldn't implement it so recklessly."
    mc "Why don't we start off small scale? Let's just use it to... answer frequently-asked candidate questions and we can move from there."
    "{i}Your boss looks disappointed, he scratches his head.{/i}"
    "{i}He reluctantly nods and takes your advice, but warns that the company must find other ways of cutting costs.{/i}"
    "{i}You get a nervous feeling. You feel that conversation could have gone better.{/i}"

    hide boss with moveoutleft
    jump scenario2


label scenario2:
    scene office with fade

    "{i}You’re sitting at your desk when a man walks up to you. His reflective glasses momentarily blind you.{/i}"

    show karim neutral at center with moveinright 

    hr "Hey! I’m Karim from HR."

    hr "I’ve been working at [company_name] since 2015. I've heard some good things about you from the boss. Thanks for helping out."

    show karim talking

    hr "So why was I here again? … Oh yeah!"

    show karim talking

    hr "We were thinking of extending the use of AI in our hiring processes."

    hr "The resumé-screening system hasn’t raised any flags so far, so we were thinking of setting up an AI system for interviewing."

    hr "Have you heard of one-way interviews?"

    hr "It’s this new system where candidates can get interviewed by a program that records their responses to pre-set questions."

    hr "No interviewer, just… a camera, a timer, and a script."

    menu:
        hr "What do you think about it?"

        "Sounds dystopian.":
            mc "I can't lie, that sounds pretty dystopian."
            mc "It strips away so much of the human element in hiring."
            hr "That's exactly the concern. But executives love the efficiency."
        "Pretty cool I must say.":
            mc "It's definitely innovative. It would save so many hours coordinating and conducting interviews."
            mc "Plus, candidates can record responses in their own time."
            hr "Right? HR loves the flexibility. But not everyone is a fan."
    
    hr "Anyways, we've been offered a software package by a high-level vendor that does just this."

    hr "They're giving us a steep discount, and executives are drooling over the promised benefits."

    hr "But I wanted to consult with you before we moved forward with the decision."

    hr "So, any advice? What should we tell the vendor?"

    menu:
        hr "What should we tell the vendor?"

        "Go for it — let's roll it out (+$80k)":
            $ process_score += 20
            $ tech_score += 20
            $ impact_score -= 20
            $ people_score -= 20
            $ company_money += 80

            "{i}This system seems promising and it hasn’t caused issues so far. This could save the company serious time and money.{/i}"
            hide karim with moveoutleft
            jump scenario3
        "Request that the vendor submit fairness audits and pass bias-testing standards (-$100k)":
            $ process_score -= 10
            $ tech_score += 20
            $ company_money -= 100

            "{i}They might not do it, and this might take a while. But this would help maintain fairness and trust within candidates.{/i}"
            hide karim with moveoutleft
            jump scenario3
        "Propose launching a controlled pilot in one department (-$20k)":
            $ process_score += 10
            $ impact_score += 10
            $ company_money -= 20

            "{i}Collect data, monitor feedback from candidates, before deciding if it’s worth scaling up. Slower for sure—but safer, and more methodical.{/i}"
            hide karim with moveoutleft
            jump scenario3

label scenario3:   
    scene office with fade
    show boss neutral at center with moveinright

    boss "So I read this article."

    mc "What's it about?"

    show boss neutral at bobble

    boss "It’s about this wild new AI tech that can analyze behavior in video interviews."

    show boss neutral at bobble

    boss "It can track tone, facial expressions, gestures—even the candidate’s background!"

    show boss neutral at bobble

    boss "It uses this data to predict which candidates would perform best if hired."

    mc "Definitely sounds cutting edge. I've heard about it as a concept, but I didn't know they were rolling it out so soon."

    show boss neutral at bobble

    boss "And guess what? I checked in with our vendor, and surprise, surprise—it’s available as an add-on to our software package!"

    show boss neutral at bobble

    boss "I’m thinking we roll it out immediately. You know—weed out the underperformers before we bring them onto our team."

    mc "Hm..."

    show boss neutral at bobble

    boss "What, not sold? It has proven results!"

    boss "But I understand."

    boss "Your job is to make this palatable for people and profitable for the company."

    show boss neutral at bobble 

    boss "That’s why I’m telling this to you."

    boss "So you tell me: what’s the best way we can implement this to avoid any blowback."

    menu:
        mc "This is a tough one. What should I recommend?"

        "Start with an industry-standard behavioral dataset (-$100k)":
            $ process_score += 20
            $ tech_score += 20
            $ impact_score -= 10
            $ company_money -= 100

            "{i}Leverage widely accepted benchmarks for professional behavior and communication. It works, and avoids the headache of collecting data on company culture{/i}"
            hide boss with moveoutleft
            jump scenario4
        "Train the system on employee behavior data (-$50k)":
            $ process_score += 30
            $ tech_score += 30
            $ impact_score -= 20
            $ people_score -= 20
            $ company_money -= 50

            "{i}This creates a highly tailored system based on our company culture, but it raises the risk of employee backlash and data security concerns{/i}"
            hide boss with moveoutleft
            jump scenario4
        "Only enable basic tracking—no scores, just qualitative comments (-$20k)":
            $ tech_score += 10
            $ people_score += 10
            $ impact_score -= 10
            $ company_money -= 20

            "{i}Use AI to highlight patterns or red flags, but keep decisions in human hands. Less efficient, but more defensible if a problem arises{/i}"
            hide boss with moveoutleft
            jump scenario4

label scenario4:
    scene office with fade
    show boss neutral at center with moveinright

    boss "So… we’ve been piloting the AI hiring program in a few departments."

    mc "And..."

    boss "And well, we’ve got a problem. Take a look at this article:"

    "The boss plops a printed news article on your desk. The headline is devastating:"

    "{i}[company_name]'s AI hiring software favors candidates based on gender and race{/i}"

    "You feel your face turn white."

    boss "What’s worse: they’ve got the data to back it up. Our system has been shown to disproportionately favor Asian applicants by 40%% and disfavor Black applicants by 60%%."

    mc "..."

    boss "We can’t just ignore this. I need your help again. What’s your call?"

    menu:
        boss "What should we tell the public?"

        "Double down. Claim that the system is optimized for performance (-$0k)":
            $ people_score -= 20
            $ impact_score -= 20
            $ company_money += 0

            "{i}Frame the algorithm as merit-based and outcome-driven. Claim that patterns are just incidental, but this risks provoking public backlash and internal divisions.{/i}"
            hide boss with moveoutleft
            jump scenario5
        "Temporarily recall the AI system and revise it to meet fairness standards (-$150k)":
            $ people_score += 20
            $ impact_score += 20
            $ process_score -= 10
            $ tech_score -= 10
            $ company_money -= 150

            "{i}Take the system down and address the bias directly. We would take a hit to our reputation and profits, but this shows leadership and accountability in the long run.{/i}"
            hide boss with moveoutleft
            jump scenario5
        "Keep the AI, but introduce a secondary fairness check (-$80k)":
            $ impact_score += 10
            $ process_score += 10
            $ tech_score += 10
            $ company_money -= 80

            "{i}A compromise. Slower, but more defensible.{/i}"
            hide boss with moveoutleft
            jump scenario5

label scenario5:
    scene office with fade
    "{i}You're sitting at your desk when you get a phone call. You pick it up.{/i}"
    
    show madison talking at center with moveinright

    pr "Hey! I don’t think we’ve properly met. I’m Madison, I handle PR for [company_name]."

    pr "I've been told to inform you that we've got a situation here."

    show madison worried

    pr "Candidates are starting to revolt and raise concerns about how we use AI in our hiring process."

    pr "Some are confused, others are worried—and honestly this isn’t looking good for us."

    pr "This might turn into a straight-up PR disaster for the company."

    show madison talking

    pr "We need to get ahead of this, and I think we do it through some form of transparency."

    pr "The question is: how transparent do we want to be?"

    menu:
        pr "What should our message to the public look like?"

        "Post a general statement on our website and job boards (-$0k)":
            $ policy_score -= 10
            $ impact_score -= 20
            $ company_money += 0
            "{i}Publish something like ‘We use AI tools to assist in the recruiting process.’ Hopefully this will calm some nerves, but it may come off as evasive.{/i}"
            hide madison with moveoutleft
            jump scenario6
        "Create a detailed statement on how AI is used at the company, including details about tools, rules, and criteria (-$0k)":
            $ policy_score += 30
            $ impact_score += 20
            $ company_money += 0

            "{i}Builds trust with the public and sets an example, but may also open the door to questions and conversations the company is not yet ready to handle.{/i}"
            hide madison with moveoutleft
            jump scenario6
        "Provide an option for candidates to opt-out of AI screening—but make it discreet (-$50k)":
            $ policy_score -= 10
            $ impact_score -= 10
            $ company_money -= 50

            "{i}May make candidates more comfortable, but could it be seen as an admission that the system is untrustworthy?{/i}"
            hide madison with moveoutleft
            jump scenario6

label scenario6:
    scene office with fade
    show boss neutral at center with moveinright

    boss "Hey, so good news."

    show boss neutral at bobble

    boss "The public outcry against [company_name] has quietened. I'd say it's time for us to take our AI hiring system international."

    show boss neutral at bobble

    boss "We're looking at a major rollout within the next six months."

    boss "You've been guiding us so far, and doing a pretty good job, so the executive board would like your input."

    menu:
        boss "What's the best strategy for taking our hiring strategy international?"

        "Launch internationally and apply a ‘figure it out as we go’ approach (+$?)":
            $ process_score += 40
            $ tech_score += 30
            $ policy_score -= 20
            $ impact_score -= 20
            $ company_money += 200
            "{i}Roll it out in all markets and adapt as problems come up. Fast, bold, and risky.{/i}"

            $ company_money -= 300
            "{i}In this scenario, the company gains an intiial surge of capital but spends more in the long-run as they battle legal and consumer acceptance issues.{/i}"

            hide boss with moveoutleft
            jump ending_scene
        "Expand slowly, region by region. Research local laws and cultural norms before implementation (+$?)":
            $ process_score += 20
            $ tech_score += 20
            $ policy_score += 20
            $ company_money += 20
            "{i}Slower and more methodical. Builds trust and avoids legal trouble, but highly resource-intensive—can the company survive this transition?{/i}"
            hide boss with moveoutleft
            jump ending_scene
        "Update and localize the AI hiring system to fit each region's cultural standards (+$?)":
            $ process_score += 20
            $ tech_score += 20
            $ policy_score += 20
            $ company_money -= 100
            "{i}Tailor the AI to respect local cultural norms, hiring expectations, and regional regulations. Thoughtful and effective — but expensive.{/i}"
            hide boss with moveoutleft
            jump ending_scene

label ending_scene:
    # ending scene.

    # Find top and worst trait.
    $ scores = [people_score, process_score, tech_score, policy_score, impact_score]
    # Flawed but ok for prototype.
    $ max_index = scores.index(max(scores))
    $ min_index = scores.index(min(scores))

    if company_money > 100:
        "Good ending."
        "{i}[company_name] remains afloat after 5 years and seems to be in a better position. It attempts to use AI responsibly and is a leader in its space.{/i}"
    elif company_money > 0:
        "Neutral ending"
        "{i}[company_name] struggles through the next five years but barely manages to stay afloat.{/i}"
        "{i}Its fate hangs in the balance as customers seem to be just accepting of their practices.{/i}"
    else:
        "Bad ending"
        "{i}After just one year, [company_name] goes bankrupt and fails to win back the trust of the people.{/i}"
        "{i}Customers and employees grow increasingly wary and slowly began to abandon the company.{/i}"
    
    "RESULTS:"
    if max_index == 0:
        "Your company seems to prioritize the well-being of employees."
    elif max_index == 1:
        "Your company seems to prioritize efficient processes and saving money."
    elif max_index == 2:
        "Your company seems to embrace technology and innovation."
    elif max_index == 3:
        "Your company is driven by strong policy and ethics."
    else:
        "Your company seems to prioritize the feelings of consumers."
    
    if min_index == 0:
        "However, your negligence over the feelings of employees has had negative consequence."
    elif min_index == 1:
        "However, your inability to design efficient and well-run processes has put you behind your competitors."
    elif min_index == 2:
        "However, your refusal to adopt to the newest tech trends have put you behind your competitors."
    elif min_index == 3:
        "However, your challenge of policy and ethics in running your company has put you in trouble with lawmakers."
    else:
        "However, your company has not prioritized the consumer enough, and has struggled to reach the heights that it once attained."

    "The End" 
    return
