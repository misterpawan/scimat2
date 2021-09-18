import random

# A girl sitting on a merry go round, moving in counter clockwise through an arc length of s m. If the angular diplacement is r rad, how far she is from the center of merry go round ?
# If the wheel of radius r m has a angular velocity of w rad/s, what is the velocity of the point at the circumference of the wheel ?
# If a point on the circumference of the wheel rotating with an angular velocity of w rad/s has a velocity of v m/s. What is the radius of the wheel ?
# If the wheel of radius r m has a angular acceleration of a rad/s2, what is the accelaration of the point at the circumference of the wheel ?  
# If a point on the circumference of the wheel rotating with an angular acceleration of aa rad/s2 has a acceleration of a m/s2. What is the radius of the wheel ? 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2500000

def cal1(o1, o2):
  return round(o1*o2,1)

def cal2(o1, o2):
  return round(o1/o2,1)

def type1():
    s = random.randint(1,1000)
    r = random.randint(1,1000)
    ra = str(cal2(s,r)) + " m\n"
    q = "A girl sitting on a merry go round, moving in counter clockwise through an arc length of " + str(s) + " m. If the angular diplacement is " + str(r) + " rad, how far she is from the center of merry go round ?\n"
    return q,ra

def type2():
    r = random.randint(1,1000)
    w = random.randint(1,1000)
    v = str(cal1(w,r)) + " m/s\n"
    q = "If the wheel of radius " + str(r) + " m has a angular velocity of " + str(w) + " rad/s, what is the velocity of the point at the circumference of the wheel ?\n"
    return q,v

def type3():
    r = random.randint(1,1000)
    aa = random.randint(1,1000)
    a = str(cal1(aa,r)) + " m/s2\n"
    q = "If the wheel of radius " + str(r) + " m has a angular acceleration of " + str(aa) + " rad/s2, what is the accelaration of the point at the circumference of the wheel ?\n"
    return q,a

def type4() :
    v = random.randint(1,1000)
    w = random.randint(1,1000)
    r = str(cal2(v,w)) + " m\n"
    q = "If a point on the circumference of the wheel rotating with an angular velocity of " + str(w) + " rad/s has a velocity of " + str(v) + " m/s. What is the radius of the wheel ?\n"
    return q,r

def type5() :
    a = random.randint(1,1000)
    aa = random.randint(1,1000)
    r = str(cal2(a,aa)) + " m\n"
    q = "If a point on the circumference of the wheel rotating with an angular acceleration of " + str(aa) + " rad/s2 has a acceleration of " + str(a) + " m/s2. What is the radius of the wheel ?\n"
    return q,r

for i in range(no_of_samples):
    types = random.randint(0,4)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3:
        ques,answer = type4()
    elif types == 4:
        ques,answer = type5()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()