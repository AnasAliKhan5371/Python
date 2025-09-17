#generates a series of simple random math problems (+, -, *) and keeps track of the user's score.
# emoji - window key+ .

import random

def quiz():
    score=0
    no_of_ques=int(input(" Enter no. of questions : "))

    print("********* QUIZ START *********")

    for i in range(no_of_ques):
        question, c_ans=make_ques()

        try:
            ans=int(input(f"\nQuestion {i+1}: {question} "))

            if ans==c_ans:
                print("Correct!! 👍")
                score+=1
            else:
                print(f"Wrong!! 👎 Correct Answer - {c_ans}")

        except ValueError:
            print(f"Invalid input / Skipping Question.  Correct Answer - {c_ans}")

    print("\n********* QUIZ START *********")
    print(f"Your final score is {score}/{no_of_ques}.")
    if score==no_of_ques:
        print("Perfect Score! 🎉🎉")

def make_ques():
    operator=['+','-','*']
    op=random.choice(operator)

    num1=random.randint(1,10)
    num2 = random.randint(1, 10)

    if op=='-':
        num1, num2 = max(num1,num2), min(num1,num2)

    ques=f"What is {num1} {op} {num2}?"

    if op=='+':
        ans=num1+num2
    elif op=='-':
        ans=num1-num2
    else:
        ans=num1*num2

    return ques,ans

if __name__=="__main__":
    quiz()