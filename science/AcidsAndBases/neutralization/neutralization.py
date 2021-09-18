import random

# v1 mL of a solution of NaOH is found to be completely neutralised by v2 mL of a given solution of HCl. If we take v3 mL of the same solution of NaOH, the amount of HCl solution (the same solution as before) required to neutralise it will be.
# v1 mL of a solution of HCl is found to be completely neutralised by v2 mL of a given solution of NaOH. If we take v3 mL of the same solution of HCl, the amount of Naoh solution (the same solution as before) required to neutralise it will be.

acids = ['HClO4', 'HCl', 'HBr', 'HI', 'HNO3', 'H2SO4', 'HClO3', 'HIO4']
bases = ['NaOH', 'KOH', 'Ca(OH)2', 'Sr(OH)2', 'Ba(OH)2', 'LiOH', 'RbOH', 'CsOH']

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

def calculation(x1, x2, x3) :
    return round((x2*x3)/x1,2)

def type1():
    v1 = random.randint(1,50)
    v2 = random.randint(1,50)
    v3 = random.randint(1,50)
    temp = random.randint(0,7)
    acid = acids[temp]
    temp = random.randint(0,7)
    base = bases[temp]
    q = str(v1) + " mL of a solution of " + str(base) + " is found to be completely neutralised by " + str(v2) + " mL of a given solution of " + str(acid) + ". If we take " + str(v3) + " mL of the same solution of " + str(base) + ", the amount of " + str(acid) + " solution (the same solution as before) required to neutralise it will be.\n"
    v4 = str(calculation(v1, v2, v3)) + " ml\n"
    return q,v4

def type2():
    v1 = random.randint(1,50)
    v2 = random.randint(1,50)
    v3 = random.randint(1,50)
    temp = random.randint(0,7)
    acid = acids[temp]
    temp = random.randint(0,7)
    base = bases[temp]
    q = str(v1) + " mL of a solution of " + str(acid) + " is found to be completely neutralised by " + str(v2) + " mL of a given solution of " + str(base) + ". If we take " + str(v3) + " mL of the same solution of " + str(acid) + ", the amount of " + str(base) + " solution (the same solution as before) required to neutralise it will be.\n"
    v4 = str(calculation(v1, v2, v3)) + " ml\n"
    return q,v4

for i in range(no_of_samples) :
    types = random.randint(1,2)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()

