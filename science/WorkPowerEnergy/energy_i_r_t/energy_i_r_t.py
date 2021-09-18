import random
import math

# An Electric Iron of resistance R ohm takes a current of I A, then what is the heat developed in t s?
# An Electric Iron of resistance R ohm takes a current of I A, if the heat developed is energy J, then what is the time taken?
# In an Electric Iron of resistance R ohm, if energy J of heat is developed in t s, then what is the current flowing through it?
# An Electric Iron takes a current of I A, if enrgy J of heat is developed in t s, then what is the value of its resistance?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 30

def type1():
    R = random.randint(1,100)
    I = random.randint(1,10)
    t = random.randint(1,1000)
    energy = str(round(I*I*R*t)) + " joule\n"
    q = "An Electric Iron of resistance "+str(R)+" ohm takes a current of "+str(I)+" A, then what is the heat developed in "+str(t)+" s?\n"
    return q,energy

def type2():
    R = random.randint(1,100)
    I = random.randint(1,10)
    energy = random.randint(1000,2000)
    t = str(round((energy/(I*I*R)),1)) + " s\n"
    q = "An Electric Iron of resistance "+str(R)+" ohm takes a current of "+str(I)+" A, if the heat developed is "+str(energy)+" J, then what is the time taken?\n"
    return q,t

def type3():
    I = random.randint(1,10)
    t = random.randint(1,100)
    energy = random.randint(1000,2000)
    R = str(round(energy/(I*I*t),1)) + " ohm\n"
    q = "An Electric Iron takes a current of "+str(I)+" A, if "+str(energy)+" J of heat is developed in "+str(t)+" s, then what is the value of its resistance?\n"
    return q,R

def type4():
    R = random.randint(1,100)
    t = random.randint(1,10)
    energy = random.randint(100,1100)
    I = str(round(math.sqrt(energy/(R*t)),1)) + " ampere\n"
    q = "In an Electric Iron of resistance "+str(R)+" ohm, if "+str(energy)+" J of heat is developed in "+str(t)+" s, then what is the current flowing through it?\n"
    return q,I

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
