import random

# Two discs of moments of inertia I1 and I2 about their respective axes, and rotating with angular speed w1 and w2 are brought into contact face to face with their axes of rotation coincident, what is the angular speed of the two-disc system? 
# Two discs of moments of inertia I1 and I2 about their respective axes, and rotating with angular speed w1 and w2 are brought into contact face to face with their axes of rotation coincident, what is the loss in kinetic energy of the two-disc system? 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(i1, i2, w1, w2) :
    return round(((i1*w1)+(i2*w2))/(i1+i2),1)

def cal2(i1, i2, w1, w2) :
    w = ((i1*w1)+(i2*w2))/(i1+i2)
    k = 0.5*(i1+i2)*w*w
    k1 = 0.5*i1*w1*w1
    k2 = 0.5*i2*w2*w2
    return round(k1+k2-k,1)

def type1() :
    i1 = random.randint(1,100)
    i2 = random.randint(1,100)
    w1 = random.randint(1,100)
    w2 = random.randint(1,100)
    q = "Two discs of moments of inertia " + str(i1) + " and " + str(i2) + " about their respective axes, and rotating with angular speed " + str(w1) + " rad/s and " + str(w2) + " rad/s are brought into contact face to face with their axes of rotation coincident, what is the angular speed of the two-disc system?\n"
    a = str(cal1(i1, i2, w1, w2)) + "rad/s\n"
    return q,a

def type2() :
    i1 = random.randint(1,100)
    i2 = random.randint(1,100)
    w1 = random.randint(1,100)
    w2 = random.randint(1,100)
    q = "Two discs of moments of inertia " + str(i1) + " and " + str(i2) + " about their respective axes, and rotating with angular speed " + str(w1) + " rad/s and " + str(w2) + " rad/s are brought into contact face to face with their axes of rotation coincident, what is the loss in kinetic energy of the two-disc system? \n"
    a = str(cal2(i1, i2, w1, w2)) + "joules\n"
    return q,a

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
