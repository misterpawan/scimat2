import random
import math

# Two balls each of mass 0.05 g, moving in opposite directions with speed 6 ms-1 collide and rebound with the same speed. What is the impulse imparted to each ball due to the other?
# A batsman deflects a ball by an angle of 45 degrees without changing its initial speed which is equal to 54 ms-1. What is the impulse imparted to the ball? (Mass of the ball is 15 g)

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

def type1():
    m = random.randint(50,2000)
    v = random.randint(2,2000)
    q = "Two balls each of mass "+str(m)+" g, moving in opposite directions with speed "+str(v)+" ms-1 collide and rebound with the same speed. What is the impulse imparted to each ball due to the other?\n"
    impulse = (2*m*v)/1000
    a = str(round(impulse,1))+" kgms-1, in the direction of final velocity for both of them\n"
    return q,a

def type2():
    m = random.randint(50,300)
    angle = random.randint(1,180)
    v = random.randint(1,200)
    q = "A batsman deflects a ball by an angle of "+str(angle)+" degrees without changing its initial speed which is equal to "+str(v)+" ms-1. What is the impulse imparted to the ball? (Mass of the ball is "+str(m)+" g)\n"
    anglerad = (angle*math.pi)/360
    impulse = (2*m*v*math.cos(anglerad))/1000
    a = str(round(impulse,1))+" kgms-1, perpendicular to point of impact on the bat\n"
    return q,a

for i in range(no_of_samples):
    type = random.randint(1,3)
    if type == 1:
        q,a = type1()
    else:
        q,a = type2()
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()