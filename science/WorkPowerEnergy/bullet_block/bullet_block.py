import random

# A bullet of mass m1 kg and horizontal speed v1 ms-1 strikes a block of wood of mass m2 kg and instantly comes to rest with respect to the block. The block is suspended from the ceiling by thin wire. Calculate the height to which the block rises. 
# A bullet of mass m1 kg and horizontal speed v1 ms-1 strikes a block of wood of mass m2 kg and instantly comes to rest with respect to the block. Estimate the amount of heat produced in the block.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
g = 9.8

def cal1(m1, v1, m2) :
    v = round((m1*v1)/(m1+m2),2)
    return round((v*v)/(2*g),1)

def cal2(m1, v1, m2) :
    v = round((m1*v1)/(m1+m2),2)
    k1 = round(0.5*m1*v1*v1,1)
    k2 = round(0.5*(m1*m2)*v*v,1)
    return k1 - k2

def type1() :
    m1 = random.randint(1,100)
    v1 = random.randint(1,100)
    m2 = random.randint(1,100)
    q = "A bullet of mass " + str(m1) + " kg and horizontal speed " + str(v1) + " ms-1 strikes a block of wood of mass " + str(m2) + " kg and instantly comes to rest with respect to the block. The block is suspended from the ceiling by thin wire. Calculate the height to which the block rises. \n"
    h = str(cal1(m1, v1, m2)) + " m\n"
    return q,h

def type2() :
    m1 = random.randint(1,100)
    v1 = random.randint(1,100)
    m2 = random.randint(1,100)
    q = "A bullet of mass " + str(m1) + " kg and horizontal speed " + str(v1) + " ms-1 strikes a block of wood of mass " + str(m2) + " kg and instantly comes to rest with respect to the block. Estimate the amount of heat produced in the block.\n"
    k = str(cal2(m1, v1, m2)) + " joules\n"
    return q,k

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
