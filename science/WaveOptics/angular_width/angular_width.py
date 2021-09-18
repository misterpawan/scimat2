import random
import math

# In a double-slit experiment the angular width of a fringe is found to be d degrees on a screen placed D m away. The wavelength of light used is l nm. What will be the angular width of the fringe if the entire experimental apparatus is immersed in liquid of refractive index mu.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

for i in range(no_of_samples):
    d = random.randint(1,10)
    d = round(d/10,1)
    D = random.randint(1,10)
    mu = random.randint(101,200)
    mu = round(mu/100,2)
    l = random.randint(1,100)
    ques = "In a double-slit experiment the angular width of a fringe is found to be " + str(d) + " degrees on a screen placed " + str(D) + " m away. The wavelength of light used is " + str(l) + " nm. What will be the angular width of the fringe if the entire experimental apparatus is immersed in liquid of refractive index " + str(mu) + ".\n"
    answer = "{:.2e}".format(d/mu) + " degrees\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
