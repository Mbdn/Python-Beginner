#   -*- coding: utf-8   -*-

#类的声明
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    #继承上面的
    def sing_me_a_song(self):
        for line in self.lyrics:#里面的元素给line
            print line

#创建列表里面包含字符串
happy_bday = Song(["Happy birthday to you",
        "I don't want to get sued",
        "so I'll stop right there"])

bulls_on_parade = Song(["they rally around the family",
    "with pockets full of shells"])

#调用对象函数等于包
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


