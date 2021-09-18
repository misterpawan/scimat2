import random

# Two heavy spheres each of mass m1 kg, m2 kg respectively are placed R m apart on a horizontal table. What is the gravitational field at the mid point of the line joining the centres of the spheres ? 
# Two heavy spheres each of mass m1 kg, m2 kg respectively are placed R m apart on a horizontal table. What is the gravitational potential at the mid point of the line joining the centres of the spheres ? 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2500000

g = 6.67 * (10**-11)

def cal1(m1, m2, R) :
    p = (-1*g*m1)/(R*R) + (g*m2)/(R*R) 
    if p < 0 :
        return -1 * p
    return p

def cal2(m1, m2, R) :
    p = (-1*g*m1)/(R) - (g*m2)/(R)
    return p

def type1() :
    m1 = random.randint(1,200)
    m2 = random.randint(1,200)
    R = random.randint(1,200)
    t = random.randint(1,2)
    if t == 1 :
        q = "Two heavy spheres each of mass " + str(m1) + " kg, " + str(m2) + " kg respectively are placed " + str(R) + " m apart on a horizontal table. What is the gravitational field at the mid point of the line joining the centres of the spheres ?\n"
    else :
        q = "Two heavy spheres each of mass " + str(m1) + " kg, " + str(m2) + " kg respectively are placed " + str(R) + " m apart on a horizontal table. What is the gravitational field at the mid point of the line joining the centres of the spheres ? G = 6.67 x 10-11\n"
    w = "{:.2e}".format(cal1(m1, m2, R/2)) + " newton/kg \n"
    return q,w

def type2() :
    m1 = random.randint(1,200)
    m2 = random.randint(1,200)
    R = random.randint(1,200)
    t = random.randint(1,2)
    if t == 1 :
        q = "Two heavy spheres each of mass " + str(m1) + " kg, " + str(m2) + " kg respectively are placed " + str(R) + " m apart on a horizontal table. What is the gravitational potential at the mid point of the line joining the centres of the spheres ?\n"
    else :
        q = "Two heavy spheres each of mass " + str(m1) + " kg, " + str(m2) + " kg respectively are placed " + str(R) + " m apart on a horizontal table. What is the gravitational potential at the mid point of the line joining the centres of the spheres ? G = 6.67 x 10-11\n"
    w = "{:.2e}".format(cal2(m1, m2, R/2)) + " joule/kg \n"
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
