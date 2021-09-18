import random
import math

# What is the magnitude and direction of i + j.
# What are the components of a vector 2 i + 3 j along the direction of i + j

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        x = random.randint(1,1500)
        temp = random.randint(1,2)
        if temp == 2:
            x = -x
        y = random.randint(-1500,1500)
        mag = math.sqrt(x**2+y**2)
        dir = math.atan(y/x)*(180/math.pi)
        q = "What is the magnitude and direction of ("+str(x)+ ") i + ("+str(y)+") j?\n"
        a = "magnitude is "+str(round(mag,1))+" ,direction is "+str(round(dir))+" degrees with +ve x-axis\n"
    elif types == 2:
        x1 = random.randint(1,100)
        y1 = random.randint(1,100)
        temp = random.randint(1,2)
        if temp == 2:
            x1 = -x1
        temp = random.randint(1,2)
        if temp == 2:
            y1 = -y1
        x2 = random.randint(1,10)
        y2 = random.randint(1,10)
        temp = random.randint(1,2)
        if temp == 2:
            x2 = -x2
        temp = random.randint(1,2)
        if temp == 2:
            y2 = -y2
        comp = (x1*x2 + y1*y2)/math.sqrt(x2**2+y2**2)
        q = "What are the components of a vector ("+str(x1)+") i + ("+str(y1)+") j along the direction of ("+str(x2)+") i + ("+str(y2)+") j?\n"
        a = str(round(comp,1)) + " units\n"
    qns.write(q)
    ans.write(a)
qns.close()
ans.close()
