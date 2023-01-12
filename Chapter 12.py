# exercise  1
def sumall(*t):
    print(sum(t))

# exercise 2
def sort_by_length(*words):
        t = []
        for word in words:
            t.append((len(word), word))

        t.sort(reverse = True)

        res = []
        for length, word in t:
            res.append(word)
        return res

#exercise3
def most_frequent(word):
    letter_vs_freq = dict()
    for letter in word:
        if letter not in letter_vs_freq:
            letter_vs_freq[letter] = 1
        else:
            letter_vs_freq[letter] += 1

    letter_vs_freq_list = letter_vs_freq.items()
    letter_vs_freq_list = sorted(letter_vs_freq_list, key=lambda x: x[1], reverse=True)

    new_word = ""
    for letter, freq in letter_vs_freq_list:
        new_word += letter*freq
    return new_word

#exercise4
def anagram_check():
    anagram_dict = dict()
    with open("words.txt") as f:
        for line in f:
            word = line.strip('\n')
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)

    for sorted_word, anagrams in anagram_dict.items():
        if len(anagrams) > 1:
            print(anagrams)

def anagram_length_order():
    anagram_dict = dict()
    with open("words.txt") as f:
        for line in f:
            word = line.strip('\n')
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
        
    sorted_word_vs_length = dict()
    for sorted_word, anagram_list in anagram_dict.items():
        sorted_word_vs_length[sorted_word] = len(anagram_list)
    sorted_word_vs_length = sorted_word_vs_length.items()
    sorted_word_vs_length = sorted(sorted_word_vs_length, key=lambda x: x[1], reverse=True)
    
    i = 0
    for sorted_word, length in sorted_word_vs_length:
        if i > 10: break
        print(anagram_dict[sorted_word])
        i += 1

def scrable_bingo():
    anagram_dict = dict()
    with open("words.txt") as f:
        for line in f:
            word = line.strip('\n')
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
    

    sorted_word_vs_length = dict()
    for sorted_word, anagram_list in anagram_dict.items():
        sorted_word_vs_length[sorted_word] = len(anagram_list)
    sorted_word_vs_length = sorted_word_vs_length.items()
    sorted_word_vs_length = sorted(sorted_word_vs_length, key=lambda x: x[1], reverse=True)

    for sorted_word, anagrams in sorted_word_vs_length:
        if len(sorted_word) == 8:
            print(anagram_dict[sorted_word])
            break


def metathesis_pair():
    anagram_dict = dict()
    with open("words.txt") as f:
        for line in f:
            word = line.strip('\n')
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
    
    metathesis_set = [] 
    for anagrams in anagram_dict.values():
        if len(anagrams) < 2: continue
        for word1, word2 in single_list_cartesian_product(anagrams):
            count = 0
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    count += 1
            if count == 2:
                metathesis_set.append((word1, word2))
    return metathesis_set

def single_list_cartesian_product(input_list):
    output_list = []
    for i in range(len(input_list)-1):
        for j in range(i+1, len(input_list)):
            output_list.append((input_list[i], input_list[j]))
    return output_list

#Exercise6
word_dict = {}
with open("words.txt","r") as f:
        for line in f:
            word = line.strip('\n')
            word_dict[word] = 0
    
def reduce_word_by_one(word):
    children_list = []
    for i in range(len(word)):
        s = word[0:i] + word[i+1:]
        if s not in children_list:
            children_list.append(s)
    return children_list

def get_all_reduced_word(word, word_list=None):
    if word_list is None:
        word_list = {}

    for w in reduce_word_by_one(word):
        if w in word_dict:
            word_list[w] = 0
            if len(w) > 0:
                get_all_reduced_word(w, word_list)
    return list(word_list.keys())

def longest_reducible_word():
    longest_reduced_word = ""
    longest_reduced_list = None
    for word in word_dict:
        if len(word) > len(longest_reduced_word):
            reduced_list = get_all_reduced_word(word)
            if "" in reduced_list:
                longest_reduced_word = word
                longest_reduced_list = reduced_list
    print(longest_reduced_word)
    print(longest_reduced_list)

def main():
    # print(get_all_reduced_word(word))
    # longest_reducible_word()
    # print(reduce_word_by_one('sprite'))
    # print(longest_reducible_word(children_word))
    # print_the_longest_reducible_word(reducible_word)
    # print(metathesis_pair())
    # print(single_list_cartesian_product([1, 'a', 2, 'b']))
    pass

if __name__ == "__main__":
    main()