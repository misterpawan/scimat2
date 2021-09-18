import random

# A signal from a spaceship reached the ground station in t s,then 
# What was the distance of the spaceship from the ground station?{signal travels with speed of light}

# Distance of a spaceship from the ground station is s m,then in what time 
# will a signal from ground station will reach the spaceship{signal travels with speed of light}

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
speed_of_light = 300000000

def calculation_s(t): 
    return round((speed_of_light * t)/1000, 1)

def calculation_t(s):
    return round(s / speed_of_light, 5)

def type1():
    t = random.randint(1,1000000) / 1000000
    s = str(calculation_s(t)) + " km\n"
    q = "A signal from a spaceship reached the ground station in " + str(round(t*1000,1)) + " ms,then what was the distance of the spaceship from the ground station?{signal travels with speed of light}?\n"
    return q,s

def type2():
    s = random.randint(int(speed_of_light/10000) ,int(speed_of_light))
    t = str(round(calculation_t(s)*1000,1)) + " ms\n"
    q = "Distance of a spaceship from the ground station is " + str(round(s/1000,1)) + " km,then in what time will a signal from ground station will reach the spaceship{signal travels with speed of light}?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
