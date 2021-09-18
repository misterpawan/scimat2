import random

# The blades of a windmill sweep out a circle of area A. If the wind flows at a velocity v perpendicular to the circle, what is the mass of the air passing through it in time t? 
# The blades of a windmill sweep out a circle of area A. If the wind flows at a velocity v perpendicular to the circle, what is the kinetic energy of the air passed in time t? 
# The blades of a windmill sweep out a circle of area A. If the wind flows at a velocity v perpendicular to the circle. Assume that the windmill converts t% of the wind’s energy into electrical energy, What is the electrical power produced?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000
d = 1.2

def cal1(A, v, t) :
    return A*v*t*d

def cal2(A, v, t) :
    return 0.5*A*v*v*v**t*d

def type1() :
    A = random.randint(1,100)
    v = random.randint(1,100)
    t = random.randint(1,100)
    q = "The blades of a windmill sweep out a circle of area " + str(A) + " m2. If the wind flows at a velocity " + str(v) + " ms-1 perpendicular to the circle, what is the mass of the air passing through it in time " + str(t) + " s? \n"
    m = str(cal1(A, v, t)) + " kg\n"
    return q,m

def type2() :
    A = random.randint(1,100)
    v = random.randint(1,100)
    t = random.randint(1,100)
    q = "The blades of a windmill sweep out a circle of area " + str(A) + " m2. If the wind flows at a velocity " + str(v) + " ms-1 perpendicular to the circle, what is the kinetic energy of the air passed in time " + str(t) + " s?\n"
    k = str(cal2(A, v, t)) + " joules\n"
    return q,k

def type3() :
    A = random.randint(1,100)
    v = random.randint(1,100)
    t = random.randint(1,100)
    q = " The blades of a windmill sweep out a circle of area " + str(A) + " m2. If the wind flows at a velocity " + str(v) + " ms-1 perpendicular to the circle. Assume that the windmill converts " + str(t) + " percent of the wind’s energy into electrical energy, What is the electrical power produced?\n"
    p = str(round(cal2(A, v, t)/100,1)) + " watts\n"
    return q,p

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    elif types == 3 :
        ques, answer = type3()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
