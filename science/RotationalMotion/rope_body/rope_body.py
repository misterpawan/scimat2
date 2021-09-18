import random

# A rope of negligible mass is wound round a hollow cylinder of mass m kg and radius r cm. What is the angular acceleration of the cylinder if the rope is pulled with a force of f N? Assume that there is no slipping.
# A rope of negligible mass is wound round a hollow cylinder of mass m kg and radius r cm. What is the liner acceleration of the rope if the rope is pulled with a force of f N? Assume that there is no slipping.
# A rope of negligible mass is wound round a solid cylinder of mass m kg and radius r cm. What is the angular acceleration of the cylinder if the rope is pulled with a force of f N? Assume that there is no slipping.
# A rope of negligible mass is wound round a solid cylinder of mass m kg and radius r cm. What is the liner acceleration of the rope if the rope is pulled with a force of f N? Assume that there is no slipping.
# A rope of negligible mass is wound round a hollow sphere of mass m kg and radius r cm. What is the angular acceleration of the sphere if the rope is pulled with a force of f N? Assume that there is no slipping.
# A rope of negligible mass is wound round a hollow sphere of mass m kg and radius r cm. What is the liner acceleration of the rope if the rope is pulled with a force of f N? Assume that there is no slipping.
# A rope of negligible mass is wound round a solid sphere of mass m kg and radius r cm. What is the angular acceleration of the sphere if the rope is pulled with a force of f N? Assume that there is no slipping.
# A rope of negligible mass is wound round a solid sphere of mass m kg and radius r cm. What is the liner acceleration of the rope if the rope is pulled with a force of f N? Assume that there is no slipping.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 4000000
c = [1,1/2,2/3,2/5]

def cal1(k, m, r, f) :
    return round((f*100)/(k*m*r),1)

def cal2(k, m, r, f) :
    return round((f)/(k*m),1)

def type1() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a hollow cylinder of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the angular acceleration of the cylinder if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal1(c[0], m, r, f)) + "rad/s2\n"
    return q,a

def type2() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a hollow cylinder of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the liner acceleration of the rope if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal2(c[0], m, r, f)) + "m/s2\n"
    return q,a

def type3() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a solid cylinder of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the angular acceleration of the cylinder if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal1(c[1], m, r, f)) + "rad/s2\n"
    return q,a

def type4() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a solid cylinder of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the liner acceleration of the rope if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal2(c[1], m, r, f)) + "m/s2\n"
    return q,a

def type5() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a hollow sphere of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the angular acceleration of the sphere if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal1(c[2], m, r, f)) + "rad/s2\n"
    return q,a

def type6() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a hollow sphere of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the liner acceleration of the rope if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal2(c[2], m, r, f)) + "m/s2\n"
    return q,a

def type7() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a solid sphere of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the angular acceleration of the sphere if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal1(c[3], m, r, f)) + "rad/s2\n"
    return q,a

def type8() :
    f = random.randint(1,100)
    m = random.randint(1,100)
    r = random.randint(1,100)
    q = "A rope of negligible mass is wound round a solid sphere of mass " + str(m) + " kg and radius " + str(r) + " cm. What is the liner acceleration of the rope if the rope is pulled with a force of " + str(f) + " N? Assume that there is no slipping.\n"
    a = str(cal2(c[3], m, r, f)) + "m/s2\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,8)
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
    else :
        ques, answer = type8()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
