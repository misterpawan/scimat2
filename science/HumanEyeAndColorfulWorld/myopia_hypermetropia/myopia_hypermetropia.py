import random

# The far point of a myopic person is x mm in front of the eye. What is the nature and power of the lens required to correct the problem.
# The near point of a hypermetropic person is x mm. What is the nature and power of the lens required to correct the problem(assume normal near point of eye is 25cm).
# A person with a myopic eye cannot see objects beyond x mm distinctly. What should be the type of the corrective lens used to restore proper vision?
# A person with a hypermetropic eye cannot see objects within x mm distinctly. What should be the type of the corrective lens used to restore proper vision?
# A person needs a lens of power – D dioptres for correcting his distant vision. What is the focal length of the lens required for correcting distant vision?
# A person needs a lens of power + D dioptres for correcting his near vision. What is the focal length of the lens required for correcting near vision?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 300000
near_point = 250

def calculation_near(far):
    return round(1000/far,2)

def calculation_far(near):
    return round(((near-near_point)*1000)/(near_point*near),2)

def type1():
    far = random.randint(500,100000)
    q = "The far point of a myopic person is "+str(far)+" mm in front of the eye. What is the nature and power of the lens required to correct the problem.\n"
    a = "concave lens, "+str(calculation_near(far)) + " diatrope\n"
    return q,a

def type2():
    near = random.randint(500,100000)
    q = "The near point of a hypermetropic person is "+str(near)+" mm. What is the nature and power of the lens required to correct the problem(assume normal near point of eye is 25cm).\n"
    a = "convex lens, "+str(calculation_far(near))+" diatrope\n"
    return q,a

def type11():
    far = random.randint(500,100000)
    q = "A person with a myopic eye cannot see objects beyond "+str(far)+" mm distinctly. What should be the type of the corrective lens used to restore proper vision?\n"
    a = "concave lens, "+str(calculation_near(far)) + " diatrope\n"
    return q,a

def type21():
    near = random.randint(500,100000)
    q = "A person with a hypermetropic eye cannot see objects within "+str(near)+" mm distinctly. What should be the type of the corrective lens used to restore proper vision?\n"
    a = "convex lens, "+str(calculation_far(near))+" diatrope\n"
    return q,a

def type3():
    D = random.randint(500,100000)
    q = "A person needs a lens of power – "+str(D)+" dioptres for correcting his distant vision. What is the focal length of the lens required for correcting distant vision?\n"
    a = str(calculation_near(D)) + " mm\n"
    return q,a

def type4():
    D = random.randint(500,100000)
    q = "A person needs a lens of power + "+str(D)+" dioptres for correcting his near vision. What is the focal length of the lens required for correcting near vision?\n"
    a = str(calculation_near(D)) + " mm\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,6)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    elif types == 4:
        ques,answer = type4()
    elif types == 5:
        ques,answer = type11()
    elif types == 6:
        ques,answer = type21()
    # print(ques,answer)
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()