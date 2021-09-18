import random
import math

# The escape speed of a projectile on the Earth’s surface is 11.2 km s-1. A body is projected out with thrice this speed. What is the speed of the body far away from the Earth?   

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 500000

def cal1(v):
  return round(math.sqrt((v*v)-(11.2*11.2)),1)

def type1():
    v = random.randint(112000,212000)
    v = round(v/1000,3)
    ra = str(cal1(v)) + " km/s\n"
    q = "The escape speed of a projectile on the Earth’s surface is 11.2 km s-1. A body is projected out with the speed of " + str(v) + " km/s. What is the speed of the body far away from the Earth?\n"
    return q,ra

for i in range(no_of_samples):
    ques,answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()