import random
import math

# Mercury has an angle of contact equal to 140° with soda-lime glass. A narrow tube of radius 1.0 mm made of this glass is dipped in a trough containing mercury. By what amount does the mercury dip down in the tube relative to the liquid surface outside? Surface tension of mercury at the temperature of the experiment is 0.465 Nm-2. Density of mercury = 13.6 x 10 kg m-3
# Two narrow bores of diameters 3.0 mm and 6.0 mm are joined together to form a U-tube open at both ends. If the U-tube contains water, what is the difference in its levels in the two limbs of the tube? Surface tension of water at the temperature of the experiment is 7.3 x 10-2 Nm-2. Take the angle of contact to be zero and density of water to be 1.0 x 103 kg m-3(g = 9.8 ms-2).

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

def type1():
    angle = random.randint(0,180)
    r = random.randint(1,10)
    st = round(random.randint(1,100)/100,2)
    density = random.randint(1,20)
    q = "A liquid has an angle of contact equal to "+str(angle)+" degrees with soda-lime glass. A narrow tube of radius "+str(r)+" mm made of this glass is dipped in a trough containing liquid. By what amount does the liquid dip down in the tube relative to the liquid surface outside? Surface tension of liquid is "+str(st)+" Nm-2. Density of liquid = "+str(density)+" x 10^3 kgm-3\n"
    h = (2*st*math.cos(angle*(math.pi/180)))/(r*density*9.8)
    a = "{:.2e}".format(h) + " m\n"
    return q,a

def type2():
    l1 = random.randint(1,20)
    l2 = random.randint(1,20)
    while l1==l2:
        l2 = random.randint(1,20)
    angle = random.randint(1,180)
    st = random.randint(1,20)
    den = random.randint(1,20)
    q = "Two narrow bores of diameters "+str(l1)+" mm and "+str(l2)+" mm are joined together to form a U-tube open at both ends. If the U-tube contains a unknown liquid, what is the difference in its levels at two ends? Surface tension of liquid is "+str(st)+" x 10^(-2) Nm-2. Take the angle of contact to be "+str(angle)+" degrees and density of liquid to be "+str(den)+" x 10^3 kgm-3.\n"
    common = (2*(st/100)*math.cos(angle*(math.pi/180)))/(den*1000*9.8)
    diff = (1000)*((1/l1)-(1/l2))
    h = abs(common*diff)
    a = "{:.2e}".format(h) + " m\n"
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