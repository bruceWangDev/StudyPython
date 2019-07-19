# -*- coding: utf-8 -* 

'''
判断输入年份是不是闰年
'''

year = int(input('年份 = '))
is_leapYear = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leapYear)