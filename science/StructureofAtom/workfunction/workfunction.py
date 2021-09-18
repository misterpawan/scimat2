import random

import math

# A photon of energy e1 eV strikes on metal surface ; the work function of the metal being e2 eV. Calculate the kinetic energy of the emission and the velocity of the photoelectron. (Given 1 eV = 1.6020 × 10-19 J).

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
m = 9.1 * 10**-31
k = 1.6 * 10**-19

def cal1(e1,e2) :
   return e2 - e1

def cal2(ke) :
    return math.sqrt((2 * ke * k)/m)

for i in range(no_of_samples):
    e1 = random.randint(1,1200)
    e2 = random.randint(e1+1,e1+1200)
    ques = "A photon of energy " + str(e1) + " eV strikes on metal surface ; the work function of the metal being " + str(e2) + " eV. Calculate the kinetic energy of the emission and the velocity of the photoelectron. (Given 1 eV = 1.6020 × 10-19 J).\n"
    ke = cal1(e1,e2)
    answer = str(ke) + " joules and " + "{:.2e}".format(cal2(ke)) + " m/s\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
