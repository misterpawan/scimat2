import random

# Suppose there existed a planet that went around the Sun twice as fast as the Earth. What would be its orbital size as compared to that of the Earth?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 30
g = 10

for i in range(no_of_samples):
    num = random.randint(1,3000)
    den = random.randint(100,3000)
    expr = str(num)+"/"+str(den)
    q = "Suppose there existed a planet that went around the Sun "+expr+" times as fast as the Earth. What would be its orbital size as compared to that of the Earth?\n"
    tp = den/num
    rp = (tp)**(2/3)
    a = str(round(rp,1))+" times faster than earth\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()