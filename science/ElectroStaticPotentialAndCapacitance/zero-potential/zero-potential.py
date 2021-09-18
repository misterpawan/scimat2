import random

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    q1 = random.randint(1,200)
    q2 = random.randint(1,200)
    d = random.randint(1,200)
    if random.randint(0,1):
        q1 = -q1
    else:
        q2 = -q2
    q = "Two charges q1 of "+str(q1)+" x 10^(-8)C and q2 of "+str(q2)+" x 10^(-8) are located "+str(d)+" cm apart. At what point(s) on the line joining the two charges is the electric potential zero(take potential at infinity as zero)?\n"
    r1 = abs((q1*d)/(q1-q2))
    absq1 = abs(q1)
    absq2 = abs(q2)
    if absq1!=absq2:
        r2 = abs((q1*d)/(q1+q2))
    
    a = "{:.2e}".format(r1) + " cm from q1 between q1 and q2"
    if absq1 == absq2:
        a += "\n"
    elif absq1 > absq2:
        a += ", {:.2e}".format(r2)+" cm from q1 to right of both charges\n"
    else:
        a += ", {:.2e}".format(r2)+" cm from q1 to left of both charges\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()