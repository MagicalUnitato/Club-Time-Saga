init python:
    import random
    def shuffle_answers(x):
            random.shuffle(x)
            return x
label easyQuestions:
    scene classroom blurred
    if gender == "male":
        hide nrm opn secb
        show nrm opn secb at right
        with fade
    elif gender == "female":
        hide nrm opn secg
        show nrm opn secg at right
        with fade
    $ timeout = 20
    $ timeout_label = "noAnswer"
    $ easyQuestions = [
        {"question": "What do you call to the language of computers?" , "answer" : [["Binary language" , "right"] , ["Computing Language" , "wrong"] , ["Pseudocode" , "wrong"] ,["Numerical Language" , "wrong"]]},
        {"question": "Which among the following is a hardware component?" , "answer" : [["Motherboard" , "right"] , ["Codes" , "wrong"] , ["Program" , "wrong"] ,["App" , "wrong"]]},
        {"question": "What do you call to numerical variables in coding?" , "answer" : [["Integer" , "right"] , ["String" , "wrong"] , ["Boolean" , "wrong"] ,["Decision" , "wrong"]]},
        {"question": "What do you call to a continuous flow that ends when a certain condition is met?" , "answer" : [["Loop" , "right"] , ["Sequence" , "wrong"] , ["Decisions" , "wrong"] ,["Variables" , "wrong"]]},
        {"question": "What is an example of a volatile memory?" , "answer" : [["RAM" , "right"] , ["Hard Drive" , "wrong"] , ["Flash Drive" , "wrong"] ,["Optical Disc" , "wrong"]]},
        {"question": "Which of the following is a property of both gases and liquids?" , "answer" : [["indefinite shape" , "right"] , ["definite shape" , "wrong"] , ["definite volume" , "wrong"] ,["indefinite volume" , "wrong"]]},
        {"question": "In which of the following pairs of properties are both chemical properties?" , "answer" : [["decomposes at 500ºC and reacts with bromine" , "right"] , ["freezes at 10ºC and nonflammable" , "wrong"] , ["poor conductor of heat and is reddish brown in color" , "wrong"] ,["has a low density and is very hard" , "wrong"]]},
        {"question": "The most abundant elements in the universe and the Earth's crust are, respectively" , "answer" : [["hydrogen and helium" , "right"] , ["oxygen and iron" , "wrong"] , ["helium and carbon" , "wrong"] ,["hydrogen and oxygen" , "wrong"]]},
        {"question": "Which of the following statements is correct" , "answer" : [["Both elements and compounds are pure substances" , "right"] , ["Compounds, but not elements, are pure substances" , "wrong"] , ["Elements, but not compounds, are pure substances" , "wrong"] ,["Neither elements nor compounds are pure substances" , "wrong"]]},
        {"question": "Normal human body cells contain how many chromosomes?" , "answer" : [["46" , "right"] , ["44" , "wrong"] , ["23" , "wrong"] ,["22" , "wrong"]]},
        {"question": "At the end of meiosis I, the resulting two cells are" , "answer" : [["genetically different" , "right"] , ["genetically identical" , "wrong"] , ["identical in all ways" , "wrong"] ,["hexaploid" , "wrong"]]},
        {"question": "Genes are composed of" , "answer" : [["DNA" , "right"] , ["proteins" , "wrong"] , ["chromosomes" , "wrong"] ,["carbohydrates" , "wrong"]]},
        {"question": "Which situation can be represented by the equation y=8x" , "answer" : [["Nilay bought x items at a store. Each item costs $8. Nilay spent a total of y dollars at the store" , "right"] , ["Nilay baked y batches of cookies. There were 8 cookies in each batch. Nilay baked a total of x cookies" , "wrong"] , ["Nilay correctly answered x questions on a quiz. Each question was worth y points. Nilay received a total of 8 points on the quiz" , "wrong"] ,["Nilay earned $8 for babysitting. He also earned x dollars for mowing lawns. Nilay earned a total of y dollars for babysitting and mowing lawns" , "wrong"]]},
        {"question": "Nadia will survey 50 students in her town to find out what their favorite summertime activity is. Which group would likely give the best representation for her survey?" , "answer" : [["50 students in her school" , "right"] , ["50 students at a library" , "wrong"] , ["50 students at a shopping mall" , "wrong"] ,["50 students taking swimming lessons" , "wrong"]]},
        {"question": "It is highly likely that Malika will randomly select the letter A from a group of letters. From which group of letters could Malika be selecting?" , "answer" : [["A, A, J, A, A, K" , "right"] , ["A, B, C, A, D" , "wrong"] , ["A, F, A, G, A, H" , "wrong"] ,["A, E, I, O, U" , "wrong"]]},
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
                        show hpy clse secb at right
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg at right
                else:
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb at right
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg at right
                    "Wrong"
            "[ans_1]":
                if b[1][1] == "right":
                    $ quizPointsE += 1
                    "That's Correct"
                    if gender == "male":
                        hide sad clse secb
                        show hpy clse secb at right
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg at right
                else:
                    "Wrong"
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb at right
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg at right
            "[ans_2]":
                if b[2][1] == "right":
                    $ quizPointsE += 1
                    "That's Correct"
                    if gender == "male":
                        hide sad clse secb
                        show hpy clse secb at right
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg at right
                else:
                    "Wrong"
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb at right
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg at right
            "[ans_3]":
                if b[3][1] == "right":
                    $ quizPointsE += 1
                    "That's Correct"
                    if gender == "male":
                        hide sad clse secb
                        show hpy clse secb at right
                    elif gender == "female":
                        hide sad clse secg
                        show hpy clse secg at right
                else:
                    "Wrong"
                    if gender == "male":
                        hide hpy clse secb
                        show sad clse secb at right
                    elif gender == "female":
                        hide hpy clse secb
                        show sad clse secg at right
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
