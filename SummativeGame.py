import AchievementBadge
import textgamelib as lib
import time
import playsound
from pygame import mixer

score = 0
score1 = 0
room = 0
questionCount = 0
j=0
restart = 0

while j<100:

    instructions = input ("Do you want instructions/help?")

    if instructions.lower() == "yes":
        print ("""
        The goal of the game is to get all of the questions right. The questions will focus on three main themes: Inclusion, Diversity, and Justice! For each one, you can achieve a badge, and you will get an overall score at the end! All questions are based on the book, The Proudest Blue.
        
        In the questions, you will be given the options a, b, or c. Please answer the question as either a, b, or c. 
        
        For yes or no, you can either type yes or no.
        
        That is all, I hope you enjoy the game!
        """)
    else:
        print ("Ok, hope you enjoy the game!")

    mixer.init() #Initialzing pyamge mixer
    mixer.music.load('dreamy-beat.mp3') #Loading Music File
    mixer.music.play()

    name = input ("What is your name?\n")
    Intro = input (f"Hello, {name}. Are you ready to learn today?\n")
    if Intro.lower() == "yes":
        print ("I knew you would say yes!")
        print ("Welcome to the Proudest Blue School. Here we learn about Diversity, Inclusion, and Justice!")
        position = input("Which classroom would you like to enter first? 1, 2, or 3?\n")


    while "yes" not in Intro.lower():
        Intro = input ("Please reconsider! Are you ready to learn today?\n")
        if Intro.lower() == "yes":
            print ("I knew you would say yes!")
            print ("Welcome to the Proudest Blue School. Here we learn about Diversity, Inclusion, and Justice!")
            position = input("Which classroom would you like to enter first? 1, 2, or 3?\n")

    if position.lower()=="1":
        room=1

    if position.lower()=="2":
        room=2

    if position.lower()=="3":
        room=3

    mixer.music.stop()

    while questionCount<6:

        if room == 1:

            mixer.init() #Initialzing pyamge mixer
            mixer.music.load('dreamy-beat.mp3') #Loading Music File

            mixer.music.play()

            InclusionIntro = input ("Welcome to the school of Inclusion. Here we learn about Inclusion and why it is important! Ready to learn?\n")

            if InclusionIntro.lower() == "yes":
                print ("Great! Let's learn!\n")

            while "yes" not in InclusionIntro.lower():
                InclusionIntro = input ("Please reconsider! Ready to learn?")
                if InclusionIntro.lower() == "yes":
                    print ("Great! Let's learn!\n")

            mixer.music.stop()

            mixer.init() #Initialzing pyamge mixer
            mixer.music.load('Jeopardy-theme-song.mp3') #Loading Music File

            mixer.music.play()
                
            Question1 = input ("Pretend you are one of the bullies.\nDo you: \na. Apologize to Asiya and tell your friends to stop\nb. Keep on mocking Asiya\nc. Stay silent\n")

            if Question1.lower() == "a":
                print (f"Great Job, {name}!")
                print (chr(int('2705',16)))
                score1 +=1
                score +=1
                questionCount += 1
                playsound.playsound ('Correct.mp3')
                playsound.playsound ('Plankton.mp3')
            else:
                print ("Sorry, not quite.")
                print (chr(int('274C',16)))
                questionCount += 1

            mixer.music.stop()

            print ("\n")



            if questionCount < 6:

                mixer.init() #Initialzing pyamge mixer
                mixer.music.load('Jeopardy-theme-song.mp3') #Loading Music File

                mixer.music.play()

                Question2 = input ("Pretend you are Asiya's Friends.\nDo you: \na. Keep on ignoring bullies and support Asiya.\nb.Join bullies.\n")

                if Question2.lower() == "a":
                    print (f"Great Job, {name}!")
                    print (chr(int('2705',16)))
                    score1 +=1
                    score +=1
                    questionCount += 1
                    playsound.playsound ('Correct.mp3')
                    playsound.playsound ('Plankton.mp3')
                else:
                    print ("Sorry, not quite.")
                    print (chr(int('274C',16)))
                    questionCount += 1

                if score1 == 2:
                    print ("You Have Received The Inclusion Badge!")
                    AchievementBadge.achievementBadge()

                mixer.music.stop()
        
            room=2
        #achievement badge

        if room==2:

            mixer.init() #Initialzing pyamge mixer
            mixer.music.load('dreamy-beat.mp3') #Loading Music File

            mixer.music.play()

            DiversityIntro = input ("Welcome to the school of Diversity. Here we learn about Diversity and why it is important! Ready to learn?\n")

            if DiversityIntro.lower() == "yes":
                print ("Great! Let's learn!\n")

            while "yes" not in DiversityIntro.lower():
                DiversityIntro = input ("Please reconsider! Ready to learn?")
                if DiversityIntro.lower() == "yes":
                    print ("Great! Let's learn!\n")

            mixer.music.stop()

            score2 = 0

            mixer.init() #Initialzing pyamge mixer
            mixer.music.load('Jeopardy-theme-song.mp3') #Loading Music File

            mixer.music.play()

            Question3 = input ("Why do you think there were kids laughing at Asiya's Hijab?\na. She was the only person wearing one\nb. She was making a funny face while wearing it\nc. They did not like the colour\n")

            if Question3.lower() == "a":
                print (f"Great Job, {name}!")
                print (chr(int('2705',16)))
                score2 +=1
                score +=1
                questionCount += 1
                playsound.playsound ('Correct.mp3')
                playsound.playsound ('Plankton.mp3')
            else:
                print ("Sorry, not quite.")
                print (chr(int('274C',16)))
                questionCount += 1

            mixer.music.stop()

            if questionCount < 6:

                Question4 = input ("Why is it important Asiya is proud of her hijab?\na. So people think her fashion sense is good.\nb. She is ignoring the bullies and she is proud of her culture\nc. So people think she is cool.\n")

                mixer.init() #Initialzing pyamge mixer
                mixer.music.load('Jeopardy-theme-song.mp3') #Loading Music File

                mixer.music.play()

                if Question4.lower() == "b":
                    print (f"Great Job, {name}!")
                    print (chr(int('2705',16)))
                    score2 +=1
                    score +=1
                    questionCount += 1
                    playsound.playsound ('Correct.mp3')
                    playsound.playsound ('Plankton.mp3')
                else:
                    print ("Sorry, not quite.")
                    print (chr(int('274C',16)))
                    questionCount += 1

                mixer.music.stop()



            if questionCount < 6:
                mixer.init() #Initialzing pyamge mixer
                mixer.music.load('Jeopardy-theme-song.mp3') #Loading Music File

                mixer.music.play()

                Question5 = input ("Why is it important Asiya has good friends?\na. So she can be popular\nb. So she can bully others.\nc. They embrace her culture and diversity\n")
                    
                if Question5.lower() == "c":
                    print (f"Great Job, {name}!")
                    print (chr(int('2705',16)))
                    score2 +=1
                    score +=1
                    questionCount += 1
                    playsound.playsound ('Correct.mp3')
                    playsound.playsound ('Plankton.mp3')
                else:
                    print ("Sorry, not quite.")
                    print (chr(int('274C',16)))
                    questionCount += 1
            
                if score2 == 3:
                    print ("You have received the Diversity Badge!")
                    AchievementBadge.achievementBadge2()

                mixer.music.stop()
            
            room=3
        #achievementbadge

        if questionCount < 6:
            if room==3:

                mixer.init() #Initialzing pyamge mixer
                mixer.music.load('dreamy-beat.mp3') #Loading Music File

                mixer.music.play()

                JusticeIntro = input ("Welcome to the school of Justice. Here we learn about Justice and why it is important! Ready to learn?\n")

                if JusticeIntro == "yes":
                    print ("Great! Let's learn!")

                while "yes" not in JusticeIntro.lower():
                    JusticeIntro = input ("Please reconsider! Ready to learn?")
                    if JusticeIntro.lower() == "yes":
                        print ("Great! Let's learn!\n")

                score3 = 0

                mixer.music.stop()

                mixer.init() #Initialzing pyamge mixer
                mixer.music.load('Jeopardy-theme-song.mp3') #Loading Music File

                mixer.music.play()

                Question6 = input ("You are a bystander (someone watching) when Asiya is being bullied. Do you:\na. Do nothing\nb. Join Asiya and her friends, tell bullies to stop, and tell a teacher.\nc. Join bullies and mock her\n")


                if Question6.lower() == "b":
                    print (f"Great Job, {name}!")
                    print (chr(int('2705',16)))
                    score3 +=1
                    score +=1
                    questionCount += 1
                    playsound.playsound ('Correct.mp3')
                    playsound.playsound ('Plankton.mp3')
                else:
                    print ("Sorry, not quite.")
                    print (chr(int('274C',16)))
                    questionCount += 1

                if score3 == 1:
                    AchievementBadge.achievementBadge3()
            
            room=1

    print (f"Your final score is: {score}")

    if score == 6:
        print (f"Amazing Job, {name}")

    if score == 0:
        print (f"It's ok, {name}, you'll do better next time!")

    if score > 0 and score < 6:
        print (f"Good effort, {name}")

    print ("You got the following badges:\n")

    if score1 == 2:
        AchievementBadge.achievementBadge()

    if score2 == 3:
        AchievementBadge.achievementBadge2()

    if score3 == 1:
        AchievementBadge.achievementBadge3()

    playsound.playsound('cheering.mp3')

    mixer.music.stop()

    survey = input("On a scale of 1 to 5, how enjoyable was the game?")

    if survey.lower == "1":
        print ("We are sorry you did not enjoy the game.")

    if survey.lower == "2":
        print ("We are sorry you did not enjoy the game.")

    if survey.lower == "3":
        print ("We are happy you enjoyed the game.")

    if survey.lower == "4":
        print ("That's great to hear!")

    if survey.lower == "5":
        print ("Wow! We are so happy you enjoyed the game so much!")
    
    redo = input ("Would you like to play again?")
    if redo.lower() == "yes":
        j += 1
        score = 0
        score1 = 0
        score2 = 0
        score3 = 0
        room = 0
        questionCount = 0
    
    if redo.lower() == "no":
        j += 100

#achievementbadge
#score