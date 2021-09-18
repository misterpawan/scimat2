import random
import math

# A circuit consists of V V battery, R ohm resistance, then what is the heat energy produced in the circuit in t s?
# A circuit consists of V V battery, R ohm resistance, then what is the time taken for produce energy J of energy in the circuit?
# A circuit consists of V V battery, unknown resistance ,if energy J of energy is produced in t s, then what is the value of resistance?
# A circuit consists of R ohm resistance, battery of unknown voltage, if energy J of energy  is produced in t s, then what is the value of voltage?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 30

def type1():
    R = random.randint(1,100)
    V = random.randint(1,10)
    t = random.randint(10,1010)
    energy = str(round((V*V*t)/R,1)) + " joule\n"
    q = "A circuit consists of "+str(V)+" V battery, "+str(R)+" ohm resistance, then what is the heat energy produced in the circuit in "+str(t)+" s?\n"
    return q,energy

def type2():
    R = random.randint(100,200)
    V = random.randint(10,19)
    energy = random.randint(1,1000)
    t = str(round(((energy*R)/(V*V)),1)) + " s\n"
    q = "A circuit consists of "+str(V)+" V battery, "+str(R)+" ohm resistance, then what is the time taken for produce "+str(energy)+" J of energy in the circuit?\n"
    return q,t

def type3():
    V = random.randint(1,10)
    t = random.randint(100,200)
    energy = random.randint(1,1000)
    R = str(round(((V*V*t)/energy),1)) + " ohm\n"
    q = "A circuit consists of "+str(V)+" V battery, unknown resistance ,if "+str(energy)+" J of energy is produced in "+str(t)+" s, then what is the value of resistance?\n"
    return q,R

def type4():
    R = random.randint(1,10)
    t = random.randint(1,100)
    energy = random.randint(10,1010)
    V = str(round(math.sqrt((energy*R)/t),1)) + " volt\n"
    q = "A circuit consists of "+str(R)+" ohm resistance, battery of unknown voltage, if "+str(energy)+" J of energy  is produced in "+str(t)+" s, then what is the value of voltage?\n"
    return q,V

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    if types == 3:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
