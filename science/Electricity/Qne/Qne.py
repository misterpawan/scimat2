import random

# Calculate the number of electrons constituting Q C of charge
# Calculate the charge of n electrons

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20
charge_of_electron = (1.6)*(1e-19)

def calculation_n(Q): 
    return round(Q/charge_of_electron)

def calculation_Q(n):
    return round(n*charge_of_electron, 1)

def type1():
    Q = random.randint(1,1000000) * charge_of_electron
    n1 = str(Q)
    n2 = n1[:7]+n1[-4:]
    n = str(calculation_n(Q)) +" \n"
    q = "Calculate the number of electrons constituting "+str(n2)+" C of charge?\n"
    return q,n

def type2():
    n = random.randint(1*(1e18),1*(1e19))
    n1 = str(n)
    n2 = n1[0] + "." + n1[1:6] + "e" + str(len(n1)-1)
    Q = str(calculation_Q(n)) + " coulomb\n"
    q = "Calculate the charge (in C) of "+n2+" electrons?\n"
    return q,Q

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
