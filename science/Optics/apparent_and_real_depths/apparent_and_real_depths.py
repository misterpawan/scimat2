
from mendeleev import element
import random

# A tank is filled with water to a height of hr cm. The apparent depth of a needle lying at the bottom of the tank is measured by a microscope to be ha cm. What is the refractive index of water? 
# A tank is filled with a liquid of refractive index mu to a height of hr cm. What is the apparent depth of a needle lying at the bottom of the tank.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1 (hr, ha) :
    return round(hr/ha,2) 

def cal2 (hr,mu) :
    return round(hr/mu,2)

def type1() :
    ha = random.randint(1,2000)
    ha = round(ha*0.1,1)
    temp = random.randint(10,500)
    temp = round(temp*0.1,1)
    hr = ha + temp
    q = "A tank is filled with water to a height of " + str(hr) + " cm. The apparent depth of a needle lying at the bottom of the tank is measured by a microscope to be " + str(ha) + " cm. What is the refractive index of water ?\n"
    a = str(cal1(hr,ha)) + "\n"
    return q,a

def type2() :
    hr = random.randint(10,6000)
    hr = round(hr*0.1,1)
    mu = random.randint(100,300)
    q = "A tank is filled with a liquid of refractive index " + str(mu) + " to a height of " + str(hr) + " cm. What is the apparent depth of a needle lying at the bottom of the tank.\n"
    a = str(cal2(hr,mu)) + " cm\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
