import random

# A metre-long tube open at one end, with a movable piston at the other end, shows resonance with a fixed frequency source (a turning fork of frequency 340 Hz) when the tube length is 25.5 cm or 79.3 cm. Estimate the speed of sound in air at the temperature of the experiment. The edge effect may be neglected.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 500000
# no_of_samples = 20

for i in range(no_of_samples):
    freq = random.randint(100,1100)
    length = random.randint(5,95)
    error = random.randint(-8,8)
    q = "A 3m long tube open at one end, with a movable piston at the other end, shows resonance with a fixed frequency source (a turning fork of frequency "+str(freq)+" Hz) when the tube length is "+str(length)+" cm or "+str(length*3+error)+" cm. Estimate the speed of sound in air.\n"
    a = "{:.2e}".format((freq*4*length)/100)+" ms-1\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()