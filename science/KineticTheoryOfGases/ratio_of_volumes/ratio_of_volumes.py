import random
import math

#  Estimate the fraction of molecular volume to the actual volume occupied by a gas at STP. Take the diameter of the gas molecule to be d A.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000

n = 6.023 * (10**23)

def cal1(d) :
    return (4*math.pi*d*d*d*1000*n)/(3*8*22.4) 

def type1() :
    d = random.randint(1,10000)
    d = round(d/10,1)
    t = random.randint(1,2)
    if t == 1 :
        q = "Estimate the fraction of molecular volume to the actual volume occupied by a gas at STP. Take the diameter of the gas molecule to be " + str(d) + " A.\n"
    else :
        q = "Estimate the fraction of molecular volume to the actual volume occupied by a gas at STP. Take the diameter of the gas molecule to be " + str(d) + " A and volume occupied by a gas at STP as 22.4 lit\n"
    a = "{:.1e}".format(cal1(d)) + "\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
