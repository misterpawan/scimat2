import random

# A metre stick is balanced on a knife edge at its centre. When two coins, each of mass m1 g and m2 g respectively are put at the t1 mark and t2 mark respectively, the stick is found to be balanced at t3 cm. What is the mass of the metre stick ?
# A metre stick is balanced on a knife edge at its centre. When a coin of mass m1 g is put at the t1 mark, the stick is found to be balanced at t2 cm. What is the mass of the metre stick ?
# A metre stick of mass m g is balanced on a knife edge at its centre. When a coin of is put at the t1 mark, the stick is found to be balanced at t2 cm. What is the mass of the metre stick ?
# A metre stick of mass m g is balanced on a knife edge at its centre. Where the stick will be balanced when a coin of mass m1 g is put at t1 mark ?
# A metre stick is balanced on a knife edge at its centre. Where the stick will be balanced , when two coins, each of mass m1 g and m2 g respectively are put at the t1 mark and t2 mark respectively ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 3500000 

def cal(m1, m2, t1, t2, t3) :
    ls = m1*(t3-t1)
    rs = m2*(t2-t3)
    if t3 > 50 :
        res = round((rs - ls)/(t3-50),1)
    elif t3 < 50:
        res = round((ls - rs)/(50-t3),1)
    else :
        return "can not be determined"  
    return res

def cal2(m, t, t1) :
    ls = m*(t1-t)
    return round(ls/(50-t1),1)

def cal3(m, t, t1) :
    rs = m*(t-t1)
    return round(rs/(t1-50),1)

def cal4(m, t, t1) :
    ls = m*(50-t1)
    return round(ls/(t1-t),1)

def cal5(m, t, t1) :
    rs = m*(t1-50)
    return round(rs/(t-t1),1)

def cal6(m, m1, t1) : 
    return round(((50*m)+(m1*t1))/(m+m1),1)

def cal7(m, m1, m2, t1, t2) :
    return round(((50*m)+(m1*t1)+(m2*t2))/(m+m1+m2),1)

def type1() :
    m1 = random.randint(1,100)
    m2 = random.randint(1,100)
    t1 = random.randint(1,48)
    t2 = random.randint(52,100)
    if m1*(50-t1) > m2*(t2-50) : 
        t3 = random.randint(t1+1,49)
    elif m1*(50-t1) > m2*(t2-50) :
        t3 = random.randint(51,t2-1)
    else :
        t3 = 50 
    q = "A metre stick is balanced on a knife edge at its centre. When two coins, each of mass " + str(m1) + " g and " + str(m2) + " g respectively are put at the " + str(t1) + " mark and " + str(t2) + " mark respectively, the stick is found to be balanced at " + str(t3) + " cm. What is the mass of the metre stick ?\n"
    a = cal(m1, m2, t1, t2, t3)
    if a == "can not be determined" :
        a = str(a) + "\n"
    else :
        a = str(a) + " g\n"
    return q,a

def type2() :
    temp = random.randint(1,2)
    if temp == 1 :
        m1 = random.randint(1,1000)
        t1 = random.randint(1,48)
        t2 = random.randint(t1+1,49)
        q = "A metre stick is balanced on a knife edge at its centre. When a coin of mass " + str(m1) + " g is put at the " + str(t1) + " mark, the stick is found to be balanced at " + str(t2) + " cm. What is the mass of the metre stick ?\n"
        a = str(cal2(m1, t1, t2)) + "g\n"
    else :
        m1 = random.randint(1,1000)
        t1 = random.randint(52,100)
        t2 = random.randint(51,t1-1)
        q = "A metre stick is balanced on a knife edge at its centre. When a coin of mass " + str(m1) + " g is put at the " + str(t1) + " mark, the stick is found to be balanced at " + str(t2) + " cm. What is the mass of the metre stick ?\n"
        a = str(cal3(m1, t1, t2)) + "g\n"
    return q,a

def type3() :
    temp = random.randint(1,2)
    if temp == 1 :
        m = random.randint(1,1000)
        t1 = random.randint(1,48)
        t2 = random.randint(t1+1,49)
        q = "A metre stick of mass " + str(m) + " g is balanced on a knife edge at its centre. When a coin is put at the " + str(t1) + " mark, the stick is found to be balanced at " + str(t2) + " cm. What is the mass of the metre stick ?\n"
        a = str(cal4(m, t1, t2)) + "g\n"
    else :
        m = random.randint(1,1000)
        t1 = random.randint(52,100)
        t2 = random.randint(51,t1-1)
        q = "A metre stick of mass " + str(m) + " g is balanced on a knife edge at its centre. When a coin is put at the " + str(t1) + " mark, the stick is found to be balanced at " + str(t2) + " cm. What is the mass of the metre stick ?\n"
        a = str(cal5(m, t1, t2)) + "g\n"
    return q,a

def type4() :
    temp = random.randint(1,2)
    if temp == 1 :
        m = random.randint(1,100)
        m1 = random.randint(1,100)
        t1 = random.randint(1,48)
        q = "A metre stick of mass " + str(m) + " g is balanced on a knife edge at its centre. Where the stick will be balanced when a coin of mass " + str(m1) + " g is put at " + str(t1) + " mark ?\n"
        a = str(cal6(m, m1, t1)) + "cm\n"
    elif temp == 2 :
        m = random.randint(1,100)
        m1 = random.randint(1,100)
        t1 = random.randint(52,100)
        q = "A metre stick of mass " + str(m) + " g is balanced on a knife edge at its centre. Where the stick will be balanced when a coin of mass " + str(m1) + " g is put at " + str(t1) + " mark ?\n"
        a = str(cal6(m, m1, t1)) + "cm\n"
    return q,a

def type5() :
    m = random.randint(1,100)
    m1 = random.randint(1,100)
    m2 = random.randint(1,100)
    t1 = random.randint(1,48)
    t2 = random.randint(52,100)
    q = "A metre stick of mass " + str(m) + " g is balanced on a knife edge at its centre. Where the stick will be balanced , when two coins, each of mass " + str(m1) + " g and " + str(m2) + " g respectively are put at the " + str(t1) + " mark and " + str(t2) + " mark respectively ?\n"
    a = str(cal7(m, m1, m2, t1, t2)) + "cm\n"
    return q,a

for i in range(no_of_samples) : 
    types = random.randint(1,5)
    if types == 1 :   
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    elif types == 3 :
        ques, answer = type3()
    elif types == 4 :
        ques, answer = type4()
    elif types == 5 :
        ques, answer = type5()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
