import random
import os

# What is the focal length of a convex lens of focal length f1 cm in contact with a concave lens of focal length f2 cm? Is the system a converging or a diverging lens? Ignore thickness of the lenses.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
 
lens = ["convex","concave"]

def cal1(f1,f2):
    return round((f1*f2)/(f1+f2),2)

def cal2(f1,f2,f3):
    return round((f1*f2*f3)/((f1*f2)+(f2*f3)+(f3*f1)),2)

def type1():
    F1 = 0
    F2 = 0
    while F1+F2 == 0 :
        f1 = random.randint(1,500)
        f2 = random.randint(1,500)
        t1 = random.randint(0,1)
        t2 = random.randint(0,1)
        if t1 == 1 :
            F1 = -1*f1
        if t2 == 1 :
            F2 = -1*f2
    f = cal1(F1,F2)
    if f < 0 :
        P = str(round(-1*f,2)) + " cm and diverging\n"
    else :
        P = str(f) + " cm and converging\n"
    q = "What is the focal length of a " + lens[t1] + " lens of focal length " + str(f1) + " cm in contact with a " + lens[t2] + " lens of focal length " + str(f2) + " cm ? Is the system a converging or a diverging lens? Ignore thickness of the lenses.\n"
    return q,P

def type2():
    F1 = 0
    F2 = 0
    F3 = 0
    while (F1*F2)+(F2*F3)+(F3*F1) == 0 :
        f1 = random.randint(1,50)
        f2 = random.randint(1,50)
        f3 = random.randint(1,50)
        t1 = random.randint(0,1)
        t2 = random.randint(0,1)
        t3 = random.randint(0,1)
        if t1 == 1 :
            F1 = -1*f1
        if t2 == 1 :
            F2 = -1*f2
        if t3 == 1 :
            F3 = -1*f3
    f = cal2(F1,F2,F3)
    if f < 0 :
        P = str(round(-1*f,2)) + " cm and diverging\n"
    else :
        P = str(f) + " cm and converging\n"
    q = "What is the focal length of a system of " + lens[t1] + " lens of focal length " + str(f1) + " cm, a " + lens[t2] + " lens of focal length " + str(f2) + " cm and a " + lens[t3] + " lens of focal length " + str(f3) + " cm? Is the system a converging or a diverging lens? Ignore thickness of the lenses.\n"
    return q,P

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques,answer = type1()
    elif types == 2 :
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
