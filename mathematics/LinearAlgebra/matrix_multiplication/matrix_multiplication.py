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
    a = random.randint(1,3)
    b = random.randint(1,3)
    c = random.randint(1,3)
    l1 = np.random.randint(1,100,(a,b))
    l2 = np.random.randint(1,100,(b,c))

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

    qn = str("Calculate the product of Matrix "+ str(M)+" and " + str(N)+ " .")
    qn = qn.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    question = re.sub('\s+',' ',qn) + "\n"

    M = Matrix(M)
    N = Matrix(N)
    an = str(M*N)
    an = an.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    answer = re.sub('\s+',' ',an) + "\n"

    qns.write(question)
    ans.write(answer)

qns.close()
ans.close()