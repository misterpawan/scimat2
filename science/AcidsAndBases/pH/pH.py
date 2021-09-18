import random
import math

# Calculate the pH of 0.1M of HCl acid.
# Calculate the pH of 0.1M of HCl acid and thus calculate its pOH.
# Calculate the pH of 0.1N of HCl acid.
# Calculate the pH of 0.1N of HCl acid and thus calculate its pOH.

acids = ['HClO4', 'HCl', 'HBr', 'HI', 'HNO3', 'H2SO4', 'HClO3', 'HIO4']
basisity = [1, 1, 1, 1, 1, 2, 1, 1]

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
    acid = acids[temp]
    q = "Calculate the pH of " + str(m) + " M of " + str(acid) + " acid.\n"
    pH = str(calculation(m)) + "\n"
    return q, pH

def type2() :
    m = random.randint(1,10000000)
    m = round(m/10000000,7)
    temp = random.randint(0,7)
    acid = acids[temp]
    q = "Calculate the pH of " + str(m) + " M of " + str(acid) + " acid and thus calculate its pOH.\n"
    pH = calculation(m)
    pOH = 14.000 - pH
    res = str(pH) + " and " + str(pOH) + "\n"
    return q, res

def type3() :
    n = random.randint(1,10000000)
    n = round(n/10000000,7)
    temp = random.randint(0,7)
    n = round(n/basisity[temp],7)
    acid = acids[temp]
    q = "Calculate the pH of " + str(n) + " N of " + str(acid) + " acid.\n"
    pH = str(calculation(n)) + "\n"
    return q, pH

def type4() :
    n = random.randint(1,10000000)
    n = round(n/10000000,7)
    temp = random.randint(0,7)
    n = round(n/basisity[temp],7)
    acid = acids[temp]
    q = "Calculate the pH of " + str(n) + " N of " + str(acid) + " acid and thus calculate its pOH.\n"
    pH = calculation(n)
    pOH = 14.000 - pH
    res = str(pH) + " and " + str(pOH) + "\n"
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