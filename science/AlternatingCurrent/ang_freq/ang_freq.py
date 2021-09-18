import random
import math

# Obtain the resonant angular frequency of a series LCR circuit with L = 2 H, C = 32 muF, R = 10 ohm.
# Obtain the Q-value of a series LCR circuit with L = 2 H, C = 32 muF, R = 10 ohm.
# A charged 30 muF capacitor is connected to 27 mH inductor. What is the angular frequency of free oscillations of the circuit?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1500000

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1 or types == 2:
        L = random.randint(1,200)
        C = random.randint(1,200)
        R = random.randint(1,200)
        arr = ["resonant angular frequency","Q-value"]
        q = "Obtain the "+arr[types-1]+" of a series LCR circuit with L = "+str(L)+" H, C = "+str(C)+" muF, R = "+str(R)+" ohm?\n"
        if types == 1:
            a = str(round((1/math.sqrt(L*C*0.000001)),1))+" s-1\n"
        else:
            a = str(round(((1/R)*math.sqrt(L/(C*0.000001))),1)) + "\n"
    elif types == 3:
        C = random.randint(1,2000)
        L = random.randint(1,2000)
        q = "A charged "+str(C)+" muF capacitor is connected to "+str(L)+" mH inductor. What is the angular frequency of free oscillations of the circuit?\n"
        a = str(round(1/math.sqrt(L*C*0.001*0.000001),1)) + " s-1\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()