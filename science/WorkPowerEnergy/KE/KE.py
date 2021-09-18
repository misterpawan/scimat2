import random
import math

# What is the kinetic energy of an object of mass m kg moving with a velocity of v m/s ?
# What is the mass of an object with kinetic energy KE J moving with a velocity of v m/s ?
# What is the velocity of an object of mass m kg having kinetic energy KE J ?
# KE = 1/2*m*v*v

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 8

def calculation_KE(m, v): 
    return round(1/2 * m * v * v , 1)

def calculation_m(KE, v):
    return round((2*KE) / (v * v), 1)

def calculation_v(KE, m):
    return round(math.sqrt((2*KE) / m) , 1)

def type1():
    m = random.randint(1,1000)
    v = random.randint(1,1000)
    KE = str(calculation_KE(m,v)) + " joule\n"
    q = "What is the kinetic energy of an object of mass " + str(m) + " kg moving with a velocity of " + str(v) + " m/s ?\n"
    return q,KE

def type2():
    KE = random.randint(499000,500000)
    v = random.randint(1,1000)
    m = str(calculation_m(KE,v)) + " kg\n"
    q = "What is the mass of a object with kinetic energy of " + str(KE) + " J moving with a velocity of " + str(v) + " m/s ?\n"
    return q,m

def type3():
    KE = random.randint(498000,500000)
    m = random.randint(1,1000)
    v = str(calculation_v(KE,m)) + " m/s\n"
    q = "What is the velocity of an object of mass " + str(m) + " kg having kinetic energy " + str(KE) + " J ?\n"
    return q,v

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2 or types == 3:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
