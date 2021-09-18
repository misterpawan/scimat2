import random
import math

# A prism is made of glass of unknown refractive index. A parallel beam of light is incident on a face of the prism. The angle of minimum deviation is measured to be 40°. What is the refractive index of the material of the prism? The refracting angle of the prism is 60°. If the prism is placed in liquid (refractive index 1.33), predict the new angle of minimum deviation of a parallel beam of light.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

for i in range(no_of_samples):
    d1 = random.randint(1,80)
    d2 = random.randint(1,80)
    mu = random.randint(101,250)
    mu = round(mu/100,2)
    ques = "A prism is made of glass of unknown refractive index. A parallel beam of light is incident on a face of the prism. The angle of minimum deviation is measured to be " + str(d1) + ". What is the refractive index of the material of the prism? The refracting angle of the prism is " + str(d2) + ". If the prism is placed in liquid (refractive index " + str(mu) + "), predict the new angle of minimum deviation of a parallel beam of light.\n"
    answ1 = math.sin((d1+d2)/2)/math.sin(d2/2)
    answ2 = 2*(math.asin(math.sin(d2/2)*(answ1/mu)) - (d2/2))
    answ1 = "{:.2e}".format(answ1)
    answ2 = "{:.2e}".format(answ2)
    answer = answ1 + " and " + answ2 + " degrees\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
