import random

# A stone of mass 0.05 kg is thrown vertically upwards. Give the direction and magnitude of the net force on the pebble,
#(a) during its upward motion,
#(b) during its downward motion,
#(c) at the highest point where it is momentarily at rest. 
# Do your answers change if the pebble was thrown at an angle of 45° with the horizontal direction

# Give the magnitude and direction of the net force acting on a stone of mass 0.1 kg,
#(a) just after it is dropped from the window of a stationary train,
#(b) just after it is dropped from the window of a train running at a constant velocity of 36 km/ h,
#(c) just after it is dropped from the window of a train accelerating with 1 ms-2,
#(d) lying on the floor of a train which is accelerating with 1 m s~2, the stone being at rest relative to the train.

# A rocket with a lift-off mass 20,000 kg is blasted upwards with an initial acceleration of 5.0 ms-2. Calculate the initial thrust (force) of the blast.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
# no_of_samples = 30

for i in range(no_of_samples):
    type = random.randint(1,5)
    if type == 1 or type == 3:
        m = random.randint(1,200)
        v = random.randint(1,200)
        angle = random.randint(0,90)
        q = "A stone of mass "+str(m)+" kg is thrown vertically upwards with a velocity of "+str(v)+" ms-1. Give the direction and magnitude of the net force on the stone,"
        t2 = random.randint(1,3)
        if t2 == 1:
            q = q + " during its upward motion, "
        elif t2 == 2:
            q = q + " during its downward motion, "
        else:
            q = q + " at the highest point where it is momentarily at rest, "
        q = q + " do the answer change if the stone was thrown at an angle of "+str(angle)+" degree with the horizontal direction?\n"
        a = str(m*10)+" newton, no answer does not change in 2nd case also.\n"
    elif type == 2 or type == 4:
        m = random.randint(10,2000)
        q = "Give the magnitude and direction of the net force acting on a stone of mass "+str(m)+" g,"
        a = str(round(m/100,1))+" newton, vertically downwards\n"
        t2 = random.randint(1,5)
        if t2 == 1:
            l = random.randint(100,2000)
            q = q + " just after it is dropped from the window of a stationary train of length "+str(l)+" m?\n"
        elif t2 == 2:
            v = random.randint(1,2000)
            q = q + " just after it is dropped from the window of a train running at a constant velocity of "+str(v)+" ms-1?\n"
        elif t2 == 3:
            acc = random.randint(1,2000)
            q = q + " just after it is dropped from the window of a train accelerating with "+str(acc)+" ms-2?\n"
        else:
            acc = random.randint(10,2000)
            q = q + " lying on the floor of a train which is accelerating with "+str(acc)+" ms-2, the stone being at rest relative to the train?\n"
            a = str(round((m*acc)/1000,1)) + " newton, along the direction of motion of train\n"
    else:
        m = random.randint(1000,20000)
        acc = random.randint(20,300)
        q = "A rocket with a lift-off mass "+str(m)+" kg is blasted upwards with an initial acceleration of "+str(acc)+" ms-2. Calculate the initial thrust (force) of the blast.\n"
        a = str(m*a) + " newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()