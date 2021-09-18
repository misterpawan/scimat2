import random

# what distance will a car travelling with a constant velocity v m/s for time t s will travel?
# A Car travelling with constant velocity has travelled a distance of s m in t s, then what is the velocity of the car?
# How much time will a car travelling with a constant velocity of v m/s take to travel a distance of s m?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_s(v, t): 
    return round(v * t, 1)

def calculation_v(s, t):
    return round(s / t, 1)

def calculation_t(s, v):
    return round(s / v, 1)

def type1():
    v = random.randint(1,1000)
    t = random.randint(1,1000)
    s = str(calculation_s(v,t)) + " m\n"
    q = "What distance will a car travelling with a constant velocity of " + str(v) + " m/s for time " + str(t) + " s will travel?\n"
    return q,s

def type2():
    s = random.randint(8000,10000)
    t = random.randint(1,1000)
    v = str(calculation_v(s,t)) + " m/s\n"
    q = "A Car travelling with constant velocity has travelled a distance of " + str(s) + " m in " + str(t) + " s, then what is the velocity of the car?\n"
    return q,v

def type3():
    s = random.randint(8000,10000)
    v = random.randint(1,1000)
    t = str(calculation_t(s,v)) + " s\n"
    q = "How much time will a car travelling with a constant velocity of " + str(v) + " m/s take to travel a distance of " + str(s) + "m?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
