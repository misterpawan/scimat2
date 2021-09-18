import random
import math

# About 5% of the power of a 100 W light bulb is converted to visible radiation. What is the average intensity of the visible radiation at a distance of d m from the bulb?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
pi = math.pi

for i in range(no_of_samples):
    per = random.randint(1,99)
    P = random.randint(1,400)
    d = random.randint(1,200)
    q = "About "+str(per)+" percent of the power of a "+str(P)+" W light bulb is converted to visible radiation. What is the average intensity of the visible radiation at a distance of "+str(d)+" m from the bulb?\n"
    P1 = (per/P)*100
    I = P1/(4*pi*d*d)
    a = "{:.2e} watt/m2\n".format(I)
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
