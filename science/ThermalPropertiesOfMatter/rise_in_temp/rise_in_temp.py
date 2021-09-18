import random

# A P kW drilling machine is used to drill a bore in a small aluminium block of mass m kg. How much is the rise in temperature of the block in t minutes, assuming p% of power is used up in heating the machine itself or lost to the surroundings? Specific heat of aluminium = 0.91 J g-1 K-1 .
# A P kW drilling machine is used to drill a bore in a small copper block of mass m kg. How much is the rise in temperature of the block in t minutes, assuming p% of power is used up in heating the machine itself or lost to the surroundings? Specific heat of copper = 0.39 J g-1 K-1 .

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(P, m, p, s, t) :
    return round((p*P*t)/(m*s),1)

def type1() :
    m = random.randint(1,20)
    P = random.randint(1,100)
    p = random.randint(10,60)
    t = random.randint(1,10)
    t1 = random.randint(1,2)
    if t1 == 1 :
        q = "A " + str(P) + " kW drilling machine is used to drill a bore in a small aluminium block of mass " + str(m) + " kg. How much is the rise in temperature of the block in " + str(t) + " minutes, assuming " + str(p) + " percent of power is used up in heating the machine itself or lost to the surroundings? Specific heat of aluminium = 0.91 J g-1 K-1 .\n"
    else :
        q = "A " + str(P) + " kW drilling machine is used to drill a bore in a small copper block of mass " + str(m) + " kg. How much is the rise in temperature of the block in " + str(t) + " minutes, assuming " + str(p) + " percent of power is used up in heating the machine itself or lost to the surroundings? Specific heat of copper = 0.39 J g-1 K-1 .\n"
    t = t * 60
    P = P * 1000
    p = p/100
    m = m * 1000
    if t1 == 1 :
        w = str(cal1(P, m, p, 0.91, t)) + " degrees c\n"
    elif t1 == 2 :
        w = str(cal1(P, m, p, 0.39, t)) + " degrees c\n"
    return q,w

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
