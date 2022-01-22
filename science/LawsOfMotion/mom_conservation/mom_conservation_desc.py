import random

# m_b * v_b = m_r * v*r
# From a rifle of mass 4 g, a bullet of mass 50 g is fired with a velocity of 35 m/s, then calculate the recoil velocity of the rifle(in m/s)?
# From a rifle, a bullet of mass 50 g is fired with a velocity of 35 m/s, if the recoil velocity of rifle is v m/s, then calculate mass of the rifle(in grams)?
# From a rifle of mass 4 g, a bullet of mass 50 g is fired, if the recoil velocity of rifle is v m/s, then calculate velocity of bullet(in m/s)?
# From a rifle of mass 4 g, a bullet is fired with a velocity of 35 m/s, if the recoil velocity of rifle is v m/s, then calculate mass of the bullet(in grams)? 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000

def type1():
    m_b = random.randint(1,100)
    m_r = (random.randint(1,100))* 100
    v_b = random.randint(900,1000)
    v_r = "from law of conservation of linear momoentum we have m_b x v_b = m_r x v_r => v_r = (m_b x v_b)/m_r => v_r = (" + str(m_b) + " x " + str(v_b) + ")/" + str(m_r) + " => v_r = " + str(round(((m_b*v_b)/m_r),1)) + " m/s\n"
    q = "From a rifle of mass " + str(m_r) + " g, a bullet of mass " + str(m_b) + " g is fired with a velocity of " + str(v_b) + " m/s, then calculate the recoil velocity of the rifle(in m/s) ?\n"
    return q,v_r

def type2():
    m_b = random.randint(1,100)
    v_b = random.randint(900,1000)
    v_r = round(random.randint(900,1000) / 100 , 2)
    m_r = "from law of conservation of linear momoentum we have m_b x v_b = m_r x v_r => m_r = (m_b x v_b)/v_r => m_r = (" + str(m_b) + " x " + str(v_b) + ")/" + str(v_r) + " => m_r = " + str(round(((m_b*v_b)/v_r),1)) + " g\n"
    q = "From a rifle, a bullet of mass " + str(m_b) + " g is fired with a velocity of " + str(v_b) + " m/s, if the recoil velocity of rifle is " + str(v_r) + " m/s, then calculate mass of the rifle(in grams) ?\n"
    return q,m_r

def type3():
    m_b = random.randint(1,100)
    m_r = (random.randint(1,100))* 100
    v_r = round(random.randint(900,1000) /100 , 2)
    v_b = "from law of conservation of linear momoentum we have m_b x v_b = m_r x v_r => v_b = (m_r x v_r)/m_b => v_b = (" + str(m_r) + " x " + str(v_r) + ")/" + str(m_b) + " => v_b = " + str(round(((m_r*v_r)/m_b),1)) + " m/s\n"
    q = "From a rifle of mass " + str(m_r) + " g, a bullet of mass " + str(m_b) + " g is fired, if the recoil velocity of rifle is " + str(v_r) + " m/s, then calculate velocity of bullet(in m/s) ?\n"
    return q,v_b

def type4():
    m_r = (random.randint(1,100)) *100
    v_b = random.randint(900,1000)
    v_r = round(random.randint(900,1000) / 100 , 2)
    m_b = "from law of conservation of linear momoentum we have m_b x v_b = m_r x v_r => m_b = (m_r x v_r)/v_b => m_b = (" + str(m_r) + " x " + str(v_r) + ")/" + str(v_b) + " => m_b = " + str(round(((m_r*v_r)/v_b),1)) + " g\n"
    q = "From a rifle of mass " + str(m_r) + " g, a bullet is fired with a velocity of " + str(v_b) + " m/s, if the recoil velocity of rifle is " + str(v_r) + " m/s, then calculate mass of the bullet(in grams) ?\n"
    return q,m_b

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    if types == 3:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
