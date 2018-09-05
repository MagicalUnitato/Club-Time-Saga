label hardQuestions:
    $ timeout = 20
    $ timeout_label = "noAnswerH"
    $ hardQuestions = [
        {"question": "It is a protocol designed to search, retrieve and display documents from remote sites on the internet." , "answer" : [["Gopher" , "right"] , ["Telnet" , "wrong"] , ["Archie" , "wrong"] ,["Ludwig" , "wrong"]]},
        {"question": "How many times does an average person blink in a minute when using the computer?" , "answer" : [["7" , "right"] , ["6" , "wrong"] , ["21" , "wrong"] ,["10" , "wrong"]]},
        {"question": "Which of the following binary codes is true?" , "answer" : [["01011001 01110010 = Yb" , "right"] , ["01010010 01101011 = Na" , "wrong"] , ["01000011 01101101 = Cl" , "wrong"] ,["01000110 01111000 = Ba" , "wrong"]]},
        {"question": "How many kilobytes are there in 5 terabytes?" , "answer" : [["5368709120 KB" , "right"] , ["5423528620 KB" , "wrong"] , ["5000000020 KB" , "wrong"] ,["5264991420 KB" , "wrong"]]},
        {"question": "November 30 is known as" , "answer" : [["Computer Security Day" , "right"] , ["Computer Programming Day" , "wrong"] , ["Computer Scientists Day" , "wrong"] ,["Computer Termination Day" , "wrong"]]},
        {"question": "Determine how many letters are there in the longest possible word a person can write using only one row in the keyboard." , "answer" : [["10" , "right"] , ["6" , "wrong"] , ["13" , "wrong"] ,["9" , "wrong"]]},
        {"question": "Which of the following statements is incorrect?" , "answer" : [["Intel HD Graphics 515 and 520 are not suitable for running Adobe Photoshop." , "right"] , ["00110011 - 00110100 = -1" , "wrong"] , ["It is not possible to create a folder named 'con' on a windows computer." , "wrong"] ,["The windows startup sound was composed using a Mac." , "wrong"]]},
        {"question": "A Macintosh LC575 has ___ speaker holes." , "answer" : [["182" , "right"] , ["134" , "wrong"] , ["56" , "wrong"] ,["85" , "wrong"]]},
        {"question": "The first micro-processor created by Intel which was originally designed for a calculator was called (Translate the code to decipher the choices)" , "answer" : [["00110100 00110000 00110000 00110100" , "right"] , ["00110100 00110000 00110000 00110011" , "wrong"] , ["00110100 00110000 00110001 00110110" , "wrong"] ,["00110100 00110000 00110011 00110010" , "wrong"]]},
        {"question": "I .Peter Gosling invented Java  II. Andy Hejlsberg reinvents Java and calls it C#" , "answer" : [["Both are false" , "right"] , ["I is True, II is False" , "wrong"] , ["I is False, II is true" , "wrong"] ,["Both are true" , "wrong"]]},
        {"question": "Under the Insert Tab in Microsoft Word, what does the 2nd option do?" , "answer" : [["Inserts a table" , "right"] , ["Inserts a picture" , "wrong"] , ["Inserts a clip art" , "wrong"] ,["Inserts an equation" , "wrong"]]},
        {"question": "Which of the following correctly solves the version number of Python which was released on August 2, 2018?" , "answer" : [["version number = 1.5.2 + 2.0.4" , "right"] , ["version number = 14.8.36 / 2" , "wrong"] , ["version number = 3.5 * 3.6.7" , "wrong"] ,["version number = 5.6.8 - 1.3.5" , "wrong"]]},
        {"question": "The 3rd language translation of the english precaution (Do not grab) indicated on the arm of the EPSON projectors of each classroom in the Ateneo de Davao University is ______." , "answer" : [["Bitte nicht drahāngen" , "right"] , ["사랑이란 무엇인가" , "wrong"] , ["Quiero morir y tomar leche" , "wrong"] ,["わたしは たまご" , "wrong"]]},
        {"question": "Which of following programs is the longest one to download?" , "answer" : [["Atom" , "right"] , ["Netbeans IDE" , "wrong"] , ["Python" , "wrong"] ,["Notepad ++" , "wrong"]]},
        {"question": "What was the name of the first electronic computer?" , "answer" : [["ENIAC" , "right"] , ["ETCPC" , "wrong"] , ["EPAIC" , "wrong"] ,["ESAIC" , "wrong"]]},
    ]

    $ quizPointsH = 0
    $ quiz_length = 20
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
