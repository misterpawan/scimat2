import random
import math

# Two circular coils X and Y of radii r1 cm and r2 cm, respectively lies in the same vertical plane containing the north to south direction. Coil A has n1 turns and carries a current of i1 A, Coil B has n2 turns and carries a current of i2 A. The sense of current in X in anti-clockwise direction and Y is clockwise direction. From an observer looking at the coils facing west, Give the magnitude and direction of net magnetic field due to the coils at the center. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2000000

pi = math.pi
mu = 4*pi*(10**-7)

def cal1(r1, r2, n1, n2, i1, i2) :
    r1 = r1*(10**-2)
    r2 = r2*(10**-2)
    b1 = (mu*n1*i1)/(2*r1)
    b2 = (mu*n2*i2)/(2*r2)
    if b1 > b2 :
        return b1-b2,1
    return b2-b1,2 

def type1() :
    r1 = random.randint(10,40)
    r2 = random.randint(10,40)
    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    i1 = random.randint(10,40)
    i2 = random.randint(10,40)
    t = random.randint(1,2)
    if t == 1 :
        q = "Two circular coils X and Y of radii " + str(r1) + " cm and " + str(r2) + " cm, respectively lies in the same vertical plane containing the north to south direction. Coil A has " + str(n1) + " turns and carries a current of " + str(i1) + " A, Coil B has " + str(n2) + " turns and carries a current of " + str(i2) + " A. The sense of current in X in anti-clockwise direction and Y is clockwise direction. From an observer looking at the coils facing west, Give the magnitude and direction of net magnetic field due to the coils at the center.\n"
    else :
        q = "Two circular coils X and Y of radii " + str(r1) + " cm and " + str(r2) + " cm, respectively lies in the same vertical plane containing the north to south direction. Coil A has " + str(n1) + " turns and carries a current of " + str(i1) + " A, Coil B has " + str(n2) + " turns and carries a current of " + str(i2) + " A. The sense of current in X in anti-clockwise direction and Y is clockwise direction. From an observer looking at the coils facing west, Give the magnitude and direction of net magnetic field due to the coils at the center. (mu = 4 x pi x 10-7)\n"
    a1, a2 = cal1(r1, r2, n1, n2, i1, i2)
    v = "{:.2e}".format(a1) + " tesla "
    if a2 == 1 :
        v = v + "and towards east"
    else :
        v = v + "and towards west"
    return q,v

def type2() :
    r1 = random.randint(10,40)
    r2 = random.randint(10,40)
    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    i1 = random.randint(10,40)
    i2 = random.randint(10,40)
    t = random.randint(1,2)
    if t == 1 :
        q = "Two circular coils X and Y of radii " + str(r1) + " cm and " + str(r2) + " cm, respectively lies in the same vertical plane containing the north to south direction. Coil A has " + str(n1) + " turns and carries a current of " + str(i1) + " A, Coil B has " + str(n2) + " turns and carries a current of " + str(i2) + " A. The sense of current in X in anti-clockwise direction and Y is clockwise direction. From an observer looking at the coils facing east, Give the magnitude and direction of net magnetic field due to the coils at the center.\n"
    else :
        q = "Two circular coils X and Y of radii " + str(r1) + " cm and " + str(r2) + " cm, respectively lies in the same vertical plane containing the north to south direction. Coil A has " + str(n1) + " turns and carries a current of " + str(i1) + " A, Coil B has " + str(n2) + " turns and carries a current of " + str(i2) + " A. The sense of current in X in anti-clockwise direction and Y is clockwise direction. From an observer looking at the coils facing east, Give the magnitude and direction of net magnetic field due to the coils at the center. (mu = 4 x pi x 10-7)\n"
    a1, a2 = cal1(r1, r2, n1, n2, i1, i2)
    v = "{:.2e}".format(a1) + " tesla "
    if a2 == 1 :
        v = v + "and towards west"
    else :
        v = v + "and towards east"
    return q,v

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    ans.write(answer)

qns.close()
ans.close()
