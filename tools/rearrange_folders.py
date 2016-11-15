import collections
import os
import shutil

l = os.listdir()
d = collections.defaultdict(list)

for file_name in l:
    width = file_name.find('_')-1
    if width<3:
        new_file_name = file_name[0]+'0'*(3-width)+file_name[1:]
        os.rename(file_name,new_file_name)
        file_name = new_file_name

    dir_name = file_name[:file_name.find('.')]
    if dir_name[-2]=='_' and dir_name[-1] in '0123456789':
        dir_name = dir_name[:-2]
    d[dir_name].append(file_name)

for dir_name in d:
    os.mkdir(dir_name)
    for file_name in d[dir_name]:
        shutil.move(file_name,dir_name)
