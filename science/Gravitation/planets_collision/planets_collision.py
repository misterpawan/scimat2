import random
import math

# Two stars each of one solar mass m kg are approaching each other for a head on collision.When they are at a distance  R km, their speeds are negligible. What is the speed with which they collide? The radius of each star is r km. Assume the stars to remain undistorted until they collide.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

g =  6.67 * (10**-11)

def cal1(m, r, R) :
    p = ((-1*g*m)/R)+ ((g*m)/(2*r))
    return math.sqrt(p)

def type1() :
    m = random.randint(1,100)
    m = m * (10**30)
    R = random.randint(1,100)
    R = R * (10**9)
    r = random.randint(1,100)
    r = r * (10**4)
    t = random.randint(1,2)
    if t == 1 :
        q = "Two stars each of one solar mass " + str(m) + " kg are approaching each other for a head on collision.When they are at a distance " + str(R) + " km, their speeds are negligible. What is the speed with which they collide? The radius of each star is " + str(r) + " km. Assume the stars to remain undistorted until they collide.\n"
    else :
        q = "Two stars each of one solar mass " + str(m) + " kg are approaching each other for a head on collision.When they are at a distance " + str(R) + " km, their speeds are negligible. What is the speed with which they collide? The radius of each star is " + str(r) + " km. Assume the stars to remain undistorted until they collide. G = 6.67 x 10-11\n"
    R = R * 1000
    r = r * 1000
    w = "{:.2e}".format(cal1(m, r, R)) + " m/s\n"
    return q,w

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
