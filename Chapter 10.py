from tqdm.auto import tqdm

#Exercise 1
def nested_sum(t):
    total_sum = 0
    for i in range(len(t)):
        if type(t[i]) == list:
            total_sum = total_sum + sum(t[i])
        else:
            total_sum = total_sum + t[i]
    return total_sum

#Exercise 2
def capitalized_nest(t):
    caplist = []
    for s in t:
        if type(s) == list:
            s = capitalized_nest(s)
        else:
            s = s.capitalize()
        caplist.append(s)
    return caplist


# Exercise 3
def cumulative_sum(t):
    new_list = []
    total_sum = 0
    for i in range(len(t)):
        if i > 0:
            t[i] = t[i] + t[i-1]
            total_sum = total_sum + t[i]
        new_list.append(t[i])
    print(new_list)

#exercise 4
def middle(t):
    del t[0]
    del t[-1]
    print(t)

#exercise 6
def is_sorted(t):
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True

#Exercise 7
def is_anagram(s1,s2):
    if (sorted(s1) == sorted(s2)): 
        return True
    else:
        return False

#Exercise 8
def has_duplicates_1(t):
    for i in range(len(t)):
        if t[i] in (t[0:i] + t[(i+1): ]):
            return True
    return False

#Exericise 9
def remove_duplicates(t):
    unique_element = []
    for i in range(len(t)-1):
        if t[i] not in (t[0:i] + t[(i+1): ]):
            unique_element.append(t[i])
    return unique_element

#Exericse 12
def reverse_check_test(t):
    reverse_pair = []
    for i in range(len(t) - 1):
        s = t[i]
        if s[::-1] in (t[0:i] + t[(i+1): ]):
            reverse_pair.append((s, s[::-1]))
    return reverse_pair

def reverse_pair_check():
    content_list = []
    with open("words.txt") as f:
        for line in f:
            content_list.append(line.strip('\n'))
    
    reverse_pair = []

    for word in tqdm(content_list):
        if word[::-1] in content_list:
            reverse_pair.append((word,word[::-1]))
    return reverse_pair

#exercise13
def interlock_check():
    content_list = []
    with open("words.txt") as f:
        for line in f:
            content_list.append(line.strip('\n'))
    
    interlock_pairs = []

    for word in tqdm(content_list):
        # word = word.strip('\n')
        even = word[0::2]
        odd = word[1::2]

        if even in content_list and odd in content_list:
            interlock_pairs.append((even, odd))

    return interlock_pairs

def main():
    # print(nested_sum([2,3,5,6]))
    # print(capitalized_nest([['bird', 'fly', 'bear', 'dog'], 'cat', 'snake']))
    # cumulative_sum([1,2,3])
    middle([1,2,3,4])
    pass

if __name__ == "__main__":
    main()