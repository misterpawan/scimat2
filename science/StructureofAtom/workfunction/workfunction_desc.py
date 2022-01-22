import random
import math

# A photon of energy e1 eV strikes on metal surface ; the work function of the metal being e2 eV. Calculate the kinetic energy of the emission and the velocity of the photoelectron. (Given 1 eV = 1.6020 × 10-19 J).

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000
m = 9.1 * 10**-31
k = 1.6 * 10**-19

def cal1(e1,e2) :
   return e1 - e2

def cal2(ke) :
    return math.sqrt((2 * ke * k)/m)

for i in range(no_of_samples):
    e2 = random.randint(1,1200)
    e1 = random.randint(e2+1,e2+1200)
    ques = "A photon of energy " + str(e1) + " eV strikes on metal surface ; the work function of the metal being " + str(e2) + " eV. Calculate the kinetic energy of the emission and the velocity of the photoelectron. (Given 1 eV = 1.6020 × 10-19 J).\n"
    ke = cal1(e1,e2)
    a = "kinetic energy of ejected photoelectron = energy of photon - workfunction = " + str(e1) + " - " + str(e2) + " = " + str(ke) 
    answer = a + " joules and if m is mass of ejected electron then velocity of ejected photo electron = sq.root((ke x 2)/m) = sq.root((" + str(ke) + " x 2)/" + str(m) + ") = " + "{:.2e}".format(cal2(ke)) + " m/s\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
