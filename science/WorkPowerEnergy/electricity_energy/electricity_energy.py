import random

# An Electric motor takes 5 A from a 220 V line. Determine the energy consumed by it in 2h ?
# An Electric motor takes 5 A from a 220 V line. Determine the time taken by it, if it consumes 1000 J of energy ?
# An Electric motor takes current from a 220 V line, if it consumes 1000 J of energy in 2h, then determine current drawn ?
# An Electric motor takes 5 A current, if it consumes 1000 J of energy in 2h, then determine potential difference ?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

def type1():
    I = random.randint(1,10)
    V = random.randint(1,100)
    t = random.randint(1,1000)
    energy = str(round(V*I*t)) + " joule\n"
    q = "An Electric motor takes "+str(I)+" A from a "+str(V)+" V line. Determine the energy consumed by it in "+str(t) +" s ?\n"
    return q,energy

def type2():
    I = random.randint(1,10)
    V = random.randint(220,240)
    energy = random.randint(1000,6000)
    t = str(round((energy/(I*V)),1)) + " s\n"
    q = "An Electric motor takes "+str(I)+" A from a "+str(V)+" V line. Determine the time taken by it, if it consumes "+str(energy)+" J of energy ?\n"
    return q,t

def type3():
    V = random.randint(220,240)
    t = random.randint(1,10)
    energy = random.randint(1000,6000)
    I = str(round((energy/(V*t)),1)) + " ampere\n"
    q = "An Electric motor takes current from a "+str(V)+" V line, if it consumes "+str(energy)+" J of energy in "+str(t)+" s, then determine current drawn ?\n"
    return q,I

def type4():
    I = random.randint(1,10)
    t = random.randint(1,100)
    energy = random.randint(100,1100)
    V = str(round((energy/(I*t)),1)) + " volt\n"
    q = "An Electric motor takes "+str(I)+" A current, if it consumes "+str(energy)+" J of energy in "+str(t)+" s, then determine potential difference ?\n"
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
