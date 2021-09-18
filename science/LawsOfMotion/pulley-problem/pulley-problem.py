import random

# Two masses 8 kg and 12 kg are connected at the two ends of a light in extensible string that goes over a friction less pulley. Find the acceleration of the masses, and the tension in the string when the masses are released.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
no_of_samples = 20
for i in range(no_of_samples):
    m1 = random.randint(1,2000)
    m2 = random.randint(1,2000)
    q = "Two masses m1, m2 of "+str(m1)+" kg and "+str(m2)+" kg are connected at the two ends of a light in extensible string that goes over a friction less pulley. Find the acceleration of the masses, and the tension in the string when the masses are released.\n"
    if m1 == m2:
        a = "acceleration of both bodies is 0 ms-2, tension is "+str(m1*10)+" newton\n"
    elif m1 > m2:
        acc = ((m1-m2)/(m1+m2))*10
        T = m2*(10+acc)
        a = "acceleration of m2 is upward, m1 is downward, both having magnitude of "+str(round(acc,1))+" ms-2, tension is "+str(round(T,1))+" newton\n"
    elif m2 > m1:
        acc = ((m2-m1)/(m1+m2))*10
        T = m1*(10+acc)
        a = "acceleration of m1 is upward, m2 is downward, both having magnitude of "+str(round(acc,1))+" ms-2, tension is "+str(round(T,1))+" newton\n"
    qns.write(q)
    ans.write(a)
    print(q)
    print(a)
qns.close()
ans.close()