import random
import math

# A circular coil of n turns and radius r cm carrying a current of i A rests with its plane normal to an external field of magnitude b T. The coil is free to turn about an axis in its plane perpendicular to the field direction. When the coil is turned slightly and released, it oscillates about its stable equilibrium with a frequency of v sec-1. What is the moment inertia of the coil about its axis of rotation.    

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

pi = math.pi

def cal1(n, i, b, r, v) :
    r = r * (10**-2)
    m = n*i*pi*r*r
    return (m*b)/(4*pi*pi*v*v)

def type1() :
    n = random.randint(1,50)
    b = random.randint(1,100)
    b = round(b*0.01,2)
    i = random.randint(1,50)
    v = random.randint(1,20)
    r = random.randint(10,20)
    q = "A circular coil of " + str(n) + " turns and radius " + str(r) + " cm carrying a current of " + str(i) + " A rests with its plane normal to an external field of magnitude " + str(b) + " T. The coil is free to turn about an axis in its plane perpendicular to the field direction. When the coil is turned slightly and released, it oscillates about its stable equilibrium with a frequency of " + str(v) + " sec-1. What is the moment of inertia of the coil about its axis of rotation.\n"
    a = "{:.2e}".format(cal1(n, i, b, r, v)) + " kgm2\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
