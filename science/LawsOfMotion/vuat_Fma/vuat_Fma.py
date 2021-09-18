import random

# A constant retarding force of 50 N is applied to a body of mass 20 kg moving initially with a speed of 15 ms-1. How long does the body take to stop?
# A constant force acting on a body of mass 3.0 kg changes its speed from 2.0 ms-1 to 3.5 ms-1 in 25 s. The direction of the motion of the body remains unchanged. What is the magnitude and direction of the force?
# The driver of a three-wheeler moving with a speed of 36 ms-1 sees a child standing in the middle of the road and brings his vehicle to rest in 4.0 s just in time to save the child. What is the magnitude of average retarding force on the vehicle? The mass of the three-wheeler is 400 kg and the mass of the driver is 65 kg.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 30

for i in range(no_of_samples):
    type = random.randint(1,3)
    if type == 1:
        m = random.randint(20,200)
        u = random.randint(1,200)
        F = random.randint(20,200)
        q = "A constant retarding force of "+str(F)+" N is applied to a body of mass "+str(m)+" kg moving initially with a speed of "+str(u)+" ms-1. How long does the body take to stop?\n"
        t = (m*u)/F
        a = str(round(t,1))+" s\n"
    elif type == 2:
        m = random.randint(5,100)
        u = random.randint(1,50)
        v = random.randint(u+1,u+20)
        t = random.randint(1,50)
        q = "A constant force acting on a body of mass "+str(m)+" kg changes its speed from "+str(u)+" ms-1 to "+str(v)+" ms-1 in "+str(t)+" s. The direction of the motion of the body remains unchanged. What is the magnitude and direction of the force?\n"
        F = (m*(v-u))/t
        a = str(round(F,1))+" newton, along the direction of motion\n"
    else:
        u = random.randint(1,50)
        m1 = random.randint(200,400)
        m2 = random.randint(60,100)
        t = random.randint(1,10)
        q = "The driver of a three-wheeler moving with a speed of "+str(u)+" ms-1 sees a child standing in the middle of the road and brings his vehicle to rest in "+str(t)+" s just in time to save the child. What is the magnitude of average retarding force on the vehicle? The mass of the three-wheeler is "+str(m1)+" kg and the mass of the driver is "+str(m2)+" kg.\n"
        F = ((m1+m2)*(u))/t
        a = str(round(F,1)) + " newton\n"
    qns.write(q)
    ans.write(a)
    print(q)
    print(a)
qns.close()
ans.close()