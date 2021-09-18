import random
import math

#A body is dropped from a height of h m with an initial velocity of u m/s. With what velocity will it strike the ground ?
#A body is dropped from a height of h m reaches the ground with a velocity v m/s. With what initial velocity it was dropped ?
#A body is dropped with a initial velocity of u m/s reaches the ground with a velocity v m/s. From what height it was dropped ? 


qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1500000
g = 9.8

def calculation_h(u,v):
  return round(((v**2 - u**2)/(2*g)),1)

def calculation_u(v,h) :
    return round(math.sqrt((v**2) - (2*g*h)), 1)

def calculation_v(u,h) :
    return round(math.sqrt((u**2) + (2*g*h)), 1)
    
def type1():
    u = random.randint(1,1000)
    v = random.randint(u,u+1000)
    h = str(calculation_h(u,v)) + " m\n"
    q = "A body is dropped with a initial velocity of " + str(u) + " m/s reaches the ground with a velocity " + str(v) + " m/s. From what height it was dropped ?\n"
    return q,h

def type2():
    h = random.randint(1,10000)
    tmp = 2*g*h
    v = random.randint(int(tmp),int(tmp)+100)
    u = str(calculation_u(v,h)) + " m/s\n"
    q = "A body is dropped from a height of " +str(h) + " m reaches the ground with a velocity " + str(v) + " m/s. With what initial velocity it was dropped ?\n"
    return q,u

def type3():
    h = random.randint(1,10000)
    u = random.randint(0,100)
    v = str(calculation_v(u,h)) + " m/s\n"
    q = "A body is dropped from a height of " + str(h) + " m with an initial velocity of " + str(u) + " m/s. With what velocity will it strike the ground ?\n"
    return q,v

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