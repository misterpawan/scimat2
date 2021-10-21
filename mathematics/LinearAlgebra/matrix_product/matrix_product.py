import random
import numpy as np

# Calculate the product of the Matrices A and B.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def arrtostr(M, n, m2) :
    m = "["
    for i in range(n) :
        m = m + "["
        for j in range(m2) :
            if j == 0 :
                m = m + str(M[i][j])
            else :
                m = m + ", " + str(M[i][j])
        if i != n-1 :
            m = m + "], "
        else :
            m = m + "]"
    m = m + "]"
    return m

def type1() :
    n = 1
    m = 1
    p = 1
    while((n == 1 and m == 1) or (m == 1 and p == 1 )) :
        n = random.randint(1,4)
        m = random.randint(1,4)
        p = random.randint(1,4)
    a1 = []
    a2 = []
    for i in range(n) :
        newrow1 = []
        for j in range(m) :
            newrow1.append(random.randint(1,20))
        a1.append(newrow1)
    for i in range(m) :
        newrow1 = []
        for j in range(p) :
            newrow1.append(random.randint(1,20))
        a2.append(newrow1)
    q = "Calculate the product of the matrices " + arrtostr(a1,n,m) + " and " + arrtostr(a2,m,p) + ".\n"
    M_sum = np.dot(np.array(a1), np.array(a2)) 
    m = arrtostr(M_sum,n,p) + "\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
