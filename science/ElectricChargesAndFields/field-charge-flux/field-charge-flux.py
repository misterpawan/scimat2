import random
import math

# A sphere of radius d1 cm has unknown charge. If the electric field at d2 cm from the centre of sphere is E N/C and points radially inward, then what is the net charge on the sphere?
# A uniformly charged conducting sphere of d cm diameter has a surface charge density of D mu-C/m2, then find the charge on the sphere?
# A uniformly charged conducting sphere of d cm diameter has a surface charge density of D mu-C/m2, then find the electric flux leaving the sphere?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

for i in range(no_of_samples):
    types = random.randint(1,6)
    if types < 3:
        d1 = random.randint(1,100)
        d2 = random.randint(1,100)
        E = random.randint(1,800)*10
        arr = ["inward","outward"]
        arr2 = ["-",""]
        types2 = types-1
        q = "A sphere of radius "+str(d1)+" cm has unknown charge. If the electric field at "+str(d1+d2)+" cm from the centre of sphere is "+str(E)+" N/C and points radially "+arr[types2]+", then what is the net charge on the sphere?\n"
        a = arr2[types2]+"{:.2e}".format(E*((d1+d2)**2)*(1/(9*(10**9))))+" C\n"
    else:
        d = random.randint(1,2000)
        D = random.randint(1,2000)
        q = "A uniformly charged conducting sphere of "+str(d)+" cm diameter has a surface charge density of "+str(D)+" micro-C/m2, then find the "
        if types < 5:
            q = q + "charge on the sphere?\n"
            a = "{:.2e}".format(D*4*math.pi*(d/2)*(d/2)*(10**(-10)))+" coulomb\n"
        else:
            q = q + "electric flux leaving the sphere?\n"
            a = "{:.2e}".format(D*4*math.pi*(d/2)*(d/2)*(10**(-10))*(1/(8.854*(10**(-12)))))+" newton-m2/coulomb\n"
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()