import random
import math

# A Circular coil of wire consisiting n turns, each of radius r cm carries a current of i A. What is the magnitude of the magnetic field B at the center of the coil.
# A Circular coil of wire consisiting n turns, each of radius r cm placed in a horizontal plane carries a current of i A in clockwise direction. What is the magnitude and direction of the magnetic field B at the center of the coil.


qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi
mu = 4*pi*(10**-7)

no_of_samples = 2000000

def cal1(n, r, i) :
    r = r * (10**-2)
    return (mu*n*i)/(2*r) 

def type1() :
    n = random.randint(1,200)
    i = random.randint(1,20)
    r = random.randint(10,1000)
    t=random.randint(1,2)
    if t == 1 :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm carries a current of " + str(i) + " A. What is the magnitude of the magnetic field B at the center of the coil. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm carries a current of " + str(i) + " A. What is the magnitude of the magnetic field B at the center of the coil.\n"
    a = "{:.2e}".format(cal1(n,r,i)) + " tesla\n"
    return q,a

def type2() :
    n = random.randint(1,200)
    i = random.randint(1,20)
    r = random.randint(10,1000)
    t=random.randint(1,2)
    if t == 1 :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm in a horizontal plane carries a current of " + str(i) + " A in clockwise direction. What is the magnitude and direction of the magnetic field B at the center of the coil. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm in a horizontal plane carries a current of " + str(i) + " A in clockwise direction. What is the magnitude and direction of the magnetic field B at the center of the coil.\n"
    a = "{:.2e}".format(cal1(n,r,i)) + " tesla vertically downwards\n"
    return q,a

def type3() :
    n = random.randint(1,200)
    i = random.randint(1,20)
    r = random.randint(10,1000)
    t=random.randint(1,2)
    if t == 1 :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm in a horizontal plane carries a current of " + str(i) + " A in anticlockwise direction. What is the magnitude and direction of the magnetic field B at the center of the coil. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A Circular coil of wire consisiting " + str(n) + " turns, each of radius " + str(r) + " cm in a horizontal plane carries a current of " + str(i) + " A in anticlockwise direction. What is the magnitude and direction of the magnetic field B at the center of the coil.\n"
    a = "{:.2e}".format(cal1(n,r,i)) + " tesla vertically upwards\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    else :
        ques, answer = type3()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
