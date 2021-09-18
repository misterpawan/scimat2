import random

# Estimate the total number of air molecules (inclusive of oxygen, nitrogen, water vapour and other constituents) in a room of capacity v m3 at a temperature of t degree C and p atm pressure.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

k = 1.38 * (10**-23)

def cal1(v,p,t1) :
    p = p * (10**5)
    t1 = t1 + 273   
    return (p*v)/(k*t1) 

def type1() :
    v = random.randint(10,110)
    t1 = random.randint(1,100)
    p = random.randint(1,100)
    t = random.randint(1,2)
    if t == 1 :
        q = "Estimate the total number of air molecules (inclusive of oxygen, nitrogen, water vapour and other constituents) in a room of capacity " + str(v) + " m3 at a temperature of " + str(t1) + " degree C and " + str(p) + " atm pressure. (k = 1.38 x 10^-23) \n"
    else :
        q = "Estimate the total number of air molecules (inclusive of oxygen, nitrogen, water vapour and other constituents) in a room of capacity " + str(v) + " m3 at a temperature of " + str(t1) + " degree C and " + str(p) + " atm pressure.\n"
    a = "{:.2e}".format(cal1(v,p,t1)) + "\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
