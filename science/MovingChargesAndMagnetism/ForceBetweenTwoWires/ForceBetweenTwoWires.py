import random
import math

# Two long and parallel straight wires A and B carring currents of i1 A and i2 A in the same direction are seperated by a distance r cm. Estimate the force and its nature on the l cm section of wire A.  

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi
mu = 4*pi*(10**-7)

no_of_samples = 2000000

def cal1(i1, i2, r, l) :
    r = r*(10**-2)
    l = l*(10**-2)
    return (mu*i1*i2*l)/(2*pi*r)  

def type1() :
    r = random.randint(1,100)
    i1 = random.randint(1,50)
    i2 = random.randint(1,50)
    l = random.randint(1,50)
    t = random.randint(1,4)
    if t == 1 :     
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the same direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire A.\n"
    elif t == 2:
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the same direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire B.\n"
    elif t == 3 :     
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the same direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire A. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the same direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire B. (mu = 4 x pi x 10-7 TmA-1)\n"
    a = "{:.2e}".format(cal1(i1, i2, r, l)) + " newtons and attractive\n"
    return q,a

def type2() :
    r = random.randint(1,100)
    i1 = random.randint(1,50)
    i2 = random.randint(1,50)
    l = random.randint(1,50)
    t = random.randint(1,4)
    if t == 1 :     
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the opposite direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire A.\n"
    elif t == 2:
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the opposite direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire B.\n"
    elif t == 3 :     
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the opposite direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire A. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "Two long and parallel straight wires A and B carring currents of " + str(i1) + " A and " + str(i2) + " A in the opposite direction are seperated by a distance " + str(r) + " cm. Estimate the force and its nature on the " + str(l) + " cm section of wire B. (mu = 4 x pi x 10-7 TmA-1)\n"
    a = "{:.2e}".format(cal1(i1, i2, r, l)) + " newtons and replusive\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
