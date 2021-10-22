import random
import numpy as np

# Calculate the trace of Matrix A.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def type1() :
    a1 = random.randint(0,10)
    b1 = random.randint(0,10)
    c1 = random.randint(0,10)
    d1 = random.randint(0,10)
    a2 = random.randint(0,10)
    b2 = random.randint(0,10)
    c2 = random.randint(0,10)
    d2 = random.randint(0,10)
    a3 = random.randint(0,10)
    b3 = random.randint(0,10)
    c3 = random.randint(0,10)
    d3 = random.randint(0,10)
    a4 = random.randint(0,10)
    b4 = random.randint(0,10)
    c4 = random.randint(0,10)
    d4 = random.randint(0,10)
    q = "Calculate the trace of Matrix [[ " + str(a1) + ", " + str(b1) + ", " + str(c1) + ", " + str(d1) + "], [ " + str(a2) + ", " + str(b2) + ", " + str(c2) + ", " + str(d2) + "], [ " + str(a3) + ", " + str(b3) + ", " + str(c3) + ", " + str(d3) + "], [ " + str(a4) + ", " + str(b4) + ", " + str(c4) + ", " + str(d4) + "]].\n"
    M = np.matrix([[a1, b1, c1, d1], [a2, b2, c2, d2], [a3, b3, c3, d3], [a4, b4, c4, d4]])
    m = str(M.trace()) + "\n"
    return q,m

def type2() :
    a1 = random.randint(0,10)
    b1 = random.randint(0,10)
    c1 = random.randint(0,10)
    a2 = random.randint(0,10)
    b2 = random.randint(0,10)
    c2 = random.randint(0,10)
    a3 = random.randint(0,10)
    b3 = random.randint(0,10)
    c3 = random.randint(0,10)
    q = "Calculate the trace of Matrix [[ " + str(a1) + ", " + str(b1) + ", " + str(c1) + "], [ " + str(a2) + ", " + str(b2) + ", " + str(c2) + "], [ " + str(a3) + ", " + str(b3) + ", " + str(c3) + "]].\n" 
    M = np.matrix([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
    m = str(M.trace()) + "\n"
    return q,m

def type3() :
    a1 = random.randint(0,20)
    b1 = random.randint(0,20)
    a2 = random.randint(0,20)
    b2 = random.randint(0,20)
    q = "Calculate the trace of Matrix [[ " + str(a1) + ", " + str(b1) + "], [ " + str(a2) + ", " + str(b2) + "]].\n" 
    M = np.matrix([[a1, b1], [a2, b2]])
    m = str(M.trace()) + "\n"
    return q,m

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
