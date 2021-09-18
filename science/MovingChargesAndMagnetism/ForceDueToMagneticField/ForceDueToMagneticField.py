import random
import math

# What is the magnitude of the mgnetic force per unit length on a wire carring a current of i A and making an angle of d degrees with the directon of uniform magnetic field of b tesla.
# A l cm of wire carring a current of i A, is placed inside a solenoid making d degrees with its axis.The magnetic field inside the solenoid is b tesla. Find the magnetic force on the wire. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi

no_of_samples = 1000000

def cal1(i, d, b, l) :
    l = l*(10**-2)
    d = math.sin((d*pi)/(180))
    return round(b*i*d*l,1) 

def type1() :
    d = random.randint(1,180)
    i = random.randint(1,200)
    b = random.randint(10,100)
    q = "What is the magnitude of the mgnetic force per unit length on a wire carring a current of " + str(i) + " A and making an angle of " + str(d) + " degrees with the directon of uniform magnetic field of " + str(b) + " tesla.\n"
    a = str(cal1(i,d,b,100)) + " newtons\n"
    return q,a

def type2() :
    d = random.randint(1,180)
    i = random.randint(1,100)
    b = random.randint(1,50)
    l = random.randint(1,50)
    q = "A " + str(l) + " cm of wire carring a current of " + str(i) + " A, is placed inside a solenoid making " + str(d) + " degrees with its axis.The magnetic field inside the solenoid is " + str(b) + " tesla. Find the magnetic force on the wire.\n"
    a = str(cal1(i,d,b,l)) + " newtons\n"
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
