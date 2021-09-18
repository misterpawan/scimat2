import random

# A solid cylinder of mass 20 kg rotates about its axis with angular speed 100 rad s-1. The radius of the cylinder is 0.25 m. What is the magnitude of angular momentum of the cylinder about its axis?
# A solid sphere of mass 20 kg rotates about its axis with angular speed 100 rad s-1. The radius of the sphere is 0.25 m. What is the magnitude of angular momentum of the sphere about its axis? 
# A hollow sphere of mass 20 kg rotates about its axis with angular speed 100 rad s-1. The radius of the sphere is 0.25 m. What is the magnitude of angular momentum of the sphere about its axis?
# A rod of mass 20 kg rotates about its end with angular speed 100 rad s-1. The length of the rod is 0.25 m. What is the magnitude of angular momentum of the rod about its end?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2000000
con = [1/2, 2/5, 2/3, 1/3]

def cal1(c, m, r, w) :
    return round(c*m*r*r*w,1)

def type1() :
    m = random.randint(1,1000)
    r = random.randint(1,40)
    w = random.randint(1,40)
    t = random.randint(0,3)
    if t == 0 :
        q = "A solid cylinder of mass " + str(m) + " kg rotates about its axis with angular speed " + str(w) + " rad s-1. The radius of the cylinder is " + str(r) + " m. What is the magnitude of angular momentum of the cylinder about its axis?\n"
        a = str(cal1(con[0], m, r, w)) + " kgm2\n"
    elif t == 1:
        q = "A solid sphere of mass " + str(m) + " kg rotates about its axis with angular speed " + str(w) + " rad s-1. The radius of the sphere is " + str(r) + " m. What is the magnitude of angular momentum of the sphere about its axis?\n"
        a = str(cal1(con[1], m, r, w)) + " kgm2\n"
    elif t == 2:
        q = "A hollow sphere of mass " + str(m) + " kg rotates about its axis with angular speed " + str(w) + " rad s-1. The radius of the sphere is " + str(r) + " m. What is the magnitude of angular momentum of the sphere about its axis?\n"
        a = str(cal1(con[2], m, r, w)) + " kgm2\n"
    elif t == 3:
        q = "A rod of mass " + str(m) + " kg rotates about its end with angular speed " + str(w) + " rad s-1. The length of the rod is " + str(r) + " m. What is the magnitude of angular momentum of the rod about its end?\n"
        a = str(cal1(con[3], m, r, w)) + " kgm2\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
