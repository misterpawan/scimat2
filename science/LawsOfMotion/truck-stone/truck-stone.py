import random
import math

# A truck starts from rest and accelerates uniformly at 2.0 ms-2. At t = 10 s, a stone is dropped by a person standing on the top of the truck (6 m high from the ground). What are the (a) velocity, and (b) acceleration of the stone at t = 11s? (Neglect air resistance.)

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    acc = random.randint(1,20)
    t1 = random.randint(1,200)
    h = random.randint(1,30)
    t2 = random.randint(t1,t1+30)
    q = "A truck starts from rest and accelerates uniformly at "+str(acc)+" ms-2. At t = "+str(t1)+" s, a stone is dropped by a person standing on the top of the truck ("+str(h)+" m high from the ground). What are the (a) velocity, and (b) acceleration of the stone at t = "+str(t2)+" s? (Neglect air resistance.)\n"
    vx = t1*acc
    vy = (t2-t1)*10
    v = math.sqrt(vx**2+vy**2)
    angle = math.atan(vy/vx)*(180/math.pi)
    a = "velocity is "+str(round(v,1))+" ms-1, at angle "+str(round(angle))+" degrees with horizontal, acceleration is g(10 ms-2) downwards\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()