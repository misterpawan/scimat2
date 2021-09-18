import random
import math

# Glycerine flows steadily through a horizontal tube of length 1.5 m and radius 1.0 cm. If the amount of glycerine collected per second at one end is 4.0 x 10-3 kg s-1, what is the pressure difference between the two ends of the tube? (Density of glycerine = 1.3 x 103 kg m-3 and viscosity of glycerine = 0.83 Pa s).

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    l = random.randint(100,2000)
    r = random.randint(1,10)
    rate = random.randint(100,1000)
    types = random.randint(0,1)
    if types:
        q = "Glycerine flows steadily through a horizontal tube of length "+str(l)+" mm and radius "+str(r)+" cm. If the amount of glycerine collected per second at one end is "+str(rate)+" x 10-4 kg s-1, what is the pressure difference between the two ends of the tube? (Density of glycerine = 1.3 x 10^3 kg m-3 and viscosity of glycerine = 0.83 Pa s)\n"
    else:
        q = "Glycerine flows steadily through a horizontal tube of length "+str(l)+" mm and radius "+str(r)+" cm. If the amount of glycerine collected per second at one end is "+str(rate)+" x 10-4 kg s-1, what is the pressure difference between the two ends of the tube?\n"
    V = (rate*(10**(-4)))/1300
    p = (8*V*0.83*l*100000)/(math.pi*(r**4))
    a = "{:.2e}".format(p) + " pascal\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()