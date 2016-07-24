# -*-  coding:utf-8    -*-

#定义函数默认值为空
def ten(arg1 = ' ',arg2 = ' '):
    global frequency           #定义为全局变量
    frequency = frequency + 1
    print "函数第%s次被调用:" % frequency
    print "参数1：%s" % arg1
    print "参数2: %s" % arg2
    print "谢谢你的实验!@#$$$$$$$$$$\n"

#变量计算运行几次 默认为0
frequency = 0 

#第一次输入两个字符串
print "10呵呵，1+1"
ten ("10呵呵","1+1")

#第二次输入两个数字
print "1,3"
ten (1,3)

#第三次输入计算式
print "1+2,2-1"
ten (1+2,2-1)

#第四次输入乘除计算式
print "2 * 2, 6 / 2 "
ten (2 * 2, 6 / 2)

#第五次从键盘接受参数raw_input接收的是字符型数据
shuru1 = raw_input("输入你要显示的汉字或字符1")
shuru2 = raw_input("输入你要显示的汉字或字符2")
ten (shuru1, shuru2)

#第六次从键盘接计算式
shuru3 = input("计算器，一同可以算两个算式,''''''!!!!必须是计算是")
ten (shuru3)

#第七次上一次的加强版可以接受字符串使得计算式
shuru4 = int(input("计算器，数字加符号"))
ten (' ' ,shuru4)

#第八次空参数
ten()


arg3 = 4
arg4 = 5
#第九次定义自变量，自变量相加
ten(arg3 + arg4)

#第十次从键盘接收一个值  自定义变量一个值
shuru5 = raw_input("请输入字符串")
shuru6 = input ("请输入数字")
ten(shuru5 + "   hehe", shuru6 + 1)


print "十次执行完毕，再见！！"
