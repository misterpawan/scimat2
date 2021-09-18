
import random

# A pump on the ground floor of a building can pump up water to fill a tank of volume v m3 in t min. If the tank is h m above the ground, and the efficiency of the pump is e%, how much electric power is consumed by the pump?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

for i in range(no_of_samples):
    e = random.randint(1,100)
    v = random.randint(1,100)
    h = random.randint(1,100)
    t = random.randint(1,30)
    ques = "A pump on the ground floor of a building can pump up water to fill a tank of volume " + str(v) + " m3 in " + str(t) + " min. If the tank is " + str(h) + " m above the ground, and the efficiency of the pump is " + str(e) + "%, how much electric power is consumed by the pump?\n"
    t = t * 60
    answ = round((100000*v*h*9.8)/(t*e),2)
    answer = str(answ) + "watts\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
