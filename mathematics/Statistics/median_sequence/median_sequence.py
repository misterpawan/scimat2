import random
import re
import numpy as np
from tqdm import tqdm
from statistics import median 

# Find the median of sequence ( 29 , 11 , 11 , 3 , 9 , 6 ) 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
num_samples = 1000000

def Rand(start, end, num): 
    res = []
    for j in range(num): 
        res.append(random.randint(start, end))
    return res

for i in tqdm(range(num_samples)):
    randLenOfSeq = random.randint(4,9)
    listOfrandomNumbers = Rand(1,50,randLenOfSeq)
    listToStr = " "
    for number in listOfrandomNumbers:
        listToStr+= str(number)+" , "
    listToStr = listToStr.rstrip(" , ")
    line3 = "Find the median of sequence ( "+listToStr+" ) "#+" with length "+str(randLenOfSeq)
    question = re.sub('\s+', ' ', line3) + "\n"

    tempAns = float(median(listOfrandomNumbers))
    if((tempAns).is_integer()):
        line3 = str(round(tempAns))
    else:
        line3 = "{:.2f}".format(tempAns)

    answer = re.sub('\s+', ' ', line3) + "\n"
    qns.write(question)
    ans.write(answer)