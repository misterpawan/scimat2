from sympy import *
from operator import add, sub
import random
import re

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
num_samples = 10000

# Integrate cos ( x ) + tan ( x ) with respect to x

x = symbols('x')

# using basic or full trigonometric functions as per need.
# trig = [sin, cos, tan, sec, csc,cot]
trig = [sin, cos, tan, sec, csc,cot, sinh, cosh, tanh, sech, csch,coth, asin, acos, atan, asec, acsc, acot , asinh, acosh, atanh, asech, acsch, acoth]
ops = [add]

# gen_exp = lambda opl, oper, opr: oper(opl, opr)
# exp1 = lambda: random.choice(ops)(random.choice(trig)(x), random.choice(trig)(x))

# list1 = [gen_exp(exp1(), random.choice(ops), exp1()) for _ in range(num_samples)]
# # diff(cos(x) + sin(x) , x) and similar statements

gen_exp = lambda opl, oper, opr: oper(opl, opr)
exp1 = lambda: random.choice(ops)(random.choice(trig)(x), random.choice(trig)(x))

# list1 = [gen_exp(exp1(), random.choice(ops), exp1()) for _ in range(num_samples)]
list1 = [exp1() for _ in range(num_samples)]

for i in list1:
  if len(str(i)) is not 1:
    file_content = str(i)

    #  Adding spaces around backets , * , - at start of sentence
    if file_content[0] or file_content[1]=='-' :
      file_content = file_content.replace("-"," - ")
    file_content = file_content.replace("("," ( ").replace(")"," ) ").replace("*"," * ")
    line = "Integrate "+file_content+" with respect to x" + "\n"
    question = re.sub('\s+',' ',line)

    a=Integral(i,x)
    output_line = str(a.doit())
    output_line = output_line.replace("("," ( ").replace(")"," ) ").replace("**"," ^ ").replace("*"," * ").replace("/"," / ").replace("-"," - ")
    answer = re.sub('\s+',' ',output_line) + "\n"

    qns.write(question)
    ans.write(answer)
qns.close()
ans.close()
