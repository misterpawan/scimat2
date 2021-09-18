import random
import math

# A rectangular wire loop of sides l1 cm and l2 cm with a small cut is moving out of a region of uniform magnetic field of magnitude b T directed normal to the loop. What is the emf developed across the cut if the velocity of the loop is v cm/s in a direction normal to the two different sides of the loop. For how long does theinduced voltage last in each case.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

pi = math.pi
mu = 4*pi*(10**-7)

def cal1(b, l, v) :
    v = v*(10**-2)
    l = l*(10**-2)
    return b*l*v , l/v   

def type1() :
    b = random.randint(1,200)
    b = round(b*0.1,1)
    v = random.randint(1,100)
    l1 = random.randint(1,30)
    l2 = random.randint(1,30)
    while l2 == l1:
        l2 = random.randint(1,30)
    q = "A rectangular wire loop of sides " + str(l1) + " cm and " + str(l2) + " cm with a small cut is moving out of a region of uniform magnetic field of magnitude " + str(b) + " T directed normal to the loop. What is the emf developed across the cut if the velocity of the loop is " + str(v) + " cm/s in a direction normal to the two different sides of the loop. For how long does theinduced voltage last in each case.\n"
    a1, a2 = cal1(b,l1,v)
    a = "{:.2e}".format(a1) + " volt for " + "{:.2e}".format(a2) + " s if velocity is perpendicular to " + str(l1) + " cm side, "
    a1, a2 = cal1(b,l2,v)
    a += "{:.2e}".format(a1) + " volt for " + "{:.2e}".format(a2) + " s if velocity is perpendicular to " + str(l2) + " cm side\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
