#!/usr/bin/env python
# coding: utf-8

# This code is used for station map and noise pathways ploting for Ambient Seismic Noise.  
# The first part of this script plots a Seismic Station map for the region of Turrialba in Costa Rica and the second part plots the different
# inter-station noise paths of the network. 

# In[1]:


import pygmt 
from numpy.random import randint
import xarray as xr
import numpy as np
import getpass
import pandas as pd


# In[213]:


fig = pygmt.Figure()
#fig.basemap(region=[-93,-82,7,18], projection="M15c", frame=True)
#fig.coast(water='lightblue', land='grey', frame=True)
fig.coast(
    region=[-86,-82.8,8,11.2],                #[xmin, xmax, ymin, ymax]
    projection='M10i',           # 4 inches mercator projection     #'a0.2i' star symbol
    shorelines="0.5p,black",
    borders=["1/0.5p,black"],
    water='lightblue',
    land='grey',
    frame=True,
    resolution='f', 
) 
#grid=("/Users/seismo_reynier/Documents/cam_slab2_dep_02.24.18.grd")
#fig.grdcontour(
#    region=[-93,-82,7,18],
    #annotation=1000,
    #interval=400,
#    grid=grid,
    #limit=[-2000, 8000],
#    projection="M10i",
#    frame=True,
#)
#fig.grdimage(grid="/Users/seismo_reynier/Documents/cam_slab2_dep_02.24.18.grd", region=[-93,-82,7,18]) 
fig.show() 


# In[220]:


fig.grdimage(
    grid= "@earth_relief_03s",
    cmap='geo',
#    region=region,
    projection='M10i',
    shading=True,
    frame=True,
)
fig.coast(
    region=[-86,-82.8,8,11.2],                #[xmin, xmax, ymin, ymax]
    projection='M10i',           # 4 inches mercator projection     #'a0.2i' star symbol
    shorelines="1.5p,black",
    borders=["1/0.5p,black"],
#    water='lightblue',
#    land='grey',
    frame=True,
    map_scale="jBR+w50k+f+o1c/1c+lKm",
)
fig.show() 


# In[221]:


fig.text(text=["Cocos Plate"], x=[-85.5], 
         y=[9], font="30p,Helvetica-Bold,black") 
fig.text(text=["Turrialba"], x=[-83.767], 
         y=[10.5], font="30p,Helvetica-Bold,black") 
fig.text(text=["San Jose"], x=[-84.5], 
         y=[9.4], font="30p,Helvetica-Bold,black") 
fig.colorbar(position="JMR", cmap=True, frame=["af", "x+lElevation", "y+lm"])          #["a400f200", "x+lElevation","y+lm"])
fig.show()


# In[222]:


#fig.text(x=-78.436, y=0, text="Cotopaxi", font="10p,Helvetica-Bold")
Data = pd.read_csv (r'/Users/seismo_reynier/Documents/Volc_plot.csv')
Data.head()
fig.plot(
    x=Data.Longitude,
    y=Data.Latitude,
    style="t1.4c",
    #style="kvolcano/0.6c", 
    pen="0.2p,white", #color="red"
    color='black',    #just for earthquake depth (do not need it)
    label="Central America Volcanoes",
    #cmap=True,
)
fig.plot(x=-83.767, y=10.025, style="kvolcano/1.8c", pen="0.5p,black", color="red")
fig.plot(x=-84.0907, y=9.9281, style="a1.4c", pen="0.2p,black", color="yellow")
fig.show()
#fig.legend(position="JTR+o-0.8c", box="+p2p,black")
    #ZOOM IN TO COSTA RICA VOLCANIC ARC 


# In[223]:


with fig.inset(position="jBL+w4.6c+o0.1c", margin=0, box="+p2p,black"):
    # Create a figure in the inset using coast. This example uses the azimuthal
    # orthogonal projection centered at 47E, 20S. The land color is set to
    # "gray" and Madagascar is highlighted in "red3".
    fig.coast(
        region=[-116, -76, 8, 31],
        projection='G-84/10/4.6c',
        land="gray",
        water="lightblue",
        dcw="CR+gred+p0.3p",
    )
fig.show()
fig.savefig(r'/Users/seismo_reynier/Documents/Tuttialba1.png', dpi = 300) 


# In[3]:


Volc = pd.read_csv (r'/Users/seismo_reynier/Documents/two_volc.csv')
Shocks = pd.read_csv (r'/Users/seismo_reynier/Documents/after_shocks.csv')
#Stat = pd.read_csv (r'/Users/seismo_reynier/Documents/stations.csv')
Stat = pd.read_csv (r'/Users/seismo_reynier/Documents/stations2.csv')
#Volc.head()
Shocks.head()
#Stat.head()


# In[4]:


#Set the region for our map based on the lat long of my data table
region = [
    Stat.longitude.min() - 0.2,
    Stat.longitude.max() + 0.2,
    Stat.latitude.min() - 0.2,
    Stat.latitude.max() + 0.2,
]


# In[5]:


fig = pygmt.Figure()
fig.coast(
    region=region,                #[xmin, xmax, ymin, ymax]
    projection='M15c',           # 4 inches mercator projection     #'a0.2i' star symbol
    shorelines="0.5p,black",
    borders=["1/0.5p,black"],
    #water='lightblue',
    land='lightgrey',
    frame=True,    #['a','+t"Station map"'],
    map_scale="jBL+w10k+f+o0.8c/0.8c+lKm",
    resolution='f',
)  
fig.show()


# In[8]:


fig.grdimage(
    grid="@earth_relief_03s",
    cmap="geo",       #haxby topo earth world
    #region=region,
    projection="M15c",
    frame=True,
    shading=True,
) 
fig.coast(
    region=region,                #[xmin, xmax, ymin, ymax]
    projection='M15c',           # 4 inches mercator projection     #'a0.2i' star symbol
    shorelines="0.5p,black",
    borders=["1/0.5p,black"],
    #water='lightblue',
    #land='lightgrey',
    frame=True,    #['a','+t"Station map"'],
    map_scale="jBL+w10k+f+o0.8c/0.8c+lKm",
    resolution='f',
)  
fig.plot(
    x=Volc.longitude,
    y=Volc.latitude,
    style="t1.5c",
    #style="kvolcano/0.6c", 
    pen="0.2p,white", 
    color='red',    
    label="Turrialba and Irazu",
    #cmap=True,
)
fig.plot(
    x=-83.793,
    y=9.948,
    style="a1.2c",
    color='blue',
    label='Earthquake',
    pen='0.1,black'
)
fig.plot(
    data=data,
    style="=0.4c+s",         #"=0.2c+ea+s", v0c+s
    pen="1.5p,black",
    #color="red",
)
fig.plot(
    x=Stat.longitude,
    y=Stat.latitude,
    style="i1.2c",
    pen="0.1,black",
    color="darkviolet",
    label="Seismic Stations"
)
fig.colorbar(position="JMB", cmap=True, frame=["af", "x+lElevation", "y+lm"])
fig.show()
fig.savefig(r'/Users/seismo_reynier/Documents/Tuttialba2.png', dpi = 300)


# In[137]:


inset = pd.read_csv (r'/Users/seismo_reynier/Documents/inset.csv')
fig = pygmt.Figure()
regionx = [
    Stat.longitude.min(),
    Stat.longitude.max(),
    Stat.latitude.min(),
    Stat.latitude.max(),
    ]
fig.coast(
    region=[-83.798802,-83.754898,10.0002,10.0286],              #[-84.196798,-83.70,9.95,10.18],
    projection='M2i',
    land="lightgray",
    frame=True
        #water="lightblue",
        #dcw="EC+gred+p0.5p",
)
fig.plot(
    x=inset.longitude,
    y=inset.latitude,
    style="i0.2c",
    pen="0.1,black",
    color="darkviolet",
    #label="Seismic Stations"
)
fig.plot(
    x=-83.767,
    y=10.025,
    style="t0.2c",
    color='red',
    pen='0.1,black'
    #label='Earthquake'
)
    

fig.show() 


# In[12]:


fig = pygmt.Figure()
fig.coast(
    region=[-83.9,-83.723,9.918,10.05],                #[xmin, xmax, ymin, ymax] #[-83.852,-83.720,9.943,10.021])
    projection='M15c',           # 4 inches mercator projection     #'a0.2i' star symbol
    shorelines="0.5p,black",
    borders=["1/0.5p,black"],
    water='lightblue',
    land='lightgrey',
    frame=True,       #['a','+t"Station map"'],
    resolution='f', 
)

fig.show()


# In[13]:


fig.grdimage(
    grid="@earth_relief_01s",
    cmap="haxby",     #haxby topo earth world
    projection='M15c',
    frame=True,
)
fig.coast(
    region=[-83.9,-83.723,9.918,10.05],                #[xmin, xmax, ymin, ymax]
    projection='M15c',           # 4 inches mercator projection     #'a0.2i' star symbol
    shorelines="0.5p,black",
    borders=["1/0.5p,black"],
    #water='lightblue',
    #land='lightgrey',
    frame=True,    #['a','+t"Station map"'],
    map_scale="jBL+w2k+f+o0.8c/0.8c+lKm",
    resolution='f',
)
fig.grdcontour(
    annotation=250,
    interval=100,
    grid="@earth_relief_03s",
    #limit=[-2000, 8000],
    projection='M15c',
    frame=True,
)
fig.plot(
    x=Volc.longitude,
    y=Volc.latitude,
    style="t1.5c",
    #style="kvolcano/0.6c", 
    pen="0.2p,white", 
    color='red',    
    label="Turrialba and Irazu",
    #cmap=True,
)
data1 = np.array([VICA+VTCG, VTUC+VTUN, VICA+VTCE, VTLA+VTUC, VICA+VTUC, VTCE+VTCV, VICA+VTLA,
                 VICA+VTUN, VTCE+VTUC, VTCV+VTUN, VTCG+VTCV, VTCG+VTUC, VTCE+VTUN, VTCV+VTUC, 
                 VTCE+VTLA, VTCE+VTCG, VTCG+VTLA, VTCG+VTUN, VTCV+VTLA, VICA+VTCV, VTLA+VTUN])
fig.plot(
    data=data1,
    style="=4c+s",         #"=0.2c+ea+s", v0c+s
    pen="2p,black",
    #color="red",
)
fig.plot(
    x=Stat.longitude,
    y=Stat.latitude,
    style="i1c",
    pen="0.1,black",
    color="darkviolet",
    #label="Seismic Stations"
)
#fig.plot(
#    x=-83.793,
#    y=9.948,
#    style="a0.5c",
#    color='black',
#    label='Earthquake',
#    pen='0.1,black'
#)
# store focal mechanisms parameters in a dict
focal_mechanism = dict(strike=247, dip=85, rake=9, magnitude=5.5)

# pass the focal mechanism data to meca in addition to the scale and event
# location
fig.meca(focal_mechanism, scale="0.9c", longitude=-83.793, latitude=9.948, depth=1.5)
fig.colorbar(position="JMB", cmap=True, frame=["af", "x+lElevation", "y+lm"])
fig.show()


# In[14]:


pygmt.makecpt(cmap="nighttime", series=[Shocks.Depth.min(), Shocks.Depth.max()])
fig.plot(
    x=Shocks.longitude,
    y=Shocks.latitude,
    size=0.02 * (2.5**Shocks.Mag),
    color=Shocks.Depth,
    style="cc",
    cmap=True,
    pen="0.1p,black",
    #style="p0.2c",
    #style="kvolcano/0.6c", 
    #label='Aftershocks',
)
fig.colorbar(position="JMR", frame='af+l"EQ Depth (km)"') #SET T
fig.text(text=["Irazu"], x=[-83.852], y=[9.95], font="20p,Helvetica-Bold,black") 
fig.text(text=["Turrialba"], x=[-83.80], y=[10.035], font="20p,Helvetica-Bold,black") 
fig.text(text=["Mw-5.5 EQ"], x=[-83.7666], y=[9.932], font="20p,Helvetica-Bold,black")
fig.text(text=["Aftershocks"], x=[-83.8500], y=[10.0166], font="20p,Helvetica-Bold,black") 
fig.show()
fig.savefig(r'/Users/seismo_reynier/Documents/Contour.png', dpi = 300)


# In[7]:


BATAN = [-83.376099, 10.0978]
CDM = [-83.763702, 9.5537]
RIFO = [-83.922798, 10.3172]
HDC3 = [-84.111397, 10.0021]
RIFO = [-83.922798, 10.3172]
VICA = [-83.844597, 9.9845]
OCM = [-83.962303, 9.8941]
RIMA = [-83.863602, 9.7666]
VPTE = [-84.198502, 10.1718]
VTCE = [-83.756798, 10.0246]
VTCG = [-83.758598, 10.0147]
VTCV = [-83.7267, 9.9831]
VTLA = [-83.7752, 10.0027]
VTRT = [-83.792702, 10.002]
VTUC = [-83.762001, 10.024]
VTUN = [-83.7635, 10.0226]
#dataR = np.array([BATAN + CDM, BATAN + HDC3, BATAN + OCM, BATAN + OCM])
data = np.array([BATAN+CDM, BATAN+HDC3, BATAN+OCM, BATAN+RIFO, BATAN+RIMA, BATAN+VICA, BATAN+VPTE, BATAN+VTCE, BATAN+VTCG, BATAN+VTCV, 
BATAN+VTLA, BATAN+VTRT, BATAN+VTUC, BATAN+VTUN, CDM+HDC3, CDM+OCM, CDM+RIFO, CDM+RIMA, CDM+VICA, CDM+VPTE, CDM+VTCE, 
CDM+VTCG, CDM+VTCV, CDM+VTLA, CDM+VTRT, CDM+VTUC, CDM+VTUN, HDC3+OCM, HDC3+RIFO, HDC3+RIMA, HDC3+VICA, HDC3+VPTE, 
HDC3+VTCE, HDC3+VTCG, HDC3+VTCV, HDC3+VTLA, HDC3+VTRT, HDC3+VTUC, HDC3+VTUN, OCM+RIFO, OCM+RIMA, OCM+VICA, OCM+VPTE, 
OCM+VTCE, OCM+VTCG, OCM+VTCV, OCM+VTLA, OCM+VTRT, OCM+VTUC, OCM+VTUN, RIFO+RIMA, 
RIFO+VICA,
RIFO+VPTE,
RIFO+VTCE,
RIFO+VTCG,
RIFO+VTCV,
RIFO+VTLA,
RIFO+VTRT,
RIFO+VTUC,
RIFO+VTUN,
RIMA+VICA,
RIMA+VPTE,
RIMA+VTCE,
RIMA+VTCG,
RIMA+VTCV,
RIMA+VTLA,
RIMA+VTRT,
RIMA+VTUC,
RIMA+VTUN,
VICA+VPTE,
VICA+VTCE,
VICA+VTCG,
VICA+VTCV,
VICA+VTLA,
VICA+VTRT,
VICA+VTUC,
VICA+VTUN,
VPTE+VTCE,
VPTE+VTCG,
VPTE+VTCV,
VPTE+VTLA,
VPTE+VTRT,
VPTE+VTUC,
VPTE+VTUN,
VTCE+VTCG,
VTCE+VTCV,
VTCE+VTLA,
VTCE+VTRT,
VTCE+VTUC,
VTCE+VTUN,
VTCG+VTCV,
VTCG+VTLA,
VTCG+VTRT,
VTCG+VTUC,
VTCG+VTUN,
VTCV+VTLA,
VTCV+VTRT,
VTCV+VTUC,
VTCV+VTUN,
VTLA+VTRT,
VTLA+VTUC,
VTLA+VTUN,
VTRT+VTUC,
VTRT+VTUN,
VTUC+VTUN])
#datax = [BATAN + CDM, BATAN + RIFO, CDM + RIFO] 
#data


# In[64]:


fig = pygmt.Figure()
regionx = [
    Stat.longitude.min() - 0.2,
    Stat.longitude.max() + 0.2,
    Stat.latitude.min() - 0.2,
    Stat.latitude.max() + 0.2,
]
fig.coast(
    region=regionx,               
    projection='M12c',           
    shorelines="0.5p,black",
    borders=["1/0.5p,black"],
    water='lightblue',
    land='lightyellow',
    frame=['a','+t"Station map"'],
    resolution='f',
    map_scale="jBR+w10k+f+o0.8c/0.8c+lKm",
)  
fig.plot(
    data=data,
    style="=0.4c+s",         #"=0.2c+ea+s", v0c+s
    pen="0.2p,black",
    #color="red",
)
fig.show() 


# In[ ]:




