#   -*-   coding: utf-8

from sys import exit

def gold_room():        
    print "This room id full of gold. How much do you take?"
    next = raw_input("> ")
    if "0" in next or "1" in next:      #1或0 还是其他
        how_much = int(next)            #转化为数值型
    else:                                #其他退出
        dead("Man, learn to type a nuber.")

    if how_much < 50:       #小于50 退出
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:                               #退出
        dead("you greedy bastard!")

#left走这里
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in from of anpther door."
    print "How are you going to move the bear?"
    #付初值False
    bear_moved = False

    while True:         #永真循环
        next = raw_input("> ")
        
        #根据输入走相应分支
        if next == "take honey":    #如果输出并应用dead
            dead("the bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:       #True and not（False） = Ture 第一次打印把bear_moved 改为Ture
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:        #调用gold_room
            gold_room()
        else:
            print "I got no idea what means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life of eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()                     #回到最初点
    elif "head" in next:
        dead("Well that was tasty!")    #退出
    else: 
        cthulhu_room()                  #从新输入

#输出why，退出程序
def dead(why):
    print why, "Good job!"
    exit (0)        #退出程序

#第一次调用
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")
    #根据输入走不同的分支
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble arond the room until you starve.")

start()

