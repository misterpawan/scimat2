import random
import math

# An aircraft of mass m kg executes a horizontal loop at a speed of 720 km/h with its wings banked at 15°. What is the radius of the loop?
# A train runs along an un banked circular track of radius 30 m at a speed of 54 km/h. The mass of the train is 106 kg. What provides the centripetal force required for this purpose the engine or the rails? What is the angle of banking required to prevent wearing out of the rail?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(1,200)
    param = random.randint(1,80)
    g = 10
    v = random.randint(30,530)
    type = random.randint(1,2)
    if type == 1:
        q = "An aircraft of mass "+str(m)+" kg executes a horizontal loop at a speed of "+str(v)+" ms-1 with its wings banked at "+str(param)+" degrees. What is the radius of the loop?\n"
        expr = (v**2)/(g*math.tan((param*math.pi)/180))
        a = str(round(expr))+" m\n"
    else:
        q = "A train runs along an un banked circular track of radius "+str(param+400)+" m at a speed of "+str(v)+" ms-1. The mass of the train is "+str(m)+" kg. What is the angle of banking required to prevent wearing out of the rail?\n"
        expr = ((math.atan((v**2)/((param+400)*g)))*180)/math.pi
        a = str(round(expr))+" degrees\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()