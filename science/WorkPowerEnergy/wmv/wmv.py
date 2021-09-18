import random
import math

# Certain force acting on a m kg mass changes its velocity from u m/s to v m/s. Calculate the work done by the force.
# Certain force acting on a m kg mass changes its velocity from u m/s to v m/s.If the force foes a work of w J, calculate the value of v.
# Certain force acting on a m kg mass changes its velocity from u m/s to v m/s.If the force foes a work of w J, calculate the value of u.
# Certain force acting on a m kg mass changes its velocity from u m/s to v m/s.If the force foes a work of w J, calculate the value of m.
  
qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_w(m, u, v): 
    return round(0.5*m*(v**2-u**2),1)

def calculation_v(m, u, w):
    return round(math.sqrt(((2*w)/m)+u**2), 1)

def calculation_u(m, v, w):
    return round(math.sqrt(v**2-((2*w)/m)), 1)

def calculation_m(u, v, w):
    return round((2*w)/(v**2-u**2),1)

def type1():
    m = random.randint(1,400)
    u = random.randint(1,50)
    v = random.randint(1,50)
    q = "Certain force acting on a " + str(m) + " kg mass changes its velocity from " + str(u) + " m/s to " + str(v) + " m/s. Calculate the work done by the force.\n"
    w = str(calculation_w(m, u, v)) + " joules\n"
    return q,w

def type2():
    w = random.randint(1,10000)
    u = random.randint(1,50)
    m = random.randint(1,10)
    q = "Certain force acting on a " + str(m) + " kg mass changes its velocity from " + str(u) + " m/s to v m/s.If the force foes a work of " + str(w) + " J, calculate the value of v.\n"
    v = str(calculation_v(m, u, w)) + " m/s\n"
    return q,v

def type3():
    w = random.randint(1,10000)
    m = random.randint(1,10)
    temp = int(round(math.sqrt((2*w)/m),1))
    v = random.randint(temp+1,temp+50)
    q = "Certain force acting on a " + str(m) + " kg mass changes its velocity from u m/s to " + str(v) + " m/s.If the force foes a work of " + str(w) + " J, calculate the value of u.\n"
    u = str(calculation_u(m, v, w)) + " m/s\n"
    return q,u

def type4():
    w = random.randint(1,10000)
    u = random.randint(0,50)
    v = random.randint(u+1,u+50)
    q = "Certain force acting on a m kg mass changes its velocity from " + str(u) + " m/s to " + str(v) + " m/s.If the force foes a work of " + str(w) + " J, calculate the value of m.\n"
    m = str(calculation_m(u, v, w)) + " kg\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3 :
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()

