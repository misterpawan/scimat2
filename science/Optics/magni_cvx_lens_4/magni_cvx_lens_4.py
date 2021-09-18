import random

# A convex lens produces a virtual image of height hi cm at a distance of v cm from it of a real object placed u cm in front of it. What is the height of the object ?
# A convex lens produces a virtual image of at a distance of v cm from it of a real object having height of ho cm and placed u cm in front of it. What is the height of the image ?
# A convex lens produces a virtual image of height hi cm of a real object having height ho cm and placed u cm in front of it. At what distance image is formed from the lens ?
# A convex lens produces a virtual image of height hi cm at a distance of v cm from it of a real object having a height of ho cm. At what distance object is placed from the lens ? 
# A convex lens produces a real image of height hi cm at a distance of v cm from it of a real object placed u cm in front of it. What is the height of the object ?
# A convex lens produces a real image of at a distance of v cm from it of a real object having height of ho cm and placed u cm in front of it. What is the height of the image ?
# A convex lens produces a real image of height hi cm of a real object having height ho cm and placed u cm in front of it. At what distance image is formed from the lens ?
# A convex lens produces a real image of height hi cm at a distance of v cm from it of a real object having a height of ho cm. At what distance object is placed from the lens ?
# m = v/u = hi/ho

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 4000000

def calculation_v (u, hi, ho):
    return round((u*hi)/ho,1)

def calculation_u(v, hi, ho) :
    return round((ho*v)/hi,1)

def calculation_hi(u, v, ho) :
    return round((v*ho)/u,1)

def calculation_ho(u, v, hi) :
    return round((hi*u)/v,1)

def type1():
    u = random.randint(1,100)
    v = random.randint(u+1,u+100)
    hi = random.randint(1,100)
    q = "A convex lens produces a virtual image of height " + str(hi) + " cm at a distance of " + str(v) + " cm from it of a real object placed " + str(u) + " cm in front of it. What is the height of the object ?\n"
    ho = str(calculation_ho(u, v, hi)) + " cm\n"
    return q,ho

def type2():
    u = random.randint(1,100)
    v = random.randint(u+1,u+100)
    ho = random.randint(1,100)
    q = "A convex lens produces a virtual image of at a distance of " + str(v) + " cm from it of a real object having height of " + str(ho) + " cm and placed " + str(u) + " cm in front of it. What is the height of the image ?\n"
    hi = str(calculation_hi(u, v, ho)) + " cm\n"
    return q,hi

def type3():
    u = random.randint(1,100)
    ho = random.randint(1,100)
    hi = random.randint(ho+1,ho+100)
    q = "A convex lens produces a virtual image of height " + str(hi) + " cm of a real object having height " + str(ho) + " cm and placed " + str(u) + " cm in front of it. At what distance image is formed from the lens ?\n"
    v = str(calculation_v(u, hi, ho)) + " cm\n"
    return q,v

def type4():
    v = random.randint(1,100)
    ho = random.randint(1,100)
    hi = random.randint(ho+1,ho+100)
    q = "A convex lens produces a virtual image of height "+ str(hi) + " cm at a distance of " + str(v) + " cm from it of a real object having a height of " + str(ho) + " cm. At what distance object is placed from the lens ?\n"
    u = str(calculation_u(v, hi, ho)) + " cm\n"
    return q,u

def type5():
    u = random.randint(1,100)
    v = random.randint(1,100)
    hi = random.randint(1,100)
    q = "A convex lens produces a real image of height " + str(hi) + " cm at a distance of " + str(v) + " cm from it of a real object placed " + str(u) + " cm in front of it. What is the height of the object ?\n"
    ho = str(calculation_ho(u, v, hi)) + " cm\n"
    return q,ho

def type6():
    u = random.randint(1,100)
    v = random.randint(1,100)
    ho = random.randint(1,100)
    q = "A convex lens produces a real image of at a distance of " + str(v) + " cm from it of a real object having height of " + str(ho) + " cm and placed " + str(u) + " cm in front of it. What is the height of the image ?\n"
    hi = str(calculation_hi(u, v, ho)) + " cm\n"
    return q,hi

def type7():
    u = random.randint(1,100)
    ho = random.randint(1,100)
    hi = random.randint(1,100)
    q = "A convex lens produces a real image of height " + str(hi) + " cm of a real object having height " + str(ho) + " cm and placed " + str(u) + " cm in front of it. At what distance image is formed from the lens ?\n"
    v = str(calculation_v(u, hi, ho)) + " cm\n"
    return q,v

def type8():
    v = random.randint(1,100)
    ho = random.randint(1,100)
    hi = random.randint(1,100)
    q = "A convex lens produces a real image of height "+ str(hi) + " cm at a distance of " + str(v) + " cm from it of a real object having a height of " + str(ho) + " cm. At what distance object is placed from the lens ?\n"
    u = str(calculation_u(v, hi, ho)) + " cm\n"
    return q,u

for i in range(no_of_samples):
    types = random.randint(1,8)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    elif types == 4:
        ques,answer = type4()
    elif types == 5:
        ques,answer = type5()
    elif types == 6:
        ques,answer = type6()
    elif types == 7:
        ques,answer = type7()
    elif types == 8:
        ques,answer = type8()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()