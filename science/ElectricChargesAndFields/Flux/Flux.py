import random
import math

# In an uniform electric field of E, what is the flux through a square of s cm, whose plane is parallel to yz-plane.
# In an uniform electric field of E, what is the flux through a square of s cm, whose plane is at theta degrees angle with x-axis.
# A Black box has net outward flux of F through its surface. What is the net charge inside the box?
# A point charge of q1 C is at distance d/2 cm directly above the centre of the square of side d cm, What is the flux through the square.
# A point charge of q1 C is at centre of cubic guassian surface d cm on edge. What is the net flux through the surface?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,5)
    if types == 1:
        E = random.randint(100,10100)
        d = random.randint(1,400)
        q = "In an uniform electric field of "+str(E)+" i N/C, what is the flux through a square of "+str(d)+" cm, whose plane is parallel to yz-plane?\n"
        a = "{:.2e}".format(E*d*d*(10**(-4)))+" newton-m2/coulomb\n"
    elif types == 2:
        E = random.randint(10,1010)*10
        d = random.randint(1,50)
        angle = random.randint(0,90)
        q = "In an uniform electric field of "+str(E)+" i N/C, what is the flux through a square of "+str(d)+" cm, whose plane is at "+str(angle)+" degrees angle with x-axis?\n"
        a = "{:.2e}".format(E*d*d*(10**(-4))*math.cos(angle*(math.pi/180)))+" newton-m2/coulomb\n"
    elif types == 3:
        F = random.randint(1000,2001000)
        q = "A Black box has net outward flux of "+str(F)+" N-m2/C through its surface. What is the net charge inside the box?\n"
        a = "{:.2e}".format(8.854*(10**(-12))*F)+" coulomb\n"
    elif types == 4:
        q1 = random.randint(100,10100)
        d = random.randint(1,400)
        q = "A point charge of "+str(q1)+" x 10^(-9)C is at distance "+str(d)+" cm directly above the centre of the square of side "+str(2*d)+" cm, What is the flux through the square\n"
        a = "{:.2e}".format((1000*q1)/(6*8.854))+" newton-m2/coulomb\n"
    else:
        q1 = random.randint(100,10100)
        d = random.randint(1,400)
        q = "A point charge of "+str(q1)+" x 10^(-9)C is at centre of cubic guassian surface "+str(d)+" cm on edge. What is the net flux through the surface?\n"
        a = "{:.2e}".format((1000*q1)/(8.854))+" newton-m2/coulomb\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
    
qns.close()
ans.close()
