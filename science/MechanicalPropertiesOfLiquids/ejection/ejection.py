import random
import math

# The cylindrical tube of a spare pump has a cross-section of 8.0 cm2 one end of which has 40 fine holes each of diameter 1.0 mm. If the liquid flow inside the tube is 1.5 m min-1, what is the speed of ejection of the liquid through the holes?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 500000
# no_of_samples = 20

for i in range(no_of_samples):
    A = random.randint(1,100)
    num = random.randint(1,200)
    dia = random.randint(1,10)
    flow = random.randint(1,10)
    q = "The cylindrical tube of a spare pump has a cross-section of "+str(A)+" cm2 one end of which has "+str(num)+" fine holes each of diameter "+str(dia)+" mm. If the liquid flow inside the tube is "+str(flow)+" m min-1, what is the speed of ejection of the liquid through the holes?\n"
    a1 = A*(10**(-4))
    v1 = flow/60
    a2 = math.pi*dia*dia*0.25*(10**(-6))
    v2 = (a1*v1)/a2
    a = "{:.2e}".format(v2) + " ms-1\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()