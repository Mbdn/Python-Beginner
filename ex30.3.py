#  -*-  coding: utf-8   -*-

people = 20
cars = 14
buese = 40

#people是否大于cars and buese 是否小于cars，True and False 等于False
if people > cars and buese < cars:
    print "yes"
#False and False 等于False
elif people < cars and buese < cars:
    print "no"
#Flase and True 等于 False
elif people < cars and buese > cars:
    print "3"
# True and True 等于 True
elif people > cars and buese > cars:
    print "4"
else:
    print "False"


if people < cars or buese < cars:
    print "5"
elif people < cars or buese < cars:
    print "6"
#True or Not（False), True or True 等于True
elif people > cars or Not(buese < cars):
    print "8"
else :
    print "9"
