label mediumQuestions:
    $ timeout = 15
    $ timeout_label = "noAnswerM"
    $ mediumQuestions = [
        {"question": "Who designed the first analytical engine?" , "answer" : [["Charles Babbage " , "right"] , ["Guglielmo Marconi" , "wrong"] , ["Nikola tesla" , "wrong"] ,["Philo Taylor Fransworth" , "wrong"]]},
        {"question": "When was Google invented?" , "answer" : [["September 1998" , "right"] , ["February 2004" , "wrong"] , ["March 1998" , "wrong"] ,["February 2001" , "wrong"]]},
        {"question": "Who designed the qwerty keyboard?" , "answer" : [["Christopher Sholes" , "right"] , ["Henry Mill" , "wrong"] , ["Carlos Glidden" , "wrong"] ,["Samuel Soule" , "wrong"]]},
        {"question": "What is the first computer language?" , "answer" : [["Fortran" , "right"] , ["Swift" , "wrong"] , ["Basic" , "wrong"] ,["Java" , "wrong"]]},
        {"question": "Which is not a type of computer mouse?" , "answer" : [["thumb mice" , "right"] , ["Optical and Laser mice" , "wrong"] , ["Inertial and Gyrosopic mice" , "wrong"] ,["3D Mice" , "wrong"]]},
        {"question": "Which of the software products below is the most expensive?" , "answer" : [["CryEngine 3 ($1.2 million)" , "right"] , ["Adobe Acrobat Capture ($20,000)" , "wrong"] , ["AutoCAD ($4,195)" , "wrong"] ,["Inventor Pro ($7,295)" , "wrong"]]},
        {"question": "Which Microsoft  Windows Operating Systems for pc that was released in conjuction with Windows Server 2008 R2?" , "answer" : [["Windows 7" , "right"] , ["Windows XP" , "wrong"] , ["Windows 8" , "wrong"] ,["Windows 10" , "wrong"]]},
        {"question": "Which keyboard shortcut in windows allows you to show your password on the sign-in screen?" , "answer" : [["Alt+F8 " , "right"] , ["F6" , "wrong"] , ["Ctrl+Spacebar" , "wrong"] ,["Shift+F10" , "wrong"]]},
        {"question": "Which part of a hardware of the computer that cannot be found in the motherboard?" , "answer" : [["Optical drive " , "right"] , ["Chipset" , "wrong"] , ["Video card" , "wrong"] ,["CMOS Battery" , "wrong"]]},
        {"question": "Cold Turkey is a software specifically used for" , "answer" : [["blocks you from using sites on the internet " , "right"] , ["creates flowcharts and diagrams" , "wrong"] , ["multi-track audio editor" , "wrong"] ,["multi-track audio editor" , "wrong"]]},
        {"question": "BIOS means" , "answer" : [["Basic Input Output System " , "right"] , ["Bytes Input Output System" , "wrong"] , ["Binary Interactive Output System" , "wrong"] ,["Binary Interactive Operating System" , "wrong"]]},
        {"question": "The 93 petaflop Sunway TaihuLight is a computer that is made from" , "answer" : [["China" , "right"] , ["Korea" , "wrong"] , ["Japan" , "wrong"] ,["Vietnam" , "wrong"]]},
        {"question": "He is a Filipino programmer who placed 25th globally in Google Code Jam 2015." , "answer" : [["Kevin Atienza " , "right"] , ["Isabel Sieh" , "wrong"] , ["Josie Trinidad" , "wrong"] ,["Armand Serano" , "wrong"]]},
        {"question": "Phlippines’ internet became available on" , "answer" : [["March 1994" , "right"] , ["February 1994" , "wrong"] , ["July 1993" , "wrong"] ,["June 1993" , "wrong"]]},
        {"question": "David Packard and Bill Hewlett are the founders of" , "answer" : [["HP" , "right"] , ["INTEL" , "wrong"] , ["ASUS" , "wrong"] ,["NVIDIA" , "wrong"]]},
    ]

    $ quizPointsM = 0
    $ quiz_length = 15
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
                    "That's Correct"
                else:
                    "Wrong"
            "[ans_1]":
                if b[1][1] == "right":
                    $ quizPointsM += 1
                    "That's Correct"
                else:
                    "Wrong"
            "[ans_2]":
                if b[2][1] == "right":
                    $ quizPointsM += 1
                    "That's Correct"
                else:
                    "Wrong"
            "[ans_3]":
                if b[3][1] == "right":
                    $ quizPointsM += 1
                    "That's Correct"
                else:
                    "Wrong"
        $ quiz_length -= 1
        if quiz_length > 0:
            jump quizm_game
    "The result is [quizPointsM]"
    if gender == "male" :
        jump bThird
    elif gender == "female":
        jump gThird
label noAnswerM: #receives if time has run out
    "You didn't answer in time, lets move on to the next question"
    $ quiz_length -= 1 #subtracts from quiz_length
    if quiz_length > 0: #loops if quiz length is not 0
        jump quizm_game
    "Your score is: [quizPointsM]"
    if gender == "male" :
        jump bThird
    elif gender == "female":
        jump gThird
