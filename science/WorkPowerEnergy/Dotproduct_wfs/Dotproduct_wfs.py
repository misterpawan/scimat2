import random


# If a force of xi + yj + zk N acts on a body and displaces it sx m in direction of x, sy m in direction of y and sz m in direction of z, then what is the wprk done by the force on the body. 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 500000

for i in range(no_of_samples):
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    z = random.randint(-10,10)
    sx = random.randint(1,50)
    sy = random.randint(1,50)
    sz = random.randint(1,50)
    ques = "If a force of " + str(x) + "i + " + str(y) + "j + " + str(z) + "k N acts on a body and displaces it " + str(sx) + " m in direction of x, " + str(sy) + " m in direction of y and " + str(sz) + " m in direction of z, then what is the work done by the force on the body.\n"
    answer = str(x*sx + y*sy + z*sz) + "\n"
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
