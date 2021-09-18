import random

# On an unknown scale temperatue of the melting point and boiling point of the water are t1 degree and t2 degree respectively, If temperature on the Celcius scale is t degree C, then what is the temperature shown on that scale. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000

def cal1(t1,t2,t,ta,tb) :
    return round((((t2-t1)*(t-ta))/(tb-ta))+t1,1) 

def type1() :
    t1 = random.randint(-100,300)
    t2 = random.randint(t1+100,t1+300)
    t = random.randint(10,160)
    q = "On an unknown scale temperatue of the melting point and boiling point of the water are " + str(t1) + " degree and " + str(t2) + " degree respectively, If temperature on the Celcius scale is " + str(t) + " degree C, then what is the temperature shown on that scale.\n"
    a = str(cal1(t1,t2,t,0,100)) + "\n"
    return q,a

def type2() :
    t1 = random.randint(-100,300)
    t2 = random.randint(t1+100,t1+300)
    t = random.randint(280,400)
    q = "On an unknown scale temperatue of the melting point and boiling point of the water are " + str(t1) + " degree and " + str(t2) + " degree respectively, If temperature on the Kelvin scale is " + str(t) + " degree K, then what is the temperature shown on that scale.\n"
    a = str(cal1(t1,t2,t,273,373)) + "\n"
    return q,a

def type3() :
    t1 = random.randint(-100,300)
    t2 = random.randint(t1+100,t1+300)
    t = random.randint(40,200)
    q = "On an unknown scale temperatue of the melting point and boiling point of the water are " + str(t1) + " degree and " + str(t2) + " degree respectively, If temperature on the Farenheit scale is " + str(t) + " degree F, then what is the temperature shown on that scale.\n"
    a = str(cal1(t1,t2,t,32,212)) + "\n"
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
