import random
import math

# An Electric bulb of resistance R ohm draws current from the service mains of potential difference V V in t s. Calculate the rate at which heat is developed in the bulb?
# An Electric bulb of resistance R ohm produces heat at P W for t s. Calculate the potential difference maintained at service mains?
# An Electric bulb draws current from the service mains of potential difference V V produces heat at P W for t s. Calculate the resistance of the bulb?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 30

def calculation_P(V, R): 
    return round((V*V)/R,1)

def calculation_V(P, R):
    return round(math.sqrt(P*R), 1)

def calculation_R(P, V):
    return round((V*V)/P, 1)

def type1():
    R = random.randint(1,1000)
    V = random.randint(10,19)
    t = random.randint(1,1000)
    P = str(calculation_P(V,R)) + " watt\n"
    q = "An Electric bulb of resistance "+str(R)+" ohm draws current from the service mains of potential difference "+str(V)+" V in "+str(t)+" s. Calculate the rate at which heat is developed in the bulb?\n"
    return q,P

def type2():
    P = random.randint(1,100)
    R = random.randint(1,100)
    t = random.randint(1,2000)
    V = str(calculation_V(P,R)) + " volt\n"
    q = "An Electric bulb of resistance "+str(R)+" ohm produces heat at "+str(P)+" W for "+str(t)+" s. Calculate the potential difference maintained at service mains?\n"
    return q,V

def type3():
    P = random.randint(1,1000)
    V = random.randint(10,110)
    t = random.randint(1,100)
    R = str(calculation_R(P,V)) + " ohm\n"
    q = "An Electric bulb draws current from the service mains of potential difference "+str(V)+" V produces heat at "+str(P)+" W for "+str(t)+" s. Calculate the resistance of the bulb?\n"
    return q,R

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1 or types == 3:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
