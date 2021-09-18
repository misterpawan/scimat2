import random
import math

# A bike starting with a initial velocity of u m/s travels on a straight road at a constant rate of a m/s2 for t s. How far does the bike travel during this time?
# A bike travels a distance of s m on a straight road at a constant rate of a m/s2 for t s. What is the initial velocity of the bike ?
# A bike starting with a initial velocity of u m/s travels a distane of s m on a straight road for t s. What is the acceleration of the bike ?
# A bike starting with a initial velocity of u m/s travels on a straight road at a constant rate of a m/s2. What is the time taken to travel a distance of s m ? 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_s(u, a, t) :
    return round((u * t) + (0.5*a*t*t), 1)

def calculation_u(s, a, t) :
    return round((s - (0.5*a*t*t))/ t, 1)

def calculation_a(s, u, t) :
    return round((2*(s - u*t))/(t*t), 1)
  
def calculation_t(s, u, a) :
    #at2+2ut-2s = 0
    temp = (4*u*u)+(8*a*s)
    return round((-(2*u) + math.sqrt(temp))/(2*a),1)
    
def type1():
    u = random.randint(1,1000)
    a = random.randint(1,100)
    t = random.randint(1,10)
    s = str(calculation_s(u, a, t)) + " m\n"
    q = "A bike starting with a initial velocity of " + str(u) + " m/s travels on a straight road at a constant rate of " + str(a) + " m/s2 for " + str(t) + " s. How far does the bike travel during this time ?\n"
    return q,s

def type2():
    a = random.randint(1,100)
    t = random.randint(1,10)
    tp = int(0.5*a*t*t)
    s = random.randint(tp,tp+1000)
    u = str(calculation_u(s, a, t)) + " m/s\n"
    q = "A bike travels a distance of " + str(s) + " m on a straight road at a constant rate of " + str(a) + " m/s2 for " + str(t) + " s. What is the initial velocity of the bike ?\n"
    return q,u

def type3():
    u = random.randint(1,100)
    t = random.randint(1,10)
    tp = u*t
    s = random.randint(tp+10,tp+1010)
    a = str(calculation_a(s, u, t)) + " m/s2\n"
    q = "A bike starting with a initial velocity of " + str(u) + " m/s travels a distane of " + str(s) + " m on a straight road for " + str(t) + " s. What is the acceleration of the bike ?\n"
    return q,a

def type4():
    u = random.randint(1,100)
    a = random.randint(1,10)
    s = random.randint(1,1000)
    t = str(calculation_t(s, u, a)) + " s\n"
    q = "A bike starting with a initial velocity of " + str(u) + " m/s travels on a straight road at a constant rate of " + str(a) + " m/s2. What is the time taken to travel a distance of " + str(s) + " m ?\n" 
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)
    #print(ques)
    #print(answer)

qns.close()
ans.close()