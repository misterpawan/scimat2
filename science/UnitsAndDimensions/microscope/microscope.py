import random

# A student measures the thickness of human hair using a microscope of magnification 100. He makes 20 observations and average width obtained in the field of view of microscope is 3.5 mm. What is the estimate on the thickness of hair?
# A student measures the thickness of human hair by magnifying it using a microscope. He makes 20 observations and average width obtained in the field of view of microscope is 3.5 mm. If the estimate on the thickness of hair is x mm, then what is its magnification?
qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 10

def type1():
    magnification = random.randint(100,200)
    num_observations = random.randint(1,500)
    avg_val = round(random.randint(100,400) / 100,2)
    ques = "A student measures thickness of human hair using a microscope of magnification "+str(magnification)+". He makes "+str(num_observations)+" observations and average width obtained in the field of view of microscope is "+str(avg_val)+" mm. What is the estimate on the thickness of hair?\n"
    answer = str(round(avg_val/magnification,4)) + " mm\n"
    return ques,answer

def type2():
    num_observations = random.randint(1,500)
    avg_val = round(random.randint(100,400) / 100,2)
    real_val = round(random.randint(100,200)*avg_val,2)
    ques = "A student measures the thickness of human hair by magnifying it using a microscope. He makes "+str(num_observations)+" observations and average width obtained in the field of view of microscope is "+str(avg_val)+" mm. If the estimate on the thickness of hair is "+str(real_val)+" mm, then what is its magnification?"
    answer = str(avg_val//real_val) + "\n"

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        ques,answer = type1()
    else:
        ques,answer = type2()
    # print(ques,answer)
    qns.write(ques)
    ans.write(answer)
qns.close()
ans.close()