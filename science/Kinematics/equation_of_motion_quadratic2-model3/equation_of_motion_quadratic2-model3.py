import random
import math

# A stone is thrown vertically upward with an initial velocity of u m/s under gravity. What is the maximum height attained by the stone?
# A stone is thrown vertically upward with reaches a maximum height of h m. What is the initial velocity of the stone?

qns = open('./question.txt', 'w')
ans = open('./answer.txt','w')
no_of_samples = 1000000
g = 9.8

def calculation_h(u):
  return round(((u**2)/(2*g)),1)

def calculation_u(h) :
    return round(math.sqrt(2*g*h), 1)
    
def type1():
    u = random.randint(1,1000000) / 100
    h = str(calculation_h(u)) + " m\n"
    q = "A stone is thrown vertically upward with an initial velocity of "+str(u)+" m/s under gravity. What is the maximum height attained by the stone ?\n"
    return q,h

def type2():
    h = random.randint(1,1000000)
    u = str(calculation_u(h)) + " m/s\n"
    q = "A stone is thrown vertically upward with reaches a maximum height of "+str(h)+" m. What is the initial velocity of the stone ?\n"
    return q,u


for i in range(no_of_samples):
    types = random.randint(0,1)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)
    #print(ques)
    #print(answer)

qns.close()
ans.close()
