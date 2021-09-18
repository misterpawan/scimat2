import random
import math

#### Consider variation of theta.
# In a harbour, wind is blowing at the speed of 72 ms-1 and the flag on the mast of a boat anchored in the harbour flutters along the N-E direction. If the boat starts moving at a speed of 51 ms-1 to the north, what is the direction of the flag on the mast of the boat?
# tan(beta) = v2*sin(theta)/(v1+v2*cos(theta)), with theta as 135

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    v1 = random.randint(1500,3500)
    v2 = random.randint(1,2000)
    q = "In a harbour, wind is blowing at the speed of "+str(v1)+" ms-1 and the flag on the mast of a boat anchored in the harbour flutters along the N-E direction. If the boat starts moving at a speed of "+str(v2)+" ms-1 to the north, what is the direction of the flag on the mast of the boat?\n"
    sin45 = 1/math.sqrt(2)
    tan_beta = v2*sin45/(v1-v2*sin45)
    beta = round(math.atan(tan_beta)*57.2958,1)
    if beta >= 45:
        a = str(round(beta-45)) + " degrees south of east\n"
    else:
        a = str(round(45-beta)) + " degrees north of east\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()