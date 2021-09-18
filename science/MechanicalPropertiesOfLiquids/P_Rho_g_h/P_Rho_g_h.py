import random

# Toricelli’s barometer used mercury. If someone duplicated it using some liquid of density 984 kgm-3. Determine the height of the liquid column for normal atmospheric pressure (density of material of barometer is 984 kgm-3).
# A vertical off-shore structure is built to withstand a maximum stress of 10^9 Pa. Is the structure suitable for putting up on top of an oil well in the ocean? Take the depth of the ocean to be roughly 3 km, and ignore ocean currents?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        d1 = random.randint(100,3000)
        d2 = random.randint(100,3000)
        q = "Toricelli’s barometer used mercury. If someone duplicated it using some liquid of density "+str(d1)+" kgm-3. Determine the height of the liquid column for normal atmospheric pressure (density of material of barometer is "+str(d2)+" kgm-3).\n"
        h = (1.01*(10**5))/(d1*9.8)
        a = str(round(h,1))+" m\n"
    else:
        d = random.randint(1,10)
        P = d*1000*980
        p = random.randint(P-200000,P+200000)
        q = "A vertical off-shore structure is built to withstand a maximum stress of "+str(p)+" Pa. Is the structure suitable for putting up on top of an oil well in the ocean? Take the depth of the ocean to be roughly "+str(d)+" km, and ignore ocean currents?\n"
        if P <= p:
            a = "no, it is not suitable\n"
        else:
            a = "yes, it is suitable\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()