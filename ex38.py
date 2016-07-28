# -*-  coding:utf-8 -*-

#创建字典
states = {
        'Oregon':   'OR',
        'Florida':  'NY',
        'Califoria':    'CA',
        'New youk':     'NY',
        'Michigan':     'MI'
        }

cities = {
        'CA':   'San Francisco',
        'MI':   'Detriit',
        'FL':   'Jacksonville'
        }

#在添加一些城市
cities['NY'] = 'New Yourk'
cities['OR'] = 'Portland'

#打印出一些城市
print '-' * 10
#根据键值打印城市
print "NY State has:", cities['NY']
print "OR State has:", cities["OR"]

#打印出来一些州
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#城市和国家
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#打印一些缩写
print '-' * 10
#items返回states所有的元素和键值
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

#打印每个城市的状态
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#在统一时间的城市
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
#Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值
state = states.get('Texas', None) 
if not state:
    print "Sorry, no Texas."

#获得一个默认的城市
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
