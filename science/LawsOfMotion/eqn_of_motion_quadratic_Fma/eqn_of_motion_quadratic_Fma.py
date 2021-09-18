import random

# A body of mass 0.40 kg moving initially with a constant speed of 10 ms-1 to the north is subject to a constant force of 8.0 N directed towards the south for 30 s. Take the instant the force is applied to be t = 0, the position of the body at that time to be x = 0, and predict its position at t = 5 s.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(1,20)
    v = random.randint(1,20)
    F = random.randint(2,200)
    t = random.randint(-30,60)
    q = "A body of mass "+str(m)+" kg moving initially with a constant speed of "+str(v)+" ms-1 to the north is subject to a constant force of "+str(F)+" N directed towards the south for 30 s. Take the instant the force is applied to be t = 0, the position of the body at that time to be x = 0, and predict its position at t = "+str(t)+" s.\n"
    if t <= 0 :
        s = v*t
        a = str(round(s))+ " m\n"
    elif t<= 30:
        s = v*t - (F*(t**2))/(2*m)
        a = str(round(s)) + " m\n"
    else:
        s30 = v*30 - (F*(30**2))/(2*m)
        v30 = v - ((F*30)/m)
        s30after = v30*(t-30)
        a = str(round(s30+s30after)) + " m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()