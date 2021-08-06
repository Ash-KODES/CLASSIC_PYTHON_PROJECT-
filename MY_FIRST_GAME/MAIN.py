##THIS GAME WILL HAVE CHOSES(QUITE RANDOM) AND YOUR TASK IS TO MAKE IT TO THE END
from sys import exit
print("HELLO,WELCOME TO THE GAME")
print("YOUR ONLY TASK IS TO MAKE IT TO THE END")

name=input("WHAT IS YOUR NAME FELLA ? ")
age=int(input("WHAT IS YOUR AGE ? "))
health=100
if age<19:
    print("SORRY YOU CANT PLAY :( CHOTU PADHO JAKE VARNA IET MAI ADMISSION HOJAYEGA")
    exit()
else:
    print("OKKAI BOI")
    play=input("DO YOU WANT TO PLAY? YES/NO  ").lower()
    if play=="yes":
        print("FINALLY A WORTHY OPONENT")
        print("I AM GIVING YOU " ,health ,"HEALTH POINTS IN THE BIGGINING")
    else:
        print("acha,YEH BHI THEEK HAI :(")
        exit()


print("HELLO", name, ",so you are ",age," year old")

crush=input("YOUR CRUSH NAME ?  ")
print("HEEHE BOI  ")
print("SENDING THIS NAME TO YOUR FREINDS RIGHT AWAY,anyways CONTINUE THE GAME")




left_or_right=input("OKAY VRO,YOUR FIRST CHOICE...WANNA GO LEFT OR RIGHT ? L/R  ").lower()
if left_or_right=='l' :
    river=input("NICE,YOU FOLLOWED THE RIGHT AND REACHED A LAKE...DO YOU WANT TO SWIM ACROSS OR GO AROUND (across/around) ?  ").lower()

    if river=='across' :
        print("WELL THERE WERE PRINNAHA IN THE LAKE AND YOU LOST SOME HEALTH...LOL")
        print("YOUR NEW HEALTH IS ",health-30 ,":(")

        play_again=input("DO YOU WANT TO continue? YES/NO").lower()
        print("KHELNA PADEGA...NO CHIOCE")

        print("AHEAD IN THE RIVER THANOS WAS WAITING FOR YOU")
        run=input("WANNA FIGHT OR RUN ? RUN/FIGHT  ").lower()
        if run=='fight':
            print("HE SNAPPED AND YOU LOST(DIED)")
            exit()
        elif run=='run':
            print("OOKAY,STILL YOU LOST SOME HEALTH COWARD")

            print("NEW HEALTH POINTS ",health-30)
            play_again=input("DO YOU WANT TO continue? YES/NO").lower()
            if play_again=='yes' :
                print("NO BOLNA THA,,,YOU DIED")
                exit()
            else :
                print("SO FINALLY YOU REACHED YOU LAST LOCATION...'A CURSED PALACE'")
                palace=input("WANNA GO IN ? YES/NO").lower()
                if palace=='no' :
                    print("YOU LOST,BAHAR BATHNE KE LIYE THODI NA GAME SURU KI THI")

                else:
                    print("SO NOW YOU ARE INSIDE THE PALACE AND SUDDENLY A 'person' ARRIVES")
                    print("AND HE ASKED YOU A VERY VERY TOUGH QUESTION(VERY TOUGH)")
                    play_again=input("WANT TO ANSWER OR LEAVE ?(since ques is tough as heck) ANS/LEAVE ").lower()
                    if play_again=='ans':
                        print("SO YOU HAVE CHOSEN DEATH")

                        print("ANSWER IT")

                        play_again=input("END SEM KI DATE AUG MAI KAB SE HAI ?")
                        if play_again=='17':
                            print("TUM TO TOMPER HO PLEASE MUJE PASS KARRA DENA,PADH LO TUM JAKE")
                            exit()
                        else :
                            print("17 SE HAI BE PADH LO JAKE KYOUKI AUR LAMBI STORY NAHI KHECH SAKTA MAI")
                            print("BTW PURE GAME MAI HEALTH KA ROLE KUCH THA NAHI PATA NAHI Maine KYO BANYA")

                            print("and THAT GUY WHO ASKED YOU THIS QUES IS NONE OTHER THAN KRUNESH SIR")
                            exit()


        else :
            print("YE KYA LIKH RAHE HO VRO TUMME MARNA PADEGA ABB")
            exit()



    elif river=='around' :
        print("OOPSI,,THERE WERE WOLF AROUND THE RIVER, YOU LOST SOME HEALTH BUT REACHED A CURSED PALACE")
        print("NEW HEALTH POINT ",health-40," :(")

        play_again=input("DO YOU WANT TO CONTINUE ? YES/NO").lower()
        if play_again=='yes':
            play_again=input("SO HERE,MET YOUR YOUR CRUSH AND IF YOU WANT YOU CAN GIVE HEALTH TO HER,WILL YOU ?  YES/NO").lower()
            if play_again=='yes' :
                print("TO MARRO FIR...LADKI KA CHAKAR BABU BHAIYA")
                exit()
            else :
                print("BADIYA BHAI PIGHALNA MAT")
                print("MUJHE GARV HAI BETA TUMPE")

                print("BUT PLOT TWIST,,,,,,YOUR CRUSH BECOME THANOS AND SNAPPED")
                print("YOU DIED")
                exit()

    else :
        print("YOU DIED")
        exit()

else :
    print("YOU FELL AND LOST...BETTER LUCK NXT TIME")
    print("SOMETIME DECISIONS WHICH SEEMS RIGHT ARE NOT ALWAYS RIGHT ~ashu2021")
    print("LOL")
    exit
