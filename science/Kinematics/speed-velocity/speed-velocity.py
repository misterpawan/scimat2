import random

# A passenger arriving in a new town wishes to go from the station to a hotel located 10 km away on a straight road from the station. A dishonest cab man takes him along a circuitous path 23 km long and reaches the hotel in 28 min. What is (a) the average speed of the taxi, (b) the magnitude of average velocity? Are the two equal?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    disp = random.randint(1,500)
    time = random.randint(1,40)
    distance = random.randint(disp+1,disp+200)
    q = "A passenger arriving in a new town wishes to go from the station to a hotel located "+str(disp)+" km away on a straight road from the station. A dishonest cab man takes him along a circuitous path "+str(distance)+" km long and reaches the hotel in "+str(time)+" min. What is (a) the average speed of the taxi, (b) the magnitude of average velocity? Are the two equal?\n"
    a = "average speed = "+str(round((distance*100)/(time*6),1))+" ms-1, average velocity = "+str(round((disp*100)/(time*6),1))+" ms-1, both of them are not equal\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
