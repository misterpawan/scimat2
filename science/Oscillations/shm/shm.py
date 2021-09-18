import random
import math

# What is the time period of the shm with equation A1sin(bwt)+A2cos(bwt).
# What is the phase of the shm with equation A1sin(bwt)+A2cos(bwt).
# What is the amplitude of the shm with equation A1sin(bwt)+A2cos(bwt).

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20
# π

for i in range(no_of_samples):
    types = random.randint(0,2)
    qn = ["time period","phase","amplitude"]
    a1 = random.randint(-200,200)
    a2 = random.randint(-200,200)
    b = random.randint(-200,200)
    while b==0:
        b = random.randint(-200,200)
    q = "What is the "+qn[types]+" of the shm with equation ("+str(a1)+")*sin("+str(b)+"wt) + ("+str(a2)+")*cos("+str(b)+"wt)?\n"
    if types == 0:
        a = "2π/"+str(abs(b))+"w sec\n"
    elif types == 1:
        q = q[:-1] + " (i.e., if written as Asin(bwt+theta), then what is the value of theta)\n"
        if a1 != 0:
            a = str(round(math.atan(a2/a1)*(180/math.pi))) + " degrees\n"
        else:
            a = "90 degrees\n"
    else:
        a = str(round(math.sqrt(a1**2+a2**2))) + "\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()