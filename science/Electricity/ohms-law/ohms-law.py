import random

# If a V V battery is connected across an unknown resistor, there is I mA in the circuit, find the value of resistance of the resistor?
# If a V V battery is connected across a resistance of R ohm, then find the current in the circuit?
# If a resistance of R ohm is connected across a battery of unknown voltage, there is I mA in the circuit, find the value of potential difference across ends of battery ?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

def type1():
    I = random.randint(1,1000)
    V = random.randint(100,1100)
    R = str(round(V/I,1)) + " ohm\n"
    q = "If a "+str(V)+" V battery is connected across an unknown resistor, there is "+str(I)+" A in the circuit, find the value of resistance of the resistor ? \n"
    return q,R

def type2():
    I = random.randint(1,1000)
    R = random.randint(1,1000)
    V = str(I*R) + " volt\n"
    q = "If a resistance of "+str(R)+" ohm is connected across a battery of unknown voltage, there is "+str(I)+" A in the circuit, find the voltage of battery ?\n"
    return q,V

def type3():
    V = random.randint(100,1100)
    R = random.randint(1,1000)
    I = str(round(V/R,1)) + " ampere\n"
    q = "If a "+str(V)+" V battery is connected across a resistance of "+str(R)+" ohm, then find the current in the circuit ?\n"
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
