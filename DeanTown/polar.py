#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 02:25:57 2020
https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html
https://newt.phys.unsw.edu.au/jw/notes.html

@author: albertovaldez
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import math
from random import randrange
#from matplotlib import patches

my_path = os.getcwd() + "/polar"

def GetFiles(pathFolderSelected):
    files_list = os.listdir(pathFolderSelected)
    files = [i for i in files_list if ".csv" in i]
    print("Found: " + str(len(files_list)) + " files.")
    return sorted(files)

files = GetFiles(my_path)
print(files)

matrix = [[] for i in files]
pitch = [[] for i in files]
position = [[] for i in files]
velocity = [[] for i in files]
length = [[] for i in files]
pitch_rad = [[] for i in files]
position_rad = [[] for i in files]


for i in range(len(files)):
    matrix[i] = pd.read_csv(my_path + "/" + files[i])
    pitch[i] = matrix[i]["Pitch"]
    position[i] = matrix[i]["Position"]
    velocity[i] = matrix[i]["Velocity"]
    length[i] = matrix[i]["Length"]
    
rangepitch = [36,96]

for i in range(len(pitch)):
    for j in range(len(pitch[i])-1):#USING -1 HERE
        x = math.degrees(((float(pitch[i][j])-min(rangepitch))/max(rangepitch)))
        pitch_rad[i].append(x)

for i in range(len(position)):#USING -1 HERE
    for j in range(len(position[i])-1):
        y = ((float(position[i][j])/max(position[i]))*math.pi)*2
        position_rad[i].append(y)

def Plot():
    #NotesInG = ["G","A","B","C","D","E","F"]
    plt.rcParams["figure.figsize"] = 16,10
    for i in range(len(files)):
        plt.plot(position[i],pitch[i],color='k', alpha = 1)
        plt.scatter(position[i],pitch[i],cmap='Reds', c = pitch[i],s = (length[i]**2)*8000)
        plt.grid(alpha = 1.0)
        #plt.xticks(range(0))
        plt.yticks([36,48,60,72,84,96])
        plt.savefig(my_path+"/bach"+str(i+1),transparent=True)
        plt.show()
#Plot()

slopes = [[] for i in files]

for i in range(len(pitch)):
    for j in range(len(pitch[i])):
        if j < len(pitch[i])-1:
            if (position[i][j+1] - position[i][j]) != 0:
                n = (pitch[i][j+1] - pitch[i][j]) / (position[i][j+1] - position[i][j])
            else:
                n = 0
            slopes[i].append(n)

randomMelody = [[] for i in files]
melodyLength = 16

print(slopes)

median = [(sum(a)/len(slopes)) for a in zip(*slopes)]
averagePosition = [(sum(a)/len(position)) for a in zip(*position)]
averagePitch = [(sum(a)/len(pitch)) for a in zip(*pitch)]

print(averagePitch)

plt.rcParams["figure.figsize"] = 10,5
plt.plot(averagePitch)
    








