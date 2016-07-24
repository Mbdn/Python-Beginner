#  -*-  coding:utf-8  -*-

#定义函数
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d\n" % (a, b)
    return a / b

print "Let's do some math with just functions!i\n"

#计算并返回最后结果
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#输出最后计算结果
print "Age: %d, Height: %d, Weight: %d, IQ: %d\n" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

#函数嵌套调用
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
