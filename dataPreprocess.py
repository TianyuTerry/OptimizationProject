#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:00:55 2020

@author: liuxiangyudediannao
"""




R = 6371 * 10 ** 3
# meter

speed = 10 #km/h
data_file = "Task3.csv"
output_name = "project3.dat"


T_max = 12 * 6

import pandas as pd
from math import radians, cos, sin, asin, sqrt, ceil



def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = [radians(i) for i in [lon1, lat1, lon2, lat2]]
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    return c * R




"""
    read in the data
"""

location = pd.read_csv(data_file)
L = len(location["Latitude"])


# create a f : index -> place name
map_index_place = {}
# create a f^-1
map_place_index = {}


list_position = []

# create a matrix, such that distance_matrix[i][j] := distance between
# f[i] and f[j]
distance_matrix = [[0 for i in range(L)] for j in range(L)]
#similar to distance_matrix
time_matrix = [[0 for i in range(L)] for j in range(L)]

# a map takes the index of attraction's index and return the cost in SGD
attraction_cost = {}
processing = {}



# create some sets which contains the indices of the places
outdoor = set({})
indoor = set({})



C = set({})
N = set({})
E = set({})
W = set({})
O = set({})
#S = set({})
#U = set({})


A = set({})
D = set({})
Hotel = set({})




for i in range(L):
   map_index_place[i] = location["Attraction name"][i]
   map_place_index[location["Attraction name"][i]] = i
   list_position.append((location["Longtitude"][i], location["Latitude"][i]))
   
   if location["Indoor/Outdoor"][i] == "Indoor":
       indoor.add(i)
   if location["Indoor/Outdoor"][i] == "Outdoor":
       outdoor.add(i)
       
   if location["Region"][i] == "C":
       C.add(i)
   if location["Region"][i] == "N":
       N.add(i)
   if location["Region"][i] == "E":
       E.add(i)       
   if location["Region"][i] == "W":
       W.add(i)       
     
   if location["Region"][i] == "O":
       O.add(i)
#   if location["Region"][i] == "U":
#       U.add(i)  
       
   if "A" in location["Attraction"][i]:
       A.add(i)
       attraction_cost[i] = int(location["Cost (SGD)"][i])
       processing[i] = 3
   if "D" in location["Attraction"][i]:
       D.add(i)
       processing[i] = 6
   if "H" in location["Attraction"][i]:
       Hotel.add(i)




for i in range(L):
    for j in range(L):
        distance_matrix[i][j] = haversine(list_position[i][0], list_position[i][1],  list_position[j][0], list_position[j][1])
        time_matrix[i][j] = ceil(distance_matrix[i][j] / (speed * 1000) * 4)




def set_2_str(s, s_name):
    string = "set " + s_name + " :="
    for i in s:
        string += " " + str(i)
    return string + ";\n"



def onedim_para_2_str(p, p_name):
    string = "param " + p_name + " := \n"
    for k in p.keys():
        string += "\t" + str(k) + "\t" + str(p[k]) + "\n"
    return string + ";\n"
        
    



def twodim_para_2_str(p, p_name):
    string = "param " + p_name + " := \n"
    for i in range(len(p)):
        for j in range(len(p[i])):
            string += "\t" + str(i) + "\t" + str(j) +"\t" + str(p[i][j]) + "\n"
    return string + ";\n"


def helper(p, p_name):
    string = "param " + p_name + " := \n"
    for i in range(len(p)):
        for j in range(len(p[i])):
            string += "\t" + str(map_index_place[i]) + "\t\t\t\t" + str(map_index_place[j]) +"\t\t\t\t" + str(p[i][j]) + "\n"
    return string + ";\n"



def main():
    string = ""
    string += "param" + " maxT" + " " + ":=" + " " + str(T_max) + ";\n"
    string += set_2_str(A, "A")
    string += set_2_str(D, "D")
    string += set_2_str(C, "C")
    string += set_2_str(E, "E")
    string += set_2_str(W, "W")
    string += set_2_str(N, "N")
    string += set_2_str(O, "O")
    
    string += set_2_str(outdoor, "Out")
    string += set_2_str(indoor, "In")
    string += set_2_str(Hotel, "Hotel")
    
    string += onedim_para_2_str(attraction_cost, "ac")
    string += onedim_para_2_str(processing, "process")
    
    string += twodim_para_2_str(distance_matrix, "dis")
    string += twodim_para_2_str(time_matrix, "tim")


    f = open(output_name, 'w')
    f.write(string)
    
    
main()
    
def not_main():
    string = helper(distance_matrix, "dis")
    string = helper(time_matrix, "tim")
    f = open("use_to_refer.txt", 'w')
    f.write(string)













