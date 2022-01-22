import random

# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply and a 3 mm thick mica sheet is inserted between the plates, then what will happen?
# A capacitor with air between it's parallel plates, each plate has an area of 6 x 10^(-3) m2 and the distance between the plates is 3 mm, if this capacitor is connected to a 100 V supply and a 3 mm thick mica sheet is inserted between the plates and then supply is disconnected, then what will happen?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply and a "+str(d)+" mm thick mica sheet is inserted between the plates, then what will happen?\n"
        c1 = (8.854*A*6)/(d*0.001)
        q1 = (8.854*A*6*V*(10**(-12)))/(d*0.001)
        des = "capacitance becomes = 6 * "+"{:.2e}".format(c1/6) +" = {:.2e}".format(c1) + " pico-farad, "+"charge = capacitance * v =  {:.2e}".format(c1*(10**(-12))) + " * "+str(V)+" = {:.2e}".format(q1)+" coulomb\n"
    elif types == 2:
        A = round(random.randint(1,2000)/10000,4)
        d = random.randint(1,50)
        V = random.randint(1,800)
        q = "A capacitor with air between it's parallel plates, each plate has an area of "+str(A)+" m2 and the distance between the plates is "+str(d)+" mm, if this capacitor is connected to a "+str(V)+" V supply and a "+str(d)+" mm thick mica sheet is inserted between the plates and then supply is disconnected, then what will happen?\n"
        c1 = (8.854*A*6)/(d*0.001)
        q1 = (8.854*A*V*(10**(-12)))/(d*0.001)
        des = "capacitance becomes = 6 * "+"{:.2e}".format(c1/6) +" = {:.2e}".format(c1) + " pico-farad, "+"charge remains  = capacitance * v =  {:.2e}".format((c1/6)*(10**(-12))) + " * "+str(V)+" = {:.2e}".format(q1)+" coulomb\n"
    qns.write(q)
    ans.write(des)
qns.close()
ans.close() 