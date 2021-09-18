import random

# What is the potential energy of an object of mass m kg placed at a height h m ?
# What is the mass of a object with potential energy of PE J placed at a height h m ?
# At what height should the object of mass m kg should be placed such that its potential energy is PE J ?
# PE = m*g*h

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
g = 9.8
no_of_samples = 1500000
# no_of_samples = 8

def calculation_PE(m, h): 
    return round(m * g * h , 1)

def calculation_m(PE, h):
    return round(PE / (g * h), 1)

def calculation_h(PE, m):
    return round(PE / (m * g), 1)

def type1():
    m = random.randint(1,1000)
    h = random.randint(1,1000)
    PE = str(calculation_PE(m,h)) + " J\n"
    q = "What is the potential energy of an object of mass " + str(m) + " kg placed at a height " + str(h) + " m ?\n"
    return q,PE

def type2():
    PE = random.randint(9000,10000)
    h = random.randint(1,1000)
    m = str(calculation_m(PE,h)) + " kg\n"
    q = "What is the mass of a object with potential energy of " + str(PE) + " J placed at a height " + str(h) + " m ?\n"
    return q,m

def type3():
    PE = random.randint(9000,10000)
    m = random.randint(1,1000)
    h = str(calculation_h(PE,m)) + " m\n"
    q = "At what height should the object of mass " + str(m) + " kg should be placed such that its potential energy is " + str(PE) + " J ?\n"
    return q,h

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
