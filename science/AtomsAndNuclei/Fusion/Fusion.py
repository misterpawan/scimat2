
from mendeleev import element
import random

# How long can an electric lamp of p W be kept glowing by fusion of m g of deuterium ? Take fusion reaction as 2H1 + 2H1 -> 3He1 + n + 3.27 MeV

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

N = 6.023 * (10**23)

for i in range(no_of_samples):
    p = random.randint(1,500)
    m = random.randint(1,2000)
    ques = "How long can an electric lamp of " + str(p) + " W be kept glowing by fusion of " + str(m) + " g of deuterium ? Take fusion reaction as 2H1 + 2H1 -> 3He1 + n + 3.27 MeV\n"
    ener = (N*m*3.27*1.6*(10**-13))/4
    answ = ener/p
    answer = "{:.2e}".format(answ) + "sec\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
