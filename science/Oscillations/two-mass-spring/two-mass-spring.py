import random
import math

# Two masses each of mass m are attached by a spring of spring constant K Nm-1, If a force F is applied at free end of both masses, then what is the time period of oscillation.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(10,200)
    k = random.randint(10,200)
    F = random.randint(10,200)
    q = "Two masses each of mass "+str(m)+" kg are attached by a spring with K = "+str(k)+" Nm-1, If a force "+str(F)+" N is applied at free ends of both masses, then what is the time period of oscillation?\n"
    t = (2*math.pi)*math.sqrt(m/(2*k))
    a = "{:.2e}".format(t) + " s\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()