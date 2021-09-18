import random


# At t = 0, a wheel is rotating with a angular velocity of w1 rad/s at a constant angular acceleration a rad/s2 about its fixed axis. It attains a angular velocity of w2 rad/s in t = t sec. What is the value of a.    
# At t = 0, a wheel is rotating with a angular velocity of w1 rad/s at a constant angular acceleration a rad/s2 about its fixed axis. It attains a angular velocity of w2 rad/s in t = t sec. What is the value of w1.
# At t = 0, a wheel is rotating with a angular velocity of w1 rad/s at a constant angular acceleration a rad/s2 about its fixed axis. It attains a angular velocity of w2 rad/s in t = t sec. What is the value of w2.
# At t = 0, a wheel is rotating with a angular velocity of w1 rad/s at a constant angular acceleration a rad/s2 about its fixed axis. It attains a angular velocity of w2 rad/s in t = t sec. What is the value of t.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

def cal1(w1, w2, t):
    return round((w2 - w1) / t,1)

def cal2(w2, a, t):
    return round(w2 - (a*t),1)

def cal3(w1, a, t):
    return round(w1 + (a*t),1)

def cal4(w1, w2,a ):
    return round((w2 - w1) / a,1)


def type1():
    w1 = random.randint(0,500)
    w2 = random.randint(w1,w1+500)
    t = random.randint(1,20)
    a = str(cal1(w1,w2,t)) + " rad/s2\n"
    q = "At t = 0, a wheel is rotating with a angular velocity of " + str(w1) + " rad/s at a constant angular acceleration a rad/s2 about its fixed axis. It attains a angular velocity of " + str(w2) + " rad/s in t = " + str(t) + " sec. What is the value of a.\n"
    return q,a

def type2():
    a = random.randint(0,40)
    t = random.randint(1,40)
    w2 = random.randint(a*t,(a*t)+1000)
    w1 = str(cal2(w2,a,t)) + " m/s\n"
    q = "At t = 0, a wheel is rotating with a angular velocity of w rad/s at a constant angular acceleration " + str(a) + " rad/s2 about its fixed axis. It attains a angular velocity of " + str(w2) + " rad/s in t = " + str(t) + " sec. What is the value of w.\n"
    return q,w1

def type3():
    w1 = random.randint(0,1000)
    a = random.randint(0,40)
    t = random.randint(1,40)
    w2 = str(cal3(w1,a,t)) + " m/s\n"
    q = "At t = 0, a wheel is rotating with a angular velocity of " + str(w1) + " rad/s at a constant angular acceleration " + str(a) + " rad/s2 about its fixed axis. It attains a angular velocity of w rad/s in t = " + str(t) + " sec. What is the value of w.\n"
    return q,w2

def type4():
    w1 = random.randint(0,500)
    w2 = random.randint(w1,w1+500)
    a = random.randint(1,20)
    t = str(cal4(w1,w2,a)) + " s\n"
    q = "At t = 0, a wheel is rotating with a angular velocity of " + str(w1) + " rad/s at a constant angular acceleration " + str(a) + " rad/s2 about its fixed axis. It attains a angular velocity of " + str(w2) + " rad/s in t = T sec. What is the value of T.\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1:
        ques,answer = type1()
    if types == 2:
        ques,answer = type2()
    if types == 3:
        ques,answer = type3()
    if types == 4:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
