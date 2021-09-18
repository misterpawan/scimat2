import random
import math

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        m = random.randint(1,30)*10
        q1 = random.randint(1,20)
        v = random.randint(1,20)
        L = random.randint(1,30)
        E = random.randint(1,20)
        q = "A particle of mass "+str(m)+" g and charge -("+str(q1)+") C enters a region between two charged particles initially moving along x-axis with speed "+str(v)+" m/s, the length of plates is "+str(L)+" cm and a uniform electric field of "+str(E)+" N/C, then find vertical deflection?\n"
        num = q1*E*L*L*(0.0001)
        den = m*v*v*(0.001)
        a = "{:.2e}".format(num/den)+" m\n"
    else:
        v = random.randint(1,2000)*1000
        d = round(random.randint(1,10)/10,2)
        E = random.randint(10,400)*10
        q = "An electron is projected between parallel plates separated by "+str(d)+" cm, having field of "+str(E)+" N/C(up to down), with a speed of "+str(v)+" ms-1, in what time will the electron strike upper plate?\n"
        num = 2*d*0.01*9.1*(10**(-31))*v*v
        den = 1.6*(10**(-19))*E
        a = "{:.2e}".format(math.sqrt(num/den)) + " m\n"
    qns.write(q)
    ans.write(a)
qns.close()
ans.close()
