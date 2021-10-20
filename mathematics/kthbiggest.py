import random
import operator

# What is the third biggest value in -0.25, 403, -1?
# Which is the biggest value?  (a) -2/79  (b) 1  (c) 6/17

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
arr = ['biggest', 'smallest']
qn_arr = ['','','second','third','fourth','fifth']
abcde = ['(a)','(b)','(c)','(d)','(e)']

def num_gen():
    types = random.randint(1,20)
    if types<=8:
        return random.randint(-100, 100),0
    elif types<=14:
        num = random.randint(-100,100)
        return round(num/100,2),0
    else:
        num = random.randint(-10,10)
        den = random.randint(1,20)
        return num, den

for j in range(no_of_samples):
    no_of_nums = random.randint(3,5)
    qn_word = random.randint(1,no_of_nums)
    big_small = random.randint(0,1)
    
    nums = []
    a_arr = []
    b_arr = []
    temp = [] 
    count = 0    
    while count < no_of_nums:
        a, b = num_gen()
        a_arr.append(a)
        b_arr.append(b)
        if b==0:
            if a in temp:
                continue
            else:
                temp.append(a)
                count+=1
        else:
            if round(a/b,2) in temp:
                continue
            else:
                temp.append(round(a/b,2))
                count+=1

    types = random.randint(1,6)
    if types!=6:
        if qn_word!=1:
            q = "Which is the "+qn_arr[qn_word]+" "+arr[big_small]+" value? "
        else:
            q = "Which is the "+arr[big_small]+" value? "     
        for i in range(no_of_nums):
            q = q + abcde[i] + " "
            if b_arr[i]==0:
                q = q + str(a_arr[i])
            else:
                q = q + str(a_arr[i])+"/"+str(b_arr[i])
            if i!=no_of_nums-1:
                q = q + " "
        q = q + "\n"
    else:
        if qn_word!=1:
            q = "What is the "+qn_arr[qn_word]+" "+arr[big_small]+" value in "
        else:
            q = "What is the "+arr[big_small]+" value in "
        for i in range(no_of_nums):
            if b_arr[i]==0:
                q = q + str(a_arr[i])
            else:
                q = q + str(a_arr[i])+"/"+str(b_arr[i])
            if i!=no_of_nums-1:
                q = q + ", "
            else:
                q = q + "?"
        q = q + "\n"

    an = ""
    enumerate_object = enumerate(temp)
    if big_small==0:
        sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1), reverse=True)   
    else:
        sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1))
    sorted_indices = []
    sorted_ele = []
    for index, element in sorted_pairs:
        sorted_indices.append(index)
        sorted_ele.append(element)
    if types == 6:
        if b_arr[sorted_indices[qn_word-1]]==0:
            an = str(a_arr[sorted_indices[qn_word-1]])
        else:
            an = str(a_arr[sorted_indices[qn_word-1]])+"/"+str(b_arr[sorted_indices[qn_word-1]])
    else:
        an = abcde[sorted_indices[qn_word-1]]
    qns.write(q)
    ans.write(an+"\n")
qns.close()
ans.close()