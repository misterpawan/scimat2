import random

#A object of mass 70 g, stands on a weighing machine in a lift, which is moving
# (a) upwards with a uniform speed of 10 ms-1.
# (b) downwards with a uniform acceleration of 5 ms-2.
# (c) upwards with a uniform acceleration of 5 ms-2.
# What would be the readings on the scale in each case?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(100,5000)
    q = "A object of mass "+str(m)+" g, stands on a weighing machine in a lift, which is moving"
    type = random.randint(1,4)
    if type == 1 or type == 2:
        v = random.randint(0,1000)
        if type == 1:
            q = q + " upwards with a uniform speed of "+str(v)+" cms-1,"
        elif type == 2:
            q = q + " downwards with a uniform speed of "+str(v)+" cms-1,"
        a = str(round(m/100,1))+" newton\n"
    elif type == 3:
        acc = random.randint(0,1000)
        q = q + " downwards with a uniform acceleration of "+str(acc)+" cms-2,"
        a = str(round((m*(10-(acc/100)))/1000,1))+" newton\n"
    elif type == 4:
        acc = random.randint(0,1000)
        q = q + " upwards with a uniform acceleration of "+str(acc)+" cms-2,"
        a = str(round((m*(10+(acc/100)))/1000,1))+" newton\n"
    q = q + " then what would be the reading on the scale?\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()