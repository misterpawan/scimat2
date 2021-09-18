import random
import math

# An LC circuit contains a 20 mH inductor and a 50 muF capacitor with an initial charge of 10 mC. The resistance of the circuit is negligible. Let the instant the circuit is closed be t = 0.
# (a) What is the initial energy stored, is it conserved during LC oscillations?
# (b) What is the natural frequency of the circuit.
# (c) At what time(s) energy stored in electrical form is x percent of total energy?
# (d) At what time(s) energy stored in magnetic form is x percent of total energy?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

for i in range(no_of_samples):
    types = random.randint(1,4)
    L = random.randint(1,200)
    C = random.randint(1,200)
    Q = random.randint(1,200)
    E = 0.5*(Q**2)*(1/C)
    v = 1/(2*math.pi*math.sqrt(L*C*(10**(-9))))
    q = "An LC circuit contains a "+str(L)+" mH inductor and a "+str(C)+" muF capacitor with an initial charge of "+str(Q)+" mC. The resistance of the circuit is negligible. Let the instant the circuit is closed be t = 0. "
    if types <= 2:
        if types == 1:
            q = q + "What is the initial energy stored, is it conserved during LC oscillations?\n"
            a = "{:.2e} joule, it is conserved during oscillations.\n".format(E)
        else:
            q = q + "What is the natural frequency of the circuit.\n"
            a = "{:.2e} hertz\n".format(v)
    else:
        x = random.randint(0,100)
        arr = ["electrical","magnetic"]
        q = q + "At what time(s) energy stored in "+arr[types-3]+" form is "+str(x)+" percent of total energy?\n"
        if types == 4:
            x = 100-x
        x = x/100
        angle = math.acos(2*x-1)
        T = (1/v)
        frac = (1/(4*math.pi))*angle
        a = str(round(frac,2))+"t, "+str(round(frac+0.5,2))+"t, "+str(round(frac+1,2))+"t, ...; where t = "+"{:.2e} s\n".format(T)
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()