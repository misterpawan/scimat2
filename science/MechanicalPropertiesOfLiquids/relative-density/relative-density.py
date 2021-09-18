import random
import math

# A U tube contains water and liquid separated by mercury. The mercury columns in the two arms are in level with 10.0 mm of water in one arm and 12.5 mm of liquid in the other. What is the relative density of liquid?
# A U tube contains water and liquid separated by mercury. The mercury columns in the two arms are in level with 10.0 mm of water in one arm and 12.5 mm of liquid in the other, if 15.0 mm of water and liquid each are further poured into the respective arms of the tube, what is the difference in the levels of mercury in the two arms? 

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,3)
    l1 = random.randint(1,2000)
    l2 = random.randint(1,2000)
    q = "A U tube contains water and liquid separated by mercury. The mercury columns in the two arms are in level with "+str(l1)+" mm of water in one arm and "+str(l2)+" mm of liquid in the other"
    if types == 1:
        q = q + ". What is the relative density of liquid?\n"
        a = str(l2) + "/" + str(l1) + "\n"
    else:
        l3 = random.randint(1,2000)
        rel = l2/l1
        q = q + ", if "+str(l3)+" mm of water and liquid each are further poured into the respective arms of the tube, what is the difference in the levels of mercury in the two arms?\n"
        h1 = l1 + l3
        h2 = l2 + l3
        h = (abs(h1/10 - rel*(h2/10)))/13.6
        a = "{:.2e}".format(h*10) + " mm\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()