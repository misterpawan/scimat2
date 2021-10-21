from sympy import *
from operator import add, sub
import random
from tqdm import tqdm

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

# Differentiate { cosh ( x ) + acsc ( x ) - acsch ( x ) + csc ( x ) }

x = symbols('x')
trig = [sin, cos, tan, sec, csc,cot, sinh, cosh, tanh, sech, csch,coth, asin, acos, atan, asec, acsc, acot , asinh, acosh, atanh, asech, acsch, acoth]
ops = [add, sub]

no_of_samples = 10000

def type1() :
    n = random.randint(3,8)
    exp = random.randint(1,100)*random.choice(trig)(x)
    for i in range(n-1) :
        exp = random.choice(ops)(exp,random.randint(1,100)*random.choice(trig)(x)) 
    q = "Differentiate { " + str(exp) + " }.\n"
    a = diff(exp,x)
    m = str(a.doit()) + "\n"
    return q,m

for i in tqdm(range(no_of_samples)):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
