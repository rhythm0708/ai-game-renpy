# Characters.
define mc = Character("You", color="#70C3FF")
define boss = Character("Boss", color="#43469D")
define hr = Character("Karim", color="#1AD87A")
define pr = Character("Madison", color="#FFDD1B")

default company_name = "{color=#f00}Fintek{/color}"

# Stats.
default people_score = 50
default process_score = 50
default tech_score = 50
default policy_score = 50
default impact_score = 50

default company_money = 600

# HUD.
screen money_hud():
    frame:
        xalign 1.0
        yalign 0.0
        background "#0008"
        text "Money: $ [company_money]" size 24 color "#fff"

# Transforms.
transform bobble:
    yoffset 0
    linear 0.2 yoffset 25
    linear 0.2 yoffset 0
    linear 0.2 yoffset 25
    linear 0.2 yoffset 0
    linear 0.2 yoffset 25
    linear 0.2 yoffset 0

label start:
    scene bg room
    show screen money_hud
    play music "audio/office theme.mp3"
    $ renpy.music.set_volume(0.15, channel='music')
    jump exposition

label exposition:
    "This is [company_name]."

    scene fintek with fade

    "[company_name] was once a thriving company, but it's been on a downward trajectory since 2015."

    "After a bad investment in {color=#f00}CorgiCoin{/color}, customers started losing trust and sales have been declining year-over-year."

    "The company is desperately in search of a strategic leader to guide them in the right direction and win back customers."

    "That's where you come in."

    # show main character

    "You are a tech consultant from {color=#f00}TechRight{/color} hired to overhaul the company’s competitive strategy."

    "You’re relatively new, but you think you have what it takes to turn this company around."

    "That’s what it says on your business card anyway."

    # flash business card

    "{color=#f00}{i}NOTE: Conserve your money! If you run low on money by the end of the simulation, the company will go out of business. Make decisions carefully!{/color}{/i}"

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

    menu:
        mc "How should the company implement its AI hiring tool?"

        "Encourage immediate company-wide deployment of the AI software (+$100)":
            $ process_score += 20
            $ people_score -= 10
            $ impact_score -= 10
            $ company_money += 100

            "{i}Let’s rip the band aid off—this will maximize cost savings, and we’ll eventually need it anyway.{/i}"
            hide boss with moveoutleft
            jump scenario2

        "Use AI to recommend and filter resumés, but have staff look over any that are flagged or rejected (-$30)":
            $ process_score += 10
            $ people_score += 10
            $ company_money -= 30

            "{i}Adding a human touch might make the transition softer and preserve trust.{/i}"
            hide boss with moveoutleft
            jump scenario2

        "Keep human screening for now, and pilot AI in low-risk, supporting roles (-$150)":
            $ process_score -= 10
            $ tech_score -= 10
            $ people_score += 10
            $ company_money -= 150

            "{i}This might not save much money in the short-term, but it's a cautious approach.{/i}"
            hide boss with moveoutleft
            jump scenario2
    
label scenario2:
    scene office with fade

    "{i}You’re sitting at your desk when a man walks up to you. They flash a smile and wave.{/i}"

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

        "Go for it — let's roll it out (+$80)":
            $ process_score += 20
            $ tech_score += 20
            $ impact_score -= 20
            $ people_score -= 20
            $ company_money += 80

            "{i}This system seems promising and it hasn’t caused issues so far. This could save the company serious time and money.{/i}"
            hide karim with moveoutleft
            jump scenario3
        "Request that the vendor submit fairness audits and pass bias-testing standards (-$100)":
            $ process_score -= 10
            $ tech_score += 20
            $ company_money -= 100

            "{i}They might not do it, and this might take a while. But this would help maintain fairness and trust within candidates.{/i}"
            hide karim with moveoutleft
            jump scenario3
        "Propose launching a controlled pilot in one department (-$20)":
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

    boss "It’s about this wild new AI tech that can analyze behavior in video interviews."

    boss "It can track tone, facial expressions, gestures—even the candidate’s background!"

    boss "It uses this data to predict which candidates would perform best if hired."

    mc "Definitely sounds cutting edge. I've heard about it as a concept, but I didn't know they were rolling it out so soon."

    boss "And guess what? I checked in with our vendor, and surprise, surprise—it’s available as an add-on to our software package!"

    boss "I’m thinking we roll it out immediately. You know—weed out the underperformers before we bring them onto our team."

    mc "Hm..."

    boss "What, not sold? It has proven results!"

    boss "But I understand."

    boss "Your job is to make this palatable for people and profitable for the company."

    boss "That’s why I’m telling this to you."

    boss "So you tell me: what’s the best way we can implement this to avoid any blowback."

    menu:
        mc "This is a tough one. What should I recommend?"

        "Start with an industry-standard behavioral dataset (-$100)":
            $ process_score += 20
            $ tech_score += 20
            $ impact_score -= 10
            $ company_money -= 100

            "{i}Leverage widely accepted benchmarks for professional behavior and communication. It works, and avoids the headache of collecting data on company culture{/i}"
            hide boss with moveoutleft
            jump scenario4
        "Train the system on employee behavior data (-$50)":
            $ process_score += 30
            $ tech_score += 30
            $ impact_score -= 20
            $ people_score -= 20
            $ company_money -= 50

            "{i}This creates a highly tailored system based on our company culture, but it raises the risk of employee backlash and data security concerns{/i}"
            hide boss with moveoutleft
            jump scenario4
        "Only enable basic tracking—no scores, just qualitative comments (-$20)":
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

        "Double down. Claim that the system is optimized for performance (-$0)":
            $ people_score -= 20
            $ impact_score -= 20
            $ company_money += 0

            "{i}Frame the algorithm as merit-based and outcome-driven. Claim that patterns are just incidental, but this risks provoking public backlash and internal divisions.{/i}"
            hide boss with moveoutleft
            jump scenario5
        "Temporarily recall the AI system and revise it to meet fairness standards (-$150)":
            $ people_score += 20
            $ impact_score += 20
            $ process_score -= 10
            $ tech_score -= 10
            $ company_money -= 150

            "{i}Take the system down and address the bias directly. We would take a hit to our reputation and profits, but this shows leadership and accountability in the long run.{/i}"
            hide boss with moveoutleft
            jump scenario5
        "Keep the AI, but introduce a secondary fairness check (-$80)":
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

        "Post a general statement on our website and job boards (-$0)":
            $ policy_score -= 10
            $ impact_score -= 20
            $ company_money += 0
            "{i}Publish something like ‘We use AI tools to assist in the recruiting process.’ Hopefully this will calm some nerves, but it may come off as evasive.{/i}"
            hide madison with moveoutleft
            jump scenario6
        "Create a detailed statement on how AI is used at the company, including details about tools, rules, and criteria (-$0)":
            $ policy_score += 30
            $ impact_score += 20
            $ company_money += 0

            "{i}Builds trust with the public and sets an example, but may also open the door to questions and conversations the company is not yet ready to handle.{/i}"
            hide madison with moveoutleft
            jump scenario6
        "Provide an option for candidates to opt-out of AI screening—but make it discreet (-$50)":
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

    boss "The public outcry for us has quietened. I'd say it's time for us to take our AI hiring system international."

    boss "We're looking at a major rollout within the next six months."

    boss "You've been guiding us so far, and doing a pretty good job, so the executive board would like your input."

    menu:
        boss "What's the best strategy for taking our hiring strategy international?"

        "Launch internationally and apply a ‘figure it out as we go’ approach (+$?)":
            $ process_score += 40
            $ tech_score += 30
            $ policy_score -= 20
            $ company_money += 200
            "{i}Roll it out in all markets and adapt as problems come up. Fast, bold, and risky.{/i}"

            $ company_money -= 300

            hide boss with moveoutleft
            jump ending_scene
        "Expand slowly, region by region. Research local laws and cultural norms before implementation (+$?)":
            $ process_score += 20
            $ tech_score += 20
            $ policy_score += 20
            $ company_money += 50
            "{i}Slower and more methodical. Builds trust and avoids legal trouble, but highly resource-intensive—can the company survive this transition?{/i}"
            hide boss with moveoutleft
            jump ending_scene
        "Only implement AI hiring in regions with similar laws and values (+$?)":
            $ process_score += 10
            $ tech_score += 0
            $ policy_score += 10
            $ company_money += 0
            "{i}Minimizes risk and complexity, but also lesser reward.{/i}"
            hide boss with moveoutleft
            jump ending_scene

label ending_scene:
    # ending scene.

    # Find top and worst trait.
    $ scores = [people_score, process_score, tech_score, policy_score, impact_score]
    # Flawed but ok for prototype.
    $ max_index = scores.index(max(scores))
    $ min_index = scores.index(min(scores))

    if company_money > 400:
        "Good ending."
        "{i}[company_name] remains afloat after 5 years and seems to be in a better position. It attempts to use AI responsibly and is a leader in its space.{/i}"
    elif company_money > 200:
        "Neutral ending"
        "{i}[company_name] struggles through the next five years but just manages to stay afloat.{/i}"
        "{i}Its fate hangs in the balance as customers seem to be just accepting of their practices.{/i}"
    else:
        "Bad ending"
        "{i}After just one year, [company_name] goes bankrupt and fails to win back the trust of enough customers.{/i}"
        "{i}Customers and employees grew increasingly wary of the brand and slowly began to abandon.{/i}"
    
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
