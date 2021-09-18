import random


# A body is dropped from a tower with an initial velocity of u m/s, reaches the ground with a velocity of v m/s under gravity.
# What is the time taken by the body to reach the ground ?

# A body is dropped from a tower with a certain initial velocity reaches the ground with a velocity of v m/s after t s.
# What is it's initial velocity ?

# A body is dropped from a tower with a initil velociy of u m/s reaches the ground after t s.
# With what velocity it reaches the ground ?



# path = './dataset'
# os.mkdir(path)

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_v(u,a,t):
    return round(u + (a*t),1)
def calculation_u(v,a,t):
    return round(v - (a*t),1)
def calculation_t(u,v,a):
    return round((v - u) / a,1)


def type1():
    u = random.randint(0,4000)
    # u = u/10.0
    a = 9.8
    t = random.randint(1,300)
    v = str(calculation_v(u,a,t)) + " m/s\n"
    q = "A body is dropped from a tower with a initil velociy of " + str(u) + " m/s reaches the ground after " + str(t) + " s. With what velocity it reaches the ground ?\n"
    return q,v

def type2():
    a = 9.8
    t = random.randint(1,300)
    v = random.randint(int(a*t),int(a*t)+4000)
    # v = v/10.0
    u = str(calculation_u(v,a,t)) + " m/s\n"
    q = "A body is dropped from a tower with a certain initial velocity reaches the ground with a velocity of " + str(v) + " m/s after " + str(t) + " s. What is it's initial velocity ?\n"
    return q,u

def type3():
    u = random.randint(0,1000)
    v = random.randint(u,u+1000)
    a = 9.8
    t = str(calculation_t(u,v,a)) + " s\n"
    q = "A body is dropped from a tower with an initial velocity of " + str(u) + " m/s, reaches the ground with a velocity of " + str(v) + " m/s under gravity. What is the time taken by the body to reach the ground ?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        ques,answer = type1()
    if types == 2:
        ques,answer = type2()
    if types == 3:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
