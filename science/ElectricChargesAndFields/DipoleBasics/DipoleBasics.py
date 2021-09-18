import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    q1 = random.randint(1,200)
    d1 = random.randint(1,200)
    d2 = random.randint(-200,-1)
    q = "Two point charges q1 = "+str(q1)+" x 10^(-6)C and q2 = - "+str(q1)+" x 10^(-6)C are located at the points A:(0, 0, - "+str(d1)+" cm) and B:(0, 0, "+str(d2)+" cm), respectively. What are the total charge and electric dipole movement of the system?\n"
    d = d1+abs(d2)
    p = q1*d*(10**(-8))
    a = "total charge is 0 coulomb, dipole is "+"{:.2e}".format(p) + " coulumb-m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
