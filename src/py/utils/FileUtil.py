#-*-coding:utf-8-*-

import os

'''
author:yirenyijiu
本类用于收集操作文件相关的工具方法。
'''



'''
方法1：renameByAddStr2FixedPos
说明：将指定目录下指定类型的所有文件重命名（并且在文件名的指定位置添加指定的字符，以重命名）
'''
def renameByAddStr2FixedPos(path,suffix,index,words):    
    #os.listdir()方法，列出指定目录下所有文件的文件名，不包含子目录
    files=os.listdir(path)
    for f in files:
        if f.endswith(suffix):
            print("原文件名：{}".format(f))
            old_file=os.path.join(path,f)
            new_file=os.path.join(path,f[0:index-1]+words+f[index-1:])
            print("文件重命名为：{}".format(new_file))
            os.rename(old_file,new_file)
        


#测试：在文件夹的第三个字符前，插入一个点号，即原文件名：01foo.mp4, 新文件名：01.foo.mp4
path="F:\\mypath\\video"
renameByAddStr2FixedPos(path,"mp4",3,".")




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