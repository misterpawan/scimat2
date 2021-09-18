import random
import math

# A circular coil of radius r cm and n turns is rotated about its vertical diameter with an angular speed of w rad/s in a uniform horizontal magnetic field of magnitude b T. Obtain the maximum and average emf induced in the coil. If a coil forms a closed loop of resistance r ohm, what is the maximum current in the coil and average power loss due to joule heating. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
pi = math.pi

def cal1(n, b, r, w, R) :
    r = r * (10**-2)
    A = pi*r*r
    e = n*w*b*A
    i = e/R
    return e , i, (e*i)/2   

def type1() :
    b = random.randint(1,100)
    b = round(b*0.1,1)
    w = random.randint(1,100)
    n = random.randint(1,20)
    R = random.randint(1,10)
    r = random.randint(20,40)
    q = "A circular coil of radius " + str(r) + " cm and " + str(n) + " turns is rotated about its vertical diameter with an angular speed of " + str(w) + " rad/s in a uniform horizontal magnetic field of magnitude " + str(b) + " T. Obtain the maximum and average emf induced in the coil. If a coil forms a closed loop of resistance " + str(R) + " ohm, what is the maximum current in the coil and average power loss due to joule heating?\n"
    a1, a2, a3 = cal1(n, b, r, w , R)
    a = "maximum emf : " + "{:.2e}".format(a1) + " volt, avg emf : 0 volts, maximum current : " + "{:.2e}".format(a2) + " amp, avg power loss : " + "{:.2e}".format(a3) + " joule\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
