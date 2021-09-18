import random

# Two bodies of masses 10 kg and 20 kg respectively kept on a smooth, horizontal surface are tied to the ends of a tight string. A horizontal force F = 600 N is applied to (i) A, (ii) B along the direction of string. What is the tension in the string in each case?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    m1 = random.randint(1,200)
    m2 = random.randint(1,200)
    F = random.randint(40,400)
    q = "Two bodies A, B of masses "+str(m1)+" kg and "+str(m2)+" kg respectively kept on a smooth, horizontal surface are tied to the ends of a tight string. A horizontal force F = "+str(F)+" N is applied to"
    acc = F/(m1+m2)
    type = random.randint(1,2)
    if type == 1:
        q = q + " A along the direction of string. What is the acceleration, tension in the string?\n"
        T = F - m1*acc
    else:
        q = q + " B along the direction of string. What is the acceleration, tension in the string?\n"
        T = F - m2*acc
    a = "acceleration is "+str(round(acc,1))+" ms-2, tension is "+str(round(T,1))+" newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()