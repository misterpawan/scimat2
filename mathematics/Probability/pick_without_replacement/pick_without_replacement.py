import random
import math
# l = list(s)
# random.shuffle(l)
# result = ''.join(l)

# What is prob of picking 1 b and 1 p when two letters picked without replacement from tpppbbpbbb?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
ascii_a = ord('a')
number_to_word = ['','one','two','three','four','five','six','seven','eight','nine','ten']

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def shuffle(inp):
    l = list(inp)
    random.shuffle(l)
    full_string = ''.join(l)
    return full_string
for i in range(no_of_samples):
    total_letters_in_use = random.randint(2,5)
    chars_relative_ascii = random.sample(range(10),total_letters_in_use)
    freq_array = []
    letters_array = []
    
    for i in range(total_letters_in_use):
        freq_array.append(random.randint(1,5))
        letters_array.append(chr(ascii_a+chars_relative_ascii[i]))
    full_string = ""
    for i in range(total_letters_in_use):
        for j in range(freq_array[i]):
            full_string = full_string + letters_array[i]
    full_string = shuffle(full_string)
    length = len(full_string)
    no_of_letters_for_subpart = random.randint(1,2)
    letter_pos_subpart = random.sample(range(total_letters_in_use),no_of_letters_for_subpart)
    freq_for_subpart = []
    for i in range(no_of_letters_for_subpart):
        freq_for_subpart.append(random.randint(1,freq_array[letter_pos_subpart[i]]))
    subpart = ""
    no_of_letters = sum(freq_for_subpart)
    numerator = 1
    denominator = nCr(length,no_of_letters)
    if no_of_letters_for_subpart == 1:
        # print(freq_array[letter_pos_subpart[0]],freq_for_subpart[0])
        numerator = numerator * nCr(freq_array[letter_pos_subpart[0]],freq_for_subpart[0])
        subpart = str(freq_for_subpart[0]) + " " + str(letters_array[letter_pos_subpart[0]])
    elif no_of_letters_for_subpart == 2:
        # print(freq_array[letter_pos_subpart[0]],freq_for_subpart[0])
        # print(freq_array[letter_pos_subpart[1]],freq_for_subpart[1])
        numerator = numerator * nCr(freq_array[letter_pos_subpart[0]],freq_for_subpart[0])
        numerator = numerator * nCr(freq_array[letter_pos_subpart[1]],freq_for_subpart[1])
        subpart = str(freq_for_subpart[0]) + " " + str(letters_array[letter_pos_subpart[0]]) + " and " + str(freq_for_subpart[1]) + " " + str(letters_array[letter_pos_subpart[1]])
    ques = "What is prob of picking " + str(subpart) + " when " + number_to_word[no_of_letters] + " letters picked without replacement from " + str(full_string) + " ?\n"
    # print(full_string)
    # print(no_of_letters)
    # print(subpart)
    # print(numerator)
    # print(denominator,length,no_of_letters)
    # print(ques)
    answer = str(numerator) + " / " + str(denominator) + "\n"
    # print(answer)
    qns.write(ques)
    ans.write(answer)
    # print(nCr())
    
qns.close()
ans.close()