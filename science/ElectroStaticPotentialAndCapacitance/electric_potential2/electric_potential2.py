import random
   
# What is the gravitational potential at a point P at a distance of r m from the center of the uniform solid sphere of radius R m and having Q C C charge distributed uniformly.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

k = 9 * (10**9)

def cal1(m, r, R):
  return (k*m)*((3*R*R)-(r*r))/(2*R*R*R)

def cal2(m, r, R):
  return (k*m)/r

def cal3(m, r):
  return (k*m)/r

def cal4(m,r) :
  return (k*m)/(2*r)  

def type1():
    Q = random.randint(-200,200)
    r = random.randint(1,500)
    R = random.randint(r+1,r+100)
    v = "{:.2e}".format(cal1(Q, r, R)) + " joule/coulomb\n"
    q = "What is the gravitational potential at a point P at a distance of " + str(r) + " m from the center of the uniform solid sphere of radius " + str(R) + " m and " + "{:.2e}".format(Q) + " C charge distributed uniformly.\n"
    return q,v

def type2():
    Q = random.randint(-200,200)
    R = random.randint(1,500)
    r = random.randint(R+1,R+100)
    v = "{:.2e}".format(cal2(Q, r, R)) + " joule/coulomb\n"
    q = "What is the gravitational potential at a point P at a distance of " + str(r) + " m from the center of the uniform solid sphere of radius " + str(R) + " m and " + "{:.2e}".format(Q) + " C charge distributed uniformly.\n"
    return q,v

def type3():
    Q = random.randint(-500,500)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal3(Q, R)) + " joule/coulomb\n"
    q = "What is the gravitational potential at a point P on the surface of the uniform solid sphere of radius " + str(R) + " m and " + "{:.2e}".format(Q) + " C charge distributed uniformly.\n"
    return q,v

def type4() :
    Q = random.randint(-500,500)
    R = random.randint(1,1000)
    v = "{:.2e}".format(cal4(Q, R)) + " joule/coulomb\n"
    q = "What is the gravitational potential at a center of the uniform solid sphere of radius " + str(R) + " m and " + "{:.2e}".format(Q) + " C charge distributed uniformly.\n"
    return q,v

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