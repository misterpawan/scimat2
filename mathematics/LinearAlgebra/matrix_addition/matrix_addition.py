import random
import numpy as np
from sympy import *
init_printing(use_unicode=True)
from tqdm import tqdm
import re

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in tqdm(range(no_of_samples)):
    a = random.randint(1,4)
    b = random.randint(2,3)
    l1 = np.random.randint(1,100,(a,b))
    l2 = np.random.randint(1,100,(a,b))

    M = []
    N = []
    for i in l1:
        temp=[]
        for j in i:
            temp.append(j)
        M.append(temp)
    for i in l2:
        temp=[]
        for j in i:
            temp.append(j)
        N.append(temp)

    qn = str("what is the sum of  Matrix "+ str(M) + " and Matrix " + str(N) +" ?")
    qn = qn.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    question = re.sub('\s+',' ',qn) + "\n"

    M = Matrix(M)
    N = Matrix(N)
    an = str(M+N)
    an = an.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    answer = re.sub('\s+',' ',an) + "\n"

    qns.write(question)
    ans.write(answer)

qns.close()
ans.close()