import random
from num2words import num2words

#2# The storage battery of a car has an emf of V V, if the internal resistance of the battery is R milliohm, what is the maximum current that can be drawn from the battery?
#3# A storage battery of emf V V and internal resistance of R1 ohm is being charged by a V2 V DC supply using a series resistor of R2 ohm. What is the terminal voltage of the battery during charging?
#6# n lead-acid type of secondary cells each of emf V V and internal resistance of R1 ohm are joined in series to provide a supply to a resistor of R2 ohm, what is current drawn/ terminal voltage?
#2# A secondary cell after long use has an emf of V1 V and large internal resistance of R ohm. What is the maximum current can be drawn from the cell?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000

for i in range(no_of_samples):
    types = random.randint(1,13)
    if types <=2 :
        E = random.randint(1,2000)
        r = random.randint(1,2000)
        q = "The storage battery of a car has an emf of "+str(E)+" V, if the internal resistance of the battery is "+str(r)+" milliohm, what is the maximum current that can be drawn from the battery?\n"
        a = str(round((E*1000)/r,1)) + " ampere\n"
    elif types <=5:
        V1 = random.randint(1,20)
        r = random.randint(1,200)
        V = random.randint(20,200)
        R = random.randint(1,30)
        q = "A storage battery of emf "+str(V1)+" V and internal resistance of "+str(r)+" milliohm is being charged by a "+str(V)+" V DC supply using a series resistor of "+str(R)+" ohm. What is the terminal voltage of the battery during charging?\n"
        V_dash = V-V1
        I = V_dash/(R+r)
        a = str(round(V-I*R,1)) + " volt\n"
    elif types <=11:
        n = random.randint(2,20)
        V = random.randint(1,20)
        r = random.randint(1,200)
        R = random.randint(5,200)
        I = (n*V)/(R+n*r*0.001)
        if types <=8:
            q = num2words(n)+" lead-acid type of secondary cells each of emf "+str(V)+" V and internal resistance of "+str(R)+" milliohm are joined in series to provide a supply to a resistor of "+str(R)+" ohm, what is the current drawn?\n"
            a = "{:.2e} ampere\n".format(I)
        else:
            q = num2words(n)+" lead-acid type of secondary cells each of emf "+str(V)+" V and internal resistance of "+str(R)+" milliohm are joined in series to provide a supply to a resistor of "+str(R)+" ohm, what is the terminal voltage?\n"
            a = "{:.2e} volt\n".format(I*R)
    else:
        E = random.randint(1,400)
        R = random.randint(1000,11000)
        q = "A secondary cell after long use has an emf of "+str(E)+" V and large internal resistance of "+str(R)+" ohm. What is the maximum current can be drawn from the cell?\n"
        a = "{:.2e} ampere\n".format(E/R)
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
