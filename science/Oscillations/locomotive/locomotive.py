import random
import math

# The piston in the cylinder head of a locomotive has a stroke (twice the amplitude) of 1.0 m. If the piston moves with simple harmonic motion with an angular frequency of 200 rev/min, what its amplitude of piston, maximum speed?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    ratio = random.randint(2,10)
    freq = random.randint(100,2000)
    amp = random.randint(10,200)
    q = "The piston in the cylinder head of a locomotive has a stroke ("+str(ratio)+" times the amplitude) of "+str(amp)+" m. If the piston moves with SHM with an angular frequency of "+str(freq)+" rev/min, what its amplitude, maximum speed?\n"
    amp2 = amp/ratio
    v = (freq*amp2)/60 
    a = "amplitude is "+"{:.2e}".format(amp2) + " m, its maximum speed is "+"{:.2e}".format(v)+" ms-1\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()