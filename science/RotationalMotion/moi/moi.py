import random

# A solid cylinder of mass m kg has a radius of r m. What is the moment of inertia with respective to its symmetric axis.
# A hollow cylinder of mass m kg has a radius of r m. What is the moment of inertia with respective to its symmetric axis.
# A solid sphere of mass m kg has a radius of r m. What is the moment of inertia with respective to its symmetric axis.
# A hollow sphere of mass m kg has a radius of r m. What is the moment of inertia with respective to its symmetric axis.
# A solid disc of mass m kg has a radius of r m. What is the moment of inertia with respective to its symmetric axis.
# A hoop of mass m kg has a radius of r m. What is the moment of inertia with respective to its symmetric axis.
# A hoop of mass m kg has a radius of r m. What is the moment of inertia with respective to its diameter.
# A rod of mass m kg has a length of r m. What is the moment of inertia with respective to its center.
# A rod of mass m kg has a length of r m. What is the moment of inertia with respective to its end.
# A solid cylinder of mass m kg has a radius of r m and length l. What is the moment of inertia with respective to its diameter.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 4000000
con = [1/2, 1, 2/5, 2/3, 1/2, 1, 1/2, 1/12, 1/3]

def cal1(c, m, r) :
    return round(c*m*r*r,1)

def type1() :
    m = random.randint(1,10000)
    r = random.randint(1,100)
    l = random.randint(1,100)
    t = random.randint(0,9)
    if t == 0 :
        q = "A solid cylinder of mass " + str(m) + " kg has a radius of " + str(r) + " m. What is the moment of inertia with respective to its symmetric axis.\n"
        a = str(cal1(con[0], m, r)) + " kgm2\n"
    elif t == 1:
        q = "A hollow cylinder of mass " + str(m) + " kg has a radius of " + str(r) + " m. What is the moment of inertia with respective to its symmetric axis.\n"
        a = str(cal1(con[1], m, r)) + " kgm2\n"
    elif t == 2:
        q = "A solid sphere of mass " + str(m) + " kg has a radius of " + str(r) + " m. What is the moment of inertia with respective to its symmetric axis.\n"
        a = str(cal1(con[2], m, r)) + " kgm2\n"
    elif t == 3:
        q = "A hollow sphere of mass " + str(m) + " kg has a radius of " + str(r) + " m. What is the moment of inertia with respective to its symmetric axis.\n"
        a = str(cal1(con[3], m, r)) + " kgm2\n"
    elif t == 4:
        q = "A solid disc of mass " + str(m) + " kg has a radius of " + str(r) + " m. What is the moment of inertia with respective to its symmetric axis.\n"
        a = str(cal1(con[4], m, r)) + " kgm2\n"
    elif t == 5:
        q = "A hoop of mass " + str(m) + " kg has a radius of " + str(r) + " m. What is the moment of inertia with respective to its symmetric axis.\n"
        a = str(cal1(con[5], m, r)) + " kgm2\n"
    elif t == 6:
        q = "A hoop of mass " + str(m) + " kg has a radius of " + str(r) + " m. What is the moment of inertia with respective to its diameter.\n"
        a = str(cal1(con[6], m, r)) + " kgm2\n"
    elif t == 7:
        q = "A rod of mass " + str(m) + " kg has a length of " + str(r) + " m. What is the moment of inertia with respective to its center.\n"
        a = str(cal1(con[7], m, r)) + " kgm2\n"
    elif t == 8:
        q = "A rod of mass " + str(m) + " kg has a length of " + str(r) + " m. What is the moment of inertia with respective to its end.\n"
        a = str(cal1(con[8], m, r)) + " kgm2\n"
    elif t == 9:
        q = "A solid cylinder of mass " + str(m) + " kg has a radius of " + str(r) + " m and length of " + str(l) + " m. What is the moment of inertia with respective to its diameter.\n"
        a = str(cal1(con[7], m, l) + cal1(con[0],m,r)) + " kgm2\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
