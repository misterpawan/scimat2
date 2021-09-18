import random
import math

# A bullet fired at an angle of 30° with the horizontal hits the ground 3 km away. By adjusting its angle of projection, can one hope to hit a target 5 km away? Assume the muzzle speed to the fixed, and neglect air resistance.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    angle = random.randint(1,89)
    dist = random.randint(200,500)
    u_2 = (dist*9.8)/math.sin((angle*math.pi)/90)
    R_opt = round(u_2/9.8)
    dist2 = random.randint(R_opt-150,R_opt+150)
    q = "A bullet fired at an angle of "+str(angle)+" degree with the horizontal hits the ground "+str(dist)+" m away. By adjusting its angle of projection, can one hope to hit a target "+str(dist2)+" m away?\n"
    if dist2 > R_opt:
        a = "no\n"
    else:
        a = "yes\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()