import random

# An oxygen cylinder of volume 30 litre has an initial gauge pressure of 15 atmosphere and a temperature of 27 °C. After some oxygen is withdrawn from the cylinder, the gauge pressure drops to 11 atmosphere and its temperature drops to 17 °C. Estimate the number of moles of oxygen taken out of the cylinder. (R = 8.3 J mol-1 K-1) 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

r = 8.31

def cal1(v,p1,p2,t1,t2) :
    p1 = p1 * (10**5)
    p2 = p2 * (10**5)
    v = v * (10**-3)
    t1 = t1 + 273
    t2 = t2 + 273
    n1 = (p1*v)/(r*t1)
    n2 = (p2*v)/(r*t2)    
    return round(n1-n2,1) 

def type1() :
    v = random.randint(20,60)
    t1 = random.randint(20,40)
    t2 = random.randint(t1+5,t1+25)
    p1 = random.randint(15,25)
    p2 = random.randint(p1-13,p1-3)
    t = random.randint(1,2)
    if t == 1 :
        q = "An oxygen cylinder of volume " + str(v) + " litre has an initial gauge pressure of " + str(p1) + " atmosphere and a temperature of " + str(t1) + " degree C. After some oxygen is withdrawn from the cylinder, the gauge pressure drops to " + str(p2) + " atmosphere and its temperature drops to " + str(t2) + " degree C. Estimate the number of moles of oxygen taken out of the cylinder. (R = 8.3 J mol-1 K-1)\n"
    else :
        q = "An oxygen cylinder of volume " + str(v) + " litre has an initial gauge pressure of " + str(p1) + " atmosphere and a temperature of " + str(t1) + " degree C. After some oxygen is withdrawn from the cylinder, the gauge pressure drops to " + str(p2) + " atmosphere and its temperature drops to " + str(t2) + " degree C. Estimate the number of moles of oxygen taken out of the cylinder.\n"
    a = str(cal1(v,p1,p2,t1,t2)) + " moles\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
