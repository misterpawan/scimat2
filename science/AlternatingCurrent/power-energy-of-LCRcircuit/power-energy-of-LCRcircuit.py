import random
import math

# Suppose the inital charge on the capacitor in an LC circuit with 30 muF capacitor and 27 mH inductor is 6 mC. What is the total energy stored in the circuit initially? What is the total energy at later time?
# A series LCR circuit with R = 20 ohm, L = 1.5 H and C = 35 muF is connected to a variable frequency of 200 V ac supply. When the frequency of the supply equals the natural frequency of the circuit, what is the average power transferred to the circuit in one complete cycle?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1500000

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        L = random.randint(1,200)
        C = random.randint(1,200)
        Q = random.randint(1,200)
        q = "Suppose the inital charge on the capacitor in an LC circuit with "+str(C)+" muF capacitor and "+str(L)+" mH inductor is "+str(Q)+" mC. What is the total energy stored in the circuit initially? What is the total energy at later time?\n"
        E = 0.5*Q*Q*(1/C)
        a = "{:.2e} joule, final value is same as initial value\n".format(E) 
    elif types == 2:
        L = random.randint(1,200)
        C = random.randint(1,200)
        R = random.randint(1,200)
        q = "A series LCR circuit with R = "+str(R)+" ohm, L = "+str(L)+" H and C = "+str(C)+" muF is connected to a variable frequency of 200 V ac supply. When the frequency of the supply equals the natural frequency of the circuit, what is the average power transferred to the circuit in one complete cycle?\n"
        a = str(round(((200*200)/R),1))+" watt\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()