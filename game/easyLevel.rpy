init python:
    import random
    def shuffle_answers(x):
            random.shuffle(x)
            return x
label easyQuestions:
    $ timeout = 10
    $ timeout_label = "noAnswer"
    $ easyQuestions = [
        {"question": "What do you call to the language of computers?" , "answer" : [["Binary language" , "right"] , ["Computing Language" , "wrong"] , ["Pseudocode" , "wrong"] ,["Numerical Language" , "wrong"]]},
        {"question": "Which among the following is a hardware component?" , "answer" : [["Motherboard" , "right"] , ["Codes" , "wrong"] , ["Program" , "wrong"] ,["App" , "wrong"]]},
        {"question": "What do you call to numerical variables in coding?" , "answer" : [["Integer" , "right"] , ["String" , "wrong"] , ["Boolean" , "wrong"] ,["Decision" , "wrong"]]},
        {"question": "What do you call to a continuous flow that ends when a certain condition is met?" , "answer" : [["Loop" , "right"] , ["Sequence" , "wrong"] , ["Decisions" , "wrong"] ,["Variables" , "wrong"]]},
        {"question": "What is an example of a volatile memory?" , "answer" : [["RAM" , "right"] , ["Hard Drive" , "wrong"] , ["Flash Drive" , "wrong"] ,["Optical Disc" , "wrong"]]},
        {"question": "The word computer is derived from?" , "answer" : [["Computing" , "right"] , ["Commuting" , "wrong"] , ["Completing" , "wrong"] ,["Communication" , "wrong"]]},
        {"question": "What is the most appropriate software for calculating in computer?" , "answer" : [["Microsoft Excel" , "right"] , ["Microsoft Powerpoint" , "wrong"] , ["Microsoft Outlook" , "wrong"] ,["Microsoft Onenote" , "wrong"]]},
        {"question": "What kind of device is Monitor?" , "answer" : [["Output" , "right"] , ["Input" , "wrong"] , ["Semi-Input" , "wrong"] ,["Semi-Output" , "wrong"]]},
        {"question": "In internet terminology IP means" , "answer" : [["Internet Protocol" , "right"] , ["Internet Password" , "wrong"] , ["Internet Pseudocode" , "wrong"] ,["Internet Passcode" , "wrong"]]},
        {"question": "In which field the expert system has application areas of A.I?" , "answer" : [["Artificial Intelligence" , "right"] , ["Robotics" , "wrong"] , ["Hardware Components" , "wrong"] ,["Computer Coding" , "wrong"]]},
    ]

    $ quizPointsE = 0
    $ quiz_length = 10 # number of questions to ask
    $ answer_length = 4
    $ q_ask = []
    $ a_ask = []

    while len(q_ask) < quiz_length:
        $ a = random.choice(easyQuestions)
        if a not in q_ask:
            $ q_ask.append(a)
        if a not in a_ask:
            $ a_ask.append(a)

    label quize_game:
        $ a = random.choice(q_ask)
        $ q_ask.remove(a)
        $ b = shuffle_answers(a["answer"])
        $ d = []
        $ question = a["question"]


        if b[0][1] == "right":
            $ ans_0 = b[0][0]
            $ d.append(b[0][0])
        elif b not in d:
            $ d.append(b[0][0])
            $ ans_0 = d[0]
        if b[1][1] == "right":
            $ ans_1 = b[1][0]
            $ d.append(b[1][0])
        elif b not in d:
            $ d.append(b[1][0])
            $ ans_1 = d[1]
        if b[2][1] == "right":
            $ ans_2 = b[2][0]
            $ d.append(b[2][0])
        elif b not in d:
            $ d.append(b[2][0])
            $ ans_2 = d[2]
        if b[3][1] == "right":
            $ ans_3 = b[3][0]
            $ d.append(b[3][0])
        elif b not in d:
            $ d.append(b[3][0])
            $ ans_3 = d[3]

        menu:
            "[question]"
            "[ans_0]":
                if b[0][1] == "right":
                    $ quizPointsE += 1
                    "That's Correct"
                    if gender == "male":
                        hide sad clse secb
                        show hpy clse secb
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg
                else:
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg
                    "Wrong"
            "[ans_1]":
                if b[1][1] == "right":
                    $ quizPointsE += 1
                    "That's Correct"
                    if gender == "male":
                        hide sad clse secb
                        show hpy clse secb
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg
                else:
                    "Wrong"
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg
            "[ans_2]":
                if b[2][1] == "right":
                    $ quizPointsE += 1
                    "That's Correct"
                    if gender == "male":
                        hide sad clse secb
                        show hpy clse secb
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg
                else:
                    "Wrong"
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg
            "[ans_3]":
                if b[3][1] == "right":
                    $ quizPointsE += 1
                    "That's Correct"
                    if gender == "male":
                        hide sad clse secb
                        show hpy clse secb
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg
                else:
                    "Wrong"
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg
        $ quiz_length -= 1
        if quiz_length > 0:
            jump quize_game
    "Your score is: [quizPointsE]"
    if quizPointsE > 6:
        if gender == "male" :
            jump bSecond
        elif gender == "female":
            jump gSecond
    else:
        if gender == "male" :
            jump failFirstB
        elif gender == "female":
            jump failFirstG
label noAnswer: #receives if time has run out
    "You didn't answer in time, lets move on to the next question"
    $ quiz_length -= 1 #subtracts from quiz_length
    if quiz_length > 0: #loops if quiz length is not 0
        jump quize_game
    "Your score is: [quizPointsE]"
    if quizPointsE > 6:
        if gender == "male" :
            jump bSecond
        elif gender == "female":
            jump gSecond
    else:
        if gender == "male" :
            jump failFirstB
        elif gender == "female":
            jump failFirstG
