import geopandas as gpd
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import mapclassify as mc
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

################# 1 data import ################################
# read the world geometry data exported form Task 1
data = gpd.read_file('Task-2-Data/Task-1-Exported-Geomeries.gpkg')
# get the GDP per capita
data['GDP per capita']= 1000000* data['GDP_MD'] / data['POP_EST']
# replace nan with 0
data['GDP per capita'] = data['GDP per capita'].fillna(0)

# define the crs
crs= ccrs.EckertIV()
# project the data
data=data.to_crs(crs)

################# 2 canvas settings ###########################

# establish a canvas
fig = plt.figure(figsize=(10, 5))
# set up and ax object
ax = fig.add_subplot(1, 1, 1, projection=crs)

# Set the extent and crs of the map
ax.set_global()
# Set parameters of the ax
for spine in ax.spines.values():
    spine.set_linewidth(1)
    spine.set_color('grey')

################ 3 classification and plotting ################

# classify the data to be 5 classes using breaks inspired by Quantiles
class_number = 5
breaks = [2000, 5000, 10000, 30000, 200000] # the breaks were inspired by results of Quantiles
#classifier = mc.Quantiles(data['GDP per capita'], k=class_number) # this script was run first to get the raw breaks
classifier = mc.UserDefined(data['GDP per capita'], breaks)
classifications = np.array(classifier.yb)

# plot the classification
cmap = plt.get_cmap('RdYlGn', class_number) #set the colormap
for i in range(class_number):
    subset = data[classifications == i]
    ax.add_geometries(subset['geometry'], crs, facecolor=cmap(i), edgecolor='black', linewidth=0.2)

# add the ocean and lakes
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAKES)

############### 4 map layout setting ############################

#set title
ax.set_title("GDP per capita in 2019 for all countries")
ax.title.set_fontname('times new roman')
ax.title.set_fontsize(16)

# set the legend
# create a list of color labels for the legend (NB: this is only fot the case of 5 classes)
color_labels = ['< 2000', '2000-5000', '5000-10000', '10000-30000', '> 30000']
# create a list of colored rectangles to use for the legend
rectangles = [Rectangle((0, 0), 1, 1, fc=cmap(i)) for i in range(class_number)]
# create the legend with the colored rectangles
legend = ax.legend(rectangles, color_labels, title='GDP per capita ($)', bbox_to_anchor=(0.25,0.51), 
fontsize=8, prop='times new roman', frameon=True, facecolor='white', edgecolor='grey', fancybox=False)
legend.get_title().set_fontname('times new roman')
legend.get_title().set_fontsize(10)

# set the gridlines
gl=ax.gridlines(draw_labels=True,linestyle=":",linewidth=0.25,color='b')
gl.top_labels=False                                                   
gl.xlabel_style={'size':8,'fontproperties':'times new roman'}                          
gl.ylabel_style={'size':8,'fontproperties':'times new roman'}

# set the metadata
# Create a text box
text_str = 'Made by: Senyang Li | Environment: Python 3.8.16\nSource: Natural Earth | CRS: Eckert IV'
text_box = ax.text(x=0.543, y=0.006, s=text_str,transform=ax.transAxes,
bbox=dict(facecolor='none', edgecolor='none', pad=5))
text_box.set_fontproperties('times new roman')
text_box.set_fontsize(5)

################# 5 map export and show ###########################

# export the map
plt.savefig('Task-2-Result (by Python).png', dpi=300, bbox_inches='tight')
# show the map
plt.show()