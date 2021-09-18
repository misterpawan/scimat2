
import random

# The average energy released per fission for 239Pu94 is 180 MeV. How much energy per fission is released if all the atoms in m g of pure 239Pu94 undergo fission.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 10000

N = 6.023 * (10**23)

for i in range(no_of_samples):
    m = random.randint(1,20000)
    m = round(m/10,1)
    ques = "The average energy released per fission for 239Pu94 is 180 MeV. How much energy per fission is released if all the atoms in " + str(m) + " g of pure 239Pu94 undergo fission.\n"
    answ = (N*m*180*1.6*(10**-13))/239
    answer = "{:.2e}".format(answ) + "joule\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
