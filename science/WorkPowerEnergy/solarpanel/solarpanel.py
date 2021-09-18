import random

# A family uses p1 kW of power. Direct solar energy is incident on the horizontal surface at an average rate of r W per square meter. If t% of this energy can be converted to useful electrical energy, how large an area is needed to supply p1 kW? 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

def cal1(p1, r, t) :
    return round((p1*t)/(r*100),1)

def type1() :
    p1 = random.randint(1,50)
    r = random.randint(1,400)
    t = random.randint(1,100)
    q = "A family uses " + str(p1) + " kW of power. Direct solar energy is incident on the horizontal surface at an average rate of " + str(r) + " W per square meter. If " + str(t) + " percent of this energy can be converted to useful electrical energy, how large an area is needed to supply " + str(p1) + " kW? \n"
    a = str(cal1(p1, r, t)) + " m2\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
