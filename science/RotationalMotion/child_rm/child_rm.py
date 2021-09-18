import random

# A child stands at the centre of a turntable with his arms outstretched. The turntable is set rotating with an angular speed of w rad/s. How much is the angular speed of the child if he folds his hands back and thereby reduces his moment of inertia to n times the initial value? Assume that the turntable rotates without friction.
# A child stands at the centre of a turntable with his arms outstretched. The turntable is set rotating with an angular speed of w rad/s. How many times is the kinetic energy of the rotation is increased if he folds his hands back and thereby reduces his moment of inertia to n times the initial value? Assume that the turntable rotates without friction.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(n1, n2, w) :
    return round((n2*w)/n1,1)

def cal2(n1, n2) :
    return round((n2*n2*n2)/(n1*n1*n1),1)

def type1() :
    w = random.randint(1,200)
    n1 = random.randint(1,100)
    n2 = random.randint(n1+1,n1+100)
    q = "A child stands at the centre of a turntable with his arms outstretched. The turntable is rotating with an angular speed of " + str(w) + " rad/s. How much is the angular speed of the child if he folds his hands back and thereby reduces his moment of inertia to " + str(n1) + "/" + str(n2) + " times the initial value?\n"
    a = str(cal1(n1, n2, w)) + "rad/s\n"
    return q,a

def type2() :
    w = random.randint(1,1000)
    n1 = random.randint(1,40)
    n2 = random.randint(n1+1,n1+40)
    q = "A child stands at the centre of a turntable with his arms outstretched. The turntable is rotating with an angular speed of " + str(w) + " rad/s. How many times is the kinetic energy of the rotation is increased if he folds his hands back and thereby reduces his moment of inertia to " + str(n1) + "/" + str(n2) + " times the initial value?\n"
    a = str(cal2(n1, n2)) + "\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    else :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
