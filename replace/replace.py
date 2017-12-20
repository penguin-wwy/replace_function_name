#!/usr/bin/python
import hashlib
import os

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)

replace_str = "2\n"
func_names = []
with open(os.path.join(dir_path, '2.code'), 'r') as fp:
    line = fp.readline()
    func_names.append(line.strip())
for func_name in func_names:
    data = hashlib.md5(func_name).hexdigest()
    md5_str = '_' + data
    replace_str = replace_str + func_name + ":" + md5_str + "\n"
with open(os.path.join(dir_path, '1.code'), 'w') as fp:
    fp.write(replace_str)

os.system("rm -f " + os.path.join(dir_path, "2.code"))