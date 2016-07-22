# coding:utf-8
x = "there are %d types of people." % 10        字符串赋值
binary = "binary"
do_not = "don't"
y = "Those who know %s and thonse who %s." % (binary, do_not)

print x             #输出
print y

print "I said : %r." % x
print "I also said: '%s'."  % y

hilarious = False       #赋值为布尔
joke_evalustion = "Isn't that joke so funny?! %r"

print joke_evalustion % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
