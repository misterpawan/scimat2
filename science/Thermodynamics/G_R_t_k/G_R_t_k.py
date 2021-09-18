import random

import math

# The equilibrium constant for a reaction is n. Calculate the value of ΔG^o, given R = 8.3 J/Kmol and T = t.
# ΔG^o = -RTlnk

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 500000
R = 8.3

def cal(n, t) :
    ans = -1*R*t*math.log(n)*2.303
    return round(ans,1)

for i in range(no_of_samples):
    n = random.randint(1,1000)
    t = random.randint(2730,3730)
    t = round(t/10,1)
    type = random.randint(1,2)
    if type == 1:
        ques = "The equilibrium constant for a reaction is " + str(n) + ". Calculate the value of ΔG^o, given R = 8.3 J/Kmol and T = " + str(t) + ".\n"
    else :
        ques = "The equilibrium constant for a reaction is " + str(n) + ". Calculate the value of ΔG^o, given T = " + str(t) + ".\n"
    answer = str(cal(n, t)) + "\n"
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
