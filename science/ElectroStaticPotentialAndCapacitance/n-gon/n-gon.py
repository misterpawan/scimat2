import random

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 500000

for i in range(no_of_samples):
    n = random.randint(3,20)
    q1 = random.randint(1,500)
    d = random.randint(1,500)
    if random.randint(0,1):
        q1 = -q1
    q = "A regular "+str(n)+"-gon with distance between each vertex and centre as "+str(d)+" cm has a charge "+str(q1)+" micro-C at each of its vertices. Calculate the potential at the centre of the n-gon?\n"
    a = "{:.2e}".format(9*(10**9)*n*(q1*(10**(-6)))*(1/(d*0.01)))+" volt\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()