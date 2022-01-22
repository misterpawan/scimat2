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

    M = []
    for i in l1:
        temp=[]
        for j in i:
            temp.append(j)
        M.append(temp)
    c = random.randint(1, 100)
    qn = str("calculate the value of "+ str(c) + " * " + str(M) +".")
    # qn = qn.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    question = re.sub('\s+',' ',qn) + "\n"

    M = Matrix(M)
    an = str(c*M)
    an = an.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    answer = re.sub('\s+',' ',an) + "\n"

    qns.write(question)
    ans.write(answer)

qns.close()
ans.close()