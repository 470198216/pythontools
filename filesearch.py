import os
import fnmatch

path = ""
filename = ""
result = []

def find_file():
    i = 0
    for root, list, file in os.walk(path):
        for file in file:
            if fnmatch.fnmatch(file, filename):
            #if filename in file:
                i = i + 1
                write = os.path.join(root, file)
                print('%d %s' % (i, write))
                result.append(write)

def find_file_and_putin_txt():
    i = 0
    open('D:\\find_file.txt', mode='w').close()
    for root, lists, files in os.walk(path):
        for file in files:
            if filename in file:
                i = i + 1
                write = os.path.join(root, file)

                file_txt = open('E:\find_file.txt', mode='a+')
                file_txt.write('%d %s' % (i, write))
                result.append(write)

if __name__ == '__main__':
    filename = input("filename:")
    path = input("search path:(C: or D:)")
    find_file()
    #find_file_and_putin_txt()