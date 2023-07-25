import os
import shutil

desktop = os.path.join(os.path.expanduser('C:\\Users\\wenjin'), 'Desktop')

print(desktop)

name = input('name of dir:')

clean = os.path.join(desktop, name)

isExit = os.path.exists(clean)
print(clean)
if isExit == False:
    os.mkdir(clean)

name_list = os.listdir(desktop)
print(name_list)

for file in name_list:
    file_path = os.path.join(desktop, file)
    if not os.path.isfile(file_path):
        continue
    elif os.path.isfile(file_path):
        fileExpand = os.path.splitext(file)[1]

        #fileExpand = fileExpand[1]
        expand_file_dir = os.path.join(clean, fileExpand)
        if not os.path.exists(expand_file_dir):
            os.mkdir(expand_file_dir)
        shutil.move(file_path, expand_file_dir)
