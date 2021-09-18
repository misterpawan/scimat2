import random

# A wire of material-1 has length of l1 m, cross-section area of A1 m2, resistivity of rho1 ohm-m, another wire of material-2 has length of l2 m, cross-section area of A2 m2, resistivity of rho2 ohm-m, then find the ratio of resistance of two wires?
# A wire of material-1 has length of l1 m, resistance of R1 ohm, resistivity of rho1 ohm-m, another wire of material-2 has length of l2 m, resistance of R2 ohm, resistivity of rho2 ohm-m, then find the ratio of cross-section area of two wires?
# A wire of material-1 has length of l1 m, cross-section area of A1 m2, resistance of R1 ohm, another wire of material-2 has length of l2 m, cross-section area of A2 m2, resistance of R2 ohm, then find the ratio of resistivity of two wires?
# A wire of material-1 has resistance of R1 ohm, cross-section area of A1 m2, resistivity of rho1 ohm-m, another wire of material-2 has resistance of R2 ohm, cross-section area of A2 m2, resistivity of rho2 ohm-m, then find the ratio of length of two wires?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

R1 = random.randint(1,10)
R2 = random.randint(1,10)
l1 = random.randint(1,10)
l2 = random.randint(1,10)
rho1 = random.randint(1,10)
rho2 = random.randint(1,10)
A1 = random.randint(1,10)
A2 = random.randint(1,10)

def type1():
    R1 = random.randint(1,10)
    R2 = random.randint(1,10)
    rho1 = random.randint(1,10)
    rho2 = random.randint(1,10)
    A1 = random.randint(1,10)
    A2 = random.randint(1,10)
    q = "A wire of material-1 has resistance of "+str(R1)+" ohm, cross-section area of "+str(A1)+" m2, resistivity of "+str(rho1)+" ohm-m, another wire of material-2 has resistance of "+str(R2)+" ohm, cross-section area of "+str(A2)+" m2, resistivity of "+str(rho2)+" ohm-m, then find the ratio of length of two wires?\n"
    l = str(R1*A1*rho2)+'/'+str(R2*A2*rho1)+"\n"
    return q,l

def type2():
    R1 = random.randint(1,10)
    R2 = random.randint(1,10)
    l1 = random.randint(1,10)
    l2 = random.randint(1,10)
    rho1 = random.randint(1,10)
    rho2 = random.randint(1,10)
    q = "A wire of material-1 has length of "+str(l1)+" m, resistance of "+str(R1)+" ohm, resistivity of "+str(rho1)+" ohm-m, another wire of material-2 has length of "+str(l2)+" m, resistance of "+str(R2)+" ohm, resistivity of "+str(rho2)+" ohm-m, then find the ratio of cross-section area of two wires?\n"
    A = str(R2*l1*rho1)+'/'+str(R1*l2*rho2)+"\n"
    return q,A

def type3():
    R1 = random.randint(1,10)
    R2 = random.randint(1,10)
    l1 = random.randint(1,10)
    l2 = random.randint(1,10)
    A1 = random.randint(1,10)
    A2 = random.randint(1,10)
    q = "A wire of material-1 has length of "+str(l1)+" m, cross-section area of "+str(A1)+" m2, resistance of "+str(R1)+" ohm, another wire of material-2 has length of "+str(l2)+" m, cross-section area of "+str(A2)+" m2, resistance of "+str(R2)+" ohm, then find the ratio of resistivity of two wires?\n"
    rho = str(R1*A1*l2)+'/'+str(R2*A2*l1)+"\n"
    return q,rho

def type4():
    l1 = random.randint(1,10)
    l2 = random.randint(1,10)
    rho1 = random.randint(1,10)
    rho2 = random.randint(1,10)
    A1 = random.randint(1,10)
    A2 = random.randint(1,10)
    q = "A wire of material-1 has length of "+str(l1)+" m, cross-section area of "+str(A1)+" m2, resistivity of "+str(rho1)+" ohm-m, another wire of material-2 has length of "+str(l2)+" m, cross-section area of "+str(A2)+" m2, resistivity of "+str(rho2)+" ohm-m, then find the ratio of resistance of two wires?\n"
    R = str(A2*l1*rho1)+'/'+str(A1*l2*rho2)+"\n"
    return q,R

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    if types == 3:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
