import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    E = random.randint(1000,11000)
    d = random.randint(1,400)
    q = "An infinite line charge produces a field of "+str(E)+" N/C at a distance of "+str(d)+" cm. Calculate the linear charge density.\n"
    a = "{:.2e}".format((E*d*0.01)/(18*(10**9)))+" coulomb/m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
