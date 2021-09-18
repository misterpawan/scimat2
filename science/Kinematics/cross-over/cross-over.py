import random

# Two trains A and B of length 400 m each are moving on two parallel tracks with a uniform speed of 71 ms-1 in the same direction, with A ahead of B. The driver of B decides to overtake A and accelerates by 1 ms-1. If after 50 s, the guard of B just brushes past the driver of A, what was the original distance between them?
# On a two-lane road, car A is travelling with a speed of 36 ms-1. Two cars B and C approach car A in opposite directions with a speed of 54 ms-1 each. At a certain instant, when the distance AB is equal to AC, both being 1 km, B decides to overtake A before C does. What minimum acceleration of car B is required to avoid an accident?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        acc = random.randint(1,10)
        t = random.randint(20,30)
        s = random.randint(1,100)
        v = random.randint(1,1000)
        q = "Two trains A and B of length "+str(s)+" m each are moving on two parallel tracks with a uniform speed of "+str(v)+" ms-1 in the same direction, with A ahead of B. The driver of B decides to overtake A and accelerates by "+str(acc)+" ms-2. If after "+str(t)+" s, the guard of B just brushes past the driver of A, what was the original distance between them?\n"
        temp = (1/2)*acc*t*t
        a = str(round(temp-2*s,1)) + " m\n"
    else:
        v1 = random.randint(1,500)
        v2 = random.randint(v1+1,v1+100)
        distance = random.randint(1,100)
        q = "On a two-lane road, car A is travelling with a speed of "+str(v1)+" ms-1. Two cars B and C approach car A in opposite directions with a speed of "+str(v2)+" ms-1 each. At a certain instant, when the distance AB is equal to AC, both being "+str(distance)+" km, B decides to overtake A before C does. What minimum acceleration of car B is required to avoid an accident?\n"
        vac = v1+v2
        vba = v2-v1
        t = (distance*1000)/vac
        acc = (2*(distance*1000 - vba*t))/(t**2)
        a = "relative speed of a w.r.t to c is "+str(vac)+" ms-1, b w.r.t to a is "+str(vba)+" ms-1, time taken by c to cover distance ac is "+str(round(t,1))+" s, minimum acceleration required is "+str(round(acc,1))+" ms-2\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()