##a simple python password generator
import string
import random

if __name__=="__main__":
    s1=string.ascii_lowercase
    #print(s1)
    s2=string.ascii_uppercase
    #print(s2)
    s3=string.digits
    #print(s3)
    s4=string.punctuation
    #print(s4)
    

    PASS_LEN=int(input("WHAT IS THE LENGTH OF PASSWORD YOU NEED ?  "))

    s=[]
    s.extend(list(s1))
    s.extend(list(s2)) 
    s.extend(list(s3))
    s.extend(list(s4)) 

    #print(s)
    random.shuffle(s)
    #print(s)

    print("YOUR SUGGESTED PASSWORD OF ",PASS_LEN,"LENGTH IS :")
    print("".join(s[0:PASS_LEN]))

    ####join----concatenate element of list




    