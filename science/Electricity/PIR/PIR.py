import random
import math

# An Electric heater of resistance R ohm draws I A current from the service mains in t s. Calculate the rate at which heat is developed in the heater?
# An Electric heater of resistance R ohm produces heat at P W for t s. Calculate the current drawn from the service mains?
# An Electric heater draws I A current from the service mains produces heat at P W for t s. Calculate the resistance of the heater?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 30

def calculation_P(I, R): 
    return I*I*R

def calculation_I(P, R):
    return round(math.sqrt(P/R), 1)

def calculation_R(P, I):
    return round(P/(I*I), 1)

def type1():
    R = random.randint(1,100)
    I = random.randint(1,10)
    t = random.randint(1,10000)
    P = str(calculation_P(I,R)) + " watt\n"
    q = "An Electric heater of resistance "+str(R)+" ohm draws "+str(I)+" A current from the service mains in "+str(t)+" s. Calculate the rate at which heat is developed in the heater?\n"
    return q,P

def type2():
    P = random.randint(50,149)
    R = random.randint(1,100)
    t = random.randint(1,2000)
    I = str(calculation_I(P,R)) + " ampere\n"
    q = "An Electric heater of resistance "+str(R)+" ohm produces heat at "+str(P)+" W for "+str(t)+" s. Calculate the current drawn from the service mains?\n"
    return q,I

def type3():
    P = random.randint(10,1010)
    I = random.randint(1,10)
    t = random.randint(1,1000)
    R = str(calculation_R(P,I)) + " ohm\n"
    q = "An Electric heater draws "+str(I)+" A current from the service mains produces heat at "+str(P)+" W for "+str(t)+" s. Calculate the resistance of the heater?\n"
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
