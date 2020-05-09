import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from matplotlib.patches import Rectangle
import matplotlib
from matplotlib import cm
import os

def Plot(title, position, pitch, length, velocity, mark, vmin1, vmax1, yTicks, path, cmp):

    fig,ax = plt.subplots(subplot_kw=dict())
    fig.subplots_adjust(top=0.8)
    ax.figure.set_size_inches(100, 10) #change to 200, 20 to big ones
    ax.set_xlabel('', fontsize = 32)
    ax.set_ylabel('', fontsize = 24)
    ax.grid(axis="both", alpha = 0.8)
    ax.set_yticks(range(0))
    ax.set_xticklabels([1*label for label in range(64)], fontsize = 0)
    ax.set_xlim(left = -1, right=64)
    
    ax.grid(which = 'major', color='k', linestyle='-', linewidth=1, alpha = 1)
    ax.grid(which = 'minor', color='k', linestyle='-',linewidth=1, alpha = .3)
    ax.xaxis.set_major_locator(MultipleLocator(4))
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
        
    cmap = cm.get_cmap(cmp)
    norm = matplotlib.colors.Normalize(vmin=vmin1, vmax=vmax1)
    
    a = (position, pitch, length, velocity)
    height = 2
    a_zipped = zip(*a)
    for a_x, a_y, a_z, a_c in a_zipped:
        _color = cmap(norm(a_c))
        ax.add_patch(Rectangle(xy=(a_x, a_y-height/2) ,
                               width=a_z, height=height, linewidth=1, color=_color, fill=True))
    
    ####SHOW GRIDS ?
    ax.axis('off')
    
    ax.scatter(position,pitch, s = 0, marker = mark, cmap='Purples', c = pitch, vmin=vmin1, vmax=vmax1)
    fig.savefig(path + title+".png", transparent=True)
    
def Sequence(part, vmin, vmax, cmp):
    position, pitch = [],[]
    for csv in os.listdir(part):
        if ".csv" in csv:
            notes = pd.read_csv(part + "/" + csv)
            position = notes["Position"].tolist()
            pitch = notes["Pitch"].tolist()
            length = notes["Length"].tolist()
            velocity = notes["Velocity"].tolist()
                        
            Plot(str(csv).split(".")[0], position, pitch, length, velocity, ">", vmin, vmax, 64, part + "/", cmp)
    

dr = os.getcwd()
#Sequence(dr + "/bass", 10, 120, 'spring')
#Sequence(dr + "/altBass", 10, 90, 'cool')
#Sequence(dr+"/keys", 0, 120, 'spring')
#Sequence(dr+"/keys2", 40, 120, 'cool')
#Sequence(dr + "/lead", 0, 120, 'spring')
#Sequence(dr + "/bassSolo", 0, 120, 'cool_r')
#Sequence(dr + "/bassLast", 0, 120, 'spring')
#Sequence(dr + "/strings", 0, 120, 'cool_r')
Sequence(dr + "/ah", 0, 120, 'cool')
#Sequence(dr + "/strings2", 0, 120, 'cool_r')

