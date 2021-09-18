
import math
import random

# An electron and a proton are detected in a cosmic ray experiment, the first with kinetic energy v1 eV, and the second with v2 eV. Which is faster, the electron or the proton? Obtain the ratio of their speeds.
# An electron and a proton are detected in a cosmic ray experiment, the first with kinetic energy v1 eV, and the second with v2 eV. Which is faster, the electron or the proton? Obtain the ratio of their speeds. (electron mass = 9.11 x 10-31 kg, proton mass = 1.67 x 10-27 kg, 1 eV= 1.60 x 1019J).

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
me = 9.11 * 10**-31
mp = 1.67 * 10**-27

for i in range(no_of_samples):
   v1 = random.randint(1,10000)
   v2 = random.randint(1,10000)
   types = random.randint(1,2)
   if types == 1 :
      ques = "An electron and a proton are detected in a cosmic ray experiment, the first with kinetic energy " + str(v1) + " eV, and the second with " + str(v2) + " eV. Which is faster, the electron or the proton? Obtain the ratio of their speeds.\n"
   else :
      ques = "An electron and a proton are detected in a cosmic ray experiment, the first with kinetic energy " + str(v1) + " eV, and the second with " + str(v2) + " eV. Which is faster, the electron or the proton? Obtain the ratio of their speeds.(electron mass = 9.11 x 10-31 kg, proton mass = 1.67 x 10-27 kg, 1 eV= 1.60 x 1019J)\n"
   t1 = me * v2
   t2 = mp * v1
   if t1 > t2 :
      answ = round(t1/t2)
      answ = round(math.sqrt(answ),2)
      answer = "elctron is faster by " + str(answ) + " times \n"
   else :
      answ = round(t2/t1)
      answ = round(math.sqrt(answ),2)
      answer = "proton is faster by " + str(answ) + " times \n"
   qns.write(ques)
   ans.write(answer)

qns.close()
ans.close()
