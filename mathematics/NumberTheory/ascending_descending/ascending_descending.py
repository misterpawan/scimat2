import random
import operator

# Put -534, 4, 3 in descending order.
# Sort -3, 10, 5, 0, -2 in decreasing order.
# Sort 2, 4, 0, 6.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
arr = ['descending', 'ascending']

def num_gen():
    types = random.randint(1,20)
    if types<=14:
        return random.randint(-100, 100),0
    elif types<=17:
        num = random.randint(-100,100)
        return round(num/100,2),0
    else:
        num = random.randint(-10,10)
        den = random.randint(1,20)
        return num, den

def number_formation(q, types):
    nums = []
    a_arr = []
    b_arr = []
    no_of_nums = random.randint(3,5)
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
    
    for i in range(no_of_nums):
        if b_arr[i]==0:
            nums.append(a_arr[i])
            q = q + str(a_arr[i])
        else:
            nums.append(round(a_arr[i]/b_arr[i],2))
            q = q + str(a_arr[i]) + "/" + str(b_arr[i])
        if i != no_of_nums - 1:
            q = q + ","
        q = q + " "
    
    an = ""
    enumerate_object = enumerate(nums)
    if types == 1 or types == 3:
        sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1), reverse=True)
    else:
        sorted_pairs = sorted(enumerate_object, key=operator.itemgetter(1))
    sorted_indices = []
    sorted_ele = []
    for index, element in sorted_pairs:
        sorted_indices.append(index)
        sorted_ele.append(element)
    for i in range(len(sorted_ele)):
        if b_arr[sorted_indices[i]]==0:
            an = an + str(sorted_ele[i])
        else:
            an = an + str(a_arr[sorted_indices[i]])+"/"+str(b_arr[sorted_indices[i]])
        if i!=len(sorted_ele)-1:
            an = an +", "
    return q, an + "\n"

for i in range(no_of_samples):
    types = random.randint(1,5)
    if types <=2:
        q = "Put "
        q, an = number_formation(q,types)
        q = q + "in " + arr[types-1] + " order.\n"
    elif types <= 5:
        q = "Sort "
        q, an = number_formation(q,types)
        if types <= 4:
            q = q + "in " + arr[types-3] + " order.\n"
        else:
            q = q[:-1]+"."+"\n"
    qns.write(q)
    ans.write(an)
qns.close()
ans.close()