label testLanderH:
    scene classroom
    $ finalScore = quizPointsE + quizPointsM + quizPointsH
    if (finalScore > 20 and finalScore < 30):
        if gender == "male":
            show hpy clse presb
        elif gender == "female":
            show hpy clse presg
        "Your final tally is [finalscore]"
    elif (finalScore > 10 and finalScore < 20):
        if gender == "male":
            show hpy clse vpb
        elif gender == "female":
            show hpy clse vpg
        "Your final tally is [finalscore]"
    elif (finalScore > 0 and finalScore > 10):
        if gender == "male":
            show hpy clse secb
        elif gender == "female":
            show hpy clse secg
        "Your final tally is [finalscore]"
    else:
        "It seems like your results didn’t make it through.... Still, you did a great job! Would you like to try again?"
menu:
    "Yes":
        jump start
    "No":
        return