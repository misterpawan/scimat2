import random
import math

# A short bar magnet placed with its axis at d degrees with a uniform external magnetic field of b T experiences a torque of magnitude equal to t J. What is the magnitude of the magnetic moment of the bar magnet.
# A short bar magnet of magnetic moment m is placed with its axis at d degrees with a uniform external magnetic field of b T. What is the magnitude of torque experienced by the bar magnet.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

pi = math.pi

def cal1(t, b, d) :
    d = math.sin((d*pi)/180)
    return t/(b*d)

def cal2(m, b, d) :
    d = math.sin((d*pi)/180)
    return m*b*d

def type1() :
    b = random.randint(1,100)
    b = round(b*0.01,2)
    d = random.randint(1,90)
    t = random.randint(1,200)
    t = round(t*0.001,3)
    q = "A short bar magnet placed with its axis at " + str(d) + " degrees with a uniform external magnetic field of " + str(b) + " T experiences a torque of magnitude equal to " + str(t) + " J. What is the magnitude of the magnetic moment of the bar magnet.\n"
    a = "{:.2e}".format(cal1(t, b, d)) + " joule/tesla\n"
    return q,a

def type2() :
    b = random.randint(1,100)
    b = round(b*0.01,2)
    d = random.randint(1,90)
    m = random.randint(1,200)
    m = round(m*0.01,2)
    q = "A short bar magnet of magnetic moment " + str(m) + " is placed with its axis at " + str(d) + " degrees with a uniform external magnetic field of " + str(b) + " T. What is the magnitude of torque experienced by the bar magnet.\n"
    a = "{:.2e}".format(cal2(m, b, d)) + " joule/tesla\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    else :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
