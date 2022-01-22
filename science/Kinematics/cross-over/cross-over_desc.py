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
        des = "initially, relative velocity(u_ba) is 0 ms-1 between the trains, when driver of train b decides to overtake train a, till the point guard of train b(end of train b) brushes driver of train a, train b has to travel a distance of s(separation distance to be travelled for driver b to reach back of train a) + length of train a(driver to train b to reach driver of train a) + length of train(for end of train b to reach driver a), total distance is equal to s+2*l, which is equal to distance = u_ba*t + 1/2*a*t^2 = 0+1/2*"+str(acc)+"*"+str(t)+"^2 = "+str(temp)+" m, hence separation s = "+str(temp)+" - 2 * "+str(s)+" = "+str(temp-2*s)+" m.\n"
    else:
        v1 = random.randint(1,500)
        v2 = random.randint(v1+1,v1+100)
        distance = random.randint(1,100)
        q = "On a two-lane road, car A is travelling with a speed of "+str(v1)+" ms-1. Two cars B and C approach car A in opposite directions with a speed of "+str(v2)+" ms-1 each. At a certain instant, when the distance AB is equal to AC, both being "+str(distance)+" km, B decides to overtake A before C does. What minimum acceleration of car B is required to avoid an accident?\n"
        vac = v1+v2
        vba = v2-v1
        t = (distance*1000)/vac
        acc = (2*(distance*1000 - vba*t))/(t**2)
        des = "relative speed of a w.r.t to c(v_ac) = "+str(v1)+"+"+str(v2)+" = "+str(vac)+" ms-1, b w.r.t to a(v_ba) = vb - va = "+str(v2)+"-"+str(v1)+" = "+str(vba)+" ms-1, time taken by c to cover distance ac  = "+str(distance*1000)+"/"+str(vac)+" = "+str(round(t,1))+" s, minimum acceleration required can be found by the formula s = u*t+(1/2)*a*t^2 => a = 2*(s-u*t)/(t^2) = 2*("+str(distance*1000)+"-"+str(vba)+"*"+str(round(t,1))+")/("+str(round(t,1))+"*"+str(round(t,1))+") = "+str(round(acc,1))+" ms-2\n"
    qns.write(q)
    ans.write(des)
    # print(q)
    # print(a)
qns.close()
ans.close()