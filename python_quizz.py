print("wellcome to my computer quize!")

paying = input("Do you want to play? ")

if paying.lower() !="yes":
    quit();

print("Ok lets play :) ")
score=0


answer = input("CPU stands for ");
if answer.lower() == "central processing unit":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")


answer = input("GPU stands for ");
if answer.lower() == "graphic processing unit":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")


answer = input("RAM stands for ");
if answer.lower() == "ramdom access memory":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")
    

answer = input("ROM stands for ");
if answer.lower() == "read only memory":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")
    
    
answer = input("PSU stands for ");
if answer.lower() == "power supply":
    print("Correct! ")
    score +=1
else:
    print("Incorrect!")


print("You got "+str(score) + " questions Correct")
print("You got "+str((score/4) *100) + "%")
