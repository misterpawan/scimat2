import random
import math

# What is Brewster angle for a material-1 of refractive index mu1 to material-2 of refractive index mu2 transition.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000

for i in range(no_of_samples):
    mu1 = random.randint(101,300)
    mu1 = round(mu1/100,2)
    mu2 = mu1
    while(mu2 == mu1) :
        mu2 = random.randint(101,300)
        mu2 = round(mu2/100,2)
    ques = "What is Brewster angle for a material-1 of refractive index " + str(mu1) + " to material-2 of refractive index " + str(mu2) + " transition.\n"
    answer = "We know that Brewster angle for a material-1 of refractive index mu1 to material-2 of refractive index mu2 transition = tan-1(mu2/mu1) = tan-1(" + str(mu2) + "/" + str(mu1) + ") = "  +  "{:.2e}".format(math.atan(mu2/mu1)) + " \n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
