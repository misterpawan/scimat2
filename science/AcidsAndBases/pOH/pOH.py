import random
import math

# Calculate the pOH of 0.1M of NaOH base.
# Calculate the pOH of 0.1M of NaOH base and thus calculate its pH.
# Calculate the pOH of 0.1N of NaOH base.
# Calculate the pOH of 0.1N of NaOH base and thus calculate its pH.

bases = ['NaOH', 'KOH', 'Ca(OH)2', 'Sr(OH)2', 'Ba(OH)2', 'LiOH', 'RbOH', 'CsOH']
acidity = [1, 1, 2, 2, 2, 1, 1, 1]

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation(conc) :
    res = -1*math.log10(conc)
    return round(res,3)

def type1() :
    m = random.randint(1,10000000)
    m = round(m/10000000,7)
    temp = random.randint(0,7)
    base = bases[temp]
    q = "Calculate the pOH of " + str(m) + " M of " + str(base) + " base.\n"
    pOH = str(calculation(m)) + "\n"
    return q, pOH

def type2() :
    m = random.randint(1,10000000)
    m = round(m/10000000,7)
    temp = random.randint(0,7)
    base = bases[temp]
    q = "Calculate the pOH of " + str(m) + " M of " + str(base) + " base and thus calculate its pH.\n"
    pOH = calculation(m)
    pH = 14.000 - pOH
    res = str(pOH) + " and " + str(pH) + "\n"
    return q, res

def type3() :
    n = random.randint(1,10000000)
    n = round(n/10000000,7)
    temp = random.randint(0,7)
    n = round(n/acidity[temp],7)
    base = bases[temp]
    q = "Calculate the pOH of " + str(n) + " N of " + str(base) + " base.\n"
    pOH = str(calculation(n)) + "\n"
    return q, pOH

def type4() :
    n = random.randint(1,10000000)
    n = round(n/10000000,7)
    temp = random.randint(0,7)
    n = round(n/acidity[temp],7)
    base = bases[temp]
    q = "Calculate the pOH of " + str(n) + " N of " + str(base) + " base and thus calculate its pH.\n"
    pOH = calculation(n)
    pH = 14.000 - pOH
    res = str(pOH) + " and " + str(pH) + "\n"
    return q, res

for i in range(no_of_samples) :
    types = random.randint(1,4)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    elif types == 4:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()