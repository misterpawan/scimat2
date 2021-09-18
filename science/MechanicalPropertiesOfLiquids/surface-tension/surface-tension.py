import random

# A U-shaped wire is dipped in a soap solution, and removed. A thin soap film formed between the wire and a light slider supports a weight of 1.5 x 10-2 N (which includes the small weight of the slider). The length of the slider is 30 cm. What is the surface tension of the film?
# A U-shaped wire is dipped in a soap solution, and removed. A thin soap film formed between the wire and a light slider supports a weight of 1.5 x 10-2 N. The length of the slider is 30 cm. What is the surface tension of the film?
# What is the pressure inside a drop of mercury of radius 3.0 mm at room temperature? Surface tension of mercury at that temperature (20°C) is 4.65 x 10-1 Nm-1. The atmospheric pressure is 1.01 x 105 Pa. Also give the excess pressure inside the drop.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types < 2:
        l = random.randint(1,2000)
        f = random.randint(1,2000)
        q = "A U-shaped wire is dipped in a soap solution, and removed. A thin soap film formed between the wire and a light slider supports a weight of "+str(f)+" x 10-3 N (which includes the small weight of the slider). The length of the slider is "+str(l)+" mm. What is the surface tension of the film?\n"
        if types:
            q = "A U-shaped wire is dipped in a soap solution, and removed. A thin soap film formed between the wire and a light slider supports a weight of "+str(f)+" x 10-3 N. The length of the slider is "+str(l)+" mm. What is the surface tension of the film?\n"
        a = str(round(f/(2*l),2)) + " newton m-1\n"
    else:
        r = random.randint(1,20)
        st = random.randint(1,2000)
        temp = random.randint(200,400)
        q = "What is the pressure inside a drop of liquid of radius "+str(r)+" mm at room temperature? Surface tension of liquid at that temperature ("+str(temp)+" K) is "+str(st)+" x 10-3 Nm-1. Also give the excess pressure inside the drop.\n"
        excess = (2*st)/r
        total = 1.01*(10**5)+excess
        a = "excess pressure is "+str(round(excess,2))+" pascal, total pressure is "+"{:.2e}".format(total)+" pascal\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()