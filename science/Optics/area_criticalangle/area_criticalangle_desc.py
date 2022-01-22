
import math
import random

# A small bulb is placed at the bottom of a tank containing liquid to a depth of h cm. What is the area of the surface of water through which light from the bulb can emerge out? Refractive index of liquid is mu.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000
# no_of_samples = 10
pi = math.pi

def cal1 (h, mu) :
    k = 1/mu
    k = k*k
    h = h * (10**-2)
    return round(pi*h*h*(k/(1-k)),2) 

def type1() :
    h = random.randint(10,300)
    mu = random.randint(110,300)
    mu = round(mu*0.01,2)
    q = "A small bulb is placed at the bottom of a tank containing liquid to a depth of " + str(h) + " cm. What is the area of the surface of water through which light from the bulb can emerge out? Refractive index of liquid is " + str(mu) + ".\n"
    a = str(cal1(h,mu)) + " m2\n"
    a1 = "if c is the critical angle, then sin(c) = 1/mu = 1/" + str(mu) + ". radius of the required circle(r) = h x tan(c). so required area = pi x r^2 = pi x (h x tan(c))^2 = pi x (h^2) x ((sin(c)^2)/(1-(sin(c))^2)) = " + a
    return q,a1

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
