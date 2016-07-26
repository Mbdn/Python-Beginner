#   -*-  coding: utf-8   -*-

#提示你选择1huo2            这个if模式为    外侧if 里面有if，elif，else   内侧elif里面有 if，else   其他else，输出
print "You enter a dark room with two doors. Do you go through door # 1 or door #2?"

#输入1或2或其他
door = raw_input("> ")

#输入1进
if door == "1":
    print "There's a giant bear eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    #第一个if里面，第一次输入1或2
    bear = raw_input("> ")
    
    #判断1 或 2
    if bear =="1":
        print "The bear eats your fae off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job."
    else:
        print "Well, doing %s is probably better. Bear runs away." %bear

#输入2进
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retna."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    #elif里面的输入
    insanity = raw_input(" >")
    
    #判断1还是其他
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

#其他
else:
    print "You stumble around and fall on a lnife and die . Good job!"

