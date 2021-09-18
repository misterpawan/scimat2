import random
import math

# Gas A has a molar mass of m1 g/mol and gas B has a molar mass of m2 g/mol. If diffusion rate of gas A is d1 cm3/sec, what is the diffusion rate of gas B.
# Gas A has a molar mass of m1 g/mol and gas B has a molar mass of m2 g/mol. If diffusion rate of gas B is d1 cm3/sec, what is the diffusion rate of gas A.
# Gas A has a diffusion rate of d1 cm3/sec and gas B has a diffusion rate of d2 cm3/sec. If molar mass of gas A is m1 g/mol, what is the molar mass of gas B.
# Gas A has a diffusion rate of d1 cm3/sec and gas B has a diffusion rate of d2 cm3/sec. If molar mass of gas B is m1 g/mol, what is the molar mass of gas A.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2000000

r = 8.31

def cal1(m1,m2,d1) :
    return round((d1*math.sqrt(m1))/math.sqrt(m2),1)

def cal2(d1,d2,m1) : 
    return round((d1*math.sqrt(m1))/d2,1) 

def type1() :
    d1 = random.randint(10,200)
    m1 = random.randint(1,300)
    m2 = random.randint(1,300)
    q = "Gas A has a molar mass of " + str(m1) + " g/mol and gas B has a molar mass of " + str(m2) + " g/mol. If diffusion rate of gas A is " + str(d1) + " cm3/sec, what is the diffusion rate of gas B.\n"
    a = str(cal1(m1,m2,d1)) + "cm3/sec\n"
    return q,a

def type2() :
    d2 = random.randint(10,200)
    m1 = random.randint(1,300)
    m2 = random.randint(1,300)
    q = "Gas A has a molar mass of " + str(m1) + " g/mol and gas B has a molar mass of " + str(m2) + " g/mol. If diffusion rate of gas B is " + str(d2) + " cm3/sec, what is the diffusion rate of gas A.\n"
    a = str(cal1(m2,m1,d2)) + "cm3/sec\n"
    return q,a

def type3() :
    d1 = random.randint(10,200)
    d2 = random.randint(10,200)
    m1 = random.randint(1,300)
    q = "Gas A has a diffusion rate of " + str(d1) + " cm3/sec and gas B has a diffusion rate of " + str(d2) + " cm3/sec. If molar mass of gas A is " + str(m1) + " g/mol, what is the molar mass of gas B.\n"
    a = str(cal2(d1,d2,m1)) + "g/mol\n"
    return q,a

def type4() :
    d1 = random.randint(10,200)
    d2 = random.randint(10,200)
    m2 = random.randint(1,300)
    q = "Gas A has a diffusion rate of " + str(d1) + " cm3/sec and gas B has a diffusion rate of " + str(d2) + " cm3/sec. If molar mass of gas B is " + str(m2) + " g/mol, what is the molar mass of gas A.\n"
    a = str(cal1(d2,d1,m2)) + "g/mol\n"
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
