import random
import math

# During blood transfusion, the needle is inserted in a vein where the gauge pressure is 2000 Pa. At what height must the blood container be placed so that blood may just enter the vein? Given: density of whole blood = 1.06 x 10^3 kg m-3.
# (a) What is the largest average velocity of blood flow in an artery of radius 2 x 103 m if the flow must remain laminar?
# (b) What is the corresponding flow rate? Take viscosity of blood to be 2.084 x 10-3 Pa-s. Density of blood is 1.06 x 103 kg/m3 .

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

def type1():
    p = random.randint(1000,11000)
    h = (p/(1060*9.8))*1000
    h1 = random.randint(max(0,round(h)-200),round(h)+200)
    q = "During blood transfusion, the needle is inserted in a vein where the gauge pressure is "+str(p)+" Pa. If the blood container is placed at "+str(h1)+" mm above the earth level so that blood may just enter the vein, is it safe for the patient?.\n"
    if h1 > h:
        a = "yes, patient is safe\n"
    else:
        a = "no, patient is not safe\n"
    return q,a

def type2():
    r = random.randint(1,2000)
    l = random.randint(1,2000)
    q = "What is the largest average velocity of blood flow in an artery of radius "+str(r)+" micrometer and length "+str(l)+" mm if flow must remain laminar, what is the corresponding flow rate.\n"
    vc = (2000*2.084)/(1.06*2*r)
    flowrate = math.pi*r*r*vc*(10**(-12))
    a = "velocity is "+str(round(vc,2))+" ms-1, corresponding flow rate is "+"{:.2e}".format(flowrate)+" m3s-1\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types == 0:
        q,a = type1()
    elif types == 1:
        q,a = type2()
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()