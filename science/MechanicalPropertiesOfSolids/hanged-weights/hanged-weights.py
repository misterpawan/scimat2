import random
import math

# A body of mass m1 kg is hanged from the roof with the help of steel wire of length l1, another body of mass m2 kg is hanged from the bottom of mass m1 with the help of bronze wire of length l2, if the cross-sectional area of both wires is A then what is the elongation of 
# (a) steel wire (Young’s modulus of steel is 2.0 x 10^11 Pa).
# (b) brass wire (Young’s modulus of brass is 0.9 x 10^11 Pa).

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    m1 = random.randint(1,20)
    m2 = random.randint(1,20)
    l1 = random.randint(1,20)
    l2 = random.randint(1,20)
    d = random.randint(1,200)
    A = math.pi * d *d * 10**(-8)
    q = "A body of mass "+str(m1)+" kg is hanged from the roof with the help of steel wire of length "+str(l1)+" m, another body of mass m2 kg is hanged from the bottom of mass m1 with the help of bronze wire of length "+str(l2)+" m, if the radius of both wires is "+str(d)+" x 10^(-4) m then what is the elongation of "
    types = random.randint(1,2)
    if types == 1:
        q = q + "steel wire (Young’s modulus of steel is 2.0 x 10^11 Pa).\n"
        F = (m1+m2)*9.8
        e = (F*l1)/(A*(2*(10**11)))
    elif types == 2:
        q = q + "brass wire (Young’s modulus of brass is 0.9 x 10^11 Pa).\n"
        F = m2*9.8
        e = (F*l2)/(A*(0.9*(10**11)))
    a = str(round(e*1000000,1)) + " x 10^(-6) m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()