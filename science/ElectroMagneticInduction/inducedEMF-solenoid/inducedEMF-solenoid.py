import random
import math

# A long solenoid with n turns per cm has a small loop of area A cm2 placed inside the solenoid normal to it's axis. if the current carried by the solenoid changes steadily from I1 A to I1+I2 A in t1 s, what is the induced emf in the loop while the current is changing?

ques = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
mu0 = math.pi*4*(10**(-7))

for i in range(no_of_samples):
    n = random.randint(1,30)
    A = random.randint(1,30)
    t = round(random.randint(1,30)/100,2)
    I1 = random.randint(1,30)
    I2 = random.randint(1,10)
    q = "A long solenoid with "+str(n)+" turns per cm has a small loop of area "+str(A)+" cm2 placed inside the solenoid normal to it's axis. if the current carried by the solenoid changes steadily from "+str(I1)+" A to "+str(I1+I2)+" A in "+str(t)+" s, what is the induced emf in the loop while the current is changing?\n"
    a = "{:.2e} volt\n".format((mu0*A*0.01*n*I2)/t)
    ques.write(q)
    ans.write(a)

ques.close()
ans.close()