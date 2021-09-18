from mendeleev import element
import random
from scipy.constants import Avogadro

# Which has more number of atoms, 100 grams of sodium or 100 grams of iron 
# (given atomic mass of Na = 23 u, Fe = 56 u) ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
avo = Avogadro
ele = []
ele_wt = []
for i in range(1,119) :
    Element = element(i)
    ele.append((Element.name.lower()))
    ele_wt.append(round(Element.atomic_weight,0))

for i in range(no_of_samples):
    at_no = random.sample(range(0,118),2)
    first_atno = at_no[0]
    second_atno = at_no[1]
    no_of_grams = random.sample(range(1,21),2)
    first_weight = no_of_grams[0]
    second_weight = no_of_grams[1]
    act_1 = ele_wt[first_atno]
    act_2 = ele_wt[second_atno]
    first_ele_name = ele[first_atno]
    second_ele_name = ele[second_atno]
    question = "Which has more number of atoms, " + str(first_weight) + " grams of " + str(first_ele_name) + " or " + str(second_weight) + " grams of " + str(second_ele_name) + " (given atomic mass of " + str(first_ele_name) + " = " + str(round(act_1)) + " u, atomic mass of " + str(second_ele_name) + " = " + str(round(act_2))+ " u) ?\n"
    if first_weight/act_1 > second_weight/act_2:
        answer = str(first_ele_name) + "\n"
    else:
        answer = str(second_ele_name) + "\n"
    qns.write(question)
    ans.write(answer)
    # print(question)
    # print(answer)
qns.close()
ans.close()
