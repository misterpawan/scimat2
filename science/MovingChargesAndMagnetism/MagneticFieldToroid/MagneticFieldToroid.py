import random
import math

# A toroid has a core of inner radius r1 cm and outer radius r2 cm, around which n turns of a wire are wound. If the current in the wire is i A, what is the magnetic field inside the core of the solenoid.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi
mu = 4*pi*(10**-7)

no_of_samples = 1000000

def cal1(n, r1, r2, i) :
    r1 = r1 * (10**-2)
    r2 = r2 * (10**-2)
    l = (r1+r2)*math.pi
    return (mu*n*i)/(l) 

def type1() :
    n = random.randint(100,300)
    i = random.randint(1,50)
    r1 = random.randint(50,150)
    r2 = random.randint(r1+1,r1+50)
    t=random.randint(1,2)
    if t == 1 :
        q = "A toroid has a core of inner radius " + str(r1) + " cm and outer radius " + str(r2) + " cm, around which " + str(n) + " turns of a wire are wound. If the current in the wire is " + str(i) + " A, what is the magnetic field inside the core of the solenoid. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A toroid has a core of inner radius " + str(r1) + " cm and outer radius " + str(r2) + " cm, around which " + str(n) + " turns of a wire are wound. If the current in the wire is " + str(i) + " A, what is the magnetic field inside the core of the solenoid.\n"
    a = "{:.2e}".format(cal1(n,r1,r2,i)) + " tesla\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
