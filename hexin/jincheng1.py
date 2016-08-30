#coding:utf-8

from time import sleep, ctime

#延迟4秒的进程
def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)                            #新建一个进程
    print 'loop 0 done at:', ctime()

#延迟两秒的进程
def loop1():
    print 'start 1 done at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()

#主函数
def main():
    print 'starting at:', ctime()
    loop0()
    loop1()
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
