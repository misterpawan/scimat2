import random
import math

# A radio can tune over the frequency range of a portion of MW broadcast band: (f1 kHz to f2 kHz). If its LC circuit has an effective inductance of 200 muH, what must be the range of its variable capacitor?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
pi = math.pi

for i in range(no_of_samples):
    f1 = random.randint(100,2000)
    f2 = random.randint(100,400)
    L = random.randint(100,400)
    q = "A radio can tune over the frequency range of a portion of MW broadcast band: ("+str(f1)+" kHz to "+str(f1+f2)+" kHz). If its LC circuit has an effective inductance of "+str(L)+" muH, what must be the range of its variable capacitor?\n"
    w1 = 2*pi*f1
    C1 = 1/((w1**2)*L)
    w2 = 2*pi*(f1+f2)
    C2 = 1/((w2**2)*L)
    a = "{:.2e} farad to {:.2e} farad\n".format(C2,C1)
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()