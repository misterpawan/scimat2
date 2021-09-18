import random

# I A of current flows through a circuit with battery of potential difference V V, then calculate the rate of heat generated?
# I A of current flows through a circuit, if the rate of heat generated is P W, Calculate the potential difference of battery?
# In a circuit with battery of potential difference V V, if the rate of heat generated is P W, Calculate the current in the circuit?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

def calculation_P(V, I): 
    return V * I

def calculation_I(P, V):
    return round(P / V, 1)

def calculation_V(P, I):
    return round(P / I, 1)

def type1():
    V = random.randint(1,1000)
    I = random.randint(1,1000)
    P = str(calculation_P(V,I)) + " watt\n"
    q = str(I)+" A of current flows through a circuit with battery of potential difference "+str(V)+" V, then calculate the rate of heat generated?\n"
    return q,P

def type2():
    P = random.randint(100,1100)
    I = random.randint(1,1000)
    V = str(calculation_V(P,I)) + " volt\n"
    q = str(I)+" A of current flows through a circuit, if the rate of heat generated is "+str(P)+" W, Calculate the potential difference of battery?\n"
    return q,V

def type3():
    P = random.randint(100,1100)
    V = random.randint(1,1000)
    I = str(calculation_I(P,V)) + " ampere\n"
    q = "In a circuit with battery of potential difference "+str(V)+" V, if the rate of heat generated is "+str(P)+" W, Calculate the current in the circuit?\n"
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
