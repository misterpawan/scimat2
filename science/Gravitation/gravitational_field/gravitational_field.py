import random

# What is the gravitational field at a point P at a distance of r m from the center of the spherical shell of radius R m and mass m kg.    
# What is the gravitational field at a point P at a distance of r m from the center of the uniform solid sphere of radius R m and mass m kg.
# What is the gravitational field at a point P at a distance of r m from a mass of m kg.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 4000000

G = 6.67 * (10**-11)

def cal1(m, r, R):
    return 0

def cal2(m, r, R):
    return (-1*G*m)/(r*r)

def cal3(m, r):
    return (-1*G*m)/(r*r)

def cal4(m, r, R) :
    return (-1*G*m*r)/(R**3)

def type1():
    m = random.randint(1,500)
    r = random.randint(1,500)
    R = random.randint(r+1,r+100)
    v = "{:.2e}".format(cal1(m, r, R)) + " newton/kg\n"
    q = "What is the gravitational field at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and mass " + str(m) + " kg.\n"
    return q,v

def type2():
    m = random.randint(1,500)
    R = random.randint(1,500)
    r = random.randint(R+1,R+100)
    v = "{:.2e}".format(cal2(m, r, R)) + " newton/kg\n"
    q = "What is the gravitational field at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and mass " + str(m) + " kg.\n"
    return q,v

def type3():
    m = random.randint(1,1000)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(m, R)) + " newton/kg\n"
    q = "What is the gravitational field at a point P on the surface of the spherical shell of radius " + str(R) + " m and mass " + str(m) + " kg.\n"
    return q,v

def type4() :
    m = random.randint(1,1000)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(m, R)) + " newton/kg\n"
    q = "What is the gravitational field at a point P at a distance of " + str(R) + " m from a mass of " + str(m) + " kg.\n"
    return q,v

def type5():
    m = random.randint(1,500)
    r = random.randint(1,500)
    R = random.randint(r+1,r+100)
    v = "{:.2e}".format(cal4(m, r, R)) + " newton/kg\n"
    q = "What is the gravitational field at a point P at a distance of " + str(r) + " m from the center of the uniform solid sphere of radius " + str(R) + " m and mass " + str(m) + " kg.\n"
    return q,v

def type6():
    m = random.randint(1,500)
    R = random.randint(1,500)
    r = random.randint(R+1,R+100)
    v = "{:.2e}".format(cal2(m, r, R)) + " newton/kg\n"
    q = "What is the gravitational field at a point P at a distance of " + str(r) + " m from the center of the uniform solid sphere of radius " + str(R) + " m and mass " + str(m) + " kg.\n"
    return q,v

def type7():
    m = random.randint(1,1000)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(m, R)) + " newton/kg\n"
    q = "What is the gravitational field at a point P on the surface of the uniform solid sphere of radius " + str(R) + " m and mass " + str(m) + " kg.\n"
    return q,v

def type8():
    m = random.randint(1,1000)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal1(m, R, R)) + " newton/kg\n"
    q = "What is the gravitational field at the centre of the uniform solid sphere of radius " + str(R) + " m and mass " + str(m) + " kg.\n"
    return q,v

for i in range(no_of_samples):
    types = random.randint(0,7)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3:
        ques,answer = type4()
    elif types == 4:
        ques,answer = type8()
    elif types == 5:
        ques,answer = type5()
    elif types == 6:
        ques,answer = type6()
    elif types == 7:
        ques,answer = type7()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()