import random

# If Q coulomb of charge flows through any section of a conductor in t s, what is the value of current?
# If current flowing through conductor is I A, then time taken for Q C charge to flow through the conductor?
# If current flowing through conductor is I A, then what is the charge flown through the conductor in t s?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

def calculation_Q(I, t): 
    return I * t

def calculation_I(Q, t):
    return round(Q / t, 1)

def calculation_t(Q, I):
    return round(Q / I, 1)

def type1():
    t = random.randint(1,1000)
    I = random.randint(1,1000)
    Q = str(calculation_Q(I,t)) + " coulomb\n"
    q = "If current flowing through conductor is "+str(I)+" A, then what is the charge flown through the conductor in "+str(t)+" s?\n"
    return q,Q

def type2():
    Q = random.randint(100,1100)
    I = random.randint(1,1000)
    t = str(calculation_t(Q,I)) + " s\n"
    q = "If current flowing through conductor is "+str(I)+" A, then time taken for "+str(Q)+" C charge to flow through the conductor?\n"
    return q,t

def type3():
    Q = random.randint(100,1100)
    t = random.randint(1,1000)
    I = str(calculation_I(Q,t)) + " ampere\n"
    q = "If "+str(Q)+" coulomb of charge flows through any section of a conductor in "+str(t)+" s, what is the value of current?\n"
    return q,I

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
