from mendeleev import element
import random
from scipy.constants import Avogadro

# If one mole of carbon atoms weigh 12 grams, what is the mass (in grams) of 1 atom of carbon?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
avo = Avogadro
ele = []
ele_wt = []
for i in range(1,119) :
    Element = element(i)
    ele.append(Element.name)
    ele_wt.append(round(Element.atomic_weight,0))

def calculation(weight,no_of_atoms):
    ret = weight*no_of_atoms/avo
    ret = str(ret)
    length = len(ret)
    ret_end = ret[length-4:]
    ret = ret[:length-4]
    ret = round(float(ret),1)
    ret = str(ret) + ret_end
    return ret

for i in range(no_of_samples):
    at_no = random.randint(0,117)
    #Element = element(at_no)
    element_name = ele[at_no]
    element_weight = ele_wt[at_no]
    no_of_atoms = random.randint(1,10000)
    # no_of_atoms = 1
    question_string = "If one mole of " + str(element_name) + " atoms weigh " + str(element_weight) + " grams, what is the mass (in grams) of "+ str(no_of_atoms) + " atoms of " + str(element_name) + " ?\n"
    qns.write(question_string)
    # print(question_string)
    answer = calculation(element_weight,no_of_atoms)
    answer_string = answer + " g\n"
    ans.write(answer_string)
    # print(answer_string)
qns.close()
ans.close()
