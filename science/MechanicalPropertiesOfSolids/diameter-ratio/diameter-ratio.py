import random
import math

# A rigid bar of mass 15 kg is supported symmetrically by three wires each 2.0 m long. Those at each end are of material-1 and the middle one is of material-2. Determine the ratios of their diameters if each is to have the same tension.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(1,20)
    l = random.randint(1,20)
    Y1 = random.randint(1,200)
    Y2 = random.randint(1,200)
    q = "A rigid bar of mass "+str(m)+" kg is supported symmetrically by three wires each "+str(l)+" m long. Those at each end are of material-1 and the middle one is of material-2. Find ratios of their diameters all have same tension (young's modulus of material-1 is "+str(Y1)+" x 10^9 Nm-2, material-2 is "+str(Y2)+" x 10^9 Nm-2).\n"
    a = "sqrt("+str(Y2)+"/"+str(Y1)+")\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()