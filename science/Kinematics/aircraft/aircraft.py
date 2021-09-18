import random
import math

# An aircraft is flying at a height of 3400 m above the ground. If the angle subtended at a ground observation point by the aircraft positions 10 s apart is 30 degrees, what is the speed of the aircraft?
# A fighter plane flying horizontally at an altitude of 1.5 km with speed 720 km h-1 passes directly overhead an anti-aircraft gun. At what angle from the vertical should the gun be fired for the shell with muzzle speed 600 m s-1 to hit the plane? At what minimum altitude should the pilot fly the plane to avoid being hit? (Take g = 10 ms-2)?


qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    type = random.randint(1,2)
    h = random.randint(500,1000)
    if type == 1:
        time = random.randint(1,200)
        angle = random.randint(0,179)
        q = "An aircraft is flying at a height of "+str(h)+" m above the ground. If the angle subtended at a ground observation point by the aircraft positions "+str(time)+" s apart is "+str(angle)+" degrees, what is the speed of the aircraft?\n"
        dist = 2*h*math.tan((angle*math.pi)/360)
        a = str(round(dist/time,1)) + " ms-1\n"
    else:
        v1 = random.randint(100,300)
        v2 = random.randint(v1+10,v1+300)
        q = "A fighter plane flying horizontally at an altitude of "+str(h)+" m with speed "+str(v1)+" ms-1 passes directly overhead an anti-aircraft gun. At what angle from the vertical should the gun be fired for the shell with muzzle speed "+str(v2)+" ms-1 to hit the plane? At what minimum altitude should the pilot fly the plane to avoid being hit? (Take g = 10 ms-2)?\n"
        angle = math.asin(v1/v2) * (180/math.pi)
        h2 = (v2*v2*(1-(v1/v2)**2))/20
        a = "angle is "+str(round(angle))+" degrees, minimum altitude is "+str(round(h2,1))+" m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()