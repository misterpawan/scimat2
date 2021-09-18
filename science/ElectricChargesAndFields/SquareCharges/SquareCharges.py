import random
import math


qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    q1 = random.randint(1,20)
    q2 = random.randint(1,20)
    q3 = random.randint(1,20)
    q4 = random.randint(1,20)
    qc = random.randint(1,20)
    if random.randint(0,1):
            q1 = -q1
    if random.randint(0,1):
            q2 = -q2
    if random.randint(0,1):
            q3 = -q3
    if random.randint(0,1):
            q4 = -q4
    if random.randint(0,1):
            qc = -qc
    d = random.randint(1,20)
    q = "Four point charges q1 = "+str(q1)+" x 10^(-6) C, q2 = "+str(q2)+" x 10^(-6) C, q3 = "+str(q3)+" x 10^(-6) C, q4 = "+str(q4)+" x 10^(-6) C, are located at corners of square ABCD of side "+str(d)+" cm. What is the force on a charge of "+str(qc)+" x 10^(-6)C placed at the centre of the square?\n"
    d1 = d / math.sqrt(2)
    if q1 > q3:
        m1 = q1 - q3
    else:
        m1 = q3 - q1
    if q2 > q4:
        m2 = q2 - q4
    else:
        m2 = q4 - q2
    F = math.sqrt(m1**2+m2**2)*qc*(9*(10**9))*(10**(-12))*(1/(d*d*0.0001))
    a = "{:.2e}".format(F)+" newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
    
qns.close()
ans.close()
