import random

# What is the excess pressure inside a bubble of soap solution of radius 5.00 mm, given that the surface tension of soap solution at the temperature (20 °C) is 2.50 x 10-2  Nm-1? If an air bubble of the same dimension were formed at depth of 40.0 cm inside a container containing the soap solution (of relative density 1.20), what would be the pressure inside the bubble? (1 atmospheric pressure is 1.01 x 105  Pa).
# A tank with a square base of area 1.0 m2 is divided by a vertical partition in the middle. The bottom of the partition has a small-hinged door of area 20 cm2. The tank is filled with water in one compartment, and an acid (of relative density 1.7) in the other, both to a height of 4.0 m. Compute the force necessary to keep the door close.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types:
        r = random.randint(1,10)
        temp = random.randint(280,300)
        st = random.randint(1,200)
        depth = random.randint(1,10)*10
        rel_den = 1 + round(random.randint(1,20)/10,1)
        q = "What is the excess pressure inside a bubble of soap solution of radius "+str(r)+" mm, given that the surface tension of soap solution at the temperature "+str(temp)+" K is "+str(st)+" x 10-3  Nm-1? If an air bubble of the same dimension was formed at depth of "+str(depth)+" cm inside a container containing the soap solution (of relative density "+str(rel_den)+"), what would be the pressure inside the bubble?.\n"
        excess = (4*st)/r
        p = (1.01*(10**5)) + (depth*rel_den*10) + (excess/2)
        a = "excess pressure inside soap bubble is "+str(round(excess,1))+" pascal, excess pressure inside air bubble floating up is "+"{:.2e}".format(p)+" pascal\n"
    else:
        a1 = random.randint(1,200)
        a2 = random.randint(1,200)
        rel_den = round(random.randint(1,20)/10,1)
        h = random.randint(1,20)
        q = "A tank with a square base of area "+str(a1)+" m2 is divided by a vertical partition in the middle. The bottom of the partition has a small-hinged door of area "+str(a2)+" cm2. The tank is filled with water in one compartment, and an acid (of relative density "+str(rel_den)+") in the other, both to a height of "+str(h)+" m. Compute the force necessary to keep the door close.\n"
        f = h*abs(rel_den-1)*0.98*a2
        a = str(round(f,1))+" newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()