import os
import shutil
import time

def addContentToCpp(class_name):
  content = f'''
/*************************************

  auther: {auther_name}
  date: {time.ctime()}
  brief: 

*************************************/

#include "{class_name}.hpp"

namespace svm ''' + "{\n  " + f"{class_name}::{class_name}()" + "{}\n  " + f"{class_name}::~{class_name}()" + "{}\n}\n\n"
  f = open(class_name + '.cpp', 'w')
  os.write(f.fileno(), content.encode())
  f.close()

# =================================================
def addContentToHpp(class_name):
  content = f'''#pragma once
/*************************************

  auther: {auther_name}
  date: {time.ctime()}
  brief: 

*************************************/

namespace svm ''' + "{\nclass " + f"{class_name} " + "{\n\npublic:\n  " + f"{class_name}();\n  ~{class_name}();\nprivate:\n\n" + "};\n}\n"

  f = open(class_name + '.hpp', 'w')
  os.write(f.fileno(), content.encode())
  f.close()


print(os.getcwd())

auther_name = input('Auther Name: ')
class_name = input("Class Name: ")

if os.path.exists(class_name):
  shutil.rmtree(class_name)

os.mkdir(class_name)

os.chdir(class_name)
os.mknod(class_name + '.cpp')
os.mknod(class_name + '.hpp')

addContentToCpp(class_name)
addContentToHpp(class_name)








