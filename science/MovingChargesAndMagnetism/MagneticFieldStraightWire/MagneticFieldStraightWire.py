import random
import math

# A long straight wire in the horizontal plane carries a current of of i A in north to south direction. What is the magnitude and direction of the magnetic field B at a point r cm east of the wire.
# A long straight wire carries a current of of i A. What is the magnitude of the magnetic field B at a point r cm from the wire.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi
mu = 4*pi*(10**-7)

no_of_samples = 4000000

def cal2(r, i) :
    r = r * (10**-2)
    return (mu*i)/(2*pi*r)

def type1() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in north to south direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm east of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in north to south direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm east of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically upwards\n"
    return q,a

def type2() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in north to south direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm west of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in north to south direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm west of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically downwards\n"
    return q,a

def type3() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in south to north direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm east of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in south to north direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm east of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically downwards\n"
    return q,a

def type4() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in south to north direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm west of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in south to north direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm west of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically upwards\n"
    return q,a

def type5() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in east to west direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm south of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in east to west direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm south of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically upwards\n"
    return q,a

def type6() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in east to west direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm north of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in east to west direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm north of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically downwards\n"
    return q,a

def type7() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in west to east direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm south of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in west to east direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm south of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically downwards\n"
    return q,a

def type8() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in west to east direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm north of the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire in the horizontal plane carries a current of of " + str(i) + " A in west to east direction. What is the magnitude and direction of the magnetic field B at a point " + str(r) + " cm north of the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla vertically upwards\n"
    return q,a

def type9() :
    i = random.randint(1,500)
    r = random.randint(10,2000)
    t=random.randint(1,2)
    if t == 1:
        q = "A long straight wire carries a current of of " + str(i) + " A. What is the magnitude of the magnetic field B at a point " + str(r) + " cm from the wire. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A long straight wire carries a current of of " + str(i) + " A. What is the magnitude of the magnetic field B at a point " + str(r) + " cm from the wire.\n"
    a = "{:.1e}".format(cal2(r,i)) + " tesla\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,9)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    elif types == 3 :
        ques, answer = type3()
    elif types == 4 :
        ques, answer = type4()
    elif types == 5 :
        ques, answer = type5()
    elif types == 6 :
        ques, answer = type6()
    elif types == 7 :
        ques, answer = type7()
    elif types == 8 :
        ques, answer = type8()
    else :
        ques, answer = type9()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
