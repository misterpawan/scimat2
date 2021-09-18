import random

# Two sitar strings A and B playing the note ‘Ga’ are slightly out of tune and produce beats of frequency 6Hz. The tension in the string A is slightly reduced and the beat frequency is found to reduce to 3Hz. If the original frequency of A is 324 Hz, what is the frequency of B?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20
arr = ["reduced","increased"]

for i in range(no_of_samples):
    fund = random.randint(100,1300)
    f1 = random.randint(1,60)
    f2 = random.randint(1,60)
    while f2 == f1:
        f2 = random.randint(1,60)
    types = random.randint(0,1)
    q = "Two sitar strings A and B playing the note ‘Ga’ are slightly out of tune and produce beats of frequency "+str(f1)+" Hz. The tension in the string A is slightly "+arr[types]+" and the beat frequency is found to be "+str(f2)+" Hz. If the original frequency of A is "+str(fund)+" Hz, what is the frequency of B?\n"
    if types == 0:
        if f2 < f1:
            a = str(fund-f1)+" hertz\n"
        else:
            a = str(fund+f1)+" hertz\n"
    else:
        if f2 < f1:
            a = str(fund+f1)+" hertz\n"
        else:
            a = str(fund-f1)+" hertz\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()