import random

# Given observations(tuples of I(in A) and V(in V)) (I1,V1), (I1,V1), (I1,V1), (I1,V1), (I1,V1), (I1,V1); determine whether the given conductor is ohmic consuctor or not. 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    setOfNumbers = set()
    while len(setOfNumbers) < 6:
        setOfNumbers.add(random.randint(1, 40))
    arr = list(setOfNumbers)
    types = random.randint(0,11)
    q = "Given observations(tuples of I(in A) and V(in V)) "
    R = random.randint(1,20)
    for i in range(6):
        string = "("
        I = arr[i]
        V = arr[i]*R
        if types == i:
            noise = random.randint(-5,5)
            while noise == 0:
                noise = random.randint(-5,5)
            V += noise
        string = string + str(I) + "," + str(V)
        if i != 5:
            string += "), "
        else:
            string += "); "
        q = q + string
    q = q + "determine whether the given conductor is ohmic consuctor or not.\n"
    if types <= 5:
        a = "no, it is not an ohmic conductor\n"
    else:
        a = "yes, it is an ohmic conductor\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()
