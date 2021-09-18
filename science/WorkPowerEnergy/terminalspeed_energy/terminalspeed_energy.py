import random

#  A raindrop of radius r mm falls from a height of h m above the ground. It falls with decreasing acceleration (due to viscous resistance of the air) until at half its original height, it attains its maximum (terminal) speed, and moves with uniform speed thereafter. What is the work done by the gravitational force on the drop in the first and second half of its journey? 
#  A raindrop of radius r mm falls from a height of h m above the ground. It falls with decreasing acceleration (due to viscous resistance of the air) until at half its original height, it attains its maximum (terminal) speed, and moves with uniform speed thereafter. What is the work done by the resistive force in the entire journey if its speed on reaching the ground is v ms-1?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
g = 9.8
d = 1000
pi = 3.14

def cal1(r, h) :
    m = (4/3)*(pi)*(r**3)*d
    return round((m*g*h)/2,1)

def cal2(r, h, v) :
    m = (4/3)*(pi)*(r**3)*d
    w1 = (m*g*h)/2
    w2 = 0.5*m*v*v
    return round(w1-w2,1)

def type1() :
    r = random.randint(1,1000)
    h = random.randint(1,1000)
    q = "A raindrop of radius " + str(r) + " mm falls from a height of " + str(h) + " m above the ground. It falls with decreasing acceleration until at half its original height, it attains its maximum (terminal) speed, and moves with uniform speed thereafter. What is the work done by the gravitational force on the drop in the first and second half of its journey? \n"
    r = r * 10**-3
    e = str(cal1(r, h)) + " joules\n"
    return q,e

def type2() :
    r = random.randint(1,100)
    h = random.randint(1,500)
    v = random.randint(1,100)
    q = "A raindrop of radius " + str(r) + " mm falls from a height of " + str(h) + " m above the ground. It falls with decreasing acceleration until at half its original height, it attains its maximum (terminal) speed, and moves with uniform speed thereafter. What is the work done by the resistive force in the entire journey if its speed on reaching the ground is " + str(v) + " ms-1?\n"
    r = r * 10**-3
    e = str(cal2(r, h, v)) + " joules\n"
    return q,e

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
