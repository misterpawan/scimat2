import random

# A satellite orbits the earth at a height of h km above the surface. How much energy must be expended to rocket the satellite out of the planet's gravitational influence? Mass of the satellite = 200 kg; mass of the planet = 6.0 x  1024 kg; radius of the planet = 6.4 x  106 m; G = 6.67 x  10-11 N m2 kg-2.
# A satellite orbits the earth at a height of h km above the surface. How much energy must be expended to rocket the satellite out of the planet’s gravitational influence? Mass of the satellite = 200 kg; mass of the planet = 6.0 x  1024 kg; radius of the planet = 6.4 x  106 m. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

g = 6.67 * (10**-11)

def cal1(m, M, r, h) :
    return (g*m*M)/(2*(r+h))

def type1() :
    m = random.randint(100,1100)
    h = random.randint(100,1100)
    M = random.randint(1,10)
    M = M * (10**24)
    r = random.randint(1,10)
    r = r * (10**6)
    t = random.randint(1,2)
    if t == 1 :
        q = "A satellite orbits the earth at a height of " + str(h) + " km above the surface. How much energy must be expended to rocket the satellite out of the planet's gravitational influence? Mass of the satellite = " + str(m) + " kg; mass of the planet = " + str(M) + " kg; radius of the planet = " + str(r) + " m; G = 6.67 x  10-11 N m2 kg-2.\n"
    elif t == 2 :
        q = "A satellite orbits the earth at a height of " + str(h) + " km above the surface. How much energy must be expended to rocket the satellite out of the planet's gravitational influence? Mass of the satellite = " + str(m) + " kg; mass of the planet = " + str(M) + " kg; radius of the planet = " + str(r) + " m.\n"
    h = h * 1000
    w = "{:.2e}".format(cal1(m, M, r, h)) + " joules\n"
    return q,w

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
