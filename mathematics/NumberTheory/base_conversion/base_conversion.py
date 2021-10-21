from sympy import *
from operator import add, sub
import random
from tqdm import tqdm

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

# Convert num1 (base a1) to base a2.

no_of_samples = 1000000

dis = {}
for i in range(10) :
    dis[i] = str(i)
dis[10] = "a"
dis[11] = "b"
dis[12] = "c"
dis[13] = "d"
dis[14] = "e"
dis[15] = "f"

def type1() :
    a1 = random.randint(2,16)
    a2 = a1
    while(a2 == a1) :
        a2 = random.randint(2,16)
    qu = ""
    sum1 = 0
    len = random.randint(3,8)
    for i in range(len) :
        if i != len-1 :
            temp = random.randint(0,a1-1)
        else :
            temp = random.randint(1,a1-1)
        qu = dis[temp] + qu
        sum1 += ((a1**i)*temp)
    a = ""
    while sum1 != 0 :
        temp = sum1%a2
        sum1 = floor(sum1/a2)
        a = str(temp) + a
    t = random.randint(1,3)
    if t == 1 :
        q = "Convert " + qu + " (base " + str(a1) + ") to base " + str(a2) + ".\n"
    elif t == 2 :
        q = qu + " (base " + str(a1) + ") in base " + str(a2) + " is.\n"
    else :
        q = "What is " + qu + " (base " + str(a1) + ") in base " + str(a2) + ".\n"
    m = a + "\n"
    return q,m

for i in tqdm(range(no_of_samples)):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
