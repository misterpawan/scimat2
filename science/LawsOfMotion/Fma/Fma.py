import random

# A force is applied on a body of mass m kg placed on a smooth surface 
# resulting in acceleration of a m/s2 , then what is the force applied ?
# A F N force is applied on a body of mass m kg placed on a smooth surface, then
# what is the resulting acceleration obtained ?
# A F N force is applied on a body placed on a smooth surface
# resulting in acceleration of a m/s2 ,then what is the mass of the body? 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 8

def calculation_F(m, a): 
    return m * a

def calculation_a(F, m):
    return round(F / m, 1)

def calculation_m(F, a):
    return round(F / a, 1)

def type1():
    m = random.randint(1,1000)
    a = random.randint(1,1000)
    F = str(calculation_F(m,a)) + " newton\n"
    q = "A force is applied on a body of mass " + str(m) + " kg placed on a smooth surface resulting in acceleration of " + str(a) + " m/s2, then what is the force applied ?\n"
    return q,F

def type2():
    F = random.randint(9000,10000)
    m = random.randint(1,1000)
    a = str(calculation_a(F,m)) + " m/s2\n"
    q = "A " + str(F) + " N force is applied on a body of mass " + str(m) + " kg placed on a smooth surface, then what is the resulting acceleration obtained ?\n"
    return q,a

def type3():
    F = random.randint(9000,10000)
    a = random.randint(1,1000)
    m = str(calculation_m(F,a)) + " kg\n"
    q = "A " + str(F) + " N force is applied on a body placed on a smooth surface resulting in acceleration of " + str(a) + "m/s2  ,then what is the mass of the body ?\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
