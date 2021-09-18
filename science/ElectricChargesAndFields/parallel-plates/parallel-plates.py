import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 500000
# no_of_samples = 20

for i in range(no_of_samples):
    sigma = random.randint(1,2000000)
    q = "Two large thin metal plates are parallel anc close to each other. On their inner faces, the plates have surface charge densities of opposite signs and of magnitude "+str(sigma)+" x 10^(-22) C/m2. What is E: "
    types = random.randint(1,12)
    if types <= 10:
        q = q + "between the plates?\n"
        a = "{:.2e}".format(sigma/(8.854*(10**10)))+" newton/coulomb\n"
    else:
        arr = ["first","second"]
        q = q +"the outer region of "+arr[types-11]+" plate?\n"
        a = "0 newton/coulomb\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
