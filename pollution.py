import numpy as np
import requests
import json
import matplotlib.pyplot as plt
import geopandas as gpd
from scipy.interpolate import griddata

gas = input('Which pollutant do you want to plot? \nAcceptable values --> [so2, pm10, pm25, no2, o3, co]: ')
print("\nProcessing..")
r = requests.get('https://api.openaq.org/v1/measurements?city=Delhi&parameter[]='+gas).content
j = json.loads(r.decode("UTF-8"))

points=[]
v=[]

for w in j['results']:
    xv = w['coordinates']['longitude']
    yv = w['coordinates']['latitude']
    points.append(np.asarray([xv,yv]))
    v.append(w['value'])

values = np.asarray(v)

grid_x, grid_y = np.mgrid[76.97:77.48:100j, 28.45:28.81:200j]
grid_z0 = griddata(np.asarray(points), values, (grid_x, grid_y), method='nearest')

city_name = "Delhi"

rails = gpd.read_file('BB/'+city_name+'/shape/railways.shp')
roads = gpd.read_file('BB/'+city_name+'/shape/roads.shp')

fig, ax = plt.subplots(figsize = (10,10))
ax.set_title("Pollution Levels Across Delhi")
im1 = ax.imshow(grid_z0.T, extent=(76.969,77.483,28.469,28.81) , origin='lower')
fig.colorbar(im1, orientation='vertical')
rails.plot(ax=ax,linewidth=0.2,color='gray')
roads.plot(ax=ax, color='black',linewidth=0.2)

plt.show()
