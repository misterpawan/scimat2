import random
import math

# If a monoatomic gas of n moles at v1 m3 is isothermally changed to volume v2 m3 at t K, then what is the work done.
# If a monoatomic gas of n moles at p1 pas is isothermally changed to volume p2 pas at t K, then what is the work done.
# If a diatomic gas of n moles at v1 m3 is isothermally changed to volume v2 m3 at t K, then what is the work done.
# If a diatomic gas of n moles at p1 pas is isothermally changed to volume p2 pas at t K, then what is the work done.
# If a gas of n moles at v1 m3 is isothermally changed to volume v2 m3 at t K, then what is the work done.
# If a gas of n moles at p1 pas is isothermally changed to volume p2 pas at t K, then what is the work done.


qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 3000000

r = 8.31

def cal1(n, t, v1, v2) :
    return round(-1*n*r*t*math.log(v2/v1),1)

def cal2(n, t, p1, p2) : 
    return round(-1*n*r*t*math.log(p1/p2),1) 

def type1() :
    n = random.randint(1,10)
    v1 = random.randint(10,60)
    v2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(v1) + " m3 is isothermally changed to volume " + str(v2) + " m3 at " + str(t) + " K, then what is the work done.\n"
    a = str(cal1(n,t,v1,v2)) + " joules\n"
    return q,a

def type2() :
    n = random.randint(1,10)
    p1 = random.randint(10,60)
    p2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " pas is isothermally changed to pressure " + str(p2) + " pas at " + str(t) + " K, then what is the work done.\n"
    a = str(cal2(n,t,p1,p2)) + " joules\n"
    return q,a

def type3() :
    n = random.randint(1,10)
    v1 = random.randint(10,60)
    v2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(v1) + " m3 is isothermally changed to volume " + str(v2) + " m3 at " + str(t) + " K, then what is the work done.\n"
    a = str(cal1(n,t,v1,v2)) + " joules\n"
    return q,a

def type4() :
    n = random.randint(1,10)
    p1 = random.randint(10,60)
    p2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " pas is isothermally changed to pressure " + str(p2) + " pas at " + str(t) + " K, then what is the work done.\n"
    a = str(cal2(n,t,p1,p2)) + " joules\n"
    return q,a

def type5() :
    n = random.randint(1,10)
    v1 = random.randint(10,60)
    v2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a gas of " + str(n) + " moles at " + str(v1) + " m3 is isothermally changed to volume " + str(v2) + " m3 at " + str(t) + " K, then what is the work done.\n"
    a = str(cal1(n,t,v1,v2)) + " joules\n"
    return q,a

def type6() :
    n = random.randint(1,10)
    p1 = random.randint(10,60)
    p2 = random.randint(10,60)
    t = random.randint(10,60)
    q = "If a gas of " + str(n) + " moles at " + str(p1) + " pas is isothermally changed to pressure " + str(p2) + " pas at " + str(t) + " K, then what is the work done.\n"
    a = str(cal2(n,t,p1,p2)) + " joules\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,6)
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
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
