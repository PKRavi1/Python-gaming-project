print("Welcome to python quiz")

playing=input("Do you want to play:")

if playing.lower() !="yes":
    quit()
print("okay!lets play...")
score=0
answer=input("who developed python?")
if answer.lower() =="guido van rossum":
    print("correct !")
    score=+1
else:
    print("incorrect !")
answer=input("what is the correct extension of python file?")
if answer.lower() == ".py":
    print("the second answer is right !")
    score=score+1
else:
    print("incorrect answer !")
answer=input("what do we use to define a block of code in python?")
if answer.lower() =="indentation":
    print("the third answer is right !")
    score=score+1
else:
    print("incorrect answer !")
answer=input("what are collection of object called?")
if answer.lower() =="classes":
    print("the forth answer is right!")
    score=score+1
else:
    print("incorrect!")
answer=input("what are methods inside the class in python")
if answer.lower() =="functions":
    print("the fifth answer is correct")
    score=score+1
else:
    print("incorrect!")
answer=input("what are syntax errors also called")
if answer.lower() =="parsing error":
    print("the sixth answer is correct !")
    score=score+1
else:
    print("incorrect")
answer=input("what is sequence of character that form search pattern?")
if answer.lower()=="regular expression":
    print("the seventh answer is correct")
    score=score+1
else:
    print("incorrect")
answer=input("what are entity of class?")
if answer.lower() =="object":
    print("the eight answer is correct")
    score=score+1
else:
    print("incorrect")
answer=input("what are the function called which called itself repeatedly?")
if answer.lower() =="recursive function":
    print("the nine question is correct")
    score=score+1
else:
    print("incorrect !")
answer=input("what are specifide after function name,inside parameters?")
if answer.lower()=="argument":
    print("the 10th answer is correct")
    score=score+1
else:
    print("incorrect !")
print("you got "+str(score)+"wuestion correct!")
print("you have got:"+str((score/10)*100)+"%")
    