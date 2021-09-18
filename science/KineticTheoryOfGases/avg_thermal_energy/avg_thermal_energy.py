import random

# Estimate the average thermal energy of a helium atom at t1 degree C.
# Estimate the average thermal energy of a helium atom at t1 degree k

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000

k = 1.38 * (10**-23)

def cal1(t1) :
    t1 = t1 + 273   
    return (1.5*k*t1) 

def cal2(t1) :   
    return (1.5*k*t1) 

def type1() :
    t1 = random.randint(1,100000)
    t = random.randint(1,2)
    if t == 1 :
        q = "Estimate the average thermal energy of a helium atom at " + str(t1) + " degree C. (k = 1.38 x 10^-23)\n"
    else :
        q = "Estimate the average thermal energy of a helium atom at " + str(t1) + " degree C.\n"
    a = "{:.1e}".format(cal1(t1)) + "\n"
    return q,a

def type2() :
    t1 = random.randint(1,100000)
    t = random.randint(1,2)
    if t == 1 :
        q = "Estimate the average thermal energy of a helium atom at " + str(t1) + " degree K. (k = 1.38 x 10^-23)\n"
    else :
        q = "Estimate the average thermal energy of a helium atom at " + str(t1) + " degree K.\n"
    a = "{:.1e}".format(cal2(t1)) + "\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    else :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
