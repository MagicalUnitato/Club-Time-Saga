label hardQuestions:
    $ timeout = 20
    $ timeout_label = "noAnswerH"
    $ hardQuestions = [
        {"question": "It is a protocol designed to search, retrieve and display documents from remote sites on the internet." , "answer" : [["Gopher" , "right"] , ["Telnet" , "wrong"] , ["Archie" , "wrong"] ,["Ludwig" , "wrong"]]},
        {"question": "How many times does an average person blink in a minute when using the computer?" , "answer" : [["7" , "right"] , ["6" , "wrong"] , ["21" , "wrong"] ,["10" , "wrong"]]},
        {"question": "Which of the following binary codes is true?" , "answer" : [["01011001 01110010 = Yb" , "right"] , ["01010010 01101011 = Na" , "wrong"] , ["01000011 01101101 = Cl" , "wrong"] ,["01000110 01111000 = Ba" , "wrong"]]},
        {"question": "How many kilobytes are there in 5 terabytes?" , "answer" : [["5368709120 KB" , "right"] , ["5423528620 KB" , "wrong"] , ["5000000020 KB" , "wrong"] ,["5264991420 KB" , "wrong"]]},
        {"question": "November 30 is known as" , "answer" : [["Computer Security Day" , "right"] , ["Computer Programming Day" , "wrong"] , ["Computer Scientists Day" , "wrong"] ,["Computer Termination Day" , "wrong"]]},
        {"question": "Samantha is painting the outside of a box that is in the shape of a rectangular prism. Its length is 18 cm, its width is 6 cm, and its height is 3 cm. What is the surface area of the box in square centimeters (cm^2)?" , "answer" : [["360 cm^2" , "right"] , ["180 cm^2" , "wrong"] , ["324 cm^2" , "wrong"] ,["162 cm^2" , "wrong"]]},
        {"question": "Jeffrey typed 110 words in 2(3/4) minutes. At this rate, how many words can he type in 4(1/4) minutes?" , "answer" : [["170 words" , "right"] , ["71 words" , "wrong"] , ["165 words" , "wrong"] ,["255 words" , "wrong"]]},
        {"question": "Chris is trimming trees. He can trim 2/3 of a tree in 1/2 of an hour. At what rate can Chris trim trees?" , "answer" : [["1(1/3) trees per hour" , "right"] , ["1(1/6) trees per hour" , "wrong"] , ["1/3 of a tree per hour" , "wrong"] ,["1/6 of a tree per hour" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
        {"question": "" , "answer" : [["" , "right"] , ["" , "wrong"] , ["" , "wrong"] ,["" , "wrong"]]},
    ]

    $ quizPointsH = 0
    $ quiz_length = 10 # number of questions to ask
    $ answer_length = 4
    $ q_ask = []
    $ a_ask = []

    while len(q_ask) < quiz_length:
        $ a = random.choice(hardQuestions)
        if a not in q_ask:
            $ q_ask.append(a)
        if a not in a_ask:
            $ a_ask.append(a)

    label quizH_game:
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
                    $ quizPointsH += 1
                    "That's Correct"
                else:
                    "Wrong"
            "[ans_1]":
                if b[1][1] == "right":
                    $ quizPointsH += 1
                    "That's Correct"
                else:
                    "Wrong"
            "[ans_2]":
                if b[2][1] == "right":
                    $ quizPointsH += 1
                    "That's Correct"
                else:
                    "Wrong"
            "[ans_3]":
                if b[3][1] == "right":
                    $ quizPointsH += 1
                    "That's Correct"
                else:
                    "Wrong"
        $ quiz_length -= 1
        if quiz_length > 0:
            jump quizH_game
    "The result is [quizPointsH]"
    if quizPointsM > 6:
        jump testLanderH
    else:
        if gender == "male" :
            jump failThirdB
        elif gender == "female":
            jump failThirdG
label noAnswerH: #receives if time has run out
    "You didn't answer in time, lets move on to the next question"
    $ quiz_length -= 1 #subtracts from quiz_length
    if quiz_length > 0: #loops if quiz length is not 0
        jump quizH_game
    "Your score is: [quizPointsH]"
    if quizPointsM > 6:
        jump testLanderH
    else:
        if gender == "male" :
            jump failThirdB
        elif gender == "female":
            jump failThirdG
