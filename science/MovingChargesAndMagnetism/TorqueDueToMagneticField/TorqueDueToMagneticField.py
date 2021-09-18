import random
import math

# A square coil of side l cm consisits of n turns and carries a current of i A. The coil is suspended vertically and the normal to the plane of the coil makes an angle od d degress with the direction of a uniform horizontal magnetic field of magnitude b tesla. What is the magnitude of the torque experienced by the coil. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi

no_of_samples = 1000000

def cal1(n, i, d, b, A) :
    A = A*(10**-4)
    d = math.sin((d*pi)/(180))
    return round(n*b*i*d*A,1) 

def type1() :
    n = random.randint(10,50)
    i = random.randint(1,20)
    d = random.randint(1,90)
    b = random.randint(1,20)
    l = random.randint(1,50)
    q = "A square coil of side " + str(l) + " cm consists of " + str(n) + " turns and carries a current of " + str(i) + " A. The coil is suspended vertically and the normal to the plane of the coil makes an angle of " + str(d) + " degress with the direction of a uniform horizontal magnetic field of magnitude " + str(b) + " tesla. What is the magnitude of the torque experienced by the coil.\n"
    A = l*l
    a = str(cal1(n,i,d,b,A)) + " newton-m\n"
    return q,a

def type2() :
    n = random.randint(10,50)
    i = random.randint(1,20)
    d = random.randint(1,90)
    b = random.randint(1,20)
    l = random.randint(1,50)
    q = "A circular coil of radius " + str(l) + " cm consists of " + str(n) + " turns and carries a current of " + str(i) + " A. The coil is suspended vertically and the normal to the plane of the coil makes an angle of " + str(d) + " degress with the direction of a uniform horizontal magnetic field of magnitude " + str(b) + " tesla. What is the magnitude of the torque experienced by the coil.\n"
    A = pi*l*l
    a = str(cal1(n,i,d,b,A)) + " newton-m\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
