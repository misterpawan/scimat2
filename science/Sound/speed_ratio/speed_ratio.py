import random

# Find the ratio of time taken by the sound wave to travel a distance of x m in material-1 and material-2 (speed of sound in material-1 is v1 m/s, in material-2 is v2 m/s) ? 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 10

for i in range(no_of_samples):
    x = random.randint(1,10)
    v1 = random.randint(1,2000)
    v2 = random.randint(8000,10000)
    ques = "Find the ratio of time taken by the sound wave to travel a distance of "+str(x)+" m in material-1 and material-2 (speed of sound in material-1 is "+str(v1)+" m/s, in material-2 is "+str(v2)+" m/s) ?\n"
    qns.write(ques)
    answer = str(round(v2/v1,1)) + "\n" 
    ans.write(answer)
    # print(ques)
    # print(answer)
 
qns.close()
ans.close()
