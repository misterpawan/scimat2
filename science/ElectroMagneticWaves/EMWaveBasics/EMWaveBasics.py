import random
import math

# Suppose that the electric field amplitude of an electromagnetic wave is E0 = 120 N/C and that its frequency is v = 50 MHz. 
# (a) determine B0?
# (b) determine angular frequency?
# (c) determine k?
# (d) determine wavelength?
# (e) find expression for E?
# (f) find expression for B?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
pi = math.pi

for i in range(no_of_samples):
    types = random.randint(1,22)
    E0 = random.randint(1,2000)
    v = random.randint(1,2000)
    q = "Suppose that the electric field amplitude of an electromagnetic wave is E0 = "+str(E0)+" N/C and that its frequency is v = "+str(v)+" MHz. "
    if types <= 2:
        q = q + "Determine B0?\n"
        a = "{:.2e} tesla\n".format(E0/(3*(10**8)))
    elif types <= 4:
        q = q + "Determine angular frequency?\n"
        a = "{:.2e} rad/s\n".format(2*pi*(10**6)*v)
    elif types <= 7:
        q = q + "Determine k?\n"
        w = 2*pi*(10**6)*v
        a = "{:.2e} rad/m\n".format(w/(3*(10**8)))
    elif types <= 10:
        q = q + "Determine wavelength?\n"
        an = 300/v
        a = str(round(an,2)) + " m\n"
    elif types <= 15:
        q = q + "Find an expression for E?\n"
        w = 2*pi*(10**6)*v
        k = w/(3*(10**8))
        a = str(E0)+"sin["+"{:.2e}".format(k)+"x-"+"{:.2e}".format(w)+"t]\n"
    else:
        q = q + "Find an expression for B?\n"
        w = 2*pi*(10**6)*v
        k = w/(3*(10**8))
        B0 = E0/(3*(10**8))
        a = "{:.2e}".format(B0)+"sin["+"{:.2e}".format(k)+"x-"+"{:.2e}".format(w)+"t]\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()
