from tqdm.auto import tqdm

#Exercise 1
def read_a_file():
    dictionary_file = dict()
    with open("words.txt") as f:
        for line in f:
            word = line.strip()
            dictionary_file[word] = word
        return dictionary_file

#Exercise 2
def histogram(s):
    d = dict()
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] = d[x] + 1
    return d

def get_key_value(s):
    h = histogram(s)
    print (h.get('o', 0))

#Exercise 3
def print_hist(s):
    s = histogram(s)
    for c in s:
        print (c, s[c])

#Exercise 4
def reverse_lookup(d,v):
    list_key = []
    for k in d:
        if d[k] == v:
            list_key.append(k)
    return list_key

#Exercise 5
def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
def inverse_dict_default(d):
    inverse = {}
    for key, val in d.items():
        inverse.setdefault(val, []).append(key)
    return inverse

#Exercise 6
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

#Exercise 8
def string_en_de_code(s):
    encoded_string = s.encode(encoding = 'utf-8')
    decoded_string = encoded_string.decode()
    # print(type(encoded_string))
    # print(type(decoded_string))
    print(encoded_string)
    print(decoded_string)

dictionary_file = dict()
with open("words.txt") as f:
    for line in f:
        word = line.strip()
        dictionary_file[word] = word

#exercise9
def has_duplicated(dictionary_file):
    duplicated_dict = {}
    for word in dictionary_file:
       duplicated_dict[word] = 1 + duplicated_dict.get(word, 0)
       if duplicated_dict[word] > 1:
        return True
    return False

#Exercise 10
def rotate_pairs(dictionary_file):
    rotate_pairs = []
    for word in tqdm(dictionary_file): 
        if word[::-1] in dictionary_file:
            rotate_pairs.append((word,word[::-1]))
    return rotate_pairs

#Exercise 11
def homophone_puzzle():
    dictionary_cmu = dict()
    with open("cmudict-0.7b") as f:
        for line in f:
            if ord('A') <= ord(line[0]) <= ord('Z'):
                word, phoneme = line.strip().split("  ")
                dictionary_cmu[word] = phoneme
            else:
                continue
    # print(dictionary_cmu)
    solutions = []
    for word, phoneme in dictionary_cmu.items():
        if len(word) == 5:
            word1 = word[1:]
            word2 = word[0] + word[2:]
            if (
                word1 in dictionary_cmu and
                word2 in dictionary_cmu and
                dictionary_cmu[word1] == phoneme and
                dictionary_cmu[word2] == phoneme
            ):
                solutions.append(word)
    return solutions

def main():
    # print(reverse_lookup({'one': 'uno', 'two': 'dos', 'three': 'tres'}, 'uno'))
    # print(inverse_dict_default({'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}))
    # print(has_duplicated(dictionary_file))
    # print(rotate_pairs(dictionary_file))
    print(homophone_puzzle())
    pass

if __name__ == "__main__":
    main()