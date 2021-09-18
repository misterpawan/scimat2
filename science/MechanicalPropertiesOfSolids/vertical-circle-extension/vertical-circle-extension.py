import random
import math

# A 14.5 kg mass, fastened to the end of a steel wire of unstretched length 1 m, is whirled in a vertical circle with an angular velocity of 2 rev/s at the bottom of the circle. The cross-sectional area of the wire is 0.065 cm2. Calculate the elongation of the wire when the mass is at the lowest point of its path. Y_steel = 2 x 10^11 Nm-2.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(20,200)
    l = random.randint(10,40)
    ang_v = random.randint(1,10)
    A = random.randint(1,100)
    q = "A "+str(m)+" kg mass, fastened to the end of a steel wire of initial length "+str(l)+" m, is whirled in a vertical circle with an angular velocity of "+str(ang_v)+" rev/s at the bottom of the circle. The cross-sectional area of the wire is "+str(A)+" mm2. Calculate the elongation of the wire when the mass is at the lowest point of its path.\n"
    F = m*(9.8+l*math.pi*math.pi*ang_v*ang_v)
    e = (F*l)/((A*(10**(-6)))*(2*(10**11)))
    a = str(round(e*100,1))+" cm\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()