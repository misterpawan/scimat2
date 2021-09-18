from mendeleev import element
import random

# How many neutrons does Helium atom have (atomic number and mass of Helium is 2 and 4 respectively) ?
# How many protons does Helium atom have (atomic number of Helium is 2) ?
# How many electrons does Helium atom have (atomic number of Helium is 2) ?
# If an atom X have an atomic mass of 4 u and 2 protons in its nucleus. How many neutrons does it have ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000

ele = []
ele_wt = []
ele_an = []
for i in range(1,119) :
    Element = element(i)
    ele.append(Element.name)
    ele_wt.append(round(Element.atomic_weight,0))
    ele_an.append(Element.atomic_number)

def type1() :
    e = random.randint(0,117)
    temp = random.randint(1,6)
    if temp == 1 :
        q = "How many neutrons does " + str(ele[e]) + " atom have (atomic number and mass of " + str(ele[e]) + " are " + str(ele_an[e]) + " and " + str(ele_wt[e]) + " respectively) ?\n"
        a = int(ele_wt[e]) - int(ele_an[e])
    elif temp == 2 :
        q = "How many protons does " + str(ele[e]) + " atom have (atomic number of " + str(ele[e]) + " is " + str(ele_an[e]) + ") ?\n"
        a = int(ele_an[e])
    elif temp == 3 :
        q = "How many electrons does " + str(ele[e]) + " atom have (atomic number of " + str(ele[e]) + " is " + str(ele_an[e]) + ") ?\n"
        a = int(ele_an[e])
    elif temp == 4 :
        q = "How many neutrons does " + str(ele[e]) + " atom have ?\n"
        a = int(ele_wt[e]) - int(ele_an[e])
    elif temp == 5 :
        q = "How many protons does " + str(ele[e]) + " atom have ?\n"
        a = int(ele_an[e])
    elif temp == 6 :
        q = "How many electrons does " + str(ele[e]) + " atom have ?\n"
        a = int(ele_an[e])
    a = str(a) + "\n"
    return q,a

def type2() :
    n = random.randint(1,300)
    w = random.randint(n+1,n+300)
    q = "If an atom X have an atomic mass of " + str(w) + " u and " + str(n) + " protons in its nucleus. How many neutrons does it have?\n"
    a = w - n
    a = str(a) + "\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,5)
    if types == 1 :
        ques,answer = type1()
    else:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
