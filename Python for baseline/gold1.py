#James Campbell
#Sept 2022
#Gold 1

import random

#set score counter to 0
score=0
for ques in range(10):
    num1=random.randint(5,50)
    num2=random.randint(5,50)
    #decide if a +, - or * question using a random number
    op=random.randint(1,3)
    print("Question", ques+1)
    
    #calculate the answer and output the question
    if op==1:
        ans=num1+ num2
        print(num1,"+",num2,"=")
    elif op==2:
        ans=num1 - num2
        print(num1,"-",num2,"=")
    elif op==3:
        ans=num1 * num2
        print(num1,"*",num2,"=")
    #endif
        
    #get the users answer and convert to an integer
    guess=input(">")
    guess=int(guess)
    #check if correct,  add one to score if it is
    if guess==ans:
        print("Correct!")
        score=score+1
    else:
        print("Incorrect, it is",ans)
    #endif
#endfor
        
print("Your final score is", score)