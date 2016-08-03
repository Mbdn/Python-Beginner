# -*- coding: utf-8   -*-

class Parent(object):

    def altered(self):
        print "PARENT altered"

class Child(Parent):
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHLID, AFTER PAERNT altered()"


dad = Parent()
son = Child()

dad.altered()
son.altered()
