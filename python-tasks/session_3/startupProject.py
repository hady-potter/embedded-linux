#!/usr/bin/python3

import os
import sys
import shutil

if len(sys.argv) != 2:
  print('Usage: ', 'python3 <startupProject.py> <project_name>')
  print('Usage: ', '<./startupProject.py> <project_name>')
  sys.exit()

project_name = sys.argv[1]

# check if project with the same name already exists
if os.path.exists(project_name):
  c = input(f'"{project_name}" already exist Do you want to delete it [y - n] ').lower()
  if(c.startswith('y')):
    shutil.rmtree(project_name)
    print(f'"{project_name}" Deleted')
  else: sys.exit()

# create project
os.mkdir(project_name)
os.mkdir(f'{project_name}/src')
os.mkdir(f'{project_name}/build')
os.mkdir(f'{project_name}/tests')
os.mknod(f'{project_name}/src/main.cpp')


# update main.cpp file
f = open(f'{project_name}/src/main.cpp', 'w')

content = '''#include <iostream>
using namespace std;

int main() {
  cout << "Hello, World!" << endl;

  //your code here


  return 0;
}
'''.encode()

# HINT: content must be encoded to bytes so we used encode()
# HINT: write is a system call so we do NOT pass file itself but we pass a file-discriptor -> f.fileno()
os.write(f.fileno(), content)
f.close()

# create cmake file
os.chdir(project_name)
os.mknod('CMakeLists.txt')

content = f'''cmake_minimum_required(VERSION 3.22)
project({project_name})
add_executable(main src/main.cpp)
'''.encode()

f = open('CMakeLists.txt', 'w')
os.write(f.fileno(), content)
f.close()


# build project using cmake and open vscode
os.chdir('./build')
os.system('cmake .. && make && ./main && cd .. && code .')






