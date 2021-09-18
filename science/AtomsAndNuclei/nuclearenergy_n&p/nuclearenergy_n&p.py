
from mendeleev import element
import random

# A given element has a mass of m g. Calculate the nuclear energy that would be required to seperate all the neutrons and protons from each other. For simplicity assume that the element is Cu.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

ele = []
ele_wt = []
ele_an = []
for i in range(1,119) :
    Element = element(i)
    ele.append(Element.name)
    ele_wt.append(Element.atomic_weight)
    ele_an.append(Element.atomic_number)

mn = 1.008665
mp = 1.007825
N = 6.023 * (10**23)

no_of_samples = 10000

for i in range(no_of_samples):
    m = random.randint(1,200)
    num = random.randint(1,100)
    ques = "A given element has a mass of " + str(m) + " g. Calculate the nuclear energy that would be required to seperate all the neutrons and protons from each other. For simplicity assume that the element is " + str(ele[num]) + "\n"
    nn = ele_wt[num] - ele_an[num]
    np = ele_an[num]
    dm = nn*mn + np*mp - ele_wt[num]
    na = (N*m)/ele_wt[num]
    answ = dm * na * 931.5 * 1.6 * (10**-13)
    answer = "{:.2e}".format(answ) + "joule\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
