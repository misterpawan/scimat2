import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    q1 = random.randint(1,200)
    q2 = random.randint(1,200)
    d = random.randint(1,200)
    if random.randint(0,1):
            q1 = -q1
    if random.randint(0,1):
            q2 = -q2
    q = "Two point charges q1 = "+str(q1)+" x 10^(-6)C and q2 = "+str(q2)+" x 10^(-6)C are located "+str(d)+" cm apart in vaccum. "
    types = random.randint(1,5)
    E = (q1-q2)*(10**(-6))*(9*(10**9))*(4/(d*d*0.0001))
    if types < 3:
        q = q + "What is the electric field at the midpoint O of the line joining two charges?\n"
        a = "{:.2e}".format(abs(E)) + " newton/coulumb\n"
    else:
        qmid = random.randint(-10,10)
        while qmid == 0:
            qmid = random.randint(-10,10)
        q = q + "What is the force on the test charge of "+str(qmid)+" x 10^(-6)C placed at midpoint of line joining two charges\n"
        a = "{:.2e}".format(abs(E*qmid*(10**(-6))))+" newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
    
qns.close()
ans.close()
