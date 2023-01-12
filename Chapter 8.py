
#Exercise 1
def display_letters_backward(s):
    i = len(s) - 1
    while i < len(s):
        letter = s[i]
        print(letter)
        i = i - 1
        if i < 0:break 

#Exercise 2
def name_of_duckling():
    prefixes = 'JKLMNOPQ'
    subfix = 'ack'
    for letter_index in range(len(prefixes)):
        if letter_index < 5 or letter_index == 6:
            print(prefixes[letter_index] + subfix)
        else: print(prefixes[letter_index] + 'u' + subfix)

#Exercise 3
def fruit_test():
    fruit = "banana"
    print (fruit[:])

#Exercise 4
def find(word, letter, index):
    while index >= 0:
        if word[index] == letter:
            return index
        index = index - 1
    return "can't find the letter"

#Exercise 5
def count(letter, word):
    count = 0
    for l in word:
        if l == letter:
            count += 1
    print(count)

#Exercise 6
def count(letter, word, index):
    count = 0
    while index >= 0:
        if word[index] == letter:
            count += 1
    print(count)

#exercise 7
def count_a(word):
    num_a = word.count('a')
    print (num_a)

#exersize 10
def is_palindrome(s):
    s_reverse = s[::-1]
    if s == s_reverse:
        return True
    else:
        return False 

#exercise 12
def rotate_word(word, rotate_number):
    index = 0
    rotated_string = ""
    while index < len(word):
        character = ord(word[index])
        rotated_character = chr(character + rotate_number)
        rotated_string = rotated_string + rotated_character
        index = index + 1
    return rotated_string

def main():
    # display_letters_backward("banana")
    # name_of_duckling()
    # count_a("banana")
    # print(is_palindrome("banana"))
    # print(rotate_word("banana", 5))
    pass

if __name__ == "__main__":
    main()