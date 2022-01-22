from sympy import *
from operator import add, sub
import random
import re

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
num_samples = 10000

# Differentiate { cosh ( x ) + acsc ( x ) - acsch ( x ) + csc ( x ) }

x = symbols('x')
trig = [sin, cos, tan, sec, csc,cot, sinh, cosh, tanh, sech, csch,coth, asin, acos, atan, asec, acsc, acot , asinh, acosh, atanh, asech, acsch, acoth]
ops = [add, sub]

gen_exp = lambda opl, oper, opr: oper(opl, opr)
exp1 = lambda: random.choice(ops)(random.choice(trig)(x), random.choice(trig)(x))

list1 = [gen_exp(exp1(), random.choice(ops), exp1()) for _ in range(num_samples)]

for i in list1:
  if len(str(i)) is not 1:    
    file_content = str(i)

    #  Adding spaces around backets , * , - at start of sentence
    if file_content[0] or file_content[1]=='-' :
        file_content = file_content.replace("-"," - ")
    file_content = file_content.replace("("," ( ").replace(")"," ) ").replace("*"," * ")
    line = "Differentiate { "+file_content+" }"
    question = re.sub('\s+',' ',line) + "\n"

    a=diff(i,x)    
    output_line = str(a.doit())
    output_line = "("+output_line+")"
    output_line = output_line.replace("("," ( ").replace(")"," ) ").replace("**"," ^ ").replace("*"," * ").replace("/"," / ").replace("-"," - ")
    answer = re.sub('\s+',' ',output_line) + "\n"

    qns.write(question)
    ans.write(answer)
qns.close()
ans.close()