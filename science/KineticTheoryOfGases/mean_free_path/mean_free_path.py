import random
import math

# Estimate the mean free path of a gas molecule in a cylinder containing gas at p atm and temperature t1 °C. Take the radius of a gas molecule to be roughly r A. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

R = 8.31
n = 6.023 * (10**23)

def cal1(p,t1,r) :
    p = p * (10**5)
    t1 = t1 + 273  
    r = r * (10**-10) 
    nu = (n*p)/(R*t1)
    return (1/((math.sqrt(2))*(math.pi)*(nu)*(4*r*r)))

def type1() :
    t1 = random.randint(1,100)
    p = random.randint(1,100)
    r = random.randint(1,100)
    t = random.randint(1,2)
    if t == 1 :
        q = "Estimate the mean free path of a gas molecule in a cylinder containing gas at " + str(p) + " atm and temperature " + str(t1) + " degree C. Take the radius of a gas molecule to be roughly " + str(r) + " A. (r = 8.31 amd Patm = 10^5 Pa) \n"
    else :
        q = "Estimate the mean free path of a gas molecule in a cylinder containing gas at " + str(p) + " atm and temperature " + str(t1) + " degree C. Take the radius of a gas molecule to be roughly " + str(r) + " A.\n"
    a = "{:.1e}".format(cal1(p,t1,r)) + "\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
