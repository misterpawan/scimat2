import random
import math

# What is the remainder when num1 is divided with num2 ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal(num1, num2) :
    return num1%num2

def type1() :
    num1 = random.randint(100,10000)
    num2 = random.randint(1,1000)
    q = "What is the remainder when " + str(num1) + " is divided with " + str(num2) + " ?\n" 
    m = str(cal(num1,num2)) + "\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
