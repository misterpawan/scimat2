import random

# A car moving along a straight highway with speed of 126 ms-1 is brought to a stop within a distance of 200 m. What is the retardation of the car (assumed uniform), and how long does it take for the car to stop?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20
for i in range(no_of_samples):
    v = random.randint(33,433)
    s = random.randint(1,10000)
    q = "A car moving along a straight highway with speed of "+str(v)+" ms-1 is brought to a stop within a distance of "+str(s)+" m. What is the acceleration of the car (assumed uniform), and how long does it take for the car to stop?\n"
    acc = (v**2)/s
    a = "a = -"+str(round(acc,1)) + " ms-2, t = "+str(round(v/acc,1))+" s\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()