import random

# A p-n photodiode is fabricated from a semiconductor with band gap of 2.8 eV. Can it detect a wavelength of 6000 nm?
# The number of silicon atoms per m3 is N1. This is doped simultaneously with N2 atoms per m3 of Arsenic and N3 atoms per m3 of Indium. Given that the ni = Ni m^(-3), calculate the number of electrons?
# The number of silicon atoms per m3 is N1. This is doped simultaneously with N2 atoms per m3 of Arsenic and N3 atoms per m3 of Indium. Given that the ni = Ni m^(-3), calculate the number of holes?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 30

def type1(types):
    N1 = random.randint(1,20)
    N2 = random.randint(1,20)
    N3 = random.randint(1,20)
    Ni = random.randint(1,2000)
    q = "The number of silicon atoms per m3 is "+str(N1)+" x 10^28. This is doped simultaneously with "+str(N2)+" x 10^(22) atoms per m3 of Arsenic and "+str(N3)+" x 10^20 atoms per m3 of Indium. Given that the ni = "+str(Ni)+" x 10^16 m^(-3), "
    Ne = N2*(10**22)-Ni*(10**16)
    Nh = (Ni*(10**(16)))**2/(Ne)
    if types == 1:
        q = q + "calculate the number of electrons, is it p-type or n-type?\n"
        a = "{:.2e}, n-type semiconductor\n".format(Ne)
    elif types == 0:
        q = q + "calculate the number of protons, is it p-type or n-type?\n"
        a = "{:.2e}, n-type semiconductor\n".format(Nh)
    return q,a

def type2():
    V = round(random.randint(1,200)/100,2)
    wavelen = random.randint(1,20000)
    q = "A p-n photodiode is fabricated from a semiconductor with band gap of "+str(V)+" eV. Can it detect a wavelength of "+str(wavelen)+" nm?\n"
    h = 6.626 * (10**(-34))
    c = 3 * (10**8)
    wavelen = wavelen*(10**(-9))
    E = (h*c)/(wavelen*(1.6*(10**(-19))))
    # print(E,V)
    if E > V:
        a = "yes, it can detect\n"
    else:
        a = "no, it cannot detect\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types!=2:
        q,a = type1(types)
    else:
        q,a = type2()
    # print(q)
    # print(a)
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()