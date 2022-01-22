import random
import math

# A solid sphere rolls down two different inclined planes of heights h1 and h2 and with angles of inclination of a1 and a2, on which it reaches bottom with more speed ? 
# A solid sphere rolls down two different inclined planes of the same heights but with angles of inclination of a1 and a2, on which it will reach the ground faster ? 
# A solid sphere rolls down two different inclined planes of heights h1 and h2 and with angles of inclination of a1 and a2, on which it will reach the ground faster ?
# A solid sphere and a hollow sphere rolls down two different inclined planes of the heights h1 and h2 and with angles of inclination of a1 and a2, which one reaches bottom with more speed ?
# A solid sphere and a hollow sphere rolls down two different inclined planes of the heights h1 and h2 and with angles of inclination of a1 and a2, which will reach the ground faster ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 3000000
# no_of_samples = 10

shapes = ["solid sphere", "hollow sphere", "solid cylinder", "hollow cylinder", "solid disk", "hoop"]
con = [2/5, 2/3, 1/2, 1, 1/2, 1]

def cal1(h1, h2, a1, a2, k1, k2) :
    v1 = h1/(k1+1)
    v2 = h2/(k2+1)
    if v1 > v2 :
        return 1
    elif v1 < v2 :
        return 2
    return 0

def cal2(h1, h2, a1, a2, k1, k2) :
    v1 = math.sqrt((k1+1)*h1)/math.sin((a1*math.pi)/180)
    v2 = math.sqrt((k2+1)*h2)/math.sin((a2*math.pi)/180)
    if v1 < v2 :
        return 1
    elif v1 > v2 :
        return 2
    return 0

def type1() :
    h1 = random.randint(1,20)
    h2 = random.randint(1,20)
    a1 = random.randint(1,90)
    a2 = random.randint(1,90)
    t = random.randint(0,5)
    q = "A " + shapes[t] + " rolls down two different inclined planes of the heights " + str(h1) + " cm and " + str(h2) + " cm and with angles of inclination of " + str(a1) + " and " + str(a2) + ", on which it reaches bottom with more speed ?\n"
    v = cal1(h1, h2, a1, a2, con[t], con[t])
    if v == 1 :
        a = "first plane has more"
        a1 = "first plane it has more"
    elif v == 2 :
        a = "second plane has more"
        a1 = "second plane it has more"
    else :
        a = "both planes have same"
        a1 = "both planes it have same"
    final_a = "speed(v) by which it reaches bottom is proportional to height(h). among the two inclined planes, " + a + " value of h. so on " + a1 + " speed on reaching the bottom.\n"
    return q,final_a

def type2() :
    h = random.randint(1,40)
    a1 = random.randint(1,90)
    a2 = random.randint(1,90)
    t = random.randint(0,5)
    q = "A " + shapes[t] + " rolls down two different inclined planes of the same height " + str(h) + " cm but with angles of inclination of " + str(a1) + " and " + str(a2) + ", on which it will reach the ground faster ? \n"
    v = cal2(h, h, a1, a2, con[t], con[t])
    if v == 1 :
        a = "first plane has less"
        a1 = "first plane it takes less"
    elif v == 2 :
        a = "second plane has less"
        a1 = "second plane it takes less"
    else :
        a = "both planes have same"
        a1 = "both planes it takes same"
    final_a = "if a is angle of inclanation of the plane, time taken (t) is inversely proportional to sin(a). among the two planes, " + a + " value of sin(a). so on " + a1 + " time to reach the ground.\n"
    return q,final_a

def type3() :
    h1 = random.randint(1,20)
    h2 = random.randint(1,20)
    a1 = random.randint(1,90)
    a2 = random.randint(1,90)
    t = random.randint(0,5)
    q = "A " + shapes[t] + " rolls down two different inclined planes of heights " + str(h1) + " and " + str(h2) + " and with angles of inclination of " + str(a1) + " and " + str(a2) + ", on which it will reach the ground faster ?\n"
    v = cal2(h1, h2, a1, a2, con[t], con[t])
    if v == 1 :
        a = "first plane has less"
        a1 = "first plane it takes less"
    elif v == 2 :
        a = "second plane has less"
        a1 = "second plane it takes less"
    else :
        a = "both planes have same"
        a1 = "both planes it takes same"
    final_a = "if a is angle of inclanation of the plane and h is height of the plane, time taken (t) is proportional to sq.root(h)/sin(a). among the two planes, " + a + " value of sq.root(h)/sin(a). so on " + a1 + " time to reach the ground.\n"
    return q,final_a

def type4() :
    h1 = random.randint(1,20)
    h2 = random.randint(1,20)
    a1 = random.randint(1,90)
    a2 = random.randint(1,90)
    t1 = random.randint(0,5)
    t2 = t1
    while t2 == t1 :
        t2 = random.randint(0,5)
    q = "A " + shapes[t1] + " and a " + shapes[t2] + " rolls down two different inclined planes of the heights " + str(h1) + " and " + str(h2) + " and with angles of inclination of " + str(a1) + " and " + str(a2) + ", which one reaches bottom with more speed ?\n"
    v = cal1(h1, h2, a1, a2, con[t1], con[t2])
    if v == 1 :
        a = "first case has more"
        a1 = shapes[t1] + " has more" 
    elif v == 2 :
        a = "second case has more"
        a1 = shapes[t2] + " has more"
    else :
        a = "both cases have same"
        a1 = "both have same"
    final_a = "if h is height of the plane and moment of inertia of object rolling = k x m x (r^2), then speed(v) is proportional to h/(1+k). among two cases " + a + " value of h/(1+k). so " + a1 + " speed on reaching the bottom.\n"
    return q,final_a

def type5() :
    h1 = random.randint(1,20)
    h2 = random.randint(1,20)
    a1 = random.randint(1,90)
    a2 = random.randint(1,90)
    t1 = random.randint(0,5)
    t2 = t1
    while t2 == t1 :
        t2 = random.randint(0,5)
    q = "A " + shapes[t1] + " and a " + shapes[t2] + " rolls down two different inclined planes of the heights " + str(h1) + " and " + str(h2) + " and with angles of inclination of " + str(a1) + " and " + str(a2) + ", which will reach the ground faster ?\n"
    v = cal2(h1, h2, a1, a2, con[t1], con[t2])
    if v == 1 :
        a = "first case has less"
        a1 = shapes[t1] + " takes less" 
    elif v == 2 :
        a = "second case has less"
        a1 = shapes[t2] + " takes less"
    else :
        a = "both cases have same"
        a1 = "both takes same"
    final_a = "if a is angle of inclanation of the plane, h is height of the plane and moment of inertia of object rolling = k x m x (r^2), then time taken(t) is proportional to sq.root(h*(k+1))/sin(a). among two cases " + a + " value of sq.root(h*(k+1))/sin(a). so " + a1 + " time to reach the ground.\n"
    return q,final_a

for i in range(no_of_samples):
    types = random.randint(1,5)
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
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
