import random

# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c, then value of d joule in new system.
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c, then value of d newton in new system.
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c, then value of d pascal in new system.
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c s, if the value of x joule is equal to d units in new system, find x?"
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c s, if the value of x newton is equal to d units in new system, find x?"
# Suppose we employ a system of units in which the unit of mass equals a kg, the unit of length equals b m, the unit of time is c s, if the value of x pascal is equal to d units in new system, find x?"

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
# no_of_samples = 30

def type1():
    a = random.randint(10,100)
    b = random.randint(10,100)
    c = random.randint(50,100)
    d = random.randint(1,10)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, if the value of x joule is equal to "+str(d)+" units in new system, find x?\n"
    a = str(round(d*(a)*(b**2)*(c**(-2)),2)) + "\n"
    return q,a

def type2():
    a = random.randint(50,110)
    b = random.randint(10,70)
    c = random.randint(10,110)
    d = random.randint(1,10)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, if the value of x newton is equal to "+str(d)+" units in new system, find x?\n"
    a = str(round(d*(a)*(b)*(c**(-2)),2)) + "\n"
    return q,a

def type3():
    a = random.randint(10,50)
    b = random.randint(1,20)
    c = random.randint(10,50)
    d = random.randint(1000,1100)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, if the value of x pascal is equal to "+str(d)+" units in new system, find x\n"
    a = str(round(d*(a)*(b**(-1))*(c**(-2)),2)) +"\n"
    return q,a

def type4():
    a = random.randint(10,50)
    b = random.randint(30,80)
    c = random.randint(50,100)
    d = random.randint(30,80)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, then value of "+str(d)+" joules in new system\n"
    a = str(round(d*(a**(-1))*(b**(-2))*(c**(2)),2)) + "\n"
    return q,a

def type5():
    a = random.randint(10,80)
    b = random.randint(10,80)
    c = random.randint(10,110)
    d = random.randint(10,20)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, then value of "+str(d)+" newton in new system\n"
    a = str(round(d*(a**(-1))*(b**(-1))*(c**(2)),2)) + "\n"
    return q,a

def type6():
    a = random.randint(100,200)
    b = random.randint(1,100)
    c = random.randint(1,50)
    d = random.randint(1,10)
    q = "Suppose we employ a system of units in which the unit of mass equals "+str(a)+" kg, the unit of length equals "+str(b)+" m, the unit of time is "+str(c)+" s, then value of "+str(d)+" pascal in new system\n"
    a = str(round(d*(a**(-1))*(b**(1))*(c**(2)),2)) +"\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,6)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    elif types == 4:
        ques,answer = type4()
    elif types == 5:
        ques,answer = type5()
    elif types == 6:
        ques,answer = type6()
    # print(ques)
    # print(answer)
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()