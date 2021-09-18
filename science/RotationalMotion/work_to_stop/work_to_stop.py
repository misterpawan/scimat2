import random

# A hoop of radius r m weighs m kg. It rolls along a horizontal floor so that its centre of mass has a speed of v m/s. How much work has to be done to stop it?
# A circular disk of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A hollow sphere of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A solid sphere of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A hollow cylinder of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?
# A solid cylinder of radius 2 m weighs 100 kg. It rolls along a horizontal floor so that its centre of mass has a speed of 20 cm/s. How much work has to be done to stop it?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 3000000
con = [1, 1/2, 2/3, 2/5, 1, 1/2]

def cal1(c, m, r, v) :
    return round(0.5*(c+1)*m*v*v,1) 

def type1() :
    m = random.randint(1,100)
    r = random.randint(1,500)
    v = random.randint(1,40)
    t = random.randint(0,5)
    if t == 0 :
        q = "A hoop of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    elif t == 1:
        q = "A circular disk of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    elif t == 2:
        q = "A hollow sphere of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    elif t == 3:
        q = "A solid sphere of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    elif t == 4:
        q = "A hollow cylinder of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    elif t == 5:
        q = "A solid cylinder of radius " + str(r) + " m weighs " + str(m) + " kg. It rolls along a horizontal floor so that its centre of mass has a speed of " + str(v) + " m/s. How much work has to be done to stop it?\n"
        a = str(cal1(con[0], m, r, v)) + " joules\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
