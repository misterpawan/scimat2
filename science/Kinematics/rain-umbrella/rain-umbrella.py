import random
import math

# Rain is falling vertically with a speed of 30 ms-1. A woman rides a bicycle with a speed of 10 ms-1 in the north to south direction. What is the direction in which she should hold her umbrella ?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    v1 = random.randint(1,2000)
    v2 = random.randint(1,2000)
    q = "Rain is falling vertically with a speed of "+str(v1)+" cms-1. A woman rides a bicycle with a speed of "+str(v2)+" cms-1 in the north to south direction. What is the direction in which she should hold her umbrella ?\n"
    a = str(round(math.atan(v2/v1)*57.2958))+" degrees south of vertical\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()