import random

# In a test experiment on a model aeroplane in a wind tunnel, the flow speeds on the upper and lower surfaces of wing are v1 ms-1 and v2 ms-1. What is the lift on the wing if its area is 2.5 m2?(Take the density of air to be 1.3 kgm-3)
# In a test experiment on a model aeroplane in a wind tunnel, the flow speeds on the upper and lower surfaces of wing are v1 ms-1 and v2 ms-1. What is the lift on the wing if its area is 2.5 m2?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    v2 = random.randint(1,100)
    v1 = random.randint(v2+1,v2+40)
    A = random.randint(1,400)*100
    types = random.randint(0,1)
    if types:
        q = "In a test experiment on a model aeroplane in a wind tunnel, the flow speeds on the upper and lower surfaces of wing are "+str(v1)+" ms-1 and "+str(v2)+" ms-1. What is the lift on the wing if its area is "+str(A)+" cm2?(Take the density of air to be 1.3 kgm-3)\n"
    else:
        q = "In a test experiment on a model aeroplane in a wind tunnel, the flow speeds on the upper and lower surfaces of wing are "+str(v1)+" ms-1 and "+str(v2)+" ms-1. What is the lift on the wing if its area is "+str(A)+" cm2?\n"
    p = 0.5*1.3*(v1**2-v2**2)
    F = p*(A/10000)
    a = str(round(F,1))+" newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()