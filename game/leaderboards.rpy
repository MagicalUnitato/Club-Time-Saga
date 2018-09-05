##label leaderboards:
##    python:
##        db = Base('database/test.pdl')
##        db.create('name' , 'score')
##        if db.exists():
##            db.open()
##        else:
##            db = Base('database/test.pdl')
##            db.create('name' , 'score')
##        db.insert(name = name , score = quizPoints)
##        db.commit()
##    jump testLanderM
