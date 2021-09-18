import random
import math

# The rear side of a lorry is open and a box of 40 kg mass is placed 5 m away from the open end. 
# The coefficient of friction between the box and the surface below it is 0.15. 
# On a straight road, the lorry starts from rest and accelerates with 2 ms-2. 
# Will the box move? If yes what is the time taken for box to fall off the lorry, 
# what is the distance moved by the lorry from the starting point by the time box fall off the lorry?.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 30
g = 10

for i in range(no_of_samples):
    m = random.randint(1,200)
    mu = round(random.randint(0,100)/100,2)
    acc = random.randint(1,20)
    distance = random.randint(1,20)
    q = "The rear side of a lorry is open and a box of "+str(m)+" kg mass is placed "+str(distance)+" m away from the open end. The coefficient of friction between the box and the surface below it is "+str(mu)+". On a straight road, the lorry starts from rest and accelerates with "+str(acc)+" ms-2. Will the box move? If yes at what distance from the starting point does the box fall off the lorry?\n"
    if acc > mu*g:
        a_net = (acc-mu*g)
        time = math.sqrt((2*distance)/a_net)
        lorry_dist = (1/2)*acc*time*time
        a = "yes, box moves with "+str(round(a_net,1))+" ms-2 with respect to lorry, it takes "+str(round(time,1))+" s to fall off the lorry, lorry would have moved "+str(round(lorry_dist,1))+" m by the time box falls off\n"
    else:
        a = "no, box will not move\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()