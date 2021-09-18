import random


# Calculate the enthalpy change on freezing of n mol of water at T1 celcius to ice at T2 celcius. A, H = 6.03 KJ/mol at 0 celcius. Cp [H20(l)J = 75.3 J mol-1 K-1; Cp [H20(s)J = 36.8 J mol-1 K-1.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
h1 = 75.3
h2 = 36.8
h = 6030

def cal(n, t1, t2) :
    ans = round(h1*t1,1) + round(h2*t2,1) + h
    return round(ans*n,1)

for i in range(no_of_samples):
    n = random.randint(1,20)
    t1 = random.randint(1,1000)
    t1 = round(t1/10,1)
    t2 = random.randint(-1000,-1)
    t2 = round(t2/10,1)
    types = random.randint(1,2)
    if types == 1 :
        ques = "Calculate the enthalpy change on freezing of " + str(n) + " mol of water at " + str(t1) + " celcius to ice at " + str(t2) + " celcius. Given, H = 6.03 KJ/mol at 0 celcius. Cp [H20(l)J = 75.3 J/molK; Cp [H20(s)J = 36.8 J/molK.\n"
    else :
         ques = "Calculate the enthalpy change on freezing of " + str(n) + " mol of water at " + str(t1) + " celcius to ice at " + str(t2) + " celcius.\n"
    answer = str(cal(n, t1, t2)) + "\n"
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
