import random
import math

# A Circular coil of wire consisiting n turns, each of radius r cm carries a current of i A. What is the magnitude of the magnetic field B at a point on the axis which is x cm from the center of the coil.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi
mu = 4*pi*(10**-7)

no_of_samples = 500000

def cal1(n, r, i, x) :
    r = r * (10**-2)
    x = x * (10**-2)
    return (mu*n*i*r*r)/(2*math.sqrt(((r*r)+(x*x))**3)) 

def type1() :
    n = random.randint(1,200)
    i = random.randint(1,20)
    r = random.randint(10,100)
    x = random.randint(10,100)
    t=random.randint(1,2)
    if t == 1 :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm carries a current of " + str(i) + " A. What is the magnitude of the magnetic field B at a point on the axis which is " + str(x) + " cm from the center of the coil. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm carries a current of " + str(i) + " A. What is the magnitude of the magnetic field B at a point on the axis which is " + str(x) + " cm from the center of the coil.\n"
    a = "{:.2e}".format(cal1(n,r,i,x)) + " tesla\n"
    return q,a


for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
