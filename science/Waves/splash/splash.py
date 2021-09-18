import random
import math

# A stone dropped from the top of a tower of height 300 m high splashes into the water of a pond near the base of the tower. When is the splash heard at the top given that the speed of sound in air is 340 ms-1 ? (g = 9.8 ms-2 )

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    h = random.randint(20,2000)
    m = random.randint(2,2000)
    if random.randint(0,1):
        q = "A stone of mass "+str(m)+" g dropped from the top of a tower of height "+str(h)+" m high splashes into the water of a pond near the base of the tower. When is the splash heard at the top given that the speed of sound in air is 340 ms-1 ? (g = 9.8 ms-2 )\n"
    else:
        q = "A stone of mass "+str(m)+" g dropped from the top of a tower of height "+str(h)+" m high splashes into the water of a pond near the base of the tower. When is the splash heard at the top given.\n"
    t1 = math.sqrt((2*h)/9.8)
    t2 = h/340
    a = str(round(t1+t2,2))+" s\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()