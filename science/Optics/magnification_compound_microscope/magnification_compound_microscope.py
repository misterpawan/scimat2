import random
import math

# A compound microscope has a magnification m. The focal length of eyepiece is f cm. Assuming that the final image is formed at least distance of distinct vision (25 cm). Find the magnification produced by objective.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000

for i in range(no_of_samples):
    f = random.randint(10,110)
    m = random.randint(10,200)
    ques = "A compound microscope has a magnification " + str(m) + ". The focal length of eyepiece is " + str(f) + " cm. Assuming that the final image is formed at least distance of distinct vision (25 cm). Find the magnification produced by objective.\n"
    answ1 = m*(1+(25/f))
    answer = "{:.2e}".format(answ1) + "\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
