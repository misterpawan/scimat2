import random
import math

# A wheel starting with an initial angular velocity of w1 rad/s accelerates with a constant angular acceleration of a rad/s2 and reaches a velocity of w2 m/s. What is its angular position ?
# A wheel was applied with a constant angular acceleration of a rad/s2 reaches a velocity of w2 rad/s when the angular position is r rad/. What is its initial angular velocity ? 
# A wheel starting with an initial angular velocity of w1 rad/s accelerates with a constant angular acceleration of a rad/s2. If it reaches a angular position of r rad , then what is it’s final velocity ?
# A wheel starting with an initial angular velocity of w1 rad/s accelerates with a constant angular acceleration reaches a final velocity of w2 rad/s when the angular position is r m. What is its acceleration ?


qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_r(w1,w2,a):
  return round(((w2**2 - w1**2)/(2*a)),1)

def calculation_w1(w2,r,a) :
    return round(math.sqrt((w2**2) - (2*a*r)), 1)

def calculation_w2(w1,r,a) :
    return round(math.sqrt((w1**2) + (2*a*r)), 1)

def calculation_a(w1,w2,r) :
    return round((((w2**2) - (w1**2))/(2*r)), 1)
    
def type1():
    w1 = random.randint(1,100)
    w2 = random.randint(w1,w1+100)
    a = random.randint(1,100)
    r = str(calculation_r(w1,w2,a)) + " m\n"
    q = "A wheel starting with an initial angular velocity of " + str(w1) + " rad/s accelerates with a constant angular acceleration of " + str(a) + " rad/s2 and reaches a velocity of " + str(w2) + " m/s. What is its angular position ?\n"
    return q,r

def type2():
    r = random.randint(1,100)
    a = random.randint(0,100)
    tmp = 2*a*r
    w2 = random.randint(int(tmp),int(tmp)+100)
    w1 = str(calculation_w1(w2,r,a)) + " m/s\n"
    q = "A wheel was applied with a constant angular acceleration of " + str(a) + " rad/s2 reaches a velocity of " + str(w2) + " rad/s when the angular position is " + str(r) + " rad. What is its initial angular velocity ?\n"
    return q,w1

def type3():
    r = random.randint(1,100)
    a = random.randint(0,100)
    w1 = random.randint(0,200)
    w2 = str(calculation_w2(w1,r,a)) + " m/s\n"
    q = "A wheel starting with an initial angular velocity of " + str(w1) + " rad/s accelerates with a constant angular acceleration of " + str(a) + " rad/s2. If it reaches a angular position of " + str(r) + " rad , then what is it’s final velocity ?\n"
    return q,w2

def type4():
    r = random.randint(1,100)
    w1 = random.randint(0,100)
    w2 = random.randint(w1,w1+100)
    a = str(calculation_a(w1,w2,r)) + " m/s2\n"
    q = "A wheel starting with an initial angular velocity of " + str(w1) + " rad/s accelerates with a constant angular acceleration reaches a final velocity of " + str(w2) + " rad/s when the angular position is " + str(r) + " rad. What is its acceleration ?\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3:
        ques,answer = type4() 
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()