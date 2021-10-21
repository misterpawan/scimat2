import random
from sympy import *

# Calculate the Determinant of Matrix A.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def arrtostr(M, n, m2) :
    m = "["
    for i in range(n) :
        m = m + "["
        for j in range(m2) :
            if j == 0 :
                m = m + str(M[i,j])
            else :
                m = m + ", " + str(M[i,j])
        if i != n-1 :
            m = m + "], "
        else :
            m = m + "]"
    m = m + "]"
    return m

def type1() :
    n = 1
    m = 1
    while(n == 1 and m == 1) :
        n = random.randint(1,4)
        m = random.randint(1,4)
    a = []
    for i in range(n) :
        newrow = []
        for j in range(m) :
            newrow.append(random.randint(1,20))
        a.append(newrow)
    M = Matrix(a)
    q = "Calculate the rref of Matrix " + arrtostr(M,n,m) + ".\n"
    M_rref,_ = M.rref()
    m = arrtostr(M_rref,n,m) + "\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
