import random

# For the travelling harmonic wave
# y(x, t) = 2.0 cos 2π (10t – 0.0080x + 0.35)
# where x and y are in cm and t in s. Calculate the phase difference between oscillatory motion of two points separated by a distance of
# (a) 4 m (b) 0.5 m
# (c) λ/2 (d) 3λ/4.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    amp = random.randint(1,50)
    w = random.randint(1,50)
    k = round(random.randint(1,50)/1000,3)
    types = random.randint(1,2)
    q = "For the travelling harmonic wave y(x, t) = "+str(amp)+" cos 2π ("+str(w)+"t – "+str(k)+"x + 0.35) where x and y are in cm and t in s. Calculate the phase difference between oscillatory motion of two points separated by a distance of "
    lamda = 1/k
    if types == 1:
        dist = random.randint(1,20)
        q = q + str(dist)+" m?\n"
        phase_diff = (2*dist*100)/(lamda)
    else:
        num = random.randint(1,6)
        den = random.randint(1,6)
        while num == den:
            den = random.randint(1,6)
        q = q +str(num)+"λ/"+str(den)+" ?\n"
        phase_diff = (2*num)/den
    a = str(round(phase_diff,1))+" π rad\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()