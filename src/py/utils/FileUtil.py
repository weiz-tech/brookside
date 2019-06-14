#-*-coding:utf-8-*-
import os
'''
本类用于收集操作文件相关的工具方法。
'''

'''
方法1：说明：将指定目录下的所有文件重命名（文件名的第三个字符位置处加个点号）
'''
#查找路径：
path="F:\\mypath\\py_file"
#os.listdir()方法，列出指定目录下所有文件的文件名，不包含子目录
files=os.listdir(path)
for f in files:
    print(f)
    if  f.endswith(".mp4"):
        print("原来的文件名字是:{}".format(f))
        #找到原文件所在的位置
        old_file=os.path.join(path,f)
        print("old_file is {}".format(old_file))
        #指定新文件的位置，如果没有使用这个方法，则新文件名生成在本项目的目录中
        new_file=os.path.join(path,f[0:2]+"."+f[2:])
        print("File will be renamed as:{}".format(new_file))
        os.rename(old_file,new_file)
        print("修改后的文件名是:{}".format(f))




#其他常用方法一览：
#path="F:\\教程\\Java并发编程原理与实战"
# 切换到 对应 目录
#os.chdir(path )
#列出目录
#print("目录为：%s"%os.listdir(os.getcwd()))
#移除
#os.remove("project30.jpg")
#移除后的目录
#print("移除后：%s"%os.listdir(os.getcwd()))