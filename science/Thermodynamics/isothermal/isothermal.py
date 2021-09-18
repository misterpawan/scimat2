import random

# If a monoatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to volume v2 lit, then what will be the pressure.
# If a diatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to volume v2 lit, then what will be the pressure.
# If a monoatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to pressure p1 atm, then what will be its volume.
# If a diatomic gas of n moles at p1 atm and volume v1 lit is isothermally changed to pressure p1 atm, then what will be its volume.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2000000

r = 8.31

def cal1(g,v1,v2,p1) :
    return round((p1*(v1**g))/(v2**g),1)

def cal2(g,p1,p2,v1) : 
    return round(((p1*(v1**g))/p2)**(1/g),1) 

def type1() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    v2 = random.randint(10,200)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to volume " + str(v2) + " lit, then what will be the pressure.\n"
    a = str(cal1(1,v1,v2,p1)) + "atm\n"
    return q,a

def type2() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    v2 = random.randint(10,200)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to volume " + str(v2) + " lit, then what will be the pressure.\n"
    a = str(cal1(1,v1,v2,p1)) + "atm\n"
    return q,a

def type3() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    p2 = random.randint(10,200)
    q = "If a monoatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to pressure " + str(p2) + " atm, then what will be its volume.\n"
    a = str(cal2(1,p1,p2,v1)) + "lit\n"
    return q,a

def type4() :
    n = random.randint(1,10)
    p1 = random.randint(10,200)
    v1 = random.randint(10,200)
    p2 = random.randint(10,200)
    q = "If a diatomic gas of " + str(n) + " moles at " + str(p1) + " atm and volume " + str(v1) + " lit is isothermally changed to pressure " + str(p2) + " atm, then what will be its volume.\n"
    a = str(cal2(1,p1,p2,v1)) + "lit\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    elif types == 3 :
        ques, answer = type3()
    elif types == 4 :
        ques, answer = type4()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
