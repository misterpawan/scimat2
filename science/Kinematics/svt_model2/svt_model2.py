import random

# v = 2*pi*r/t 

# If an artifical satellite moving with a speed of v m/s in a circular orbit takes t s to complete
# a rotation, then what is the radius of it's orbit?

# If an artificial satellite is moving in a circular orbit of radius r m,
# then calculate its speed if it takes t s to complete a rotation?

# If an artificial satellite moving with a speed of v m/s in a circular orbit 
# of radius r m,Calculate time taken by it to complete a rotation?

s_to_r = 2 * (3.14)
qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_r(v, t): 
    return round((v * t) / s_to_r, 1)

def calculation_v(r, t):
    return round((s_to_r * r) / t, 1)

def calculation_t(r, v):
    return round((s_to_r * r ) / v,1)

def type1():
    v = random.randint(1,1000)
    t = random.randint(1,1000)
    r = str(calculation_r(v,t)) + " m\n"
    q = "If an artifical satellite moving with a speed of " + str(v) + " m/s in a circular orbit takes " + str(t) + " s to complete a rotation, then what is the radius of it's orbit?\n"
    return q,r

def type2():
    r = random.randint(1100 , 2100)
    t = random.randint(1,1000)
    v = str(calculation_v(r,t)) + " m/s\n"
    q = "If an artificial satellite is moving in a circular orbit of radius " + str(r) + " m,then calculate its speed if it takes " + str(t) + " s to complete a rotation?\n"
    return q,v

def type3():
    r = random.randint(1100,2100)
    v = random.randint(1,1000)
    t = str(calculation_t(r,v)) + " s\n"
    q = "If an artificial satellite moving with a speed of " + str(v) + " m/s  in a circular orbit of radius " + str(r) + " m,Calculate time taken by it to complete a rotation?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
