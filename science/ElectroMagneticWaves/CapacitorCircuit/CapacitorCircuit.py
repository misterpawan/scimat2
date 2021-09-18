import random
import math

# A capacitor made of two circular plates of radius r cm, and separated by s cm. The capacitor is being charged by an external source. The charging current is constant and equal to I A.
# (a) Calculate the capacitance between the plates
# (b) Calculate the rate of charge of potential difference between the plates.
# (c) Obtain the displacement current across the plates.

# A parallel plate capacitor made of circular plates of radius r = r cm has a capacitance C = c pF. The capacitor is connected to a V V ac supply with a(angular) frequency of f rad s-1.
# (a) What is the rms value of the conduction current?
# (b) Determine the amplitude of B at a point d cm from the axis between the plates?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
pi = math.pi

for i in range(no_of_samples):
    types = random.randint(1,13)
    if types <= 7:
        r = random.randint(1,200)
        s = random.randint(1,200)
        I = random.randint(1,200)
        ep = 8.85 * (10**(-12))
        C = (ep*pi*r*r*0.01)/s
        q = "A capacitor made of two circular plates of radius "+str(r)+" cm, and separated by "+str(s)+" cm. The capacitor is being charged by an external source. The charging current is constant and equal to "+str(I)+" mA. "
        if types <=3:
            q = q + "Calculate the capacitance between the plates?\n"    
            a = "{:.2e} farad\n".format(C)
        elif types<=6:
            q = q + "Calculate the rate of charge of potential difference between the plates?\n"
            a = "{:.2e} volt/s\n".format(I/(C*1000))
        else:
            q = q + "Obtain the displacement current across the plates?\n"
            a = str(round(I/1000,3)) + " ampere\n"
    else:
        r = random.randint(10,200)
        c = random.randint(1,200)
        f = random.randint(1,200)*10
        I = 230*f*c*(10**(-12))
        q = "A parallel plate capacitor made of circular plates of radius r = "+str(r)+" cm has a capacitance C = "+str(c)+" pF. The capacitor is connected to a 230 V ac supply with a(angular) frequency of "+str(f)+" rad/s. "
        if types <=10:
            q = "What is the rms value of the conduction current?\n"
            a = "{:.2e} ampere\n".format(I)
        else:
            d = random.randint(1,10)
            q = "Determine the amplitude of B at a point "+str(d)+" cm from the axis between the plates?\n"
            mu0 = 2*(10**(-7))
            I0 = math.sqrt(2)*I
            B = (mu0*d*I0)/(r*r*0.01)
            a = "{:.2e} tesla\n".format(B)
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
