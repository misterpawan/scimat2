import random
import math

# A steel cable with a radius of 1.5 cm supports a chairlift at a ski area. If the maximum stress is not to exceed 108 Nm-2 what is the maximum load the cable can support ?
# Two strips of metal are riveted together at their ends by four rivets, each of diameter 6.0 mm. What is the maximum tension that can be exerted by the riveted strip if the shearing stress on the rivet is not to exceed 6.9 x 107 Pa? Assume that each rivet is to carry one-quarter of the load.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:    
        r = random.randint(1,200)
        stress = random.randint(1,40000)
        q = "A steel cable with a radius of "+str(r)+" mm supports a chairlift at a ski area. If the maximum stress is not to exceed "+str(stress)+" x 10^(6) Nm-2 what is the maximum load the cable can support?\n"
        a = str(round((stress*math.pi*(r*r))/1000000,1))+" x 10^(6) newton\n"
    else:
        d = random.randint(1,20)
        p = random.randint(100,200000)*100
        q = "Two strips of metal are riveted together at their ends by four rivets, each of diameter "+str(d)+" mm. What is the maximum tension that can be exerted by the riveted strip if the shearing stress on the rivet is not to exceed "+"{:.5e}".format(p)+"? Assume that each rivet is to carry one-quarter of the load.\n"
        r = d/2
        a = p*math.pi*r*r*(10**(-6))*4
        a = "{:.1e}".format(a) + " newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()