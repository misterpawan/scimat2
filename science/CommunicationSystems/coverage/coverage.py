import random
import math

# A TV antenna is 81 m tall. How much service area can it cover if the receving antenna is at ground level?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 10000

for i in range(no_of_samples):
    l = random.randint(100,40000)
    q = "A TV antenna is "+str(l)+" cm tall. How much service area can it cover if the receving antenna is at ground level?\n"
    a = "{:.2e} m2\n".format(math.pi * 2 * 6.4 * 10000 * l)
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()