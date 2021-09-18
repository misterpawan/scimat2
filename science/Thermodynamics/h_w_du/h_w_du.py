import random


# In a process, h J of heat is absorbed by a system and w J of work is done by the system. What is the change in internal energy for the process ?
# In a process, h J of heat is released by a system and w J of work is done by the system. What is the change in internal energy for the process ?
# In a process, h J of heat is absorbed by a system and w J of work is done on the system. What is the change in internal energy for the process ?
# In a process, h J of heat is released by a system and w J of work is done on the system. What is the change in internal energy for the process ?
# In a process, change in internal energy of the system is du J. If w J of work is done by the system, what is the amount of heat absorbed by the process ?
# In a process, change in internal energy of the system is du J. If w J of work is done on the system, what is the amount of heat absorbed by the process ?  
# In a process, h J of heat is absorbed by the system and caused a change of du J in internal energy of the system, what is the work done by the system ?
# In a process, h J of heat is released by the system and caused a change of du J in internal energy of the system, what is the work done by the system ?

#U = H + w

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_du (h, w):
    return h + w

def calculation_h_w (du, val):
    return du - val

def type1():
    h = random.randint(1,10000)
    w = random.randint(1,10000)
    du = str(calculation_du(h, -1*w)) + "\n"
    q = "In a process, " + str(h) + " J of heat is absorbed by a system and " + str(w) + " J of work is done by the system. What is the change in internal energy for the process ?\n"
    return q,du

def type2():
    h = random.randint(1,10000)
    w = random.randint(1,10000)
    du = str(calculation_du(-1*h, -1*w)) + "\n"
    q = "In a process, " + str(h) + " J of heat is released by a system and " + str(w) + " J of work is done by the system. What is the change in internal energy for the process ?\n"
    return q,du

def type3():
    h = random.randint(1,10000)
    w = random.randint(1,10000)
    du = str(calculation_du(h, w)) + "\n"
    q = "In a process, " + str(h) + " J of heat is absorbed by a system and " + str(w) + " J of work is done on the system. What is the change in internal energy for the process ?\n"
    return q,du

def type4():
    h = random.randint(1,10000)
    w = random.randint(1,10000)
    du = str(calculation_du(-1*h, w)) + "\n"
    q = "In a process, " + str(h) + " J of heat is released by a system and " + str(w) + " J of work is done on the system. What is the change in internal energy for the process ?\n"
    return q,du

def type5():
    du = random.randint(-10000,10000)
    w = random.randint(1,10000)
    h = str(calculation_h_w(du, -1*w)) + "\n"
    q = "In a process, change in internal energy of the system is " + str(du) + " J. If " + str(w) + " J of work is done by the system, what is the amount of heat absorbed by the process ?\n"
    return q,h

def type6():
    du = random.randint(-10000,10000)
    w = random.randint(1,10000)
    h = str(calculation_h_w(du, w)) + "\n"
    q = "In a process, change in internal energy of the system is " + str(du) + " J. If " + str(w) + " J of work is done on the system, what is the amount of heat absorbed by the process ?\n"
    return q,h

def type7():
    du = random.randint(-10000,10000)
    h = random.randint(1,10000)
    w = str(calculation_h_w(du, h)) + "\n"
    q = "In a process, " + str(h) + " J of heat is absorbed by the system and caused a change of " + str(du) + " J in internal energy of the system, what is the work done by the system ?\n"
    return q,w

def type8():
    du = random.randint(-10000,10000)
    h = random.randint(1,10000)
    w = str(calculation_h_w(du, -1*h)) + "\n"
    q = "In a process, " + str(h) + " J of heat is absorbed by the system and caused a change of " + str(du) + " J in internal energy of the system, what is the work done by the system ?\n"
    return q,w

for i in range(no_of_samples):
    types = random.randint(1,8)
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
    elif types == 7:
        ques,answer = type7()
    elif types == 8:
        ques,answer = type8()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
