import random

#A stone is thrown vertically upward with a velocity of u m/s. What is the time taken by it to reach the maximum height?
#A stone is thrown vertically upward reaches a maximum height after t s. With what velocity it is thrown up ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

def calculation_u(a,t):
    return round((a*t),1)
def calculation_t(u,a):
    return round(u / a,1)


def type1():
    u = random.randint(0,1000000)
    a = 9.8
    t = str(calculation_t(u,a)) + " s\n"
    q = "A stone is thrown vertically upward with a velocity of " + str(u) + " m/s. What is the time taken by it to reach the maximum height ?\n"
    return q,t

def type2():
    a = 9.8
    t = random.randint(0,1000000)
    u = str(calculation_u(a,t)) + " m/s\n"
    q = "A stone is thrown vertically upward reaches a maximum height after " + str(t) + " s. With what initial velocity it is thrown up ?\n"
    return q,u

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        ques,answer = type1()
    if types == 2:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
