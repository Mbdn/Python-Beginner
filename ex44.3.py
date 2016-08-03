# -*-  coding: utf-8  -*-

class Other(object):

    def voverride(self):
        print "OTHER override()"

    def implicit(self):
        print "OtHER implicit()"

    def altered(self):
        print "OTHER atered()"

class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()
son.implicit()
son.override()
son.altered()
