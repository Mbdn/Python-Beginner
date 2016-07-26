#coding:utf-8

#定义三个变量里面存放数值
people = 20
cats = 30
dogs = 15

#判断20 是否大于 30 ，正确就执行紧跟在他后面缩进的语句，为假不执行之间诶跳过
if people < cats:
    print "Too many cats! The world is dommed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


#dogs = dogs + 5
dogs += 5

#判断20 是否大于等于20 
if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are dogs."

#判断是否相等
if people == dogs:
    print "People are dogs."
