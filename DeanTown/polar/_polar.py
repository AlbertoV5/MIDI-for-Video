import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from matplotlib.patches import Rectangle
import matplotlib
from matplotlib import cm
import os

def Plot(title, position, pitch, length, velocity, mark, vmin1, vmax1, yTicks, path, cmp):
    
    for i in range(len(position)):
        position[i] = (position[i]/(8))  * 6.283
    
    for i in range(len(length)):
        length[i] = (length[i]/8) *3.141
        
    fig,ax = plt.subplots(subplot_kw=dict(projection="polar"))
    ax.figure.set_size_inches(20, 20)
    fig.subplots_adjust(top=0.75)
    ax.set_xlabel('', fontsize = 32)
    ax.set_ylabel('', fontsize = 24)
    ax.grid(axis="both", alpha = 1)
    ax.set_yticks(range(0))
    ax.set_xticklabels([1*label for label in range(64)], fontsize = 0)
    
        
    cmap = cm.get_cmap(cmp)
    norm = matplotlib.colors.Normalize(vmin=vmin1, vmax=vmax1)
    
    a = (position, pitch, length, velocity)
    height = 4
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

Sequence(dr, 0, 120, 'spring')



