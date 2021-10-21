from sympy import *
from operator import add,sub
import random
from tqdm import tqdm

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

# Differentiate 724 * x + sin ( x ) + sec ( x ) with respect to x

x = symbols('x')

# trig = [sin, cos, tan, sec, csc,cot]
trig = [sin, cos, tan, sec, csc, cot, sinh, cosh, tanh, sech, csch, coth, asin, acos, atan, asec, acsc, acot , asinh, acosh, atanh, asech, acsch, acoth]
ops = [add,sub]

def rand_alg():
  p = random.randint(1,5000)
  alg = [p*x , p*x*x, p/x, p*log(x), p/(x*x)]
  return random.choice(alg)

def type1() :
    n = random.randint(3,6)
    exp = rand_alg()*random.choice(trig)(x)
    for i in range(n-1) :
        exp = random.choice(ops)(exp,rand_alg()*random.choice(trig)(x)) 
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