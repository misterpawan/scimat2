import random

# The coefficient of volume expansion of glycerine is 49 x 10-5K-1. What is the change in its volume v m3 for a rise in temperature from t1 degree C to t2 degree C?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 3000000

def cal1(t1,t2,d1,a) :
    return round(d1*a*(t2-t1),2)

def type1() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 49 * 10**-5
    q = "The coefficient of volume expansion of glycerine is 49 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

def type2() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 5.1 * 10**-5
    q = "The coefficient of volume expansion of copper is 5.1 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

def type3() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 6 * 10**-5
    q = "The coefficient of volume expansion of brass is 6 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

def type4() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 3.6 * 10**-5
    q = "The coefficient of volume expansion of steel is 3.6 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

def type5() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 49 * 10**-5
    q = "The coefficient of linear expansion of glycerine is 16.3 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

def type6() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 5.1 * 10**-5
    q = "The coefficient of linear expansion of copper is 1.7 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

def type7() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 6 * 10**-5
    q = "The coefficient of linear expansion of brass is 2 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

def type8() :
    t1 = random.randint(10,110)
    t2 = random.randint(t1+150,t1+400)
    d1 = random.randint(10,110)
    a = 3.6 * 10**-5
    q = "The coefficient of linear expansion of steel is 1.2 x 10-5K-1. What is the change in its volume " + str(d1) + " m3 for a rise in temperature from " + str(t1) + " degree C to " + str(t2) + " degree C?\n"
    a = str(cal1(t1,t2,d1,a)) + " m3\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,8)
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
    elif types == 7 :
        ques, answer = type7()
    elif types == 8 :
        ques, answer = type8()
    
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
