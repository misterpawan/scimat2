import random
import math
from tqdm import tqdm

# Calculate/What is the smallest/lowest/least common multiple of 351 and 141.
# Calculate/Find/What is the common denominator of -29/936 and -115/48.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
num_samples = 1500000
start_word = ["What is","Calculate","Find"]
middle_word = ["smallest","lowest","least"]

for i in tqdm(range(num_samples)):
    if random.randint(0,1):
        start = random.randint(0,1)
        middle = random.randint(0,1)
        q = start_word[start]+" the "+middle_word[middle] + " common multiple of "
        prob_gcd = random.randint(1,200)
        mul1 = random.randint(1,500)
        mul2 = random.randint(1,500)
        while mul1 == mul2:
            mul2 = random.randint(1,500)
        q += str(mul1*prob_gcd) + " and " + str(mul2*prob_gcd)
        if start:
            q += ".\n"
        else:
            q += "?\n"
    else:
        start = random.randint(0,2)
        q = start_word[start] + " the common denominator of "
        prob_gcd = random.randint(1,20)
        mul1 = random.randint(2,20)
        mul2 = random.randint(2,20)
        num1 = random.randint(1,200)
        num2 = random.randint(1,200)
        while mul1 == mul2:
            mul2 = random.randint(2,20)
        q += str(num1)+"/"+str(mul1*prob_gcd)+" and "+str(num2)+"/"+str(mul2*prob_gcd)
        if start:
            q += ".\n"
        else:
            q += "?\n"
    a = str((mul1*mul2*prob_gcd*prob_gcd)/math.gcd(mul1*prob_gcd,mul2*prob_gcd))+"\n"
    qns.write(q)
    ans.write(a)
qns.close()
ans.close()