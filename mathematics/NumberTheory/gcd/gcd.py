import random
import math
from tqdm import tqdm

# Calculate/What is the highest/greatest common divisor of 1300 and 300.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
num_samples = 1500000
start_word = ["What is","Calculate"]
middle_word = ["highest","greatest"]

for i in tqdm(range(num_samples)):
    start = random.randint(0,1)
    middle = random.randint(0,1)
    q = start_word[start]+" the "+middle_word[middle]+" common divisor of "
    prob_gcd = random.randint(1,400)
    mul1 = random.randint(1,500)
    mul2 = random.randint(1,500)
    while mul1 == mul2:
        mul2 = random.randint(1,500)
    q += str(mul1*prob_gcd) + " and " + str(mul2*prob_gcd)
    if start:
        q += ".\n"
    else:
        q += "?\n"
    a = str(math.gcd(prob_gcd*mul1,prob_gcd*mul2))+"\n"
    qns.write(q)
    ans.write(a)
qns.close()
ans.close()