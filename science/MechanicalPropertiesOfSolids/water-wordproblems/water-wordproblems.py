import random

# What is the density of water at a depth where pressure is 80.0 atm, given that its density at the surface is 1.03 x 10^3 kgm-3
# How much should be pressure the a litre of water be changed to compress it by 0.10 %? Bulk modulus of elasticity of water = 2.2 x 10^9 Nm-2.
# The trench is located in the Ocean. The water pressure at the bottom of the trench is about 1.1 x 10^8 Pa. A steel ball of initial volume 0.32 m3 is dropped into the ocean and falls to the bottom of the trench. What is the change in the volume of the ball when it reaches to the bottom?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
# no_of_samples = 20

def type1():
    extra = random.randint(100,40000)
    den = random.randint(950,1050)
    delvbyv = extra*45.8*(10**(-8))
    p_qn = round(extra*1000+(1.013*(10**5)))
    q = "What is the density of water at a depth where pressure is "+str(p_qn)+" Pa, given that its density at the surface is "+str(den)+" kgm-3?\n"
    a = den/(1-delvbyv)
    a = str(round(a,1))+" kgm-3\n"
    return q,a

def type2():
    percent = round(random.randint(1,999)/10,1)
    vol = random.randint(1,10000)
    q = "How much should be pressure the a "+str(vol)+" ml of water be changed to compress it by "+str(percent)+" %? Bulk modulus of elasticity of water = 2.2 x 10^9 Nm-2.\n"
    a = ((2*(10**9))*percent)/100
    a = "{:.1e}".format(a) + " pascal\n"
    return q,a

def type3():
    p_bot = random.randint(50,10000)
    v = random.randint(1,1000)
    q = "The trench is located in the Ocean. The water pressure at the bottom of the trench is about "+str(p_bot)+" x 10^4 Pa. A steel ball of initial volume "+str(v)+" dm3 is dropped into the ocean and falls to the bottom of the trench. What is the change in the volume of the ball when it reaches to the bottom?\n"
    delv = (p_bot*10*v)/(1.6*(10**11))
    a = "{:.1e}".format(delv) + " m3\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,5)
    if types == 1 or types == 4:
        q,a = type1()
    elif types == 2:
        q,a = type2()
    elif types == 3 or types == 5:
        q,a = type3()
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()