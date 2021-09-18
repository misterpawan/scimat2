import random

# A large steel wheel is to befitted on to a shaft of the same material. At t1 degree C, the outer diameter of the shaft is d1 cm and the diameter of the central hole in the wheel is, d2 cm. The shaft is cooled using ‘dry ice’. At what temperature of the shaft does the wheel slip on the shaft ? Assume coefficient of linear expansion of the steel to be constant over the required temperature range αsteel= 1.20 x 10-5K-1. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000

def cal1(t1,d1,d2,a) :
    return round(t1-((d2-d1)/(a*d1)),1) 

def type1() :
    t1 = random.randint(10,210)
    d1 = random.randint(10,210)
    d2 = random.randint(1,20)
    d2 = round(d2/1000,3)
    d2 = d1 - d2
    a = 1.2 * 10**-5
    q = "A large steel wheel is to befitted on to a shaft of the same material. At " + str(t1) + " degree C, the outer diameter of the shaft is " + str(d1) + " cm and the diameter of the central hole in the wheel is, " + str(d2) + " cm. The shaft is cooled using ‘dry ice’. At what temperature of the shaft does the wheel slip on the shaft ? Assume coefficient of linear expansion of the steel to be constant over the required temperature range αsteel= 1.2 x 10-5K-1.\n"
    a = str(cal1(t1,d1,d2,a)) + " degree c\n"
    return q,a

def type2() :
    t1 = random.randint(10,210)
    d1 = random.randint(10,210)
    d2 = random.randint(1,20)
    d2 = round(d2/1000,3)
    d2 = d1 - d2
    a = 2 * 10**-5
    q = "A large brass wheel is to befitted on to a shaft of the same material. At " + str(t1) + " degree C, the outer diameter of the shaft is " + str(d1) + " cm and the diameter of the central hole in the wheel is, " + str(d2) + " cm. The shaft is cooled using ‘dry ice’. At what temperature of the shaft does the wheel slip on the shaft ? Assume coefficient of linear expansion of the brass to be constant over the required temperature range αbrass= 2 x 10-5K-1.\n"
    a = str(cal1(t1,d1,d2,a)) + " degree c\n"
    return q,a

def type3() :
    t1 = random.randint(10,210)
    d1 = random.randint(10,210)
    d2 = random.randint(1,20)
    d2 = round(d2/1000,3)
    d2 = d1 - d2
    a = 1.7 * 10**-5
    q = "A large copper wheel is to befitted on to a shaft of the same material. At " + str(t1) + " degree C, the outer diameter of the shaft is " + str(d1) + " cm and the diameter of the central hole in the wheel is, " + str(d2) + " cm. The shaft is cooled using ‘dry ice’. At what temperature of the shaft does the wheel slip on the shaft ? Assume coefficient of linear expansion of the copper to be constant over the required temperature range αcopper= 1.7 x 10-5K-1.\n"
    a = str(cal1(t1,d1,d2,a)) + " degree c\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    elif types == 3 :
        ques, answer = type3()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
