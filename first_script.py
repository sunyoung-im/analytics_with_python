# -*- coding: utf-8 -*-

from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os

print("Output #1: I'm excited to learn Python.")

#두 수를 더하래
x=4
y=5
z=x+y
print ("Output #2: Four plus five equals {0:d}.".format(z))

#두 리스트를 더하래
a=[1,2,3,4]
b=["first", "second", "third", "fourth"]
c=a+b
print("Output #3: {0}, {1}, {2}".format(a,b,c))

x=9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))
print("Output #7: {0:.3f}".format(int(8.3)/int(2.7)))
y=2.5*4.8
print("Output #8: {0:.1f}".format(y))
r=8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))

print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))

print("Output #14: {0:s}".format('I\'m enjoying learning Python'))
print("Output #15: {0:s}".format("This is a long string. Without the backslash\
 it would run off the page on the right in the text editor and be very\
 difficult to read and edit."))
print("Output #16: {0:s}".format('''You can use triple single quotes
for multi-line comment strings.'''))
print("Output #17: {0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))

string1="this is a "
string2="short string."
sentence= string1+string2
print("output #18: {0:s}".format(sentence))
print("output #19: {0:s} {1:s} {2:s}".format("she is", "very "*4, "beautiful."))
m=len(sentence)
print("output #20: {0:d}".format(m))

string1="my deliverable is due in May"
string1_list1=string1.split()
string1_list2=string1.split(" ", 2)
print("output #21:{0}".format(string1_list1))
print("output #22: first piece:{0} second piece:{1} second piece:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2="your,deliverable,is,due,in,June"
string2_list=string2.split(',')
print("output #23: {0}".format(string2_list))
print("output #24: {0} {1} {2}".format(string2_list[1], string2_list[5],\
string2_list[-1]))
print("ouput #25: {0}".format(','.join(string2_list)))

string3=" Remove    unwanted characters     from this string.\t\t   \n"
print("output #26: string3: {0:s}".format(string3))
string3_lstrip=string3.lstrip()
print("output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip=string3.rstrip()
print("output #27: rstrip: {0:s}".format(string3_rstrip))
string3_strip=string3.strip()
print("output #27: strip: {0:s}".format(string3_strip))

string4="$$Here's another string that has unwanted characters.__---++"
print("output #30: {0:s}".format(string4))
string4="$$The unwanted characters have been removed.__----++"
string4_strip=string4.strip('$_-+')
print("output #31: {0:s}".format(string4_strip))

string5="Let's replace the spaces in this sentence with other chracters."
string5_replace=string5.replace(" ", "!@!")
print("output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace=string5.replace(" ", ",")
print("output #33 (with commas): {0:s}".format(string5_replace))

string6="here's WHAT happens WHEN you USe lower."
print("output #34: {0:s}".format(string6.lower()))
string7="here's whaT happenS when you use UPPer"
print("output #35: {0:s}".format(string7.upper()))
string5="here's what happenS when you user CAPitalize."
print("output #36: {0:s}".format(string5.capitalize()))
string5_list=string5.split()
print("output #34: (on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))

string="The quick brown fox jumps over the lazy dog."
string_list=string.split()
pattern=re.compile(r"The", re.I)
count=0
for word in string_list:
    if pattern.search(word):
        count+=1
    print("output #38: {0:d}".format(count))


#문자열 내에서 발견된 패턴 출력하기
string="The quick brown fox jumps over the lazy dog."
string_list=string.split()
pattern=re.compile(r"(?P<match_word>The)", re.I)
print("output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))


#문자열 내 "a"를 "the"로 대체하기
string="The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("output #40: {:s}".format(pattern.sub("a", string)))


today=date.today()
#{0!s} !는 전달된 값이 숫자여도 sentence로 포맷팅하라는 것
print("output #41: today: {0!s}".format(today))
print("output #42: {0!s}".format(today.year))
print("output #43: {0!s}".format(today.month))
print("output #44: {0!s}".format(today.day))
current_datetime=datetime.today()
print("output #45: {0!s}".format(current_datetime))

one_day=timedelta(days=-1)
yesterday=today+one_day
print("output #46: yesterday: {0!s}".format(yesterday))
eight_hours=timedelta(hours=-8)
print("output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

date_diff = today - yesterday
print("output #48: {0!s}".format(date_diff))
print("output #49: {0!s}".format(str(date_diff).split()[0]))
print(date_diff)

print("output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("output #50: {:s}".format(today.strftime('%m/%d/%y')))
# %y와 %Y의 차이는 17, 2017
print("output #51: {:s}".format(today.strftime('%b %d, %Y')))
# %b abbreviated name of month, %B full name of month
print("output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("output #53: {:s}".format(today.strftime('%B %d, %Y')))

date1=today.strftime('%m/%d/%Y')
date2=today.strftime('%b %d, %Y')
date3=today.strftime('%Y-%m-%d')
date4=today.strftime('%B %d, %Y')
print("output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))
# strptime 함수에 전달하는 argument는 형식을 맞춰줘야 하고, 결과 값은 무조건 datetime 기본형
print("output #56: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("output #57: {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))

a_list=[1,2,3]
print("output #58: {}".format(a_list))
print("output #59: a_list has {} elements.".format(len(a_list)))
print("output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("output #61: the minimum value in a_list is {}.".format(min(a_list)))

another_list=['printer', 5, ['star', 'circle', 9]]
print("output #62: {}".format(another_list))
print("output #63: another_list also has {} elements".format(len(another_list)))
print("output #64: 5 is in another_list {} time".format(another_list.count(5)))

print("output #65: {}".format(a_list[0]))
print("output #66: {}".format(a_list[1]))
print("output #67: {}".format(a_list[2]))
print("output #68: {}".format(a_list[-1]))
print("output #69: {}".format(a_list[-2]))
print("output #70: {}".format(a_list[-3]))
print("output #71: {}".format(another_list[2]))
print("output #72: {}".format(another_list[-1]))

print("output #73: {}".format(a_list[0:2]))
print("output #74: {}".format(another_list[:2]))
print("output #75: {}".format(a_list[1:3]))
print("output #76: {}".format(another_list[1:]))
#[x:y] x는 포함, y는 불포함

a_new_list = a_list[:]
print("output #77: {}".format(a_new_list))

a_longer_list = a_list + another_list
print("output #78: {}".format(a_longer_list))

a=2 in a_list
print("output #80: 2 is in {}.".format(a_list))
if 2 in a_list:
    print("output #80: 2 is in {}.".format(a_list))
b=6 not in a_list
print("output #81: {}".format(b))
if 6 not in a_list:
    print("output #82: 6 is not in {}.".format(a_list))

a_list.append(4)
a_list.append(5)
a_list.append(6)
print("output #83: {}".format(a_list))
a_list.remove(5)
print("output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("output #85: {}".format(a_list))

a_list.reverse()
print("output #86: {}".format(a_list))
a_list.reverse()
print("output #87: {}".format(a_list))

unordered_list = [3,5,1,7,2,8,4,9,0,6]
print("output #88: {}".format(unordered_list))
list_copy=unordered_list[:]
list_copy.sort()
print("output #89: {}".format(list_copy))
print("output #90: {}".format(unordered_list))

my_lists=[[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3=sorted(my_lists, key=lambda index_value: index_value[3])
print("output #91: {}".format(my_lists_sorted_by_index_3))

my_lists=[[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678],\
[578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0=sorted(my_lists, key = itemgetter(3,0))
print("output #92: {}".format(my_lists_sorted_by_index_3_and_0))

my_tuple=('x', 'y','z')
print("output #93: {}".format(my_tuple))
print("output #94: my_tuple has {} elements.".format(len(my_tuple)))
print("output #95: {}".format(my_tuple[1]))
longer_tuple=my_tuple+my_tuple
print("output #96: {}".format(longer_tuple))
#리스트와 튜플의 차이. 어레이는 원소를 바꿀 수 있고 튜플은 그렇지 않아

one, two, three = my_tuple
print("output #97: {0} {1} {2}".format(one, two, three))
var1='red'
var2='robin'
print("output #98: {} {}".format(var1, var2))
var1, var2 = var2, var1
print("output #99: {} {}".format(var1, var2))

my_list=[1,2,3]
my_tuple=('x', 'y', 'z')
print("output #100: {}".format(tuple(my_list)))
print("output #101: {}".format(list(my_tuple)))

empty_dict={}
a_dict={'one':1, 'two':2, 'three':3}
print("output #102: {}".format(a_dict))
print("output #103: a_dict has {!s} elements.".format(len(a_dict)))
another_dict={'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("output #104: {}".format(another_dict))
print("output #105: another_dict also has {!s} elements".format(len(another_dict)))
#list=[], tuple=(), dictionary={}

print("output #106: {}".format(a_dict['two']))
print("output #107: {}".format(another_dict['z']))

a_new_dict = a_dict.copy()
print("output #108: {}".format(a_new_dict))

print("output #109: {}".format(a_dict.keys()))
print("output #110: {}".format(a_dict.values()))
print("output #111: {}".format(a_dict.items()))

if 'y' in another_dict:
    print("output #114: y is a key in another_dict: {}."\
    .format(another_dict.keys()))
if 'c' not in another_list:
    print("output #115: c is not a key in another_dict: {}."\
    .format(another_dict.keys()))
print("output #116: {!s}".format(a_dict.get('three')))
print("output #117: {!s}".format(a_dict.get('four')))
print("output #118: {!s}".format(a_dict.get('four', 'Not in dict')))

print("output #119: {}".format(a_dict))
dict_copy=a_dict.copy()
ordered_dict1=sorted(dict_copy.items(), key=lambda item: item[0])
print("output #120 (order by keys): {}".format(ordered_dict1))
ordered_dict2=sorted(dict_copy.items(), key=lambda item: item[1])
print("output #121 (order by values): {}".format(ordered_dict2))
ordered_dict3=sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print("output #122 (order by values, descending): {}".format(ordered_dict3))
ordered_dict4=sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print("output #122 (order by values, ascending): {}".format(ordered_dict4))

x=5
if x>4 or x!=9:
    print("output #124: {}".format(x))
else:
    print("output #124: x is not greater than 4")

if x>6:
    print("output #125: x is greater than six")
elif x>4 and x==5:
    print("output #125: {}".format(x*x))
else:
    print("output #255: x is not greater than 4")


y=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
z=['ann', 'betty', 'claire', 'daphne', 'ellie', 'franchesca', 'greta', 'holly', 'isabel','jenny']

print("output #126:")
for month in y:
    print("{!s}".format(month))
print("output #127: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}: {1:s}".format(i, z[i]))
print("output #128: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('j'):
        print("{!s}".format(y[j]))
print("output #129:")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))

my_data=[[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep=[row for row in my_data if row[2]>5]
print("output #130: (list comprehension): {}".format(rows_to_keep))

my_data=[(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1={x for x in my_data}
print("output #131 (set comprehension): {}".format(set_of_tuples1))
set_of_tuples2=set(my_data)
print("output #132 (set function): {}".format(set_of_tuples2))


my_dictionary={'customer1':7, 'customer2':9, 'customer3':11}
my_results={key: value for key, value in my_dictionary.items() if value >10}
print("output #133 (dictionary comprehension): {}".format(my_results))

print("output #134:")
x=0
while x <11:
    print("{!s}".format(x))
    x+=1

def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues)>0\
    else float('nan')
my_list=[2,2,4,4,6,6,8,8]
print("output #135 (mean): {!s}".format(getMean(my_list)))


import numpy as np
print("output #136 (mean): {!s}".format(np.mean(my_list)))

def getMean(numericValues):
    return sum(numericValues)/len(numericValues)
my_list2=[]
try:
    print("output #137 (error): {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("output #137 (error): {}".format(float('nan')))
    print("output #137 (error): {}".format(detail))

try:
    result=getMean(my_list2)
except ZeroDivisionError as detail:
    print("output #138 (error): {}".format(float('nan')))
    print("output #138 (error): {}".format(detail))
else:
    print("output #138 (The mean is): {}".format(result))
finally:
    print("output #138 (Finally): The finally block is executed every time")



# print("output #139: ")
# input_file = sys.argv[1]
# filereader = open(input_file, 'r')
# for row in filereader:
#     print(row.strip())
# filereader.close()
#
# input_file=sys.argv[1]
# print("output #140: ")
# with open(input_file, 'r', newline='') as filereader:
#     for row in filereader:
#         print("{}".format(row.strip()))


# print("output #141: ")
# inputPath=sys.argv[1]
# for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
#     with open(input_file, 'r', newline='') as filereader:
#         for row in filereader:
#             print("{}".format(row.strip()))

# my_letters=['a', 'b', 'c', 'd', 'e', 'f']
# max_index=len(my_letters)
# output_file=sys.argv[1]
# filewriter=open(output_file, 'w')
# for index_value in range(len(my_letters)):
#     if index_value < (max_index -1):
#         filewriter.write(my_letters[index_value]+'\t')
#     else:
#         filewriter.write(my_letters[index_value]+'\n')
# filewriter.close()
# print("output #142: output written to file")


my_numbers=[0,1,2,3,4,5,6,7,8,9]
max_index=len(my_numbers)
output_file=sys.argv[1]
filewriter=open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value<(max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("output #143: output appended to file")
