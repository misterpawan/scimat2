import random
import math

# Suppose that the electric field part of an electromagnetic wave in vacuum is E = E0cos[ky+wt].

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
pi = math.pi

for i in range(no_of_samples):
    types = random.randint(1,10)
    E0 = random.randint(1,2000)
    k = random.randint(1,2000)
    w = round((3*(10**8))/k)
    q = "Suppose that the electric field part of an electromagnetic wave in vacuum is E = "+str(E0)+"cos["+str(k)+"y+"+str(w)+"t]. "
    if types <= 2:
        q = q + "What is the wavelength?\n"
        a = "{:.2e} m\n".format((2*pi)/k)
    elif types <= 4:
        q = q + "What is the frequency?\n"
        a = "{:.2e} rad/s\n".format(w/(2*pi))
    elif types <= 6:
        q = q + "What is the amplitude of the magnetic field part of the wave?\n"
        B0 = E0/(3*(10**8))
        a = "{:.2e} tesla\n".format(B0)
    elif types <= 10:
        q = q + "Write an expression for the magnetic field part of the wave?\n"
        B0 = E0/(3*(10**8))
        a = "{:.2e}".format(B0)+"cos["+str(k)+"y+"+str(w)+"t]\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()
