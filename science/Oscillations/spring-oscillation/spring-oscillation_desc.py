import random
import math

# A spring balance has a scale that reads from 0 to 50 kg. The length of the scale is 20 cm. A body suspended from this balance, when displaced and released, oscillates with a period of 0.6 s. What is the weight of the body?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 500000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(10,200)
    l = random.randint(10,200)
    t = random.randint(10,200)*5
    q = "A spring balance has a scale that reads from 0 to "+str(m)+" kg. The length of the scale is "+str(l)+" cm. A body suspended from this balance, when displaced and released, oscillates with a period of "+str(t)+" ms. What is the weight of the body?\n"
    k = (m*9.8)/(l*0.01)
    w = (t*t*0.000001*k)/(4*math.pi*math.pi)
    a = "spring constant k can be found out using maximum mass and length of the scale as k = weight(m*g)/length, which is "+str(m)+"9.8/"+str(round(l*0.01,2))+" = "+str(round(k,2))
    a += ", we know that time period of a shm is t = 2*pi*sqrt(m/k), which implies, m = (t*t*k)/4*pi*pi, multiplying resulting mass with g, we get weight, which is equal to ("+str(t)+"*"+str(t)+"*"+str(round(k,2))+")/4*pi*pi = "
    a += "{:.2e}".format(w*9.8) + " newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()