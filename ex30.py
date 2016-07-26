#  -*-  coding:utf-8    -*-

#申请三个变量
people = 30
cars = 40
buses = 15


#首先判断cars是否大于people，如果大于执行他下面缩进的语句，如果为假在判断cars 是否大于people，为真输出下面缩进的行。如果两次判断都没有就执行else下面的语句
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."


if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
