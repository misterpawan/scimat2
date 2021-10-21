import random
import math

# What are the prime factors of 329 ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000

def cal(n) :
    a = set()
    while n % 2 == 0 :
        a.add(2)
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0 :
            a.add(i)
            n = n / i
    if n > 2:
        a.add(math.floor(n))
    return a

def type1() :
    num = random.randint(2,20000)
    q = "What are the prime factors of " + str(num) + " ?\n"
    a = cal(num)
    m = ""
    prime_list = []
    for i in a :
        prime_list.append(i)
    prime_list.sort()
    m = m + str(prime_list[0])
    for i in range(1,len(prime_list)) :
        m = m + ", " + str(prime_list[i])  
    m = m + "\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
