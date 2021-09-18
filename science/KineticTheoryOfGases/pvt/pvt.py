import random

# An air bubble of volume v cm3 rises from the bottom of a lake h m deep at a temperature of t1 degree C. To what volume does it grow when it reaches the surface, which is at a temperature of 35 °C.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(v,h,t1,t2) :
    p1 = (10**5) + (1000*9.8*h)
    p2 = (10**5)
    t1 = t1 + 273
    t2 = t2 + 273
    return round((p1*v*t2)/(t1*p2),1) 

def type1() :
    v = random.randint(10,110)
    t1 = random.randint(5,25)
    t2 = random.randint(t1+10,t1+20)
    h = random.randint(10,310)
    t = random.randint(1,2)
    if t == 1 :
        q = "An air bubble of volume " + str(v) + " cm3 rises from the bottom of a lake " + str(h) + " m deep at a temperature of " + str(t1) + " degree C. To what volume does it grow when it reaches the surface, which is at a temperature of " + str(t2) + " degree C. (g = 9.8 m/s and atmospheric pressure = 10^5 N/m2)\n"
    else :
        q = "An air bubble of volume " + str(v) + " cm3 rises from the bottom of a lake " + str(h) + " m deep at a temperature of " + str(t1) + " degree C. To what volume does it grow when it reaches the surface, which is at a temperature of " + str(t2) + " degree C.\n"
    a = str(cal1(v,h,t1,t2)) + " cm3\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
