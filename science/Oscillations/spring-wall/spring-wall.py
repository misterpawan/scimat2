import random
import math

# A spring having with a spring constant 1200 Nm-1 is mounted on a horizontal table as shown in Fig. A mass of 3 kg is attached to the free end of the spring. The mass is then pulled sideways to a distance of 2.0 cm and released. Determine 
# (i) the frequency of oscillations, 
# (ii) maximum acceleration of the mass, and 
# (iii) the maximum speed of the mass.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
# no_of_samples = 30

for i in range(no_of_samples):
    types = random.randint(0,5)
    qn = ["frequency of oscillations","maximum acceleration","maximum speed"]
    K = random.randint(100,2000)
    m = random.randint(2,80)
    d = random.randint(2,50)
    if types <= 2:
        q = "A spring having with a spring constant "+str(K)+" Nm-1 is mounted on a horizontal table. A mass of "+str(m)+" kg is attached to the free end of the spring. The mass is then pulled sideways to a distance of "+str(d)+" cm and released. Determine "+qn[types]+" of the mass\n"
        if types == 0:
            a = "{:.2e}".format((math.sqrt(K/m))*(1/(2*math.pi)))+" hz\n"
        elif types == 1:
            a = "{:.2e}".format((K*(0.01*d)/m)) + " ms-2\n"
        else:
            a = "{:.2e}".format((0.01*d)*math.sqrt(K/m)) + " ms-1\n"
    else:
        qntype = ["mean position","maximum stretched position","maximum compressed position"]
        q = "A spring with K = "+str(K)+" Nm-1 is mounted on a table. A mass of "+str(m)+" kg is attached to it. The mass is then pulled sideways by distance of "+str(d)+" cm and released. Assuming the spring is in unstretched position at x=0, direction from left-right as +ve x-axis, Give x as a function of t when mass is at "+qntype[types-3]+"\n"
        w = math.sqrt(K/m)
        if types == 3:
            a = "x = "+str(d)+" sin("+str(round(w))+"t) \n"
        elif types == 4:
            a = "x = "+str(d)+" cos("+str(round(w))+"t) \n"
        else:
            a = "x = -"+str(d)+" cos("+str(round(w))+"t) \n"

    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()