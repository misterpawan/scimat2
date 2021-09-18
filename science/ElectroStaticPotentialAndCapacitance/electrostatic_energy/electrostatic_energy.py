import random

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 30

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        c = random.randint(1,2000)
        v = random.randint(1,2000)
        q = "A "+str(c)+" pF capacitor is connected to a "+str(v)+" V battery. How much electrostatic energy is stored in the capacitor?\n"
        a = "{:.2e}".format(0.5*c*v*v*(10**(-12))) + " joule\n"
    else:
        c1 = random.randint(1,200)
        c2 = random.randint(1,200)
        v = random.randint(1,200)
        q = "A "+str(c1) + " pF capacitor is charged by a "+str(v)+" V supply. It is then disconnected from the supply and is connected to another uncharged "+str(c2)+" pF capacitor. How much electrostatic energy is lost in this process?\n"
        E = 0.5*c1*v*v
        c3 = (c1*c2)/(c1+c2)
        E1 = 0.5*c3*v*v
        a = "{:.2e}".format((E-E1)*(10**(-12)))+" joule\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)

qns.close()
ans.close() 