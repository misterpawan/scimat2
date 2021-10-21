import random
import numpy as np

# Calculate the Determinant of Matrix A.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def type1() :
    a1 = random.randint(1,100)
    b1 = random.randint(1,100)
    c1 = random.randint(1,100)
    a2 = random.randint(1,100)
    b2 = random.randint(1,100)
    c2 = random.randint(1,100)
    a3 = random.randint(1,100)
    b3 = random.randint(1,100)
    c3 = random.randint(1,100)
    q = "Calculate the Determinant of Matrix [[ " + str(a1) + ", " + str(b1) + ", " + str(c1) + "], [ " + str(a2) + ", " + str(b2) + ", " + str(c2) + "], [ " + str(a3) + ", " + str(b3) + ", " + str(c3) + "]].\n" 
    m = str(round(np.linalg.det(np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])),0)) + " units\n"
    return q,m

def type2() :
    a1 = random.randint(1,100)
    b1 = random.randint(1,100)
    a2 = random.randint(1,100)
    b2 = random.randint(1,100)
    q = "Calculate the Determinant of Matrix [[ " + str(a1) + ", " + str(b1) + "], [ " + str(a2) + ", " + str(b2) + "]].\n" 
    m = str(round(np.linalg.det(np.array([[a1, b1], [a2, b2]])),0)) + " units\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
