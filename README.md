# Manual: Spatial Data Cleaning and Mapping in Python


## Introduction

This manual gives detailed instructions about how to set up the Python environment and how to handle spatial data including the data cleaning about the geometry and data mapping in the Python environment. The content of the manual includes the description of prerequisites, methods, codes, results and possible troubles.

By default the manual applies to both Windows and MacOS and has been tested in Windows 10 and MacOS Ventura platform.  Anything needing attention about the two platforms are explained in the body.

The links for all the software and Python package documentation introduced can be found in the end of the manual.



## 1 Starter: Set up Python Environment

#### 1.1  Set up the environment in Anaconda and install packages

Anaconda is a popular Python distribution that provides a set of tools and libraries. Anaconda allows user to create virtual Python environments with their own set of dependencies, packages, and configurations. Setting up Python environment in Anaconda is easy and time-saving. Anaconda is available for Windows, macOS, and Linux, so it is convenient to share Python environments across different operating systems.

![Untitled](README%20Images/Untitled.png)

Let’s open Anaconda and create a new environment as Python 3.8, which supports for all libraries we need and is stable for the for spatial data analysis in VS code.

![Untitled](README%20Images/Untitled%201.png)

We can then search for the packages in the search bar and install them. For our task we need to install the libraries as follows:

(image below shows the installation of `Geopandas`)

- `Pandas`: Popular open-source data analysis and manipulation Python library for tabular and time-series data.
- `Geopandas`: Python library that extends `Pandas`, with additional geospatial functionality for spatial data.
- `Numpy`: Python library for scientific computing that provides support for working with large, multi-dimensional arrays and matrices, and a collection of mathematical functions.
- `Matplotlib`: Python data visualization library to create a variety of static, animated, and interactive plots, graphs, and charts.
- `Cartopy`: Python library built on top of Matplotlib that provides a set of tools for creating maps and visualizations of geospatial data.
- `Mapclassify`: Python library for choropleth map classification, providing various methods to classify and visualize geospatial data.

![Untitled](README%20Images/Untitled%202.png)



#### 1.2 Write Jupyter Notebook (ipynb.) / Python script (py.) in VS Code

After we set up the environment, we can start to write the scripts. We will do all the coding in VS Code. VS Code is a free and open-source code editor developed by Microsoft with powerful features, customisable interface, and vast library of extensions. 

VS Code supports multiple programming languages and provides features like debugging, Git integration, and intelligent code completion. By simply installing extension of Python, we can edit Python script (py.) and Jupyter Notebook (ipynb.) in VS Code.

![Untitled](README%20Images/Untitled%203.png)

A Python script is a plain text file with a “.py” extension that contains Python code. It can be run on any system with Python installed by invoking the Python interpreter and specifying the path to the script. Python scripts can automate tasks, manipulate data, and build applications. The scripts can be run as a whole. Jupyter Notebook is a web-based interactive computing platform with a “.ipynb” extension that allows users to create and documents that contain live Python code, visualisations, and narrative text.  It provides a user-friendly interface for data exploration, and prototyping. We can run the code by block and get real-time results. To show their different features, the spatial data cleaning will be done with Jupyter Notebook (ipynb.) and spatial data mapping will be done with Python script (py.).

To start writing scripts, we switch the environment to what we have created and open VS Code in Anaconda. Then we pick a file directory and create a ipynb. and py. file. After opening them, we could find the VS code was running with the Python environment we created. (See top right corner).

![Untitled](README%20Images/Untitled%204.png)

![Untitled](README%20Images/Untitled%205.png)

After writing, we can run the codes of Jupyter notebook by tapping “Run” button beside each block and we will get the result of this block beneath it. We can also tap “Run All” button in the above panel and get the results of all blocks.

![Untitled](README%20Images/Untitled%206.png)

For Python script, we simply tap “Run Python File” and the code will be run from the start to the end. The output information can be checked in the Terminal.

![Untitled](README%20Images/Untitled%207.png)



#### 1.3 Do version control using Git and push the project to GitHub

Version control is essential as it allows developers to track changes, collaborate effectively, revert to previous versions, and maintain code integrity, leading to better management. Git is a free and open-source version control system widely used to manage and track changes in code, and GitHub is a web-based hosting service that provides a platform for Git repositories. VS Code supports the user to build and develop the repository for version control after installing the Git and pushes the repository to GitHub. The manual will also introduce how to the version control via Git for the project.

First, open source control and add the repository from the local directory.

![Untitled](README%20Images/Untitled%208.png)

Next, after every changes of our code in the directory, we get notification from the source control panel. We can check the changes we made in the panel. If it is fine, we can stage the changes, add commitment message and commit them.

![Untitled](README%20Images/Untitled%209.png)

![Untitled](README%20Images/Untitled%2010.png)

If it is the first time of commitment, we can publish branch, log in our GitHub account and publish the repository to GitHub. After that, we can also synchronise the changes to the repository in GitHub every time we commit.

![Untitled](README%20Images/Untitled%2011.png)

By doing this, we will have local and remote (in GitHub) repositories that contain our project and track the changes of the codes.



## 2 Spatial Data Cleaning (Task 1)

*Python environment: Python 3.8*

*Format of code: Jupyter Notebook (.ipynb)*

*Input Data: Online Natural Earth data (world country geometries); Offline ISO_A2_list.csv*

*Output Data: Task-1-Exported-Geometries.gpkg (exported from Geodataframe,  containing ISO_A2 code,  full name of countries, population and GDP in 2019, and geometries)* 



#### 2.1 Download geometry data

To begin with, we need to import `pandas` for managing the csv file, `geopandas` for spatial data, `numpy` for the arrays.

```python
import pandas as pd
import geopandas as gpd
import numpy as np
```

Then, we get the Url from Natural Earth for 1:10m country geometries (NB. The original link leading to the download didn’t work in Python. We need to ask browser to analyse the link and get a redirected link.) The `read_file` function in geopandas can easily read the shapefile inside the zip. file we downloaded from Natural Earth.

```python
# Get geometry data from Natural Earth
url = "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip"
data_v1 = gpd.read_file(url)
print(data_v1.head())
```

Then we have a Geodataframe variable called `data_v1`. We can use the `to_crs` function to make its CRS to WGS_1984 (SRS=4326).

```python
# Set SRS=4326
data_v1 = data_v1.to_crs(epsg=4326)
print(data_v1.crs)
```



#### 2.2 Read, clean and join the csv. data

Next, we start to clean the offline *ISO_A2_list 2.csv* provided. It is read by `read_csv` function in Pandas and becomes a Dataframe. We can find that the arrangement of the content is very messy (See left image below). We need to get rid of all the NaN rows, and split the first column by “;”, and make the results to be different new columns (column `‘iso_a2’`: ISO_A2 code for countries; `‘name_part2’`: second part of the country full names). The column `‘Unnamed: 1’` refers to the first part of the country full names, so we should fill the NaN values here to be a blank string, and concatenate the `‘Unnamed: 1’` with `‘name_part2’`, which will generate the full names of countries stored in `‘name’` column. Finally, we capitalised the iso_a2 code for the data joining later and get rid of all unnecessary columns. The right image below shows the cleaned table.

```python
# Read the ISO_A2 list file
countries = pd.read_csv('Task-1-Data/iso_a2_list 2.csv')
# Get rid of all the nan rows
countries = countries.dropna(how="all")
# Split the first colmn
countries['iso_a2'] = countries['iso_a2;country_name_eng'].str.split(';').apply(lambda x: x[0])
countries['name_part2'] = countries['iso_a2;country_name_eng'].str.split(';').apply(lambda x: x[1])
# Get the full name of the country
countries['name'] = countries['Unnamed: 1'].fillna('') + ' ' + countries['name_part2']
# Captionise the iso_a2 code
countries['iso_a2'] = countries['iso_a2'].str.upper()
# Drop the unnecessary columns
countries=countries.drop(['Unnamed: 1','name_part2','iso_a2;country_name_eng'],axis=1)
print(countries)
```

![Untitled](README%20Images/Untitled%2012.png)

The cleaned table can then joined to the geometry data. It can done using merge function of `geopandas`. The geodataframe contains a `‘ISO_A2_EH’` column about the ISO_A2 list, and can match the `‘iso_a2’` column of the Dataframe. We set them to be `left_on` and `right_on`. The unmatched columns will be deserted. We only keep columns about ISO_A2 code,  full name of countries, population and GDP in 2019, and geometries.  Finally we get a Geodataframe named `data_v3` with 245 rows.

```python
# Match the geometry with the ISO_A2 list
data_v2 = data_v1.merge(countries, left_on='ISO_A2_EH',right_on='iso_a2')
# Keep only full name, ISO_A2, geometry, populatio and GDP of the table
data_v3 = data_v2[['geometry', 'name', 'iso_a2','POP_EST','GDP_MD']]
print(data_v3)
```

![Untitled](README%20Images/Untitled%2013.png)



#### 2.3 Validate the geometries

The validation of geometries is essential for spatial data. `Geopandas` contains `is_valid` function to check the validity of the geometries. It returns a table of logical variable (True or False) for different geometries. By using the the function all(), we can easily check whether the results for geometries are True. If they are all True, we can say all geometries are valid. If not, at least one geometry is not valid.  We can find the index of row which is False using `where()` function in `numpy` and locate the row in the geometry data. To make it valid, we can use `buffer()` function. With a buffer distance of 0, we can create a new geometry that has the same shape and location as the original one but with any self-intersections, gaps, or other issues resolved. Then we re-examined the geometries. 

```python
# check validity of data
validity = data_v3.is_valid

if validity.all():
    print('All geometries are valid')
# if some geometry is not valid, correct the geometry by setting the buffer
else:
    print('At least one geometry is not valid')
    # get the index where validity is False
    invalid_row_idx = np.where(validity == False)[0]
    print('Invalid row index:', invalid_row_idx)
    # locate the invalid geometries and set the buffer
    selected_rows = data_v3.iloc[invalid_row_idx] 
    selected_rows['geometry'] = selected_rows['geometry'].buffer(0)
    data_v3.iloc[invalid_row_idx] = selected_rows
    # reexmaine the validity
    validity_v2=data_v3.is_valid
    if validity_v2.all():
        print('the invalid geometry has been corrected, and all geometries are valid')
    else:
        print('Still at least one geometry is not valid')
```

For out data, there is one geometry not valid whose row index is 160. We validated it by `buffer(0)`.

![Untitled](README%20Images/Untitled%2014.png)

![Untitled](README%20Images/Untitled%2015.png)



#### 2.4 Export the data

The Geodataframe `data_v3`  is what we want, containing ISO_A2 code,  full name of countries, population and GDP in 2019, and validated geometries. We can export it to be geopackage using `to_file()` function.

```python
# Export the data to geopackage
data_v3.to_file('Task-2-Data/Task-1-Exported-Geometries.gpkg', layer='ISO_A2_Geometries', driver="GPKG")
```



## 3 Spatial Data Mapping (Task 2)

*Python environment: Python 3.8*

*Format of code: Python script (.py)*

*Input Data: Task-1-Exported-Geometries.gpkg (exported from Geodataframe,  containing ISO_A2 code,  full name of countries, population and GDP in 2019, and geometries.);  Online Natural Earth data (oceans and lakes)*

*Output: Task-2-Result (by Python).png (GDP per capita in 2019)*



#### 3.1 Import and initialise the spatial data

Importing the libraries is always the first step. We should import `geopandas` for spatial data, `numpy` for the arrays., `cartopy.crs` for getting projection, `cartopy.feature` for adding features to the map, `mapclassify` for classify the data, `matplotlib.pyplot` for plotting the images and `Rectangle` for building legends.

```python
import geopandas as gpd
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import mapclassify as mc
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
```

To make a GDP per capita map for the countries, we first read the data exported from Data Cleaning part. Then we set and calculate the `'GDP per capita'` dividing `'GDP_MD’` (unit: million $) by `'POP_EST'`. We need to multiply the result by 1000000 to get the GDP per capita with the unit of $ per person. As there is row with population as 0, we get some result as NaN. The solution is to omit this part and fill the NaN with 0.

Eckert IV is a very popular projection for global thematic map. We set CRS to be Eckert IV during our mapping.

```python
################# 1 data import ################################
# read the world geometry data exported form Task 1
data = gpd.read_file('Task-2-Data/Task-1-Exported-Geometries.gpkg')
# get the GDP per capita
data['GDP per capita']= 1000000* data['GDP_MD'] / data['POP_EST']
# replace nan with 0
data['GDP per capita'] = data['GDP per capita'].fillna(0)

# define the crs
crs= ccrs.EckertIV()
# project the data
data=data.to_crs(crs)
```



#### 3.2 Set up the figure and axis

The figure set by `figure()` is the base for plotting with `Matplotlib`. On top of the figure, we need to set an axis object accommodating the map. As we create global map, we can use `set_global()` to set the extent of the axis to be global. The linewidth of axis is set to 1 and colour to grey.

```python
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
```



#### 3.3 Classify the spatial data and plot the result

Before mapping, we can classify the data to be 5 classes. We basically use Quantiles method to do it, as every classes contain equal number of countries. `mapclassify` provides `Quantiles` function to conduct it. After that, we can check the breaks of the classification. And then we manually adjust the break values to them more neat. Then we redo the classification with custom breaks. `UserDefined` function of `mapclassify` can be applied. We then  get an classifier.  `classifier.yb` can extract  an array containing the class labels for each country in the `data['GDP per capita']` array based on the breaks
defined earlier.

```python
################ 3 classification and plotting ################

# classify the data to be 5 classes using breaks inspired by Quantiles
class_number = 5
breaks = [2000, 5000, 10000, 30000, 200000] # the breaks were inspired by results of Quantiles
#classifier = mc.Quantiles(data['GDP per capita'], k=class_number) # this script was run first to get the raw breaks
classifier = mc.UserDefined(data['GDP per capita'], breaks)
classifications = np.array(classifier.yb)
```

Before plotting the classification, we set the colormap to be ‘RdYnGn’. Lower value is more red and higher one is more green. Then we have a loop to iterate over each class in the classification and plots the corresponding data on the map. For each class `i`, it creates a subset of the Dataframe containing only the rows where `classifications == i` . It then plots the geometries  from this subset.

```python
# plot the classification
cmap = plt.get_cmap('RdYlGn', class_number) #set the colormap
for i in range(class_number):
    subset = data[classifications == i]
    ax.add_geometries(subset['geometry'], crs, facecolor=cmap(i), edgecolor='black', linewidth=0.2)
```

Additionally, we can add the ocean and lakes features from `Cartopy.feature` , which will get the data from Natural Earth.

```python
# add the ocean and lakes
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAKES)
```



#### 3.4 Design map element

All the map elements can be designed based on axis. For the title, font name is Times New Roman and font size is 16. It is by default on the center of the map.

```python
############### 4 map layout setting ############################

#set title
ax.set_title("GDP per capita in 2019 for all countries")
ax.title.set_fontname('times new roman')
ax.title.set_fontsize(16)
```

For legend, we can build 5 rectangles icons with the different colors in the colormap. as we make custom breaks, it is also suitable to make custom labels beside the rectangles. And the position of legend is custom to be in the place near to left bottom corner of the map.

```python
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
```

The gridlines are set to be dash lines with width of 0.25 and colour of blue. We have title on the top so we disable the labels in the top.

```python
# set the gridlines
gl=ax.gridlines(draw_labels=True,linestyle=":",linewidth=0.25,color='b')
gl.top_labels=False                                                   
gl.xlabel_style={'size':8,'fontproperties':'times new roman'}                          
gl.ylabel_style={'size':8,'fontproperties':'times new roman'}
```

Finally, we create a text box containing all the metadata. And the position is also custom to be in the place near the bottom centre. 

```python
# set the metadata
# Create a text box
text_str = 'Made by: Senyang Li | Environment: Python 3.8.16\nSource: Natural Earth | CRS: Eckert IV'
text_box = ax.text(x=0.543, y=0.006, s=text_str,transform=ax.transAxes,
bbox=dict(facecolor='none', edgecolor='none', pad=5))
text_box.set_fontproperties('times new roman')
text_box.set_fontsize(5)
```



#### 3.5 Export the map

We save the figure to be a png. with resolution of 300m and trim the unnecessary fringe. The figure is also shown after running the script by using `plt.show()`.

```python
################# 5 map export and show ###########################

# export the map
plt.savefig('Task-2-Result (by Python).png', dpi=300, bbox_inches='tight')
# show the map
plt.show()
```

![Task-2-Result (by Python).png](README%20Images/Task-2-Result_(by_Python).png)



## Useful Links

#### Software Download

Anaconda: [https://www.anaconda.com/download/](https://www.anaconda.com/download/)

VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)

Git: [https://git-scm.com/](https://git-scm.com/)

#### Python Library Documentation

Pandas: [https://pandas.pydata.org/docs/user_guide/index.html](https://pandas.pydata.org/docs/user_guide/index.html)

Geopandas: [https://geopandas.org/en/stable/docs.html](https://geopandas.org/en/stable/docs.html)

Matplotlib: [https://matplotlib.org/stable/index.html](https://matplotlib.org/stable/index.html)

Cartopy: [https://scitools.org.uk/cartopy/docs/latest/getting_started/index.html](https://scitools.org.uk/cartopy/docs/latest/getting_started/index.html)

Numpy: [https://numpy.org/doc/](https://numpy.org/doc/)

Mapclassify: [https://pysal.org/mapclassify/tutorial.html](https://pysal.org/mapclassify/tutorial.html)
