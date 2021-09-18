import random
import math

#A body is dropped from the top of a building with an initial velocity of u m/s under gravity,and it reaches the ground after t s.What is the height of the building ?
#A body is dropped from the top of a building of height h m with an initial velocity of u m/s under gravity. After what time it reaches the ground ?
#A body is dropped from the top of a building of height h m reaches the ground after t s under gravity. With what inintial velocity it is dropped ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_s(u, a, t) :
    return round((u * t) + (0.5*a*t*t), 1)

def calculation_u(s, a, t) :
    return round((s - (0.5*a*t*t))/ t, 1)
  
def calculation_t(s, u, a) :
    #at2+2ut-2s = 0
    temp = (4*u*u)+(8*a*s)
    return round((-(2*u) + math.sqrt(temp))/(2*a),1)
    
def type1():
    a = 9.8
    u = random.randint(1,5000)
    t = random.randint(1,200)
    s = str(calculation_s(u, a, t)) + " m\n"
    q = "A body is dropped from the top of a building with an initial velocity of " + str(u) + " m/s under gravity,and it reaches the ground after " + str(t) + " s.What is the height of the building ?\n"
    return q,s

def type2():
    a = 9.8
    t = random.randint(1,200)
    tp = int(0.5*a*t*t)
    s = random.randint(tp,tp+5000)
    u = str(calculation_u(s, a, t)) + " m/s\n"
    q = "A body is dropped from the top of a building of height " + str(s) + " m reaches the ground after " + str(t) + " s under gravity. With what inintial velocity it is dropped ?\n"
    return q,u

def type3():
    a = 9.8 
    u = random.randint(1,200)
    s = random.randint(u,u+5000)
    t = str(calculation_t(s, u, a)) + " s\n"
    q = "A body is dropped from the top of a building of height " + str(s) + " m with an initial velocity of " + str(u) + " m/s under gravity. After what time it reaches the ground ?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    #print(ques)
    #print(answer)

qns.close()
ans.close()