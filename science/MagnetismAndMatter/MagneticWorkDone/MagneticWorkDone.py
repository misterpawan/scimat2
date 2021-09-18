import random
import math

# A bar magnet of magnetic moment is m JT-1 is keplt in a uniform magnetic field of b T. What is the work done by an external torque to turn the magnet which is alligned at an angle of d1 with magnetic field to an angle of d2.
# A solenoid of magnetic moment is m JT-1 is keplt in a uniform magnetic field of b T. What is the work done by an external torque to turn the magnet which is alligned at an angle of d1 with magnetic field to an angle of d2.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

pi = math.pi

def cal1(m, b, d1, d2) :
    d1 = math.cos((d1*pi)/180)
    d2 = math.cos((d2*pi)/180)
    return -1*m*b*(d1-d2)

def type1() :
    b = random.randint(1,100)
    b = round(b*0.01,2)
    m = random.randint(1,200)
    m = round(m*0.01,2)
    d1 = random.randint(1,150)
    d2 = random.randint(d1+1,180)
    q = "A bar magnet of magnetic moment is " + str(m) + " J/T is kept in a uniform magnetic field of " + str(b) + " T. What is the work done by an external torque to turn the magnet which is alligned at an angle of" + str(d1) + " degrees with magnetic field to an angle of " + str(d2) + " degrees.\n"
    a = "{:.2e}".format(cal1(m, b, d1, d2)) + " joule\n"
    return q,a

def type2() :
    b = random.randint(1,100)
    b = round(b*0.01,2)
    m = random.randint(1,200)
    m = round(m*0.01,2)
    d1 = random.randint(1,150)
    d2 = random.randint(d1+1,180)
    q = "A solenoid of magnetic moment is " + str(m) + " J/T is kept in a uniform magnetic field of " + str(b) + " T. What is the work done by an external torque to turn the magnet which is alligned at an angle of" + str(d1) + " degrees with magnetic field to an angle of " + str(d2) + " degrees.\n"
    a = "{:.2e}".format(cal1(m, b, d1, d2)) + " joule\n"
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
