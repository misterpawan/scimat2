import random
import math

# An object is projected with an initial velocity of v ms-1 at an angle theta from the ground, what is the horizontal range of the object?
# An object is projected at an angle theta from the ground, if the horizontal range of the object is h m, what is the initial velocity of it?
# An object is projected with an initial velocity of v ms-1, if the horizontal range of the object is h m, what is the angle of projection?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
# no_of_samples = 30
g = 9.8

def type1():
    v = random.randint(1,20000)
    theta = random.randint(0,90)
    q = "An object is projected with an initial velocity of "+str(v)+" ms-1 at an angle "+str(theta)+" from the ground, what is the horizontal range of the object?\n"
    range = ((v**2)*math.sin(2*theta*(math.pi/180)))/g
    a = str(round(range,1)) + " m\n"
    return q,a

def type2():
    h = random.randint(1,20000)
    theta = random.randint(1,90)
    q = "An object is projected at an angle "+str(theta)+" from the ground, if the horizontal range of the object is "+str(h)+" m, what is the initial velocity of it?\n"
    v = math.sqrt((h*g)/(math.sin(2*theta*(math.pi/180))))
    a = str(round(v,1)) + " ms-1\n"
    return q,a

def type3():
    v = random.randint(450,850)
    h = random.randint(1,20000)
    q = "An object is projected with an initial velocity of "+str(v)+" ms-1, if the horizontal range of the object is "+str(h)+" m, what is the angle of projection?\n"
    theta = math.asin(g*h/(v**2))*(180/math.pi)
    a = str(round(theta/2))+" or "+ str(round((180-theta)/2))+" degrees w.r.t to ground\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    # print(ques)
    # print(answer)
    qns.write(ques)
    ans.write(answer)
qns.close()
ans.close()