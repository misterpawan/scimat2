import random

# The edge of a cube is 10 cm long. One face of the cube is firmly fixed to a vertical wall. A mass of 100 kg is then attached to the opposite face of the cube. The shear modulus of material of cube is 25 GPa. What is the vertical deflection of this face?
# A piece of copper having a rectangular cross-section of 15.2 mm x 19.1 mm is pulled in tension with 44,500 N force, producing only elastic deformation. Calculate the resulting strain? Shear modulus of elasticity of copper is 42 x 10^9 N/m2.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        s = random.randint(1,200)
        m = random.randint(20,200)
        Y = random.randint(1,200)
        q = "The edge of a cube is "+str(s)+" cm long. One face of the cube is firmly fixed to a vertical wall. A mass of "+str(m)+" kg is then attached to the opposite face of the cube. The shear modulus of material of cube is "+str(Y)+" GPa. What is the vertical deflection of this face?\n"
        a = (m*9.8)/(Y*(10**9)*(s*(10**(-2))))
        a = str(round(a*10**(9),1))+" nm\n"
    else:
        l = random.randint(1,100)
        b = random.randint(1,100)
        F = random.randint(1,800)*100
        q = "A piece of copper having a rectangular cross-section of "+str(l)+" mm x "+str(b)+" mm is pulled in tension with "+str(F)+" N force, producing only elastic deformation. Calculate the resulting strain? Shear modulus of elasticity of copper is 42 x 10^9 N/m2.\n"
        A = l*b*(10**(-6))
        a = F/(A*(42*(10**9)))
        a = str(round(a*(10**6),1))+" x 10^(-6)\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()