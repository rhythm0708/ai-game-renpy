﻿# Characters.
define mc = Character("You", color="#70C3FF")
define boss = Character("Boss", color="#e0452b")
define hr = Character("Karim", color="#1AD87A")
define pr = Character("Madison", color="#FFDD1B")

# Company Info.
default company_info = {
    "name": "{color=#4ac7d1}Fintek{/color}",
    "name_raw": "Fintek",
    "crypto": "{color=#FFDD1B}CorgiCoin{/color}",
    "crypto_raw": "CorgiCoin",
    "consultant": "{color=#00a14b}TechRight{/color}",
    "consultant_raw": "TechRight"
}

# Game Manager.
default game = GameManager()

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

# -------------- GAME STARTS HERE --------------------------
label start:
    scene smoke
    hide screen money_hud
    play music "audio/office theme.mp3"
    $ renpy.music.set_volume(0.1, channel='music')
    jump exposition

label exposition:
    show fintek bldg with dissolve

    "This is [company_info['name']]."

    "[company_info['name']] was once a thriving company, but it's been on a downward trajectory since 2015."

    "After a bad investment in [company_info['crypto']], customers started losing trust and sales have been declining year-over-year."

    "The company is desperately in search of a strategic leader to guide them in the right direction and win back customers."

    "That's where you come in."

    hide fintek with dissolve
    show you with dissolve
    # fix timing

    "You are a tech consultant from [company_info['consultant']] hired to overhaul the company’s competitive strategy."

    "You’re relatively new, but you think you have what it takes to turn this company around."

    hide you
    show business card

    "That’s what it says on your business card anyway."

    hide business card

    # "For some reason when we printed it, only the name was smudged out. That's strange?"

    #add a smoother transition here

    jump scenario0

label scenario0:

    # elevator scene start
    show elevator floor1 with dissolve

    "{i}It's your first day on the job.{/i}"

    show elevator floor3

    "{i}Your palms are clammy, but you're confident you can save this company...probably.{/i}"

    show elevator floor6

    mc "Geez, this elevator is taking forever."
    
    show elevator floor8

    "{i}You can feel your heart racing as the floor grows nearer. Just how will things turn out from each decision you make?{/i}"

    show elevator doorsopen

    "{i}Suddenly, the doors open to reveal a hairy, stout man in an ill-fitted suit. His eyes crinkle up at the sight of you.{/i}"

    show boss smile at center with dissolve

    boss "Ah, you're here! I'm glad you could make it today. Please come in!"

    "{i}You awkwardly shuffle past him at the elevator doors. This is a welcome surprise.{/i}"

    mc "Hi there. Is this Fintek?"

    boss "Yes, yes, welcome! Let me take you to your office."

    "{i}He leads you down the short hallway until your reach a door near the opposite end.{/i}"

    hide boss smile
    show office with dissolve

    "{i}The office is sparse. A single desk sat in the center with a small filing cabinet by its side.{/i}"

    "{i}The only decoration is an oddly framed paper with the words 'Office Sweet Office' on it.{/i}"

    show boss smile at center with moveinright

    boss "Office, sweet, office! That's what we like to say here."

    boss "I hope you settle in well, we have a lot of work to do this week."

    hide boss smile
    show boss neutral at center

    boss "Frankly, the company hasn't been doing too well recently so we're really relying on you to help us get through it."

    menu:
        boss "How are you feeling?"

        "I'm confident.":
            mc "I feel pretty confident I can help turn this company around."
            mc "After all, that's what you hired me to do."
            hide boss neutral
            show boss smile
            boss "I love to hear that."
        "I'm a bit nervous.":
            mc "I'm honestly a bit nervous."
            mc "But I think we can figure it out together."
            boss "That's understandable. It's your first day, after all."
            boss "But please try your best, we're in quite the pinch."
        "Confused.":
            mc "Honestly, I'm still a little confused about all of it."
            mc "I'm not really sure what I should be doing."
            boss "Don't worry, I'll help you settle in first."
            boss "But please try your best, we're in quite the pinch."

    hide boss smile
    show boss neutral at center
    boss "Before you start, I also have to remind you."

    boss "Unfortunately, we can only allocate a budget of $[game.company_money]k for all your decision-making needs."

    show screen money_hud with dissolve

    boss "Sadly that is all we can afford right now so I hope you spend it wisely."

    "{color=#e0452b}{i}NOTE: Conserve your money! If you run low on money, the company will go out of business. Make decisions carefully!{/color}{/i}"

    boss "Anyway, I'll let you get settled in for now. If you need me, I'll be in my office next door."

    hide boss neutral with moveoutleft

    jump scenario1

# ---------- SCENARIO 1 ------------
label scenario1:
    scene office with fade

    "{i}A couple hours passed of settling in. Outside your office door was radio silence. Were there even other employees?{/i}"

    "{i}'What am I supposed to be doing right now?' you think to yourself.{/i}"

    "{i}In an instant, as if he heard your thoughts himself, the boss knocks on your door and approaches with a laptop in hand.{/i}"

    # "{i}You’re sitting at your desk in front of a mass of spreadsheets when your boss approaches you with a laptop in hand.{/i}"
    # change this depending on scene

    show boss neutral at center with moveinright 

    boss "Hey, so we’ve been looking at trends in AI and we see that a lot of major companies are beginning to incorporate it."

    show boss neutral at bobble

    boss "Apparently it can speed up workflow and help the company save costs. It sounds like exactly what we need right now!"

    show boss neutral at bobble

    boss "We’re thinking of doing a trial on it in our hiring system. It seems like the safest place to start with this kind of thing."

    show boss neutral at bobble

    boss "Here. This is what Karim, the head of HR, showed me this morning."

    # computer screen with AI screening program

    "{i}Your boss opens their laptop and gestures to the screen. On it, you see the familiar progress bars, upload prompts, and verification steps of A.I software.{/i}"

    show boss neutral at bobble

    boss "It’s an AI resumé-screening program. It scans resumés and cover letters for requirements and keywords, and returns a score for each candidate."

    show boss neutral at bobble

    boss "You’re a tech consultant, what do you think? We need your guidance on how to best implement this tool."

label scenario_1_decision:
    $ hover_text = ""
    $ options = [
        {
            "text": "Encourage immediate company-wide deployment of the AI software.",
            "hover": "{i}This will maximize cost savings, and we’ll eventually need it anyway{/i} (+$100k)",
            "label": "choice_1a"
        },
        {
            "text": "Use AI to recommend and filter resumés, but have staff look over any that are flagged or rejected.",
            "hover": "{i}Adding a human touch might make the transition softer and preserve trust{/i} (-$30k)",
            "label": "choice_1b"
        },
        {
            "text": "Keep human screening for now, and pilot AI in low-risk, supporting roles.",
            "hover": "{i}A cautious approach might not save much money but avoids ethical pitfalls{/i} (-$150k)",
            "label": "choice_1c"
        }
    ]
    show screen decision_hud(options)
    "How should the company implement its AI hiring tool?"
    return

label choice_1a:
    $ game.update_scores(-10, 20, 10, -10, -10)
    $ game.company_money += 100
    $ game.boss_satisfaction += 10

    hide screen decision_hud
    "{i}You encourage the boss to immediately deploy the AI tool and fix problems as they come up.{/i}"
    mc "Don't let your company fall behind your competitors."
    "{i}Your boss nods. He leaves to give instructions to the rest of the staff.{/i}"
    # maybe add more to this? 

    hide boss with moveoutleft
    jump scenario2

label choice_1b:
    $ game.update_scores(10, 10, 5, 0, 0)
    $ game.company_money -= 30

    hide screen decision_hud
    mc "It's a good idea to keep employees part of the process, especially during the early stages."
    mc "It reduces liability if things come up, and backlash from the public from cutting jobs."
    "{i}Your boss nods, scribbling notes onto a notepad.{/i}"
    "{i}He leaves to inform the rest of the staff.{/i}"

    hide boss with moveoutleft
    jump scenario2

label choice_1c:
    $ game.update_scores (10, -10, -10, 10, 15)
    $ game.company_money -= 150
    $ game.boss_satisfaction -= 20

    hide screen decision_hud
    mc "AI is still a burgeoning technology. We shouldn't implement it so recklessly."
    mc "Why don't we start off small scale? Let's just use it to answer frequently-asked questions."
    mc "And if that goes well, we can move up from there."
    "{i}Your boss looks disappointed, he scratches his head.{/i}"
    "{i}He reluctantly nods and takes your advice, but warns that the company must find other ways of cutting costs.{/i}"
    "{i}You get a nervous feeling. You feel that conversation could have gone better.{/i}"

    hide boss with moveoutleft
    jump scenario2

label scenario2:
    scene office with fade
    
    "{i}The early morning fatigue is already getting to you.{/i}"

    mc "I need a coffee."

    "{i}You fumble your way outside to what you think is the coffee station. The room is so barren, it's unclear.{/i}"

    "{i}Ahhhhhhh. Nothing like a good coffee first thing in the morning.{/i}"

    # maybe like a meaningless coffee choice here or smth

    hr "Hi there. Are you new?"

    "{i}You look over to see a tall curly-haired man. His reflective glasses momentarily blind you.{/i}"

    show karim neutral at center with moveinright 

    hr "Hey, I’m Karim from HR."

    show karim talking

    hr "I’ve been working at [company_info['name']] since 2015. I've heard some good things about you from the boss. Thanks for helping out."

    show karim neutral at center

    hr "So why was I here again? … Oh yeah!"

    show karim talking

    hr "We were thinking of extending the use of AI in our hiring processes."

    hr "The resumé-screening system hasn’t raised any flags so far, so we were thinking of setting up an AI system for interviewing."

    show karim neutral at center

    hr "Have you heard of one-way interviews?"

    show karim talking

    hr "It’s this new system where candidates can get interviewed by a program that records their responses to pre-set questions."

    hr "No interviewer, just… a camera, a timer, and a script."

    show karim neutral at center

    menu:
        hr "What do you think about it?"

        "Sounds dystopian.":
            mc "I can't lie, that sounds pretty dystopian."
            mc "It strips away so much of the human element in hiring."
            show karim talking
            hr "That's exactly the concern. But executives love the efficiency."
        "Pretty cool I must say.":
            mc "It's definitely innovative. It would save so many hours coordinating and conducting interviews."
            mc "Plus, candidates can record responses in their own time."
            show karim talking
            hr "Right? HR loves the flexibility. But not everyone is a fan."
    
    hr "Anyways, we've been offered a software package by a high-level vendor that does just this."

    hr "They're giving us a steep discount, and executives are drooling over the promised benefits."

    hr "But I wanted to consult with you before we moved forward with the decision."

    hr "So, any advice? What should we tell the vendor?"
    show karim neutral

label scenario_2_decision:
    $ hover_text = ""
    $ options = [
        {
            "text": "Purchase the software package and roll it out immediately",
            "hover": "{i}This system seems promising and it hasn’t caused issues so far. This could save the company serious time and money{/i} (+80k)",
            "label": "choice_2a"
        },
        {
            "text": "Request that the vendor submit fairness audits and pass bias-testing standards",
            "hover": "{i}They might not do it, and this might take a while. But this would help maintain fairness and trust within candidates{/i} (-$100k)",
            "label": "choice_2b"
        },
        {
            "text": "Launch a controlled pilot in one department",
            "hover": "{i}Collect data and monitor feedback from candidates before deciding whether it’s worth scaling up. Slower but safer, and more methodical{/i} (-$20k)",
            "label": "choice_2c"
        }
    ]
    show screen decision_hud(options)
    "What should the company tell the vendor?"
    return

label choice_2a:
    $ game.update_scores(-20, 20, 20, 0, -20)
    $ game.company_money += 80
    $ game.boss_satisfaction += 10

    hide screen decision_hud
    "{i}You encourage [hr] to purchase the software package and implement it as soon as possible.{/i}"
    mc "I've heard about this concept. It's promising."
    mc "Many Fortune-500 companies have already implemented this technology and done the testing for us."
    mc "This should be a no-brainer. We can deal with the issues as they come up."
    "{i}[hr] nods and agrees. He walks away to prepares a memo for the software vendor.{/i}"

    hide karim with moveoutleft
    jump scenario3

label choice_2b:
    $ game.update_scores(10, -10, 0, 10, 10)
    $ game.company_money -= 100

    hide screen decision_hud
    mc "It's always a good idea to perform checks with these types of things."
    mc "Overpromise, underdeliver. And the customers will always blame us. It's best if we do our due diligence."
    show karim talking
    hr "Won't that be expensive? But I suppose you're right. Let's do it your way then."
    show karim
    "{i}You and [hr] part ways with some sense of mutual agreement.{/i}"

    hide karim with moveoutleft
    jump scenario3

label choice_2c:
    $ game.update_scores (0, -15, -15, 0, 15)
    $ game.company_money -= 20
    $ game.boss_satisfaction -= 20

    hide screen decision_hud
    mc "I think we're moving too fast. We should start with a controlled pilot in one or two departments at most."
    mc "This technology is... new. We shouldn't just dive right into it."
    mc "We should observe what happens in the first case and adapt from there. If it creates legal liability issues then that would be bad for the company in the long run." 
    "{i}[hr] gives you an understanding look.{/i}"
    "{i}He expresses agreement, but he doesn't seem too happy about it.{/i}"
    "{i}The look on his face is of concern. He scuttles out of the room.{/i}"

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

    boss "So you tell me: what’s the best way we can implement this to avoid any blowback?"

label scenario_3_decision:
    $ hover_text = ""
    $ options = [
        {
            "text": "Implement it with an industry-standard behavioral dataset",
            "hover": "{i}Leverage widely accepted benchmarks for professional behavior and communication. It works, and avoids the headache of collecting data on company culture{/i} (-100k)",
            "label": "choice_3a"
        },
        {
            "text": "Collect employee behavior data and train the hiring system on company culture",
            "hover": "{i}This creates a highly tailored system based on our company culture, but it raises the risk of employee backlash and data security concerns{/i} (+$50k)",
            "label": "choice_3b"
        },
        {
            "text": "Only enable basic tracking—no scores, just qualitative comments",
            "hover": "{i}Use AI to highlight patterns or red flags, but keep decisions in human hands. Less efficient, but more defensible if a problem arises{/i} (-$20k)",
            "label": "choice_3c"
        }
    ]
    show screen decision_hud(options)
    "This is a tough one. What should I recommend?"
    return

label choice_3a:
    $ game.update_scores(0, 15, 15, -5, -10)
    $ game.company_money -= 100
    $ game.boss_satisfaction += 20

    hide screen decision_hud
    "{i}A bit of a dystopian practice, but you wouldn't dare let your boss know that.{/i}"
    "{i}You know that some companies track employee behavior data to train these datasets...{/i}"
    "{i}... but you decide not to let your boss know about that.{/i}"
    "{i}Instead, you talk to your boss about buying an industry-standard behavioral dataset: it tracks basic benchmarks for strong company performance, for a one-time price.{/i}"
    "{i}Your boss listens attentively. He seems to be weighing the pros and cons in his mind.{/i}"
    "{i}Next week in the office, you hear coworkers talk about how the boss decided to go for it.{/i}"

    hide boss with moveoutleft
    jump scenario4

label choice_3b:
    $ game.update_scores(-20, 30, 30, -15, -20)
    $ game.company_money += 50
    $ game.boss_satisfaction += 25

    hide screen decision_hud
    "{i}A bit of a dystopian practice, but you wouldn't dare let your boss know that.{/i}"
    "{i}You know that most companies who do this tend to collect detailed data on their employees.{/i}"
    "{i}Keystroke monitoring, biometric scans... you never thought your company would be part of this transformation.{/i}"
    "{i}You let your boss know about this 'common industry practice.'{/i}"
    "{i}You think you may have noticed a glint in his eye as you brought up employee monitoring.{/i}"
    "{i}You leave feeling not great about your contribution.{/i}"

    hide boss with moveoutleft
    jump scenario4

label choice_3c:
    $ game.update_scores (10, -10, 0, 0, 0)
    $ game.company_money -= 20
    $ game.boss_satisfaction -= 20

    hide screen decision_hud
    "{i}You're a bit skeptical about this technology and you let your boss know.{/i}"
    "{i}You recommend holding back for now. Instead, you propose using AI in a simpler manner: just use it to analyze the video and give broad comments.{/i}"
    "{i}Your boss seems disappointed and opens his mouth to speak.{/i}"
    "{i}But, he quickly closes his mouth again. He must have realized that you're the expert.{/i}"
    "{i}Weeks later, you hear no talk about the software package ever being implemented.{/i}"

    hide boss with moveoutleft
    jump scenario4

label scenario4:
    scene office with fade
    show boss neutral at center with moveinright

    boss "So… we’ve been piloting the AI hiring program in a few departments."

    mc "And..."

    boss "And well, we’ve got a problem. Take a look at this article:"

    "The boss plops a printed news article on your desk. The headline is devastating:"

    "{i}[company_info['name']]'s AI hiring software favors candidates based on gender and race{/i}"

    "You feel your face turn pale."

    boss "What’s worse: they’ve got the data to back it up. Our system has been shown to disproportionately favor Asian applicants by 40%% and disfavor Black applicants by 60%%."

    mc "..."

    boss "We can’t just ignore this. I need your help again. What’s your call?"

label scenario_4_decision:
    $ hover_text = ""
    $ options = [
        {
            "text": "Double down. Claim that the system is optimized for performance",
            "hover": "{i}Frame the algorithm as merit-based and outcome-driven. Claim that patterns are just incidental, but this risks provoking public backlash and internal divisions{/i} (-$0k)",
            "label": "choice_4a"
        },
        {
            "text": "Temporarily recall the AI system and revise it to meet fairness standards",
            "hover": "{i}Take the system down and address the bias directly. We would take a hit to our reputation and profits, but this shows leadership and accountability in the long run{/i} (-$150k)",
            "label": "choice_4b"
        },
        {
            "text": "Keep the AI, but introduce a secondary fairness check",
            "hover": "{i}A compromise. Slower, but more defensible{/i} (-$80k)",
            "label": "choice_4c"
        }
    ]
    show screen decision_hud(options)
    "What should we tell the public?"
    return

label choice_4a:
    $ game.update_scores(-20, 0, 0, -10, -10)
    $ game.company_money += 0
    $ game.boss_satisfaction += 10

    hide screen decision_hud
    "{i}You encourage the boss to double down on the decision."
    mc "The company will look weak and guilty if we back down now. We have to double down."
    mc "Say that our company values performance over all, and that AI is the future of a fair and non-discriminatory hiring process."
    "{i}Your boss nods. He seems to agree.{/i}"
    "{i}He rushes to give instructions to the rest of the staff.{/i}"

    hide boss with moveoutleft
    jump scenario5

label choice_4b:
    $ game.update_scores(20, -20, -10, 10, 10)
    $ game.company_money -= 150
    $ game.boss_satisfaction += 10

    hide screen decision_hud
    mc "This seems bad. I think it's a good idea to temporarily disable the AI hiring system and resume human-led hiring."
    boss "Won't that make us look really guilty?"
    mc "Yes, but we already look bad. This gives us a chance to recover our reputation in the long run. At least it shows that we acknowledge our mistakes and work towards becoming better."
    "{i}Your boss nods, seeming to understand.{/i}"
    "{i}He scribbles a note for the PR team and thanks you, before shuffling off.{/i}"

    hide boss with moveoutleft
    jump scenario5

label choice_4c:
    $ game.update_scores(0, 0, 0, 5, 5)
    $ game.company_money -= 80
    $ game.boss_satisfaction -= 20

    hide screen decision_hud
    mc "It's too expensive to rewrite the AI hiring system, but it also looks bad if we don't acknowledge it."
    "{i}You pause and think for a moment.{/i}"
    mc "I think we should keep the AI system running, but add a secondary check — have humans review the rejected applicants and the reasons why, to make sure they're valid."
    mc "This would quell the criticisms about AI unfairness and probably increase compliance with other hiring standards."
    boss "{i}That would cost a pretty penny though...{/i}"
    "{i}You thought you heard the boss mutter something underneath his breath. He didn't seem happy.{/i}"
    "{i}You leave the conversation feeling confused. You thought you had found a good compromise...{/i}"

    hide boss with moveoutleft
    jump scenario5

label scenario5:
    scene office with fade
    "{i}You're sitting at your desk when you get a phone call. You pick it up.{/i}"
    
    show madison talking at center with moveinright

    pr "Hey! I don’t think we’ve properly met. I’m Madison, I handle PR for [company_info['name']]."

    pr "I've been told to inform you that we've got a situation here."

    show madison worried

    pr "Candidates are starting to revolt and raise concerns about how we use AI in our hiring process."

    pr "Some are confused, others are worried—and honestly this isn’t looking good for us."

    pr "This might turn into a straight-up PR disaster for the company."

    show madison talking

    pr "We need to get ahead of this, and I think we do it through some form of transparency."

    pr "The question is: how transparent do we want to be?"

label scenario_5_decision:
    $ hover_text = ""
    $ options = [
        {
            "text": "Post a general statement on our website and job boards",
            "hover": "{i}Publish something like ‘We use AI tools to support our recruitment process.’ Hopefully this will calm some nerves, but it may come off as evasive{/i} (-$0k)",
            "label": "choice_5a"
        },
        {
            "text": "Create a detailed statement on how AI is used at the company, including details about tools, rules, and criteria",
            "hover": "{i}Builds trust with the public and sets an example, but may also open the door to questions and conversations the company is not yet ready to handle{/i} (-$50k)",
            "label": "choice_5b"
        },
        {
            "text": "Provide an option for candidates to opt-out of AI screening, but make it discreet",
            "hover": "{i}May make candidates more comfortable, but could it be seen as an admission that the system is untrustworthy?{/i} (-$20k)",
            "label": "choice_5c"
        }
    ]
    show screen decision_hud(options)
    "Another PR disaster. What should the company's message to the public look like?"
    return

label choice_5a:
    $ game.update_scores(-10, 0, 0, -5, -15)
    $ game.company_money += 0
    $ game.boss_satisfaction += 20

    hide screen decision_hud
    "{i}'Go general,' you say almost instinctively. There will be critics, but this will quell the immediate criticisms of the public.{/i}"
    "{i}[pr] looks almost shocked. She gives you a look that kind of says: 'Wow. You're a natural.'{/i}"
    "{i}The conversation was short but productive.{/i}"
    "{i}A few weeks later, the public outcry about the company becomes quiet.{/i}"
    "{i}Is [company_info['name']] finally in the clear?{/i}"

    hide madison with moveoutleft
    jump scenario6

label choice_5b:
    $ game.update_scores(15, 0, 0, 15, 5)
    $ game.company_money -= 50
    $ game.boss_satisfaction += 0

    hide screen decision_hud
    mc "We should take the transparent route."
    mc "I've seen a lot of companies make a mistake by not acknowledging their use of technology, but that almost always ends badly."
    mc "It sews long-term distrust within the company's customer base, and even when the public stops complaining, customers don't always return."
    "{i}[pr] gives you a thoughtful, but almost relieved nod.{/i}"
    "{i}'I trust you,' she says, before rushing to tell the rest of her team.{/i}"

    hide madison with moveoutleft
    jump scenario6

label choice_5c:
    $ game.update_scores(-10, 0, 0, -10, -10)
    $ game.company_money -= 20
    $ game.boss_satisfaction -= 20

    hide screen decision_hud
    "{i}'We can't be held liable if it was the candidate's choice,' you think. That's probably the easiest way to get out of this.{/i}"
    mc "Why don't we provide an option, a disreet one, that allows candidates to opt-out of AI screening. We can't be held liable if candidates have that decision."
    "{i}[pr] gives you a look. It's a mixture of concern and confusion.{/i}"
    "{i}You can't tell if she's nervous or just processing.{/i}"
    mc "Trust me. It's how we get out of this."
    "{i}[pr] nods, but you can't tell if it's in agreement or defeated acceptance.{/i}"

    hide madison with moveoutleft
    jump scenario6

label scenario6:
    scene office with fade
    show boss neutral at center with moveinright

    boss "Hey, so good news."

    show boss neutral at bobble

    boss "The public outcry against [company_info['name']] has quietened. I'd say it's time for us to take our AI hiring system international."

    show boss neutral at bobble

    boss "We're looking at a major rollout within the next six months."

    boss "You've been guiding us so far, and doing a pretty good job, so the executive board would like your input."

label scenario_6_decision:
    $ hover_text = ""
    $ options = [
        {
            "text": "Launch internationally and apply a ‘figure it out as we go’ approach",
            "hover": "{i}Roll it out in all markets and adapt as problems come up. High risk, high reward.{/i} (-$?k)",
            "label": "choice_6a"
        },
        {
            "text": "Expand slowly, region by region. Research local laws and cultural norms before implementation",
            "hover": "{i}Slower and more methodical. Builds trust and avoids legal trouble, but highly resource-intensive. Can the company survive this transition?{/i} (-$?k)",
            "label": "choice_6b"
        },
        {
            "text": "Update and localize the AI hiring system to fit each region's cultural standards",
            "hover": "{i}Tailor the AI to respect local cultural norms, hiring expectations, and regional regulations. Thoughtful and effective — but expensive{/i} (-$?k)",
            "label": "choice_6c"
        }
    ]
    show screen decision_hud(options)
    "What's the best strategy to take our hiring program international?"
    return

label choice_6a:
    $ game.update_scores(0, 30, 30, -30, -20)
    $ game.company_money += 0
    $ game.boss_satisfaction += 30

    hide screen decision_hud
    mc "Let's just go for it. We can figure it out as we go."
    mc "There's no real way to know how things will go until we let it happen. Plus, this will save the company a ton of time and cash."
    "{i}For the first time, your boss seems to smile.{/i}"
    # BOSS HAPPY
    boss "And here I was, thinking that you'd be more hesitant. Thanks for the reassurance."
    "{i}The boss slaps you on the back, and returns to his desk drinking coffee.{/i}"

    hide boss with moveoutleft
    jump ending_scene

label choice_6b:
    $ game.update_scores(0, 20, 10, 20, 20)
    $ game.company_money += 0
    $ game.boss_satisfaction += 10

    hide screen decision_hud
    mc "Okay well, why don't we take a careful approach? We should assign the legal team to do research on local laws and cultures before wildly implementing the tech."
    mc "Who knows? We might, or probably will encounter a lot of resistance to this kind of stuff overseas."
    mc "Not just by candidates, by local law enforcement and governments too."
    "{i}Your boss' mouth slowly opens to a smile.{/i}"
    # BOSS HAPPY
    boss "Hoho! That's right! That's a smart idea. That's why we hired you, pal. Thanks."
    "{i}Chuckling while holding his mug of coffee, he waddles off to inform the rest of the staff.{/i}"

    hide boss with moveoutleft
    jump ending_scene

label choice_6c:
    $ game.update_scores(0, 20, 20, 10, 0)
    $ game.company_money -= 150
    $ game.boss_satisfaction -= 40

    hide screen decision_hud
    "{i}You think about your boss' proposal. You notice and subsequently point out some of the flaws.{/i}"
    mc "Well, in its current state, our AI hiring system is only designed to abide by our country's laws. When we go overseas, we may face legal trouble and resistance."
    mc "One thing I think we might have to do is update the AI for each region that we roll it out into. We have to make sure that it abides by local laws and customs."
    "{i}Your boss looks deep in thought. He seems uncomfortable with the complexity and cost of this whole endeavor.{/i}"
    mc "Then, we'd have to research each local region, which would probably require some hours from our legal staff. But that's what we have to do to do it right."
    "{i}Your boss finally looks up at you. He clearly has mixed feelings about this.{/i}"
    "{i}'Hard to argue with right, I suppose.'{/i}"
    "{i}He tells you he'll get back to you. He stumbles back to his desk without another word.{/i}"

    hide boss with moveoutleft
    jump ending_scene

# ---------- ENDING -----------------
label ending_scene:
    # Ending 1, 2, 3, 4 etc - cross reference company reputation with internal performance metrics - your first performance report?

    # COMPANY STATUS.
    if game.company_money >= 100:
        "Ending 1"
        "{i}[company_info['name']] remains afloat after 5 years and seems to be in a better position. It attempts to use AI responsibly and is a leader in its space.{/i}"
    elif game.company_money >= 0:
        "Neutral Ending"
        "{i}[company_info['name']] struggles through the next five years but barely manages to stay afloat.{/i}"
        "{i}Its fate hangs in the balance as customers seem to be just accepting of their practices.{/i}"
    else:
        "Bad Ending"
        "{i}After just one year, [company_info['name']] goes bankrupt and fails to win back the trust of the people.{/i}"
        "{i}Customers and employees grow increasingly wary and slowly begin to abandon the company.{/i}"
    
    # REPUTATION.
    if game.boss_satisfaction <= 25:
        "Your reputation at [company_info['name']] is poor."
        "You have few friends in the company, and people seem to avoid you."
        "Coworkers say that you make their jobs more difficult."
        "Over time, your boss stops approaching you for advice, and eventually, you are laid off."
    elif game.boss_satisfaction >= 80:
        "You have an excellent reputation at [company_info['name']]."
        "You have made good acquaintances at the company, and coworkers frequently consult you for advice."
        "Whether you give good advice or not, we're unsure."
        "When your contract expires, the company re-hires you with a small bonus."
        "You retire comfortably after working at [company_info['name']] for ten years."
    else:
        "You are a respected employee at [company_info['name']]."
        "Coworkers approach you for small talk, and you are on friendly terms with most of upper management."
        "You are respected by your associates, and the company keeps you on year after year."
        "Your continued employment seems to be tied with the company's trajectory."
        "Some questions keep you up at night:"
        "{i}If the company becomes too successful, will they still need you?{/i}"
        "{i}Should I perform just well enough to be essential?{/i}"
        "Only time will tell."
    
    # Scores.
    $ ending_scores = game.evaluate_ending()
    "Company Scores"
    "{b}PEOPLE{/b} (Did you treat customers and employees well?): [ending_scores[0]]"
    "{b}PROCESS{/b} (How efficient are your processes? Did you help the company save time and money?): [ending_scores[1]]"
    "{b}TECH{/b} (Did you leverage new technology? Are you ahead or behind competitors?): [ending_scores[2]]"
    "{b}POLICY{/b} (Is the company compliant with local and global technology laws?): [ending_scores[3]]"
    "{b}IMPACT{/b} (How positively does your company affect people and society?): [ending_scores[4]]"

    "The End" 
    return