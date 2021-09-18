import random
import math

# What is the force between two small charged spheres having charges q1 and q2 placed d cm apart
# The electrostatic force on a small sphere of charge q1 due to another small charge of q2 in air is F. What is the distance between spheres, 
# The electrostatic force on a small sphere of charge q1 due to another small charge of q2 in air is F. What is force on the second sphere due to first? 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(0,4)
    if types < 3:
        q1 = random.randint(1,200)
        q2 = random.randint(1,200)
        if random.randint(0,1):
            q1 = -q1
        if random.randint(0,1):
            q2 = -q2
        F = random.randint(1,200)
        q = "The electrostatic force on a small sphere of charge "+str(q1)+" x (10^(-6))C due to another small charge of "+str(q2)+" x (10^(-6))C in air is "+str(F)+" N. "
        if types!=2:
            q = q + "What is the distance between spheres?\n"
            r = math.sqrt(abs((q1*q2*(9*(10**9))*(10**(-12)))/F))
            a = "{:.2e}".format(r)+" m\n"
        else:
            q = q + "What is force on the second sphere due to first?\n"
            a = str(F)+" newton\n"
    else:
        q1 = random.randint(1,200)
        q2 = random.randint(1,200)
        if random.randint(0,1):
            q1 = -q1
        if random.randint(0,1):
            q2 = -q2
        d = random.randint(1,100)
        F = (9*(10**9)*q1*q2*(10**(-12)))/(d*d*0.0001)
        q = "What is the force between two small charged spheres having charges "+str(q1)+" x (10^(-6))C and "+str(q2)+" x (10^(-6))C placed "+str(d)+" cm apart?\n"
        a = "{:.2e}".format(F) + " newton\n"    
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
    
qns.close()
ans.close()
