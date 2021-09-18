import random

# To maintain a rotor at a uniform angular speed of w rad s-1, an engine needs to transmit a torque of t Nm. What is the power required by the engine?
# To maintain a rotor at a uniform angular speed of w rad s-1, an engine required a power of p W. What is the torque transmitted by the engine?
# Torque of t Nm is transmitted to a engine at a power of p W. What is the angular speed of the rotor.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000

def cal1(w, t) :
    return w*t

def cal2(w,p) :
    return round(p/w,1)

def cal3(t,p) :
    return round(p/t,1)

def type1() :
    w = random.randint(1,1000)
    t = random.randint(1,1000)
    q = "To maintain a rotor at a uniform angular speed of " + str(w) + " rad s-1, an engine needs to transmit a torque of "+ str(t) + " Nm. What is the power required by the engine?\n"
    a = str(cal1(w, t)) + "watts\n"
    return q,a

def type2() :
    w = random.randint(1,1000)
    p = random.randint(1,1000)
    q = "To maintain a rotor at a uniform angular speed of " + str(w) + " rad s-1, an engine required a power of " + str(p) + " W. What is the torque trabsmitted by the engine?\n"
    a = str(cal2(w, p)) + "newtonm\n"
    return q,a

def type3() :
    t = random.randint(1,1000)
    p = random.randint(1,1000)
    q = "Torque of " + str(t) + " Nm is transmitted to a engine at a power of " + str(p) + " W. What is the angular speed of the rotor.\n"
    a = str(cal3(t, p)) + "rads-1\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1 :
        ques, answer = type1()
    elif types == 3 :
        ques, answer = type3()
    else :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
