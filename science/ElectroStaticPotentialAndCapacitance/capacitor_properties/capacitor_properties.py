import random

# A capacitor with air between it's parallel plates has a capacitance of 8 pF. What will be the capacitance if the distance between the plates is reduced by half, and the space between them is filled with a substance of dielectric constant 6?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm. Calculate the capacitance of the capacitor?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply, find charge on each plate of the capacitor?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply and a 3 mm thick mica sheet is inserted between the plates, then what will happen?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply and a 3 mm thick mica sheet is inserted between the plates and then supply is disconnected, then what will happen?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 3000000
# no_of_samples = 30

for i in range(no_of_samples):
    types = random.randint(1,5)
    if types == 1:
        c = random.randint(1,2000)
        dist_ratio = random.randint(1,10)
        dielectric = random.randint(1,200)
        q = "A capacitor with air between it's parallel plates has a capacitance of "+str(c)+" pF. What will be the capacitance if the distance between the plates is reduced to 1/"+str(dist_ratio)+", and the space between them is filled with a substance of dielectric constant "+str(dielectric)+"?\n"
        a = "{:.3e}".format(c*dist_ratio*dielectric)+" pico-farad\n"
    elif types == 2:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,2000)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm. Calculate the capacitance of the capacitor?\n"
        a = "{:.2e}".format((8.854*A)/(d*0.001))+" pico-farad\n"
    elif types == 3:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply, find charge on each plate of the capacitor?\n"
        a = "{:.2e}".format((8.854*A*V*(10**(-12)))/(d*0.001)) + " coulomb\n"
    elif types == 4:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply and a "+str(d)+" mm thick mica sheet is inserted between the plates, then what will happen?\n"
        c1 = (8.854*A*6)/(d*0.001)
        q1 = (8.854*A*6*V*(10**(-12)))/(d*0.001)
        a = "capacitance becomes {:.2e}".format(c1) + " pico-farad, "+"charge becomes {:.2e}".format(q1)+" coulomb\n"
    elif types == 5:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply and a "+str(d)+" mm thick mica sheet is inserted between the plates and then supply is disconnected, then what will happen?\n"
        c1 = (8.854*A*6)/(d*0.001)
        q1 = (8.854*A*V*(10**(-12)))/(d*0.001)
        a = "capacitance becomes {:.2e}".format(c1) + " pico-farad, "+"charge remains {:.2e}".format(q1)+" coulomb\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close() 