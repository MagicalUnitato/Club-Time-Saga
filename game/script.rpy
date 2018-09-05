# Add Emotion Branches, include final backgrounds and transitions.
# If still reachable add leaderboards in the end
# Import new question and answers that are 20 items
# Deadline by Friday 9/7/18
# Complete Art deadline by 9/10/18
# Noted on 9/5/18
init python:
    import unicodedata
define y = Character("[name]")
define bs = Character("Dava")
define gs = Character("Ysa")
define bvp = Character("Kyle")
define gvp = Character("Beatrice")
define bp = Character("Oscar")
define gp = Character("Ella")
define p = Character("President")
define t = Character("Teacher")
define a = Character("Alone")
label start:
    stop music
    "*alarm rings*"
    "*wakes up*"
    "Oh no! I'm late for school"
label school:
    t "You! New Comer! You're late! What's your name?"
    $ name = renpy.input("I'm")
    $ name = name.strip()
    while len(name) <= 0 :
        t "You didn't tell me your name yet."
        $ name = renpy.input("I'm")
    y "I apologize for being late Sir."
    t "Since it's the first day, you're excused."
    "Choose your preference:"
menu:
    "Boy":
        $ gender = "male"
        jump watchFF
    "Girl":
        $ gender = "female"
        jump watchFF
label watchFF:
    ## show fast forward watch here
    y "I can't believe that I have Pre-Calculus as a last subject."
    y "Ughh."
    y "That was the most exhausting experience of my life! And NOW, I have to attend club."
    y "Crap! I still have to find the club room."
label clubTime:
    ## club time animation
    if gender == "male":
        show nrm opn presb
        with fade
    elif gender == "female":
        show nrm opn presg
        with fade
    p "Welcome to the first meeting of the STEM Club! As the president of this club, I made a quiz bowl for you to enjoy!"
    p "This quiz has three levels:"
    p "Easy, Moderate and Difficult."
    p "Don’t worry, this game is just for fun! However, if you do manage to pass, you will be rewarded by the end of the game!"
    p "Are you ready?"
menu :
    "Um, sure?":
        jump clubFill
    "I’m kind of not in the mood.":
        jump clubFill2
label clubFill:
    p "That's good to hear! Let's start the quiz!"
    if gender == "male" :
        jump bFirst
    elif gender == "female":
        jump gFirst
label clubFill2:
    p "You do realize that you still need to take part in this quiz because you're a club member, right?"
    y "Are you kidding me?"
    p "No I'm not."
    y "Dangit, Fine."
    if gender == "male" :
        jump bFirst
    elif gender == "female":
        jump gFirst

label bFirst:
    show nrm opn secb
    with fade
    bs "Hi [name]."
    y "Hello, and you're..."
    bs "Oh sorry, my name is Dave."
    bs "I'm the Secretary of this club and I'll be the one to ask you the questions for the easy round."
    y "Oh, okay."
    bs "So the first question is..."
    jump easyQuestions

label gFirst:
    show nrm opn secg
    with fade
    y "Hello, I'm..."
    gs "You're name is [name], I know already."
    y "Um..."
    gs "Look, all you need to know is people call me Ysa."
    gs "I'll be the one to ask you the questions for the easy round because I'm the Secretary of this club."
    y "Well, Nice to me-"
    gs "Ughh, enough chit chat, let us just get this over with!"
    gs "The first question will be..."
    jump easyQuestions
label failFirstG:
    y "placeholder girl"
    jump gSecond
label failFirstB:
    y "placeholder boi"
    jump bSecond
label gSecond:
    show hpy clse secg
    hide nrm opn secg
    with fade
    gs "Wow [name], I actually didn't expect you to make it to the next round!"
    y "That's a compliment coming from you."
    gs "Don't expect it again from me."
    y "I probably won't."
    gs "Would you still like to continue?"
menu:
    "Sure, why not.":
        show hpy clse secg
        gs "Hmm, you could've said no."
        y "Why?"
        gs "Doesn't matter, the club's Vice President will be in charge of the moderate round."
        y "Oh okay, which one is she?"
        gs "She's the girl with short hair over there at the table."
        y "Thank you."
        gs "Oh yea before I forget, her name is Beatrice."
        y "Okay."
        "*walks over to said girl who is busy arranging some papers on the table*"
        y "Excuse me, Beatrice."
        "*said girl looks up towards you"
        hide hpy clse secb dissolve
        hide sad clse secb dissolve
        show hpy clse vpg
        with fade
        gvp "Oh hello! I guess you know my name from Ysa."
        y "Yep."
        gvp "Good, Let's start off with the first question..."
        jump mediumQuestions
    "May I go?":
        show nrm clse secg
        gs "Who says you can?"
        y "But I..."
        gs "No excuses! Just go talk to the Vice President because she'll be in charge of the moderate round."
        y "What does she look like?"
        gs "She's the girl with short hair over there at the table."
        y "Thank you."
        gs "Oh yea before I forget, her name is Beatrice."
        y "Okay."
        "*walks over to said girl who is busy arranging some papers on the table*"
        y "Excuse me, Beatrice."
        "*said girl looks up towards you"
        hide nrm clse secb dissolve
        hide sad clse secb dissolve
        show nrm clse vpg
        with fade
        gvp "Oh hello! I guess you know my name from Ysa."
        y "Yep."
        gvp "Good, Let's start off with the first question..."
        jump mediumQuestions
label bSecond:
    show hpy clse secb
    hide nrm opn secb
    with fade
    bs "Hey [name]! You made it to the next round!"
    y "Thanks?"
    bs "Would you still like to continue?"
menu:
    "Sure.":
        show hpy clse secb
        bs "Great! However, for the next round our Vice President will be the one to ask you the questions."
        y "Who?"
        bs "His name is Kyle."
        y "That doesn't help me..."
        bs "He's the one over there in the navy blue sweater."
        y "Oh, thanks."
        "*walks over to said boy who seems to be busy looking at his phone*"
        y "Excuse me."
        "*boy looks up towards you*"
        hide hpy clse secb dissolve
        hide sad clse secb dissolve
        show hpy clse vpb
        with fade
        bvp "Oh! My apologies, I didn't notice someone walking up in front of me."
        y "Ehh, it's cool."
        bvp "Alright then, My name is Kyle, which you probably already know."
        y "Yep."
        bvp "Splendid!"
        bvp "Let's start this off with the first item..."
        jump mediumQuestions
    "Uhm...I'm sorry but I kinda have to go.":
        show nrm clse secb
        bs "Go where?"
        y "Uhm..."
        bs "Don't worry, the questions next round aren't that difficult."
        y "Fine fine."
        bs "Great! However, for the next round our Vice President will be the one to ask you the questions."
        y "Who?"
        bs "His name is Kyle."
        y "That doesn't help me..."
        bs "He's the one over there in the navy blue sweater."
        y "Oh, thanks."
        "*walks over to said boy who seems to be busy looking at his phone*"
        y "Excuse me."
        "*boy looks up towards you*"
        hide nrm clse secb dissolve
        hide sad clse secb dissolve
        show hpy clse vpb
        with fade
        bvp "Oh! My apologies, I didn't notice someone walking up in front of me."
        y "Ehh, it's cool."
        bvp "Alright then, My name is Kyle, which you probably already know."
        y "Yep."
        bvp "Splendid!"
        bvp "Let's start this off with the first item..."
        jump mediumQuestions
label failSecondG:
    y "placeholder girl"
    jump gThird
label failSecondB:
    y "placeholder boi"
    jump bThird
label gThird:
    show hpy opn vpg
    with fade
    gvp "You’re doing great [name]! One last round before you beat the game!"
    y "Oh coo-"
    y "Wait."
    y "What game?"
    gvp "Sorry! I meant quiz, I'm a little bit tired from classes."
    y "Are you okay?"
    gvp "Yes, don't worry about me, I'll be fine."
    y "Oh okay."
    gvp "So, are you ready for the final round?"
menu:
    "Why not?":
        show hpy opn vpg
        gvp "Perfect!"
        gvp "It's good that you're willing to continue!"
        gvp "But for this last round...."
        gvp "Our president will be the one to ask the questions for this round."
        y "Really?"
        gvp "Mhm, don't be scared, she's really nice."
        y "I'm not, don't worry."
        y "So, which one is she?"
        "*looks around the room*"
        gvp "You already know what she looks like."
        y "Huh?"
        gvp "She's the one who announced this whole quiz bowl earlier."
        y "Oh her! She's the one in a pony tail with a clipboard in her hands right?"
        gvp "That's right."
        y "Thanks!"
        "*walks over to said girl*"
        y "Um excuse me, I'm here for the final round?"
        hide hpy opn vpg dissolve
        show hpy opn presg
        with fade
        gp "Hey [name]. It's nice to see you participating in club activities."
        y "You and I both."
        gp "Congratulations for reaching this round."
        y "Thanks, it means a lot coming from you um..."
        gp "Ella."
        y "Ella."
        gp "Sorry, I forgot you don't know my name."
        y "It's cool. I don't mind."
        gp "Thank you."
        y "Now, lets begin with the first question..."
        jump hardQuestions
    "No thanks.":
        show hpy opn vpg
        gvp "Hey, this will be the last round, so don't give up yet."
        gvp "Don't worry, you'll do fine."
        y "Whatever you say, I guess?"
        gvp "Plus, the president will be the one to ask you the questions this time"
        gvp "It's good that you're willing to continue!"
        gvp "But for this last round...."
        gvp "Our president will be the one to ask the questions for this round."
        y "Really?"
        gvp "Mhm, don't be scared, she's really nice."
        y "I'm not, don't worry."
        y "So, which one is she?"
        "*looks around the room*"
        gvp "You already know what she looks like."
        y "Huh?"
        gvp "She's the one who announced this whole quiz bowl earlier."
        y "Oh her! She's the one in a pony tail with a clipboard in her hands right?"
        gvp "That's right."
        y "Thanks!"
        "*walks over to said girl*"
        y "Um excuse me, I'm here for the final round?"
        hide hpy opn vpg dissolve
        show hpy opn presg
        with fade
        gp "Hey [name]. It's nice to see you participating in club activities."
        y "You and I both."
        gp "Congratulations for reaching this round."
        y "Thanks, it means a lot coming from you um..."
        gp "Ella."
        y "Ella."
        gp "Sorry, I forgot you don't know my name."
        y "It's cool. I don't mind."
        gp "Thank you."
        y "Now, lets begin with the first question..."
        jump hardQuestions
label bThird:
    show hpy opn vpb
    with fade
    bvp "I'm impressed with your progress, just one more round before you finish game."
    y "Game? What game?"
    bvp "I meant quiz, sorry. Are you ready for the final round?"
menu:
    "I've made it this far.":
        show hpy opn vpb
        bvp "That's good to hear! However, for this last round...."
        bvp "Our president will be the one to ask the questions."
        y "Oh, cool!"
        bvp "Cool indeed, he's the one over there. He's the same one who announced this whole quiz bowl."
        "*Kyle points towards a boy with an Ateneo Varsity Jacket*"
        y "Oh I see, Thanks."
        "*walks over to said boy and reaches over to poke him on the shoulder to get his attention*"
        "*the boy turns around and regards you with a smile*"
        hide hpy opn vpb dissolve
        show hpy opn presb
        with fade
        bp "Hey there [name]!"
        y "Hello."
        bp "Congratulations for reaching this round!"
        bp "Before we start, I'm Oscar, the greatest basketball player of all time!"
        y "Uhm, it's nice to see you putting yourself in high regard?"
        bp "Yep! Now, let us start with the first question..."
        jump hardQuestions
    "I'm tired.":
        show nrm opn vpb
        bvp "Hey, don't give up now."
        bvp "Don't worry, this will be the last round."
        y "Ok fine fine."
        bvp "Excellent! However, for this last round...."
        bvp "Our president will be the one to ask the questions."
        y "Oh, cool!"
        bvp "Cool indeed, he's the one over there. He's the same one who announced this whole quiz bowl."
        "*Kyle points towards a boy with an Ateneo Varsity Jacket*"
        y "Oh I see, Thanks."
        "*walks over to said boy and reaches over to poke him on the shoulder to get his attention*"
        "*the boy turns around and regards you with a smile*"
        hide hpy opn vpb dissolve
        show hpy opn presb
        with fade
        bp "Hey there [name]!"
        y "Hello."
        bp "Congratulations for reaching this round!"
        bp "Before we start, I'm Oscar, the greatest basketball player of all time!"
        y "Uhm, it's nice to see you putting yourself in high regard?"
        bp "Yep! Now, let us start with the first question..."
        jump hardQuestions
