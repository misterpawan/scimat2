import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 500000
# no_of_samples = 20

for i in range(no_of_samples):
    q1 = random.randint(1,50)
    q2 = random.randint(1,50)
    if random.randint(0,1):
            q1 = -q1
            q2 = -q2
    d = random.randint(1,50)
    r1 = random.randint(2,5)
    r2 = random.randint(2,5)
    d2 = random.randint(2,5)
    q = "Two copper spheres A, B are separated by a distance "+str(d)+" cm. The force of repulsion if the charge on A is "+str(q1)+" x 10^(-6)C, B is "+str(q2)+" x 10^(-6)C is F1. The Force of repulsion if charge on A becomes "+str(r1)+" times, charge on B becomes "+str(r2)+" times, distance between them becomes "+str(d2)+" times is F2. Find F1/F2?\n"
    a = str(d2**2)+"/"+str(r1*r2)+"\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
    
qns.close()
ans.close()
