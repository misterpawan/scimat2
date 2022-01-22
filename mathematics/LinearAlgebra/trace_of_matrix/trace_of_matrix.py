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
    l1 = np.random.randint(0,100,(a,a))

    M = []
    for i in l1:
        temp=[]
        for j in i:
            temp.append(j)
        M.append(temp)

    qn = str("Calculate the Trace of Matrix "+ str(M)+" .")
    qn = qn.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    question = re.sub('\s+',' ',qn) + "\n"

    M = Matrix(M)
    an = str(trace(M))
    an = an.replace("("," ( ").replace(")"," ) ").replace("["," [ ").replace("]"," ] ").replace("*"," * ").replace("-"," - ")
    answer = re.sub('\s+',' ',an) + "\n"

    qns.write(question)
    ans.write(answer)

qns.close()
ans.close()