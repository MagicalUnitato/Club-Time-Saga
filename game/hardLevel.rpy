label hardQuestions:
    scene classe corner blurred
    if gender == "male":
        hide hpy opn presb
        show nrm opn presb at right
        with fade
    elif gender == "female":
        hide hpy opn presg
        show nrm opn presg at right
        with fade
    $ timeout = 60
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
        {"question": "Phil used 3 gallons of paint to cover 1,125 square feet of a wall. At this same rate, what is the total area of the wall, in square feet, that Phil will cover using 5 gallons of paint?" , "answer" : [["1,875 square feet" , "right"] , ["1,575 square feet" , "wrong"] , ["1,800 square feet" , "wrong"] ,["675 square feet" , "wrong"]]},
        {"question": "A force applied to a rocket gives it an upward acceleration equal to 2 times the acceleration of gravity. The magnitude of the force is equal to" , "answer" : [["three times the weight of the rocket" , "right"] , ["four times the weight of the rocket" , "wrong"] , ["twice the weight of the rocket" , "wrong"] ,["the weight of the rocket" , "wrong"]]},
        {"question": "A satellite is observed to move in a circle about the earth at a constant speed. This means that the force acting upon it is" , "answer" : [["perpendicular to the direction of the satellite's instantaneous velocity" , "right"] , ["none of the above" , "wrong"] , ["parallel to the direction of the satellite's instantaneous velocity" , "wrong"] ,["zero" , "wrong"]]},
        {"question": "When a person stands on a scale in an elevator at rest, the scale reads 800 newtons. When the elevator is allowed to fall freely with acceleration of gravity, the scale reads one of the following. Does the scale read" , "answer" : [["0 newtons" , "right"] , ["400 newtons" , "wrong"] , ["800 newtons" , "wrong"] ,["1600 newtons" , "wrong"]]},
        {"question": "A machine's output is 4000 joules and its frictional losses are 1000 joules. Which of the following is its efficiency? Is it" , "answer" : [["80%" , "right"] , ["75%" , "wrong"] , ["30%" , "wrong"] ,["25%" , "wrong"]]},
        {"question": "Which of these is not true about citric acid cycle?" , "answer" : [["It includes the prep reaction" , "right"] , ["It occurs in the mitochondria" , "wrong"] , ["It produces ATP by substrate-level ATP synthesis" , "wrong"] ,["It is a metabolic pathway, as is glycolysis" , "wrong"]]},
        {"question": "During cellular respiration, acetyl CoA accumulates in which location?" , "answer" : [["Mitochondrial Matrix" , "right"] , ["Mitochondrial Inner Membrane" , "wrong"] , ["Mitochondrial Intermembrane Space" , "wrong"] ,["Cytosol" , "wrong"]]},
        {"question": "Which statement is NOT TRUE?" , "answer" : [["H+ concentration is higher in the stroma than in the thylakoid space" , "right"] , ["The electron transport chain pumps H+ from the stroma into the thylakoid space" , "wrong"] , ["The ATP synthase complex is present in the thylakoid membrane" , "wrong"] ,["None of the above" , "wrong"]]},
        {"question": "The product(s) of the Calvin cycle and a reactant(s) in many plant metabolic pathway is/are" , "answer" : [["Glyceraldehyde-3-phosphate, G3P" , "right"] , ["Adenosine diphosphate, ADP" , "wrong"] , ["Ribulose 1,5-biphosphate, RuBP" , "wrong"] ,["Carbon dioxide, CO2" , "wrong"]]},
        {"question": "An individual has the right to file the WRIT OF AMPARO before the investigation of an administrative case filed against him/her. What fundamental right is invoked by the individual?" , "answer" : [["Right to life, liberty and security" , "right"] , ["Right to self-defense" , "wrong"] , ["Right to due process" , "wrong"] ,["Right to be defended by a public attorney" , "wrong"]]},
        {"question": "Why is it not advisable to repeatedly open the door of a refrigerator?" , "answer" : [["The warm air outside lowers the temperature inside, thus making the refrigerator less efficient" , "right"] , ["It will loosen the refrigerator’s door " , "wrong"] , ["It leads to wastage in electrical energy" , "wrong"] ,["Repeated opening introduces bacteria into the refrigerator" , "wrong"]]},
        {"question": "Which does not exemplify the importance of theoretical framework?" , "answer" : [["None of the above" , "right"] , ["Articulating the theoretical assumptions of a research study forces you to address questions of why and how" , "wrong"] , ["The theoretical framework connects the researcher to existing knowledge" , "wrong"] ,["An explicit statement of  theoretical assumptions permits the reader to evaluate them critically" , "wrong"]]},
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
                    if gender == "male":
                        hide sad clse presb
                        show hpy clse presb at right
                    elif gender == "female":
                        hide sad clse presg
                        show hpy clse presg at right
                    "That's Correct"
                else:
                    if gender == "male":
                        hide hpy clse presb
                        show sad clse presb at right
                    elif gender == "female":
                        hide hpy clse presb
                        show sad clse presg at right
                    "Wrong"
            "[ans_1]":
                if b[1][1] == "right":
                    $ quizPointsH += 1
                    if gender == "male":
                        hide sad clse presb
                        show hpy clse presb at right
                    elif gender == "female":
                        hide sad clse presg
                        show hpy clse presg at right
                    "That's Correct"
                else:
                    if gender == "male":
                        hide hpy clse presb
                        show sad clse presb at right
                    elif gender == "female":
                        hide hpy clse presb
                        show sad clse presg at right
                    "Wrong"
            "[ans_2]":
                if b[2][1] == "right":
                    $ quizPointsH += 1
                    if gender == "male":
                        hide sad clse presb
                        show hpy clse presb at right
                    elif gender == "female":
                        hide sad clse presg
                        show hpy clse presg at right
                    "That's Correct"
                else:
                    if gender == "male":
                        hide hpy clse presb
                        show sad clse presb at right
                    elif gender == "female":
                        hide hpy clse presb
                        show sad clse presg at right
                    "Wrong"
            "[ans_3]":
                if b[3][1] == "right":
                    $ quizPointsH += 1
                    if gender == "male":
                        hide sad clse presb
                        show hpy clse presb at right
                    elif gender == "female":
                        hide sad clse presg
                        show hpy clse presg at right
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
