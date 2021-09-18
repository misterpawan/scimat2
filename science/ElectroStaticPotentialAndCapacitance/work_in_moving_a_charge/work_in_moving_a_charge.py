import random

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 30

for i in range(no_of_samples):
    q1 = random.randint(1,20)
    q2 = random.randint(1,20)
    p = random.randint(1,20)
    q = random.randint(1,20)
    r1 = random.randint(1,20)
    r2 = random.randint(1,20)
    types1 = random.randint(1,3)
    types2 = random.randint(1,3)
    types3 = random.randint(1,3)
    P = ""
    Q = ""
    R = ""
    if types1 == 1:
        P = "("+str(p)+" cm, 0, 0)"
    elif types1 == 2:
        P = "(0, "+str(p)+" cm, 0)"
    else:
        P = "(0, 0, "+str(p)+" cm)"
    if types2 == 1:
        Q = "("+str(q)+" cm, 0, 0)"
    elif types2 == 2:
        Q = "(0, "+str(q)+" cm, 0)"
    else:
        Q = "(0, 0, "+str(q)+" cm)"
    if types3 == 1:
        R = "(0, "+str(r1)+" cm, "+str(r2)+" cm)"
    elif types3 == 2:
        R = "("+str(r1)+" cm, 0, "+str(r2)+" cm)"
    else:
        R = "("+str(r1)+" cm, "+str(r2)+" cm, 0)"
    qu = "A charge of "+str(q1)+" mC is located at the origin. Calculate the work done in taking a charge "+str(q2)+ " nC from a point P"+P+" to a point Q"+Q+", via a point R"+R+".\n"
    a = "{:.2e}".format(abs(q1*q2*(0.009)*(1/p-1/q)))+" joule\n"
    qns.write(qu)
    ans.write(a)
    # print(qu)
    # print(a)

qns.close()
ans.close() 