import random
import math

# A 70 kg man stands in contact against the inner wall of a hollow cylindrical drum of radius 3 m rotating about its vertical axis with 200 rev/min. The coefficient of friction between the wall and his clothing is 0.15. What is the minimum rotational speed of the cylinder to enable the man to remain stuck to the wall (without falling) when the floor is suddenly removed?
# A disc revolves with a speed of 33 1/3  rpm and has a radius of 15 cm. Two coins are placed at 4 cm and 14 cm away from the centre of the record. If the coefficient of friction between the coins and record is 0.15, which of the coins will revolve with the record? 

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 30
g = 10

def type1():
    m = random.randint(50,100)
    r = random.randint(2,10)
    mu = round(random.randint(1,100)/100,2)
    rot_speed = random.randint(1,5)
    q = "A "+str(m)+" kg man stands in contact against the inner wall of a hollow cylindrical drum of radius "+str(r)+" m rotating about its vertical axis with "+str(rot_speed)+" rev/s. The coefficient of friction between the wall and his clothing is "+str(mu)+". What is the minimum rotational speed of the cylinder to enable the man to remain stuck to the wall (without falling) when the floor is suddenly removed?\n"
    w = math.sqrt(g/mu*r)
    w = str(round(w,1)) + " rad/s\n"
    return q,w

def type2():
    rot_speed = random.randint(10,50)
    r1 = random.randint(1,50)
    r2 = random.randint(r1+1,r1+49)
    mu = round(random.randint(1,100)/100,2)
    q = "A disc revolves with a speed of "+str(rot_speed)+" rpm and has a radius of 1 m. Two coins are placed at "+str(r1)+" cm(coin-1) and "+str(r2)+" cm(coin-2) away from the centre of the record. If the coefficient of friction between the coins and record is "+str(mu)+", which of the coins will revolve with the record?\n"
    w = (math.pi/30)*rot_speed
    r_opt = ((mu*g)/(w*w))*100
    if r1 < r_opt:
        a = "coin1 will revolve,"
    else:
        a = "coin1 will not revolve,"
    if r2 < r_opt:
        a = a + "coin2 will revolve\n"
    else:
        a = a + "coin2 will not revolve\n"
    return q,a

for i in range(no_of_samples):
    type = random.randint(1,3)
    if type == 1:
        q,a = type1()
    else:
        q,a = type2()
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()