import random
import re
from tqdm import tqdm

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
num_samples = 1000000

def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end))
    return res

for i in tqdm(range(num_samples)):
    randLenOfSeq1 = random.randint(2,7)
    randLenOfSeq2 = random.randint(2,7)

    list1 = list(set(random.sample(range(1, 30), randLenOfSeq1)))
    list2 = list(set(random.sample(range(1, 30), randLenOfSeq2)))
    #print('list1')
    #print(list1)
    list1.sort()
    list2.sort()
    #print('list1')
    #print(list1)
    listToStr1 = " "
    listToStr2 = " "
    for number in list1:
        listToStr1+= str(number)+" , "
    for number in list2:
        listToStr2+= str(number)+" , "

    listToStr1 = listToStr1.rstrip(" , ")
    listToStr2 = listToStr2.rstrip(" , ")

    line3 = "Find the intersection of { "+listToStr1+" } and { "+listToStr2+" } "
    #k1 = re.sub('\s+', ' ', line1)
    #k2 = re.sub('\s+', ' ', line2)
    question = re.sub('\s+', ' ', line3) + "\n"

    list3 = list(set(list1) & set(list2))
    list3.sort()
    listToStr3 = " "
    for number in list3:
        listToStr3+= str(number)+" , "
    listToStr3 = listToStr3.rstrip(" , ")
    listToStr3 = " { "+listToStr3+" } "
    #k1 = re.sub('\s+', ' ', line1)
    #k2 = re.sub('\s+', ' ', line2)
    answer = re.sub('\s+', ' ', listToStr3) + "\n"
    
    qns.write(question)
    ans.write(answer)

qns.close()
ans.close()
