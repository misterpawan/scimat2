import random
import math

# Four identical hollow cylindrical columns of mild steel support a big structure of mass 50,000 kg. The inner and outer radii of each column are 30 cm and 60 cm respectively. Assuming the load distribution to be uniform, calculate the compressional strain of each column. Young’s modulus, Y = 2.0 x 10^11 Pa.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20
number = [4,6,9,12,15,16]

for i in range(no_of_samples):
    num = number[random.randint(0,5)]
    r1 = random.randint(10,40)
    r2 = random.randint(r1+10,r1+40)
    m = random.randint(1000,5000)*10
    q = str(num)+" identical hollow cylindrical columns of mild steel support a big structure of mass "+str(m)+" kg. The inner and outer radii of each column are "+str(r1)+" cm and "+str(r2)+" cm respectively, calculate the compressional strain of each column.\n"
    F = (m*9.8)/num
    A = math.pi*(r2**2-r1**2)*(10**(-4))
    strain = F/(A*(2*(10**11)))
    a = str(round(strain*(10**9),1))+" x 10^(-9)\n" 
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()