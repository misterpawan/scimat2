import random
import math

# What is the De-Broglie wavelength associated with a mass of m kg and having a velocity of v m/s.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

h = 6.626 * (10**-34)

for i in range(no_of_samples):
    m = random.randint(1,10000000)
    m = round(m/10000000,7)
    v = random.randint(1,100)
    t = random.randint(1,2)
    if t == 1 :
        ques = "What is the De-Broglie wavelength associated with a mass of " + "{:.4e}".format(m) + " kg and having a velocity of " + str(v) + " m/s.\n"
    else :
        ques = "What is the De-Broglie wavelength associated with a mass of " + "{:.4e}".format(m) + " kg and having a velocity of " + str(v) + " m/s. (h = 6.626 x 10^-34 Js)\n"
    answer = "{:.2e}".format(h/(m*v)) + " \n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
