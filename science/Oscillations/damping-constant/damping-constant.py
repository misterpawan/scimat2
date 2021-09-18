import random
import math

# You are riding an automobile of mass 3000 kg. Assuming that you are examining the oscillation characteristics of its suspension system. The suspension sags 15 cm when the entire automobile is placed on it. Also, the amplitude of oscillation decreases by 50% during one complete oscillation. Estimate the values of (a) the spring constant k and (b) the damping constant b for the spring and shock absorber system of one wheel, assuming that each wheel supports 750 kg. g = 10 m/s2.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

def type1(m,p,x):
    q = "You are riding an automobile of mass "+str(m)+" kg. The suspension sags "+str(x)+" cm when the entire automobile is placed on it. Also, the amplitude of oscillation decreases by "+str(p)+" percent during one complete oscillation. Estimate the value of the spring constant k?\n"
    k = (m*10)/(0.04*x)
    return q, "{:.2e}".format(k) + " newton-m-1\n"

def type2(m,p,x):
    q = "You are riding an automobile of mass "+str(m)+" kg. The suspension sags "+str(x)+" cm when the entire automobile is placed on it. Also, the amplitude of oscillation decreases by "+str(p)+" percent during one complete oscillation. Estimate the value of the damping constant b for the spring and shock absorber system of one wheel\n"
    ## x = x0*(e^(-bt/2m))
    k = (m*10)/(0.04*x)
    t = 2*math.pi*math.sqrt(m/k)
    b = (2*m*2.303*0.3010)/t
    return q, "{:.2e}".format(b) + " kgs-1\n" 

for i in range(no_of_samples):
    types = random.randint(1,3)
    m = random.randint(50,1000)*20
    percent = random.randint(1,90)
    x = random.randint(10,200)
    if types == 1:
        q,a = type1(m,percent,x)
    else:
        q,a = type2(m,percent,x)
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
