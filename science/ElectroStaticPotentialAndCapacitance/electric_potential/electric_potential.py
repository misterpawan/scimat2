import random

# What is the gravitational potential at a point P at a distance of r m from the center of the spherical shell of radius R m and having Q C charge distributed uniformly on it.    
# What is the gravitational potential at a point P at a distance of r m from a charge of Q C.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

k = 9 * (10**9)

def cal1(m, r, R):
  return (k*m)/R

def cal2(m, r, R):
  return (k*m)/r

def cal3(m, r):
  return (k*m)/r

def type1():
    q = random.randint(-200,200)
    r = random.randint(1,500)
    R = random.randint(r+1,r+100)
    v = "{:.2e}".format(cal1(q, r, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    return Q,v

def type2():
    q = random.randint(-200,200)
    R = random.randint(1,500)
    r = random.randint(R+1,R+100)
    v = "{:.2e}".format(cal2(q, r, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P at a distance of " + str(r) + " m from the center of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    return Q,v

def type3():
    q = random.randint(-500,500)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(q, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P on the surface of the spherical shell of radius " + str(R) + " m and having " + "{:.2e}".format(q) + " C charge distributed uniformly on it.\n"
    return Q,v

def type4() :
    q = random.randint(-500,500)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(q, R)) + " joule/coulomb\n"
    Q = "What is the gravitational potential at a point P at a distance of " + str(R) + " m from a charge of " + "{:.2e}".format(q) + " C.\n"
    return Q,v

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()