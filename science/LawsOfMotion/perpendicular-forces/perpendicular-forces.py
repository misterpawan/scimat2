import random
import math

# A body of mass 5 kg is acted upon by two perpendicular forces 8 N and 6 N. Give the magnitude and direction of the acceleration of the body.
# A body of mass 5 kg is acted upon by the force (8) i + (6) j N. Find the acceleration of the body (in vector notation).
# A body of mass 5 kg is acted upon by the force (8) i + (6) j N. Give the magnitude and direction of the acceleration of the body.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(1,200)
    f_x = random.randint(20,200)
    f_y = random.randint(20,200)
    type = random.randint(1,3)
    angle = math.atan(f_y/f_x) * (180/math.pi)
    f_res = math.sqrt(f_x**2+f_y**2)
    if type == 1:
        q = "A body of mass "+str(m)+" kg is acted upon by two perpendicular forces "+str(f_x)+" N and "+str(f_y)+" N. Give the magnitude and direction of the acceleration of the body.\n"
        a = str(round(f_res/m,1))+" ms-2, "+str(round(angle))+" degrees with "+str(f_x)+" newton force\n"
    else:
        if random.randint(0,1):
            f_x = -f_x
        if random.randint(0,1):
            f_y = -f_y
        expr = "("+str(f_x)+") i + ("+str(f_y)+") j N."
        if type == 2:
            q = "A body of mass "+str(m)+" kg is acted upon by the force "+expr+"Find the acceleration of the body (in vector notation).\n"
            a = "("+str(round(f_x/m,1))+") i + ("+str(round(f_y/m,1))+") j ms-2\n"
        elif type == 3:
            f_res = math.sqrt(f_x**2+f_y**2)
            q = "A body of mass "+str(m)+" kg is acted upon by the force "+expr+"Give the magnitude of acceleration of the body.\n"
            a = str(round(f_res/m,1))+" ms-2\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()