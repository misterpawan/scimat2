import random

# A satelite of mass m kg orbits around a planet at a height of h m from the surface of the planet. What is the gravitational potential energy on the satelite due to planets magnetic field. Mass of planet = M kg and radius of the planet = R m.
# A satelite of mass m kg orbits around a planet at a height of h m from the surface of the planet. What is the gravitational potential on the satelite due to planets magnetic field. Mass of planet = M kg and radius of the planet = R m.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2000000

g = 6.67 * (10**-11)

def cal1(m, M, h, R) :
    return (-1*g*M)/(h+R)

def cal2(m, M, h, R) :
    return (-1*g*M*m)/(h+R)

def type1() :
    m = random.randint(400,600)
    M = random.randint(1,100)
    M = M * (10**10)
    h = random.randint(1,10)
    h = h * (10**3)
    R = random.randint(1,10)
    R = R * (10**6)
    t = random.randint(1,2)
    if t == 1 :
        q = "A satelite of mass " + str(m) + " kg orbits around a planet at a height of " + str(h) + " m from the surface of the planet. What is the gravitational potential energy on the satelite due to planets magnetic field. Mass of planet = " + str(M) + " kg and radius of the planet = " + str(R) + " m.\n"
    else :
        q = "A satelite of mass " + str(m) + " kg orbits around a planet at a height of " + str(h) + " m from the surface of the planet. What is the gravitational potential energy on the satelite due to planets magnetic field. Mass of planet = " + str(M) + " kg and radius of the planet = " + str(R) + " m. G = 6.67 x 10-11\n"
    w = "{:.2e}".format(cal1(m, M, h, R)) + " joule \n"
    return q,w

def type2() :
    m = random.randint(400,600)
    M = random.randint(1,100)
    M = M * (10**10)
    h = random.randint(1,10)
    h = h * (10**3)
    R = random.randint(1,10)
    R = R * (10**6)
    t = random.randint(1,2)
    if t == 1 :
        q = "A satelite of mass " + str(m) + " kg orbits around a planet at a height of " + str(h) + " m from the surface of the planet. What is the gravitational potential on the satelite due to planets magnetic field. Mass of planet = " + str(M) + " kg and radius of the planet = " + str(R) + " m.\n"
    else :
        q = "A satelite of mass " + str(m) + " kg orbits around a planet at a height of " + str(h) + " m from the surface of the planet. What is the gravitational potential on the satelite due to planets magnetic field. Mass of planet = " + str(M) + " kg and radius of the planet = " + str(R) + " m. G = 6.67 x 10-11\n"
    w = "{:.2e}".format(cal2(m, M, h, R)) + " joule/kg \n"
    return q,w

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    else :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
