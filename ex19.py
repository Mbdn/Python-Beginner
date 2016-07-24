#coding:utf-8

#定义一个函数有两个参数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crachers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#调用函数传20,30
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#再定义两个变量
print "OR, we can use variabkes from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#调用函数传上面的变量
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#传运算式
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5+ 6)

#传不同的计算式，
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 100)

