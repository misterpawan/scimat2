import random
import math

# In a p-n junction diode, the current I can be expressed as I = I0*exp((e*V/2*k_b*T)-1), k_b = 8.6 * 10^(-5) eV/K. If for given diode I0 = 5 x 10^(-12) A and T = 300

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1500000
e = 1.6 * (10**(-19))
k_b2 = 1.376 * (10**(-23))

for i in range(no_of_samples):
    I0 = random.randint(1000,3000)
    T = random.randint(280,300)
    types = random.randint(1,3)
    q = "In a p-n junction diode, the current I can be expressed as I = I0*exp((e*V/2*k_b*T)-1), k_b = 8.6 * 10^(-5) eV/K. If for given diode I0 = "+str(I0)+" x 10^(-15) A and T = "+str(T)+" K, "
    if types == 1:
        V = round(random.randint(100,300)/1000,3)
        q = q + "what will be the forward current at a forward voltage of "+str(V)+" V?\n"
        a = (I0*(10**(-15)))*math.exp((e*V)/(k_b2*T)-1)
        a = "{:.2e} ampere\n".format(a)
    elif types == 2:
        V1 = round(random.randint(1,20)/10,1)
        V2 = round(random.randint(1,20)/10,1)
        q = q + "what will be the increase in the current if the voltage across the diode is increased from "+str(V1)+" V to "+str(round(V1+V2,1))+" V?\n"
        I1 = (I0*(10**(-15)))*math.exp((e*V1)/(k_b2*T)-1)
        I2 = (I0*(10**(-15)))*math.exp((e*(V1+V2))/(k_b2*T)-1)
        a = "{:.2e} ampere\n".format(I2-I1)
    elif types == 3:
        V1 = round(random.randint(1,20)/10,1)
        V2 = round(random.randint(1,20)/10,1)
        q = q + "what will be dynamic resistance if the voltage across the diode is increased from "+str(V1)+" V to "+str(round(V1+V2,1))+" V?\n"
        I1 = (I0*(10**(-15)))*math.exp((e*V1)/(k_b2*T)-1)
        I2 = (I0*(10**(-15)))*math.exp((e*(V1+V2))/(k_b2*T)-1)
        a = "{:.2e} ohm\n".format((V2)/(I2-I1))        
 

    # print(q)
    # print(a)
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()