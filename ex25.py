#coding:utf-8

#第一个函数
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')        #截取字符串一空格为基准，截取为列表
    return words                    #返回words
#第二个函数
def sort_words(words):
    """Sorts the words."""          #注释，帮助文档引用
    return sorted(words)            #按从小到大的顺序排序，然后返回

def print_firsr_work(words):
    """Prints the first word after popping if off."""
    word = words.pop(0)             #把列表的元组移出给对象，默认为最后一个
    print word                      

def print_last_word(words):
    """Prints the last word after popping  it off."""
    word = words.pop(-1)            #pop是提取某个元素给对象，默认为最后一个
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the eorted words."""
    words = break_woeds(sentence)
    return sort_woeds(words)

def print_first_and_last(sentence):
    """Prinds the first and last words of the sentence."""
    words = break_woeds(sentence)
    print_firsr_work(woeds)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sortd the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
