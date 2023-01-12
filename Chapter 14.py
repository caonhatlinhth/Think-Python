from dataclasses import replace
import os
import dbm
import pickle

def open_file():
    with open('text.txt', 'w') as f:
        line2 = "Linh iu anh Tai rat nhiu.\n"
        f.write(line2)
    print (f)

def add_values_to_string():
    with open('text.txt', 'w') as f:
        line2 = "Linh iu anh Tai rat nhiu.\n"
        f.write(line2)
        x = 52
        f.write(str(x))
    print(f)

def format_operator():
    color = input('what is your favorite color? ')
    # a = "My favorite color is: {}".format(color)
    # print (a)
    print(f"My favorite color is: {color}")

def walk(dirname):
    name_of_files = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            name_of_files.append(path)
        else:
            walk(path)
    return name_of_files

# def sed(pattern, replacement):
#     try:
#         open_file1 = open('file1.txt','r')
#         open_file2 = open('file2.txt','w')
#         for line in open_file1:
#             line = line.replace(pattern, replacement)
#             open_file2.write(line)
#             print (open_file2)
#         open_file1.close
#         open_file2.close
#     except:
#         print('something went wrong')
#     print()

def create_database():
    import dbm
    db = dbm.open('caption.db', 'c')
    db['clease.png'] = 'photo of John Clease'
    print (db)

def pickling():
    t = [1,2,3]
    s = pickle.dumps(t)
    print (s)



def main():
    pickling()
    pass

if __name__ == "__main__":
    main()