import random

# Two moving coil meters M1 and M2 have the following particulars R1 = r1 ohms, N1 = n1, A1 = a1 m2 , B1 = b1 T, K1 = k and  R2 = r2 ohms, N2 = n2, A1 = a2 m2 , B1 = b2 T, K2 = k2. Determine the ratio of current sensitivities of M1 and M2.
# Two moving coil meters M1 and M2 have the following particulars R1 = r1 ohms, N1 = n1, A1 = a1 m2 , B1 = b1 T, K1 = k and  R2 = r2 ohms, N2 = n2, A1 = a2 m2 , B1 = b2 T, K2 = k2. Determine the ratio of voltage sensitivities of M1 and M2. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000

def cal1(n1,a1, r1, k1, b1, n2, a2, r2, b2, k2) :
    return round((n1*b1*a1*k2)/(n2*b2*a2*k1),1)

def cal2(n1,a1, r1, k1, b1, n2, a2, r2, b2, k2) :
    return round((n1*b1*a1*k2*r2)/(n2*b2*a2*k1*r1),1)

def type1() :
    n1 = random.randint(1,10)
    r1 = random.randint(1,10)
    a1 = random.randint(1,10)
    a1 = a1 * (10**-4)
    k1 = random.randint(1,10)
    b1 = random.randint(1,10)
    n2 = random.randint(1,10)
    r2 = random.randint(1,10)
    a2 = random.randint(1,10)
    a2 = a2 * (10**-4)
    k2 = random.randint(1,10)
    b2 = random.randint(1,10)
    q = "Two moving coil meters M1 and M2 have the following particulars R1 = " + str(r1) + " ohms, N1 = " + str(n1) + ", A1 = " + str(a1) + " m2 , B1 = " + str(b1) + " T, K1 = " + str(k1) + " and  R2 = " + str(r2) + " ohms, N2 = " + str(n2) + " , A1 = " + str(a2) + " m2 , B1 = " + str(b2) + " T, K2 = " + str(k2) + ". Determine the ratio of current sensitivities of M1 and M2.\n"
    a = "Ratio of current sensitivity of M1 to M2 is given by, n1 x b1 x a1 x k2 : n2 x b2 x a2 x k1 = " + str(n1) + " x " + str(b1) + " x " + str(a1) + " x " + str(k2) + " : " + str(n2) + " x " + str(b2) + " x " + str(a2) + " x " + str(k1) + " = " + str(cal1(n1,a1, r1, k1, b1, n2, a2, r2, b2, k2)) + "\n"
    return q,a

def type2() :
    n1 = random.randint(1,10)
    r1 = random.randint(1,10)
    a1 = random.randint(1,10)
    a1 = a1 * (10**-4)
    k1 = random.randint(1,10)
    b1 = random.randint(1,10)
    n2 = random.randint(1,10)
    r2 = random.randint(1,10)
    a2 = random.randint(1,10)
    a2 = a2 * (10**-4)
    k2 = random.randint(1,10)
    b2 = random.randint(1,10)
    q = "Two moving coil meters M1 and M2 have the following particulars R1 = " + str(r1) + " ohms, N1 = " + str(n1) + ", A1 = " + str(a1) + " m2 , B1 = " + str(b1) + " T, K1 = " + str(k1) + " and  R2 = " + str(r2) + " ohms, N2 = " + str(n2) + " , A1 = " + str(a2) + " m2 , B1 = " + str(b2) + " T, K2 = " + str(k2) + ". Determine the ratio of voltage sensitivities of M1 and M2.\n"
    a = "Ratio of voltage sensitivity of M1 to M2 is is given by, n1 x b1 x a1 x k2 x r2 : n2 x b2 x a2 x k1 x r1 = " + str(n1) + " x " + str(b1) + " x " + str(a1) + " x " + str(k2) + " x " + str(r2) + " : " + str(n2) + " x " + str(b2) + " x " + str(a2) + " x " + str(k1) + " x " + str(r1) + " = " + str(cal1(n1,a1, r1, k1, b1, n2, a2, r2, b2, k2)) + "\n"
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
