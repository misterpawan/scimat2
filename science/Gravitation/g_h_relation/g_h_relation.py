import random

# A body weighs w N on the surface of the Earth. What is the gravitational force on it due to the Earth at a height equal to n/d the radius of the Earth ?
# Assuming the earth to be a sphere of uniform mass density, how much would a body weigh n/d down to the centre of the earth if it weighed w N on the surface ?  

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

def cal1(w, n, d):
  return round(w*(1/(1+(n/d))),1)

def cal2(w, n, d):
  return round(w*(1-(n/d)),1)

def type1():
    w = random.randint(1,1000)
    n = random.randint(1,100)
    d = random.randint(n+1, n+100)
    ra = str(cal1(w, n, d)) + " newtons\n"
    q = "A body weighs " + str(w) + " N on the surface of the Earth. What is the gravitational force on it due to the Earth at a height equal to " + str(n) + "/" + str(d) + " the radius of the Earth ?\n"
    return q,ra

def type2():
    w = random.randint(1,1000)
    n = random.randint(1,100)
    d = random.randint(n+1, n+100)
    v = str(cal2(w, n, d)) + " newtons\n"
    q = "Assuming the earth to be a sphere of uniform mass density, how much would a body weigh " + str(n) + "/" + str(d) + " down to the centre of the earth if it weighed " + str(w) + " N on the surface ?\n"
    return q,v

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()