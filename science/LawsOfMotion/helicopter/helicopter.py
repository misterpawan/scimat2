import random

# A helicopter of mass 1000 kg rises with a vertical acceleration of 15 ms-2. The crew and the passengers weigh 300 kg. Give the magnitude and direction of
# (a) force on the floor by the crew and passengers,
# (b) action of the rotor of the helicopter on surrounding air,
# (c) force on the helicopter due to the surrounding air

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    m1 = random.randint(500,2500)
    m2 = random.randint(200,400)
    acc = random.randint(1,20)
    type = random.randint(1,3)
    q = "A helicopter of mass "+str(m1)+" kg rises with a vertical acceleration of "+str(acc)+" ms-2. The crew and the passengers weigh "+str(m2)+" kg. Give the magnitude and direction of"
    if type == 1:
        q = q + " force on the floor by the crew and passengers\n"
        an = m2*(10+acc)
        a = str(an)+" newton, vertically downwards\n"
    elif type == 2:
        q = q + " action of the rotor of the helicopter on surrounding air\n"
        an = (m1+m2)*(10+acc)
        a = str(an)+" newton, vertically downwards\n"
    elif type == 3:
        q = q + "  force on the helicopter due to the surrounding air\n"
        an = (m1+m2)*(10+acc)
        a = str(an)+" newton, vertically upwards\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()