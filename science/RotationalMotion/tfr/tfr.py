import random
import math

# Calculate the torque produced by a f N force acting at the end of a l m long wrench at an angle of r degrees to the wrench.
# A torque of t Nm is produced by a f N force acting at the end of a l m long wrench at an angle of r degrees to the wrench. What is the value of f.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
ang = [0, math.pi/6, math.pi/3, math.pi/2]

def cal1(f, l, r) :
    return round(f*l*math.sin(r),1)

def cal2(t, l, r) :
    return round((t)/(l*math.sin(r)),1)

def type1() :
    f = random.randint(1,500)
    l = random.randint(1,500)
    temp = random.randint(0,3)
    q = "Calculate the torque produced by a " + str(f) + " N force acting at the end of a " + str(l) + " m long wrench at an angle of " + str(ang[temp]) + " degrees to the wrench.\n"
    a = str(cal1(f, l, ang[temp])) + "newton-m\n"
    return q,a

def type2() :
    t = random.randint(500,1000)
    l = random.randint(1,500)
    temp = random.randint(1,3)
    q = "A torque of " + str(t) + " Nm is produced by a f N force acting at the end of a " + str(l) + " m long wrench at an angle of " + str(ang[temp]) + " degrees to the wrench. What is the value of f.\n"
    a = str(cal2(t, l, ang[temp])) + "newton\n"
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
