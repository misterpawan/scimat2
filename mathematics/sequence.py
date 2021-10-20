import random

# What is next in 85, 84, 83, 82?
# What comes next: 50, 19, -24, -85, -170, -285, -436, -629?
# What is the next term in -363, -368, -383, -414, -467, -548, -663?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
num_samples = 1000000
templates = ["What is next in ", "What comes next: ", "What is the next term in "]

for i in range(num_samples):
    types = random.randint(1,3)
    num_of_terms = random.randint(4,9)
    term1 = random.randint(-1000,1000)
    common_diff = random.randint(-1000,1000)
    q = templates[types-1]
    for i in range(num_of_terms):
        q += str(term1+common_diff*i)
        if i==num_of_terms-1:
            q+="?\n"
        else:
            q+=", "
    a = str(term1+common_diff*num_of_terms) + "\n"
    qns.write(q)
    ans.write(a)
qns.close()
ans.close()