import random

# On a long horizontally moving belt (Fig.), a child runs to and fro with n speed 9 km h-1 (with respect to the belt) between his father and mother located 50 a part on the moving belt. The belt moves with a speed of 4 km h-1 . For an observe a stationary platform outside, what is the
# (a) Speed of the child running in the direction of motion of the belt?
# (b) Speed of the child running opposite to the direction of motion of the belt?
# (c) Time taken by the child in (a) and (b)?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20
for i in range(no_of_samples):
    v2 = random.randint(1,80)
    v1 = random.randint(v2+1,v2+50)
    distance = random.randint(1,1000)
    q = "On a long horizontally moving belt, a child runs to and fro with speed "+str(v1)+" ms-1 (with respect to the belt) between his parents located "+str(distance)+" m a part on the moving belt. The belt moves with a speed of "+str(v2)+" ms-1 . For an observer on a stationary platform outside, what is the "
    types = random.randint(1,4)
    if types == 1:
        q = q + "speed of the child running in the direction of motion of the belt? \n"
        a = str(v2+v1) + " ms-1\n"
    elif types == 2:
        q = q + "speed of the child running opposite to the direction of motion of the belt?\n"
        a = str(v1-v2) + " ms-1\n"
    elif types == 3 or types == 4:
        q = q + "time taken by the child to go from one parent to another parent?\n"
        a = str(round(distance/v1,1)) + " s\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()