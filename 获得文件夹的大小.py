import os
s=0#定义一个全局变量
def get_size(dir1):
    '''获取文件夹的大小'''
    global s
    dlist = os.listdir(dir1)
    for f in dlist:
        file = os.path.join(dir1,f)
        s += os.path.getsize(file)
        if os.path.isdir(file):
            get_size(file)
    return s
#print(get_size("./a"))
# #./a为输入的文件夹的路径
