#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 02:34:41 2020

@author: liuxiangyudediannao
"""




"""

take a string in the form "(*, *, *), ..."
return with three elements tuple

"""

from dataPreprocess import map_index_place, map_place_index





# X_0 = "(8,56,6) (22,51,3) (25,32,3) (30,38,3) (33,72,0) (9,19,6) (23,48,3) (28,42,3) (31,13,3) (34,0,0) (15,1,3) (24,64,3) (29,8,3) (32,26,3) (34,5,0)"
# W_0 = "(1,22,6) (11,18,3) (14,10,3) (19,47,3) (26,52,3) (33,72,0) (7,60,6) (12,1,3) (16,5,3) (20,43,3) (27,56,3) (10,68,3) (13,14,3) (18,38,3) (21,29,3) (33,0,0)"

X_100 = "(1,22,6) (11,29,3) (17,7,3) (20,43,3) (34,72,0) (7,60,6) (13,18,3) (18,38,3) (26,52,3) (37,0,0) (10,14,3) (14,1,3) (19,47,3) (27,56,3) (37,68,0)"
W_100 = "(8,56,6) (15,1,4) (24,47,3) (29,42,3) (32,26,3) (9,18,7) (22,64,3) (25,12,3) (30,30,3) (34,0,0) (12,7,3) (23,67,3) (28,52,3) (31,36,4) (34,72,0)"

X_20 = "(8,59,7) (15,1,5) (28,42,3) (31,48,3) (34,0,0) (34,68,0) (9,23,7) (24,54,3) (30,31,10) (33,72,0) (34,7,14)"
W_20 = "(1,22,8) (12,1,3) (17,42,3) (26,52,3) (33,0,0) (33,72,0) (7,60,6) (14,31,8) (19,47,3) (27,56,3) (33,5,16) (37,68,3)"


X_5 = "(1,18,7) (12,1,7) (27,50,4) (33,9,8) (34,72,0) (6,56,9) (17,42,6) (33,0,0) (33,67,1) (37,26,12)"
W_5 = "(2,20,10) (15,1,9) (28,67,3) (34,11,7) (34,72,0) (8,54,6) (24,62,3) (34,0,0) (34,32,20)"


X_40 = "(0,60,6) (13,67,4) (28,47,3) (31,37,3) (34,12,4) (9,18,6) (15,8,3) (29,42,3) (32,25,4) (37,0,0) (12,3,3) (24,52,3) (30,30,4) (33,1,1) (37,72,0)"
W_40 = "(3,18,9) (14,1,4) (19,46,3) (27,55,3) (37,72,0) (7,59,6) (17,8,3) (20,42,3) (35,14,2) (11,67,4) (18,29,11) (26,51,3) (37,0,0)"



X_task2 = "(0,65)    (12,61)   (17,6)    (27,11)   (30,33)   (33,0)    (33,72)    (9,26)    (15,56)   (24,45)   (28,50)   (31,39)   (33,18)"

def index_to_time(i):
    time = [9, 0]
    while i != 0:
        i -= 1
        time[1] += 10
        if time[1] == 60:
            time[0] += 1
            time[1] = 0
    return time


def foo(string_num):
    return tuple(int(i) for i in string_num)

def parse(string):
    step1 = string.split()
    step2 = []
    for i in step1:
        i = i.strip("(").strip(")").split(",")
        step2.append(i)
    return [foo(i) for i in step2]

    

def recoverPath(list_tuple):
    result = sorted(list_tuple, key = lambda x: x[1])
    result = [(lambda x: (map_index_place[x[0]], index_to_time(x[1]), x[2]*10))(i) for i in result]
    return result

def recoverPath2(list_tuple):
    result = sorted(list_tuple, key = lambda x: x[1])
    result = [(lambda x: (map_index_place[x[0]], index_to_time(x[1])))(i) for i in result]
    return result


def total(string):
    return recoverPath(parse(string))


def total2(string):
    return recoverPath2(parse(string))

dict_result= {}
dict_result[100] = total(X_100), total(W_100)
dict_result[20]  = total(X_20), total(W_20)
dict_result[5]   = total(X_5), total(W_5)
dict_result[40]  = total(X_40), total(W_40)
dict_result["task2"] = total2(X_task2), total2(X_task2)
#print(total(X_0), total(W_0))


f = open("task3_result.txt", 'w')
f.write(str(dict_result))
f.close()



    