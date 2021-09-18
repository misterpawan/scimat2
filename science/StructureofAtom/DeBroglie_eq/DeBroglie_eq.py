import random


# The mass of a particle is m × 10-31 kg. If its velocity is v m/s, calculate its wavelength.
# A particle has a velocity of v m/s and wavelength w A. Find its mass.
# The mass of a particle is 9.1 × 10-31 kg. If its wavelength is w A, calculate its velocity.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000
h = 6.6 * (10**-34)

def cal1(m, v) :
   return round(h/m*v,2)

def cal2(v, w) :
    return round(h/v*w,2)

def cal3(m, w) :
    return round(h/m*w,2)

def type1() :
    v = random.randint(1,10000)
    m = random.randint(1,1000)
    m = m * 10**-31
    q = "The mass of a particle is " + str(m) + " kg. If its velocity is " + str(v) + " m/s, calculate its wavelength.\n"
    w = str(cal1(m, v)) + "m\n"
    return q,w

def type2() :
    w = random.randint(1,10000)
    v = random.randint(1,10000)
    w = w * 10**-10
    q = "A particle has a velocity of " + str(v) + " m/s and wavelength " + str(w) + " A. Find its mass.\n"
    m = str(cal2(v, w)) + "kg\n"
    return q,m

def type3() :
    w = random.randint(1,10000)
    m = random.randint(1,1000)
    m = m * 10**-31
    w = w * 10**-10
    q = "The mass of a particle is " + str(m) + " kg. If its wavelength is " + str(w) + " A, calculate its velocity.\n"
    v = str(cal3(m, w)) + "m/s\n"
    return q,v

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1 :
        ques,answer = type1()
    elif types == 2 :
        ques,answer = type2()
    elif types == 3 :
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
