import random
import math

# A small pin fixed on a table top is viewed from above from a distance of d cm. By what distance would the pin appear to be raised if it is viewed from the same point through a t cm thick glass slab held parallel to the table? Refractive index of glass = mu.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

for i in range(no_of_samples):
    d = random.randint(1,100)
    t = random.randint(1,100)
    mu = random.randint(150,300)
    mu = round(mu/100,2)
    ques = "A small pin fixed on a table top is viewed from above from a distance of " + str(d) + " cm. By what distance would the pin appear to be raised if it is viewed from the same point through a " + str(t) + " cm thick glass slab held parallel to the table? Refractive index of glass = " + str(mu) + ".\n"
    answ1 = t*(1-(1/mu))
    answer = "{:.2e}".format(answ1) + " cm\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
