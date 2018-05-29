import os
import time
import shutil
from os.path import join,getsize

USB = 'D:\\'  # u盘目录
SAVE = 'C:\\Users\Leticia\Desktop\copy'  # 保存目录

def getdirsize(dir):
    size=0
    for root,dirs,files in os.walk(dir):
        size+=sum([getsize(join(root,name)) for name in files])
    print(size)
    return size

def usbcopy():
    shutil.copytree(USB, SAVE)


def main():
    old_dirsize = 0
    new_dirsize = 0
    while (1):
        if os.path.exists(USB):
            print("检测到U盘")
            new_dirsize = getdirsize(USB)
            if old_dirsize != new_dirsize:
                usbcopy()
                old_dirsize = new_dirsize
            else:
                print("没有变化")
        else:
            print("暂时没有U盘")
        print("开始休眠")
        time.sleep(5)  # 休眠时间

        print("休眠结束")

main()