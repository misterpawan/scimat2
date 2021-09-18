import random
import math

# A man can swim with a speed of 4.0 ms-1 in still water. How long does he take to cross a river 1.0 km wide if the river flows steadily at 3.0 ms-1 and he makes his strokes normal to the river current? How far down the river does he go when he reaches the other bank, what is angle of deviation of his path from normal?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20
for i in range(no_of_samples):
    v1 = random.randint(1,200)
    v2 = random.randint(1,200)
    s = random.randint(1,100)
    q = "A man can swim with a speed of "+str(v1)+" ms-1 in still water. How long does he take to cross a river "+str(s)+" km wide if the river flows steadily at "+str(v2)+" ms-1 and he makes his strokes normal to the river current? How far down the river does he go when he reaches the other bank, what is angle of deviation of his path from normal?\n"
    deviation_angle = round(math.atan(v2/v1)*57.2958)
    time = (s*1000)/v1
    a = "time taken is "+str(round(time,1))+" s, deviation angle is "+str(deviation_angle)+" degrees\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()