import random


# A copper wire has cross-section area of A m2 and resistivity of rho ohm-m.What is the length of this wire makes its resistance R ohm ?
# A copper wire has length of l m and resistivity of rho ohm-m.What is the cross-section area of this wire makes its resistance R ohm ?
# A copper wire has cross-section area of A m2 and length of l m.What is the resistivity of this wire makes its resistance R ohm ?
# A copper wire has cross-section area of A m2, length of l m and resistivity of rho ohm-m.What is its resistance ?


qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

def type1():
    R = random.randint(1,100)
    A = random.randint(1,100)
    rho = random.randint(1,100)
    l = str(round((R*A)/rho,1)) + " m\n"
    q = "A copper wire has cross-section area of "+str(A)+" m2 and resistivity of "+str(rho)+" ohm-m.What is the length of this wire makes its resistance "+str(R)+" ohm ?\n"
    return q,l

def type2():
    rho = random.randint(1,100)
    l = random.randint(1,100)
    R = random.randint(1,100)
    A = str(round((rho*l)/R,1)) + " m2\n"
    q = "A copper wire has length of "+str(l)+" m and resistivity of "+str(rho)+" ohm-m.What is the cross-section area of this wire makes its resistance "+str(R)+" ohm ?\n"
    return q,A

def type3():
    R = random.randint(1,100)
    A = random.randint(1,100)
    l = random.randint(1,100)
    rho = str(round((R*A)/l,1)) + " ohm-m\n"
    q = "A copper wire has cross-section area of "+str(A)+" m2 and length of "+str(l)+" m.What is the resistivity of this wire makes its resistance "+str(R)+" ohm ?\n"
    return q,rho

def type4():
    rho = random.randint(1,100)
    l = random.randint(1,100)
    A = random.randint(1,100)
    R = str(round((rho*l)/A,1)) + " ohm\n"
    q = "A copper wire has cross-section area of "+str(A)+" m2, length of "+str(l)+" m and resistivity of "+str(rho)+" ohm-m.What is its resistance ?\n"
    return q,R

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    if types == 3:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
