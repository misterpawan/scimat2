import random

# What is the electric field at a point P at a distance of r m from the center of the spherical shell of radius R m and having Q C charge distributed uniformly on it .    
# What is the electric field at a point P at a distance of r m from the center of the uniform solid sphere of radius R m and having Q C charge distributed uniformly on it .

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 3000000

k = 9 * (10**9)

def cal2(m, r, R):
    return (k*m)/(r*r)

def cal3(m, r):
    return (k*m)/(r*r)

def cal4(m, r, R) :
    return (k*m*r)/(R**3)

def type1():
    q = random.randint(-200,200)
    q = q * (10**-8)
    r = random.randint(1,500)
    R = random.randint(r+1,r+100)
    v = "0 newton/coulomb\n"
    Q = "What is the electric field at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    return Q,v

def type2():
    q = random.randint(-200,200)
    q = q * (10**-8)
    R = random.randint(1,500)
    r = random.randint(R+1,R+100)
    v = "{:.2e}".format(cal2(q, r, R)) + " newton/coulomb\n"
    Q = "What is the electric field at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    return Q,v

def type3():
    q = random.randint(-200,200)
    q = q * (10**-8)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(q, R)) + " newton/coulomb\n"
    Q = "What is the electric field at a point P on the surface of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    return Q,v

def type4():
    q = random.randint(-200,200)
    q = q * (10**-8)
    r = random.randint(1,500)
    R = random.randint(r+1,r+100)
    v = "{:.2e}".format(cal4(q, r, R)) + " newton/coulomb\n"
    Q = "What is the electric field at a point P at a distance of " + str(r) + " m from the center of the uniform solid sphere of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly.\n"
    return Q,v

def type5():
    q = random.randint(-200,200)
    q = q * (10**-8)
    R = random.randint(1,500)
    r = random.randint(R+1,R+100)
    v = "{:.2e}".format(cal2(q, r, R)) + " newton/coulomb\n"
    Q = "What is the electric field at a point P at a distance of " + str(r) + " m from the center of the uniform solid sphere of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly.\n"
    return Q,v

def type6():
    q = random.randint(-200,200)
    q = q * (10**-8)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(q, R)) + " newton/coulomb\n"
    Q = "What is the electric field at a point P on the surface of the uniform solid sphere of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly.\n"
    return Q,v

def type7():
    q = random.randint(-200,200)
    q = q * (10**-8)
    R = random.randint(1,1000)
    v = "0 newton/coulomb\n"
    Q = "What is the electric field at the centre of the uniform solid sphere of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly.\n"
    return Q,v

for i in range(no_of_samples):
    types = random.randint(0,5)
    if types == 0:
        types2 = random.randint(0,1)
        if types2 == 0:
            ques,answer = type1()
        else:
            ques,answer = type7()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3:
        ques,answer = type4()
    elif types == 4:
        ques,answer = type5()
    elif types == 5:
        ques,answer = type6()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()