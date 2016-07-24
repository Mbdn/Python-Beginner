# -*-   coding:utf-8    -*-
from sys import argv
from os.path import exists

#申请三个变量
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file)        #打开文件给in_file
indata = in_file.read()         #把in_file的内容给indata变量

print "Does the output file exist? %r" % len(indata)

print "Does the output file exist? %r " % exists(to_file)
print "Ready, hit RETURN to contunue, CTRL-C to abort."
#一个缓冲
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)      #把文件1给文件2

print "Alright ,all done."

#关闭文件
out_file.close()
in_file.close()
