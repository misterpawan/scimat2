import random
import math

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    dipole = random.randint(1,200)
    E = random.randint(1,200)
    theta = random.randint(0,179)
    q = "An Electric dipole with dipole moment "+str(dipole)+" x 10^(-9) C-m is aligned at "+str(theta)+" degrees with the direction of a uniform electric field of magnitude "+str(E)+" x 10^4 N C-1. Calculate the magnitude of torque acting on the dipole?\n"
    a = "{:.1e}".format(dipole*E*math.sin(theta*(math.pi/180))*(10**(-5))) + " newton-m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
