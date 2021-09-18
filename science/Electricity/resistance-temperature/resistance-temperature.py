import random

# At temperature(T1 degree C) the resistance of a heating element is R1. What is the temperature of the element if the resistance is found to be R2(temp coeff = 1.7 x 10^(-4) degree C-1)?
# A wire made up of unknown material has a resistance R1 at T1 degree C, and a resistance of R2 at T2 degree C. Determine the temperature coefficient of resistivity of that material?
# A heating element using nichrome connected to a V V supply draws an initial current of I A which settles after a few seconds to a steady value of I2 A. What is the steady temperature of the heating element if room temperature is T degree C(temp coeff of nichrome is 1.70 x 10^(-4) degree C-1)?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        T = random.randint(0,200)
        R1 = random.randint(1,800)
        R2 = random.randint(1,50)
        q = "At temperature("+str(T)+" degree C) the resistance of a heating element is "+str(R1)+" ohm. What is the temperature of the element if the resistance is found to be "+str(R1+R2)+" ohm(temp coeff = 1.7 x 10^(-4) degree C-1)?\n"
        a = str(round((R2/(R1*1.7*(10**(-4)))+T),1)) + " degree centigrade\n" 
    elif types == 2:
        R1 = random.randint(1,200)
        T1 = random.randint(1,200)
        R2 = random.randint(1,20)
        T2 = random.randint(1,20)
        q = "A wire made up of unknown material has a resistance "+str(R1)+" ohm at "+str(T1)+" degree C, and a resistance of "+str(R1+R2)+" ohm at "+str(T1+T2)+" degree C. Determine the temperature coefficient of resistivity of that material?\n"
        a = "{:.2e} degree centigrade-1".format((R2/(R1*T2))) + "\n"
    else:
        V = random.randint(220,240)
        I1 = random.randint(1,2000)
        I2 = random.randint(1,200)
        R1 = (V/(I1+I2))*1000
        R2 = (V/I1)*1000
        q = "A heating element using nichrome connected to a "+str(V)+" V supply draws an initial current of "+str(I1+I2)+" mA which settles after a few seconds to a steady value of "+str(I1)+" mA. What is the steady temperature of the heating element if room temperature is 27 degree C(temp coeff of nichrome is 1.70 x 10^(-4) degree C-1)?\n"
        a = str(round((R2-R1)/(R1*(1.7*(10**(-4))))+27,1)) + " degree centigrade\n"
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
