import random

# If a car has initial velocity of 1 m/s and has a constant acceleration of 0.1 m/s2 for 20 s,
#  then what is the final velocity of the car?

# If a car attains a velocity of 10 m/s by applying a constant acceleration of 0.1 m/s2 for 20s,
# then what is the initial velocity of the car?

# If a car has initial velocity of 1 m/s and attains a velocity of 10 m/s in 20s ,
# then what is the acceleration of the car?

# If a car has initial velocity of 1 m/s and has a constant acceleration of 0.1 m/s2,
# then what is the time taken by the car to attain a velocity of 10 m/s?

# path = './dataset'
# os.mkdir(path)

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_v(u,a,t):
    return round(u + (a*t),1)
def calculation_u(v,a,t):
    return round(v - (a*t),1)
def calculation_a(u,v,t):
    return round((v - u) / t,1)
def calculation_t(u,v,a):
    return round((v - u) / a,1)


def type1():
    u = random.randint(0,1000)
    a = random.randint(0,40)
    t = random.randint(1,40)
    v = str(calculation_v(u,a,t)) + " m/s\n"
    q = "If a car has initial velocity of " +str(u) + " m/s and has a constant acceleration of " + str(a) + " m/s2 for " + str(t) + " s,then what is the final velocity of the car?\n"
    return q,v

def type2():
    a = random.randint(0,40)
    t = random.randint(1,40)
    v = random.randint(a*t,(a*t)+1000)
    u = str(calculation_u(v,a,t)) + " m/s\n"
    q = "If a car attains a velocity of " +str(v) + " m/s by applying a constant acceleration of " + str(a) + " m/s2 for " + str(t) + " s, then what is the initial velocity of the car?\n"
    return q,u

def type3():
    u = random.randint(0,500)
    v = random.randint(u,u+500)
    t = random.randint(1,20)
    a = str(calculation_a(u,v,t)) + " m/s2\n"
    q = "If a car has initial velocity of " +str(u)+ " m/s and attains a velocity of " + str(v) + " m/s in " + str(t) + " s ,then what is the acceleration of the car?\n"
    return q,a

def type4():
    u = random.randint(0,500)
    v = random.randint(u,u+500)
    a = random.randint(1,20)
    t = str(calculation_t(u,v,a)) + " s\n"
    q = "If a car has initial velocity of " + str(u) + " m/s and has a constant acceleration of " + str(a) + " m/s2,then what is the time taken by the car to attain a velocity of " + str(v) + " m/s?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1:
        ques,answer = type1()
    if types == 2:
        ques,answer = type2()
    if types == 3:
        ques,answer = type3()
    if types == 4:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
