import random

# A monkey of mass 40 kg climbs on a rope which can stand a maximum tension of 600 N. In which of the following cases will the rope break: the monkey
# (a) climbs up with an acceleration of 6 ms-2
# (b) climbs down with an acceleration of 4 ms-2
# (c) climbs up with a uniform speed of 5 ms-1

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20
for i in range(no_of_samples):
    m = random.randint(10,70)
    T = random.randint(50,1050)
    upacc = random.randint(1,10)
    downacc = random.randint(1,10)
    vel = random.randint(1,10)
    q = "A monkey of mass "+str(m)+" kg climbs on a rope which can stand a maximum tension of "+str(T)+" N. In which of the following cases will the rope break: the monkey (a) climbs up with an acceleration of "+str(upacc)+" ms-2, (b) climbs down with an acceleration of "+str(downacc)+" ms-2, (c) climbs up (or) down with a uniform speed of "+str(vel)+" ms-1\n"
    a = ""
    if T < m*(10+upacc):
        a = a + "(a) break, "
    else:
        a = a + "(a) not break, "
    if T < m*(10-downacc):
        a = a + "(b) break, "
    else:
        a = a + "(b) not break, "
    if T < m*10:
        a = a + "(c) break\n"
    else:
        a = a + "(c) not break\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()