label mediumQuestions:
    scene classe middle blurred
    if gender == "male":
        hide hpy clse vpb
        show nrm opn vpb at right
        with fade
    elif gender == "female":
        hide hpy clse vpg
        show nrm opn vpg at right
        with fade
    $ timeout = 30
    $ timeout_label = "noAnswerM"
    $ mediumQuestions = [
        {"question": "Who designed the first analytical engine?" , "answer" : [["Charles Babbage " , "right"] , ["Guglielmo Marconi" , "wrong"] , ["Nikola tesla" , "wrong"] ,["Philo Taylor Fransworth" , "wrong"]]},
        {"question": "When was Google invented?" , "answer" : [["September 1998" , "right"] , ["February 2004" , "wrong"] , ["March 1998" , "wrong"] ,["February 2001" , "wrong"]]},
        {"question": "Who designed the qwerty keyboard?" , "answer" : [["Christopher Sholes" , "right"] , ["Henry Mill" , "wrong"] , ["Carlos Glidden" , "wrong"] ,["Samuel Soule" , "wrong"]]},
        {"question": "What is the first computer language?" , "answer" : [["Fortran" , "right"] , ["Swift" , "wrong"] , ["Basic" , "wrong"] ,["Java" , "wrong"]]},
        {"question": "Which is not a type of computer mouse?" , "answer" : [["thumb mice" , "right"] , ["Optical and Laser mice" , "wrong"] , ["Inertial and Gyrosopic mice" , "wrong"] ,["3D Mice" , "wrong"]]},
        {"question": "Pairs of chromosomes that are similar in size and genetic composition are" , "answer" : [["Homologous Chromosomes" , "right"] , ["Haploid" , "wrong"] , ["Diploid" , "wrong"] ,["Chromitids" , "wrong"]]},
        {"question": "Modification of proteins takes place, often determining the final destination for these proteins" , "answer" : [["Golgi Apparatus" , "right"] , ["Nucleus" , "wrong"] , ["Mitochondria" , "wrong"] ,["Smooth and Rough Endoplasmic Reticulum" , "wrong"]]},
        {"question": "Saliva contains all of the following EXCEPT" , "answer" : [["Hormones" , "right"] , ["Amylase" , "wrong"] , ["Bacteria-killing Enzymes" , "wrong"] ,["Antibodies" , "wrong"]]},
        {"question": "Some bacteria are metabolically active in hot springs because" , "answer" : [["Their enzymes have high optimal temperatures" , "right"] , ["They are able to maintain a cooler internal temperature" , "wrong"] , ["High temperatures make catalysis unnecessary" , "wrong"] ,["They use molecules other than proteins or RNAs as their main catalysts" , "wrong"]]},
        {"question": "Which of the following is not true?" , "answer" : [["Fermentation : anaerobic breakdown of glucose that results in a gain of 2 ATP and the end product is only lactate" , "right"] , ["Pyruvate : end product of glycolysis" , "wrong"] , ["Citric acid cycle : occurs in mitochondria and produces CO2, ATP NADH and FADH2" , "wrong"] ,["Anaerobic : growing or metabolizing in the absence of oxygen" , "wrong"]]},
        {"question": "The most abundant elements in the universe and the Earth's crust are, respectively" , "answer" : [["hydrogen and oxygen" , "right"] , ["oxygen and iron" , "wrong"] , ["helium and carbon" , "wrong"] ,["hydrogen and helium" , "wrong"]]},
        {"question": "The total number of atoms present in one formula unit of CO2(SO4)3 is" , "answer" : [["17" , "right"] , ["14" , "wrong"] , ["16" , "wrong"] ,["15" , "wrong"]]},
        {"question": "The nuclear charge for an atom of F is" , "answer" : [["+9" , "right"] , ["0" , "wrong"] , ["+27" , "wrong"] ,["+15" , "wrong"]]},
        {"question": "A mole of a chemical substance represents" , "answer" : [["6.02×10^23 chemical particles of the substance" , "right"] , ["the mass of the substance that will combine with 12.0 g of carbon" , "wrong"] , ["the mass of the substance that will combine with 100.0 g of oxygen" , "wrong"] ,["6.02×10^-23 chemical particles of the substance" , "wrong"]]},
        {"question": "Which of the following was the first to happen?" , "answer" : [["Aguinaldo declared Philippine independence" , "right"] , ["Guerilla warfare against the US was initiated" , "wrong"] , ["The Philippines was ceded to the US by the Treaty of Paris" , "wrong"] ,["Aguinaldo was captured" , "wrong"]]},
        {"question": "Armel is a college professor in humanities. He conducted a research study that is aligned to his discipline. Which type of format or style in citation does Armel needs to follow?" , "answer" : [["MLA" , "right"] , ["APA" , "wrong"] , ["Turbian" , "wrong"] ,["NTFS" , "wrong"]]},
        {"question": "Which part of research paper that consists of concepts and together with their definitions and reference to relevant scholarly literature?" , "answer" : [["Theoretical Framework" , "right"] , ["Research Design" , "wrong"] , ["Literature Review" , "wrong"] ,["Research Question" , "wrong"]]},
        {"question": "Tims had conducted a research in which he focused on the lived experiences of his participants. Which kind of qualitative research design he conducted?" , "answer" : [["Phenomenological Study" , "right"] , ["Ethnographic Study" , "wrong"] , ["Field Research" , "wrong"] ,["Grounded Theory" , "wrong"]]},
        {"question": "An ice cube is floating on the surface of water: How will the water level be affected by melting of this ice cube?" , "answer" : [["Water level will remain the same" , "right"] , ["Water level will first rise up then it will go down" , "wrong"] , ["Water level will go down" , "wrong"] ,["Water level will be raised" , "wrong"]]},
        {"question": "As defined in physics, work is:" , "answer" : [["a scalar quantity" , "right"] , ["always a positive quantity" , "wrong"] , ["a vector quantity" , "wrong"] ,["always zero" , "wrong"]]},
        ]
    $ quizPointsM = 0
    $ quiz_length = 10 # number of questions to ask
    $ answer_length = 4
    $ q_ask = []
    $ a_ask = []

    while len(q_ask) < quiz_length:
        $ a = random.choice(mediumQuestions)
        if a not in q_ask:
            $ q_ask.append(a)
        if a not in a_ask:
            $ a_ask.append(a)

    label quizm_game:
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
                    $ quizPointsM += 1
                    if gender == "male":
                        hide sad clse vpb
                        show hpy clse vpb at right
                    elif gender == "female":
                        hide sad clse vpg
                        show hpy clse vpg at right
                    "That's Correct"
                else:
                    if gender == "male":
                        hide hpy clse vpb
                        show sad clse vpb at right
                    elif gender == "female":
                        hide hpy clse vpb
                        show sad clse vpg at right
                    "Wrong"
            "[ans_1]":
                if b[1][1] == "right":
                    $ quizPointsM += 1
                    if gender == "male":
                        hide sad clse vpb
                        show hpy clse vpb at right
                    elif gender == "female":
                        hide sad clse vpg
                        show hpy clse vpg at right
                    "That's Correct"
                else:
                    if gender == "male":
                        hide hpy clse vpb
                        show sad clse vpb at right
                    elif gender == "female":
                        hide hpy clse vpb
                        show sad clse vpg at right
                    "Wrong"
            "[ans_2]":
                if b[2][1] == "right":
                    $ quizPointsM += 1
                    if gender == "male":
                        hide sad clse vpb
                        show hpy clse vpb at right
                    elif gender == "female":
                        hide sad clse vpg
                        show hpy clse vpg at right
                    "That's Correct"
                else:
                    if gender == "male":
                        hide hpy clse vpb
                        show sad clse vpb at right
                    elif gender == "female":
                        hide hpy clse vpb
                        show sad clse vpg at right
                    "Wrong"
            "[ans_3]":
                if b[3][1] == "right":
                    $ quizPointsM += 1
                    if gender == "male":
                        hide sad clse vpb
                        show hpy clse vpb at right
                    elif gender == "female":
                        hide sad clse vpg
                        show hpy clse vpg at right
                    "That's Correct"
                else:
                    if gender == "male":
                        hide hpy clse vpb
                        show sad clse vpb at right
                    elif gender == "female":
                        hide hpy clse vpb
                        show sad clse vpg at right
                    "Wrong"
        $ quiz_length -= 1
        if quiz_length > 0:
            jump quizm_game
    "The result is [quizPointsM]"
    if quizPointsM > 6:
        if gender == "male" :
            jump bThird
        elif gender == "female":
            jump gThird
    else:
        if gender == "male" :
            jump failSecondB
        elif gender == "female":
            jump failSecondG
label noAnswerM: #receives if time has run out
    "You didn't answer in time, lets move on to the next question"
    $ quiz_length -= 1 #subtracts from quiz_length
    if quiz_length > 0: #loops if quiz length is not 0
        jump quizm_game
    "Your score is: [quizPointsM]"
    if quizPointsM > 6:
        if gender == "male" :
            jump bThird
        elif gender == "female":
            jump gThird
    else:
        if gender == "male" :
            jump failSecondB
        elif gender == "female":
            jump failSecondG
