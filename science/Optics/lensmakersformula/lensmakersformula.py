import random

# A double convex lens has radius of curvatres r1 cm and r2 cm is made of material having refractive index mu. What is the focal length of the lens.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(r1, r2, mu) :
    m = (mu-1)*((r2-r1)/r1*r2)
    return round(1/m,2)

def type1() :
    r1 = random.randint(1,100)
    r2 = random.randint(1,100)
    mu = random.randint(101,200)
    mu = round(mu/100,2)
    q = "A double convex lens has radius of curvatres " + str(r1) + " cm and " + str(r2) + " cm is made of material having refractive index " + str(mu) + ". What is the focal length of the lens.\n"
    e = str(cal1(r1, -1*r2, mu)) + " cm\n"
    return q,e

def type2() :
    r1 = random.randint(1,100)
    r2 = random.randint(1,100)
    mu = random.randint(101,200)
    mu = round(mu/100,2)
    q = "A double concave lens has radius of curvatres " + str(r1) + " cm and " + str(r2) + " cm is made of material having refractive index " + str(mu) + ". What is the focal length of the lens.\n"
    e = str(cal1(-1*r1, r2, mu)) + " cm\n"
    return q,e

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
