import random
import math

# A stone tied to the end of a string 80 cm long is whirled in a horizontal circle with a constant speed. If the stone makes 14 revolutions in 25 s, what is the magnitude and direction of acceleration of the stone?
# An aircraft executes a horizontal loop of radius 1.00 km with a steady speed of 900 km/h. Compare its centripetal acceleration with the acceleration due to gravity.
# A cyclist is riding with a speed of 27 ms-1. As he approaches a circular turn on the road of radius 80 m, he applies brakes and reduces his speed at the constant rate of 0.50 ms-1 every second. What is the magnitude and direction of the net acceleration of the cyclist on the circular turn?


qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
# no_of_samples = 30

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        len = random.randint(1,200)
        rev = random.randint(20,220)
        time = random.randint(10,210)
        q = "A stone tied to the end of a string "+str(len)+" cm long is whirled in a horizontal circle with a constant speed. If the stone makes "+str(rev)+" revolutions in "+str(time)+" s, what is the magnitude and direction of acceleration of the stone?\n"
        w = 2*math.pi*(rev/time)
        acc = w*w*(len/100)
        a = "a = "+str(round(acc,1))+", towards the centre\n"
    elif types == 2:
        r = random.randint(20,2000)
        v = random.randint(33,2050)
        q = "An aircraft executes a horizontal loop of radius "+str(r)+" m with a steady speed of "+str(v)+" ms-1. Compare its centripetal acceleration with the acceleration due to gravity.\n"
        g = 9.8
        acc = (v*v)/r
        a = "centripetal acceleration is "+ str(round(acc,1))+ ", ratio is " +str(round(acc/g,1)) + "\n"
    else:
        r = random.randint(10,200)
        v = random.randint(10,200)
        ta = random.randint(10,200)
        q = "A cyclist is riding with a speed of "+str(v)+" ms-1. As he approaches a circular turn on the road of radius "+str(r)+" m, he applies brakes and reduces his speed at the constant rate of "+str(ta)+" ms-1 every second. What is the magnitude and direction of the net acceleration of the cyclist on the circular turn?\n"
        ca = (v**2)/r
        beta = math.atan(ca/ta) * (180/math.pi)
        acc = math.sqrt(ca**2+ta**2)
        a = "magnitude is "+str(round(acc,1))+" ,"+str(round(beta))+" degrees from the -ve direction of velocity\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()