
import math
import random

# A radioactive isotope has a half-life of T years. How long will it take the activity to reduce to p percent.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

for i in range(no_of_samples):
    T = random.randint(1,1000)
    p = random.randint(10,990)
    p = round(p/10,1)
    ques = "A radioactive isotope has a half-life of " + str(T) + " years. How long will it take the activity to reduce to " + str(p) + " percent.\n"
    answ = (math.log(100/p)*T)/0.693
    answer = "{:.2e}".format(answ) + "years\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
