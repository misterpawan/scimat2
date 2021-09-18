import random
import math

# Compute the bulk modulus of a material from the following data: Initial volume = 100.0 litre, Pressure increase = 100.0 atm (1 atm = 1.013 x 10^5 Pa), Final volume = 100.5 litre.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    V = random.randint(100,300)
    P = random.randint(100,300)
    inc = random.randint(100,300)
    q = "Compute the bulk modulus of a material from the following data: Initial volume = "+str(V)+" litre, Pressure increase = "+str(P)+" atm (1 atm = 1.013 x 10^5 Pa), volume increased = "+str(inc)+" ml.\n"
    B = (P * 1.013 * (10**8) * V )/ (inc)
    a = "{:.2e}".format(B) + "\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()