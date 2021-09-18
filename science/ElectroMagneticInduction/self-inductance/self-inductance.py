import random

# Current in a circuit falls from I1+I2 A to I2 A in t s.If an average emf of V V induced, give an estimate of the self-inductance of the circuit.

ques = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    I1 = random.randint(1,200)
    I2 = random.randint(1,20)
    t = round(random.randint(1,20)/100,2)
    V = random.randint(100,300)
    q = "Current in a circuit falls from "+str(I1+I2)+" A to "+str(I2)+" A in "+str(t)+" s. If an average emf of "+str(V)+" V induced, give an estimate of the self-inductance of the circuit.\n"
    a = "{:.2e} henry\n".format((V*t)/I1)
    ques.write(q)
    ans.write(a)

ques.close()
ans.close()