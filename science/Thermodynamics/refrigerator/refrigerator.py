import random
import math

# A refrigerator is to maintain eatables kept inside at t1 degree C, if room temperature is t2 degree C. Calculate the coefficient of performance.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000

r = 8.31

def cal1(t1,t2) :
    t1 = t1 + 273
    t2 = t2 + 273   
    return round(t1/(t2-t1),1) 

def cal2(t1,t2) :  
    return round(t1/(t2-t1),1) 

def type1() :
    t = random.randint(1,2)
    if t == 1 :
        t2 = -200
        t1 = random.randint(-100,20)
        while(t2 <= t1) :
            t2 = random.randint(10,100)
        q = "A refrigerator is to maintain eatables kept inside at " + str(t1) + " degree C, if room temperature is " + str(t2) + " degree C. Calculate the coefficient of performance.\n"
        a = str(cal1(t1,t2)) + "\n"
    else :
        t2 = -200
        t1 = random.randint(-172,293)
        while(t2 <= t1) :
            t2 = random.randint(283,373)
        q = "A refrigerator is to maintain eatables kept inside at " + str(t1) + " K, if room temperature is " + str(t2) + " K. Calculate the coefficient of performance.\n"
        a = str(cal2(t1,t2)) + "\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
