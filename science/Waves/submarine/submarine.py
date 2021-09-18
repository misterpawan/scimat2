import random

# A SONAR system fixed in a submarine operates at a frequency 40.0 kHz. An enemy submarine moves towards the SONAR with a speed of 360 km h-1. What is the frequency of sound reflected by the submarine? Take the speed of sound in water to be 1450 ms-1.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    f = random.randint(1000,9000)*10
    v = random.randint(100,900)
    q = "A SONAR system fixed in a submarine operates at a frequency "+str(f)+" Hz. An enemy submarine moves towards the SONAR with a speed of "+str(v)+" kmph. What is the frequency of sound reflected by the submarine? Take the speed of sound in water to be 1450 ms-1.\n"
    v1 = v*(5/18)
    nu1 = ((1450+v1)/(1450-v1))*f
    a = "{:.2e}".format(nu1) + " hertz\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()