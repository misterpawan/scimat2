import random

# A car weighs m kg. The distance between its front and back axles is d m. Its centre of gravity is x m behind the front axle. Determine the force exerted by the level ground on  
#    a) each front wheel and 
#    b) each back wheel.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000
g = 9.8

def cal1(m, d, x) :
    return round((m*g*(d-x))/d,1)

def cal2(m, d, x) :
    return round((m*g*x)/d,1)

def type1() :
    m = random.randint(1000,2000)
    x = random.randint(1,100)
    d = random.randint(x+1,x+100)
    q = "A car weighs " + str(m) + " kg. The distance between its front and back axles is " + str(d) + " m. Its centre of gravity is " + str(x) + " m behind the front axle. Determine the force exerted by the level ground on each front wheel and each back wheel.\n"
    a = str(cal1(m, d, x)) + " newtons and " + str(cal2(m, d, x)) + "newtons\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
