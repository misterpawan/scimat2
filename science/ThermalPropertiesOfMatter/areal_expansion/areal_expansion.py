import random
import math

# A hole is drilled in a copper sheet. The diameter of the hole is 4.24 cm at 27.0 °C. What is the change in the diameter of the hole when the sheet is heated to 227 °C ? Coefficient of linear expansion of copper = 1.70 x 10-5K-1. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2000000

def cal1(t1,t2,d1,a) :
    d2 = d1*(math.sqrt(1+(a*d1*(t2-t1))))
    return round(d2-d1,3)

def type1() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 2.4 * 10**-5
    q = "A hole is drilled in a steel sheet. The diameter of the hole is " + str(d1) + " cm at " + str(t1) + " degree C. What is the change in the diameter of the hole when the sheet is heated to " + str(t2) + " degree C ? Coefficient of linear expansion of steel = 1.2 x 10-5K-1.\n"
    a = str(cal1(t1,t2,d1,a)) + " cm\n"
    return q,a

def type2() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 3.4 * 10**-5
    q = "A hole is drilled in a copper sheet. The diameter of the hole is " + str(d1) + " cm at " + str(t1) + " degree C. What is the change in the diameter of the hole when the sheet is heated to " + str(t2) + " degree C ? Coefficient of linear expansion of copper = 1.7 x 10-5K-1.\n"
    a = str(cal1(t1,t2,d1,a)) + " cm\n"
    return q,a

def type3() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 4 * 10**-5
    q = "A hole is drilled in a brass sheet. The diameter of the hole is " + str(d1) + " cm at " + str(t1) + " degree C. What is the change in the diameter of the hole when the sheet is heated to " + str(t2) + " degree C ? Coefficient of linear expansion of brass = 2 x 10-5K-1.\n"
    a = str(cal1(t1,t2,d1,a)) + " cm\n"
    return q,a

def type4() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 2.4 * 10**-5
    q = "A hole is drilled in a steel sheet. The diameter of the hole is " + str(d1) + " cm at " + str(t1) + " degree C. What is the change in the diameter of the hole when the sheet is heated to " + str(t2) + " degree C ? Coefficient of aereal expansion of steel = 2.4 x 10-5K-1.\n"
    a = str(cal1(t1,t2,d1,a)) + " cm\n"
    return q,a

def type5() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 3.4 * 10**-5
    q = "A hole is drilled in a copper sheet. The diameter of the hole is " + str(d1) + " cm at " + str(t1) + " degree C. What is the change in the diameter of the hole when the sheet is heated to " + str(t2) + " degree C ? Coefficient of aereal expansion of copper = 3.4 x 10-5K-1.\n"
    a = str(cal1(t1,t2,d1,a)) + " cm\n"
    return q,a

def type6() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 4 * 10**-5
    q = "A hole is drilled in a brass sheet. The diameter of the hole is " + str(d1) + " cm at " + str(t1) + " degree C. What is the change in the diameter of the hole when the sheet is heated to " + str(t2) + " degree C ? Coefficient of aereal expansion of brass = 4 x 10-5K-1.\n"
    a = str(cal1(t1,t2,d1,a)) + " cm\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
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
    elif types == 6 :
        ques, answer = type6()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
