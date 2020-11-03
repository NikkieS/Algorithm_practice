'''
Date : 11/03/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/12901
Description : find what day of the week of a given date is
'''
from datetime import date

'''
datetime module
date.weekday() returns the day of the week as an integer
Mon=0 ~ Sun=6
'''

def solution(a,b):
    weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    week = date(2016, a, b).weekday()

    return weekday[week]
