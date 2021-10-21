import random
import math

# What is the hundreds digit of 31253?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal(num, place) :
    for i in range(0,place-1) :
        num = math.floor(num/10)
    return num%10

def type1() :
    num = random.randint(1,500000)
    q = "What is the units digit of " + str(num) + "?\n" 
    m = str(cal(num,1)) + "\n"
    return q,m

def type2() :
    num = random.randint(1,500000)
    q = "What is the tens digit of " + str(num) + "?\n" 
    m = str(cal(num,2)) + "\n"
    return q,m
    
def type3() :
    num = random.randint(1,500000)
    q = "What is the hundreds digit of " + str(num) + "?\n" 
    m = str(cal(num,3)) + "\n"
    return q,m

def type4() :
    num = random.randint(1,500000)
    q = "What is the thousands digit of " + str(num) + "?\n" 
    m = str(cal(num,4)) + "\n"
    return q,m

def type5() :
    num = random.randint(1,500000)
    q = "What is the tenthousands digit of " + str(num) + "?\n" 
    m = str(cal(num,5)) + "\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,5)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    elif types == 3 :
        ques, answer = type3()
    elif types == 4 :
        ques, answer = type4()
    elif types == 5 :
        ques, answer = type5()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
