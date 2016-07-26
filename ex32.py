#   -*- coding: utf-8   -*-

#列表里面存放数据——列表要用[]扩住
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennues',2,'dimes',3,'quarters']

#for形式是 for i in x：i 是临时变量，x 是对象
#把列表里的元素打印出来
for number in the_count:
    print "This is vount %d" % number

#把列表里面的数据打印出来
for fruit in fruits:
    print "A fruit of type: %s" % fruits

#把列change里面的元素打印出来
for i in change:
    print "I got %r" % i

#申请空列表
elements = []

#range（0,6）——产生从零到6（不包含六）个数字0,1,2,3,4,5
for i in range(0,6):
    print "Adding %d to the list." % i          #输出0——5
    elements.append(i)      #把i里面的数据给列表elements并添加到最后

#输出elements列表里面的元素
for i in elements:
    print "Element was: %d" % i

#上面的两个可以写为
elements1 = []
elements1.append(range(0,6))
print elements1
