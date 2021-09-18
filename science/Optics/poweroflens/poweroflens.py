import random

# Find the power of a convex lens whose focal length is f cm.
# Find the power of a concave lens whose focal length is f cm.
# Find the focal length of a convex lens whose power is PD.
# Find the focal length of a concave lens whose power is PD.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 500000

def calculation_P1(f):
    return round(100/f,1)

def calculation_P2(f):
    return round(1/f,1)

def calculation_f(P):
    return round(1/P,1)

def type1():
    f = random.randint(1,500000)
    f = round(f/100,2)
    P = str(calculation_P1(f)) + " diatrope\n"
    q = "Find the power of a convex lens whose focal length is " + str(f) + " cm.\n"
    return q,P

def type2():
    f = random.randint(1,10000)
    f = round(f/100,2)
    P = str(calculation_P2(f)) + " diatrope\n"
    q = "Find the power of a convex lens whose focal length is " + str(f) + " m.\n"
    return q,P

def type3():
    f = random.randint(1,500000)
    f = round(f/100,2)
    P = str(calculation_P1(f)) + " diatrope\n"
    q = "Find the power of a concave lens whose focal length is " + str(f) + " cm.\n"
    return q,P

def type4():
    f = random.randint(1,10000)
    f = round(f/100,2)
    P = str(calculation_P2(f)) + " diatrope\n"
    q = "Find the power of a concave lens whose focal length is " + str(f) + " m.\n"
    return q,P

def type5() :
    P = random.randint(1,10000)
    P = round(P/100,2)
    f = str(calculation_f(P)) + " m\n"
    q = "Find the focal length of a convex lens whose power is " + str(P) + " D.\n"
    return q,f

def type6() :
    P = random.randint(1,10000)
    P = round(P/100,2)
    f = str(calculation_f(P)) + " m\n"
    q = "Find the focal length of a concave lens whose power is " + str(P) + " D.\n"
    return q,f

for i in range(no_of_samples):
    types = random.randint(1,24)
    if types >=1 and types <= 10:
        ques,answer = type1()
    elif types > 10 and types <= 20:
        ques,answer = type3()
    elif types == 21:
        ques,answer = type2()
    elif types == 22:
        ques,answer = type4()
    elif types == 23:
        ques,answer = type5()
    elif types == 24:
        ques,answer = type6()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()