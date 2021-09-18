import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
# no_of_samples = 20

def force(q1,q2,d):
    const = 9*(10**9)
    F = const*q1*q2*(1/d)*(1/d)*(10**(-8))
    return F

for i in range(no_of_samples):
    qa = random.randint(1,200)
    qb = random.randint(1,200)
    if random.randint(0,1):
            qa = -qa
    if random.randint(0,1): 
            qb = -qb
    d = random.randint(1,200)
    q = "Two spheres q1 of charge "+str(qa)+" x 10^(-6)C, q2 of charge "+str(qb)+" x 10^(-6)C are placed at a distance "+str(d)+" cm, if an uncharged sphere C first comes in contact with A, then with B and placed at "+str(d)+" cm from both of them, then what is the "
    types = random.randint(1,15)
    if types<3:
        q = q +"final charge on A?\n"
        a = str(round(qa/2,2))+" coulomb\n"
    elif types<5:
        q = q +"final charge on B?\n"
        a = str(round(qa/4+qb/2,2))+" coulomb\n"
    elif types<7:
        q = q +"final charge on C?\n"
        a = str(round(qa/4+qb/2,2))+" coulomb\n"
    elif types<10:
        q = q + "final force between A and B\n"
        a = "{:.2e}".format(force(qa/2,qa/4+qb/2,d))+" newton\n"
    elif types<13:
        q = q + "final force between A and C\n"
        a = "{:.2e}".format(force(qa/2,qa/4+qb/2,d))+" newton\n"
    else:
        q = q + "final force between C and B\n"
        a = "{:.2e}".format(force(qa/4+qb/2,qa/4+qb/2,d))+" newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
    
qns.close()
ans.close()
