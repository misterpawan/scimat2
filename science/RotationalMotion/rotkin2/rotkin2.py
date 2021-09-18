import random
import math

# A wheel starting with a initial angular velocity of w1 rad/s is applied with a constant angular acceleration of a rad/s2. What is the angular position of t s ?
# A wheel reaches a angular position of r rad when applied with a constant angular acceleration of a rad/s2 for t s. What is its initial angular velocity velocity ?
# A wheel starting with a initial angular velocity of w1 rad/s reaches a angular position of r rad after t s by the application of constant angular acceleration. What is the angular acceleration applied ?
# A wheel starting with a initial angular velocity of w1 rad/s is applied with a constant angular acceleration of a rad/s2. What is the time taken to reach a angular position of r rad ? 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_r(w1, a, t) :
    return round((w1 * t) + (0.5*a*t*t), 1)

def calculation_w1(r, a, t) :
    return round((r - (0.5*a*t*t))/ t, 1)

def calculation_a(r, w1, t) :
    return round((2*(r - w1*t))/(t*t), 1)
  
def calculation_t(r, w1, a) :
    temp = (4*w1*w1)+(8*a*r)
    return round((-(2*w1) + math.sqrt(temp))/(2*a),1)
    
def type1():
    w1 = random.randint(1,1000)
    a = random.randint(1,100)
    t = random.randint(1,10)
    s = str(calculation_r(w1, a, t)) + " m\n"
    q = "A wheel starting with a initial angular velocity of " + str(w1) + " rad/s is applied with a constant angular acceleration of " + str(a) + " rad/s2. What is the angular position of " + str(t) + " s ?\n"
    return q,s

def type2():
    a = random.randint(1,100)
    t = random.randint(1,10)
    tp = int(0.5*a*t*t)
    r = random.randint(tp,tp+1000)
    w1 = str(calculation_w1(r, a, t)) + " m/s\n"
    q = "A wheel reaches a angular position of " + str(r) + " rad when applied with a constant angular acceleration of " + str(a) + " rad/s2 for " + str(t) + " s. What is its initial angular velocity velocity ?\n"
    return q,w1

def type3():
    w1 = random.randint(1,100)
    t = random.randint(1,10)
    tp = w1*t
    r = random.randint(tp+10,tp+1010)
    a = str(calculation_a(r, w1, t)) + " m/s2\n"
    q = "A wheel starting with a initial angular velocity of " + str(w1) + " rad/s reaches a angular position of " + str(r) + " rad after " + str(t) + " s by the application of constant angular acceleration. What is the angular acceleration applied ?\n"
    return q,a

def type4():
    w1 = random.randint(1,100)
    a = random.randint(1,10)
    r = random.randint(1,1000)
    t = str(calculation_t(r, w1, a)) + " s\n"
    q = "A wheel starting with a initial angular velocity of " + str(w1) + " rad/s is applied with a constant angular acceleration of " + str(a) + " rad/s2. What is the time taken to reach a angular position of " + str(r) + " rad ?\n" 
    return q,t

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