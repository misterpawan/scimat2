import random

# A stream of liquid (density rho kgm-3) flowing horizontally with a speed of 15 ms-1 pushes out of a tube of cross sectional area 10-2 m2, and hits at a vertical wall nearby. What is the force exerted on the wall by the impact of water, assuming that it does not rebound?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 500000
# no_of_samples = 20

for i in range(no_of_samples):
    v = random.randint(1,20)
    area = random.randint(100,300)
    rho = random.randint(10,2010)
    q = "A stream of liquid (density "+str(rho)+" kgm-3) flowing horizontally with a speed of "+str(v)+" ms-1 pushes out of a tube of cross sectional area "+str(area)+" cm2, and hits at a vertical wall nearby. What is the force exerted on the wall by the impact of liquid, assuming that it does not rebound?\n"
    expr = (area*rho*v*v)/10000
    a = str(round(expr,1))+" newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()