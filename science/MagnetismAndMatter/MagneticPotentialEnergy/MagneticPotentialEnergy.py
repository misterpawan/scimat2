import random
import math

# A short bar magnet of magnetic moment m is placed in a uniform magnetic field of b T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at stable position.
# A short bar magnet of magnetic moment m is placed in a uniform magnetic field of b T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at unstable position.
# A short bar magnet of magnetic moment m is placed in a uniform magnetic field of b T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at a position making an angle of d degrees with magnetic field.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000

pi = math.pi

def cal1(m, b, d) :
    d = math.cos((d*pi)/180)
    return -1*m*b*d

def type1() :
    b = random.randint(1,2000)
    b = round(b*0.01,2)
    m = random.randint(1,2000)
    m = round(m*0.01,2)
    q = "A short bar magnet of magnetic moment " + str(m) + " J/T is placed in a uniform magnetic field of " + str(b) + " T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at stable position.\n"
    a = "{:.2e}".format(cal1(m, b, 0)) + " joule\n"
    return q,a

def type2() :
    b = random.randint(1,2000)
    b = round(b*0.01,2)
    m = random.randint(1,2000)
    m = round(m*0.01,2)
    q = "A short bar magnet of magnetic moment " + str(m) + " J/T is placed in a uniform magnetic field of " + str(b) + " T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at unstable position.\n"
    a = "{:.2e}".format(cal1(m, b, 180)) + " joule\n"
    return q,a

def type3() :
    b = random.randint(1,100)
    b = round(b*0.01,2)
    m = random.randint(1,200)
    m = round(m*0.01,2)
    d = random.randint(1,179)
    q = "A short bar magnet of magnetic moment " + str(m) + " J/T is placed in a uniform magnetic field of " + str(b) + " T. If the magnet is free to rotate in the plane of the field, what is the potential energy of the magnet at a position making an angle of " + str(d) + " degrees with magnetic field.\n"
    a = "{:.2e}".format(cal1(m, b, d)) + " joule\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    else :
        ques, answer = type3()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
