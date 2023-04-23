# Manual: Spatial Data Cleaning and Mapping in Python

# Introduction

This manual gives detailed instructions about how to set up the Python environment and how to handle spatial data including the data cleaning about the geometry and data mapping in the Python environment. The content of the manual includes the description of prerequisites, methods, codes, results and possible troubles.

By default the manual applies to both Windows and MacOS and has been tested in Windows 10 and MacOS Ventura platform.  Anything needing attention about the two platforms are explained in the body.

The links for all the software and Python package documentation introduced can be found in the end of the manual.

# 1 Starter: Set up Python Environment

### 1.1  Set up the environment in Anaconda and install packages

Anaconda is a popular Python distribution that provides a set of tools and libraries. Anaconda allows user to create virtual Python environments with their own set of dependencies, packages, and configurations. Setting up Python environment in Anaconda is easy and time-saving. Anaconda is available for Windows, macOS, and Linux, so it is convenient to share Python environments across different operating systems.

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled.png)

Let’s open Anaconda and create a new environment as Python 3.8, which supports for all libraries we need and is stable for the for spatial data analysis in VS code.

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%201.png)

We can then search for the packages in the search bar and install them. For our task we need to install the libraries as follows:

(image below shows the installation of Geopandas)

- Pandas: Popular open-source data analysis and manipulation Python library for tabular and time-series data.
- Geopandas: Python library that extends Pandas, with additional geospatial functionality for spatial data.
- Numpy: Python library for scientific computing that provides support for working with large, multi-dimensional arrays and matrices, and a collection of mathematical functions.
- Matplotlib: Python data visualization library to create a variety of static, animated, and interactive plots, graphs, and charts.
- Cartopy: Python library built on top of Matplotlib that provides a set of tools for creating maps and visualizations of geospatial data.
- Mapclassify: Python library for choropleth map classification, providing various methods to classify and visualize geospatial data.

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%202.png)

### 1.2 Write Jupyter Notebook (ipynb.) / Python script (py.) in VS Code

After we set up the environment, we can start to write the scripts. We will do all the coding in VS Code. VS Code is a free and open-source code editor developed by Microsoft with powerful features, customisable interface, and vast library of extensions. 

VS Code supports multiple programming languages and provides features like debugging, Git integration, and intelligent code completion. By simply installing extension of Python, we can edit Python script (py.) and Jupyter Notebook (ipynb.) in VS Code.

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%203.png)

A Python script is a plain text file with a “.py” extension that contains Python code. It can be run on any system with Python installed by invoking the Python interpreter and specifying the path to the script. Python scripts can automate tasks, manipulate data, and build applications. The scripts can be run as a whole. Jupyter Notebook is a web-based interactive computing platform with a “.ipynb” extension that allows users to create and documents that contain live Python code, visualisations, and narrative text.  It provides a user-friendly interface for data exploration, and prototyping. We can run the code by block and get real-time results. To show their different features, the spatial data cleaning will be done with Jupyter Notebook (ipynb.) and spatial data mapping will be done with Python script (py.).

To start writing scripts, we switch the environment to what we have created and open VS Code in Anaconda. Then we pick a file directory and create a ipynb. and py. file. After opening them, we could find the VS code was running with the Python environment we created. (See top right corner).

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%204.png)

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%205.png)

### 1.3 Do version control using Git and push the project to GitHub

Version control is essential as it allows developers to track changes, collaborate effectively, revert to previous versions, and maintain code integrity, leading to better management. Git is a free and open-source version control system widely used to manage and track changes in code, and GitHub is a web-based hosting service that provides a platform for Git repositories. VS Code supports the user to build and develop the repository for version control after installing the Git and pushes the repository to GitHub. The manual will also introduce how to the version control via Git for the project.

First, open source control and add the repository from the local directory.

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%206.png)

Next, after every changes of our code in the directory, we get notification from the source control panel. We can check the changes we made in the panel. If it is fine, we can stage the changes, add commitment message and commit them.

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%207.png)

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%208.png)

If it is the first time of commitment, we can publish branch, log in our GitHub account and publish the repository to GitHub. After that, we can also synchronise the changes to the repository in GitHub every time we commit.

![Untitled](Manual%20Spatial%20Data%20Cleaning%20and%20Mapping%20in%20Python%2033deb7d995f3444ba29767b44359488f/Untitled%209.png)

By doing this, we will have local and remote (in GitHub) repositories that contain our project and track the changes of the codes.

# 2 Spatial Data Cleaning

*Python environment: Python 3.8*

*Format of code: Jupyter Notebook (.ipynb)*

*Input Data: Online Natural Earth data (world country geometries); Offline ISO_A2_list.csv*

*Output Data: Task-1-Exported-Geomeries.gpkg ( exported from Geodataframe,  containing ISO_A2 code,  full name of countries, population and GDP in 2019, and geometries.*

### 2.1 Download geometry data

```python
import pandas as pd
import geopandas as gpd
import numpy as np
```

### 2.2 Read, clean and join the csv. data

### 2.3 Validate the geometries

### 2.4 Export the data

- Which scripts to run and how?

 downloads the **geometries** of **ISO 3166-1 alpha-2 (ISO_A2) country list**, and **validates the geometries**.

1. Troubleshooting: It is important to include a troubleshooting section that provides guidance on common errors or issues that users may encounter when setting up or running the software. You can provide suggestions for resolving these issues, or provide links to relevant resources or forums where users can get additional help.
2. Troubleshooting
a. Common errors or issues
b. Suggestions for resolving issues
c. Links to additional resources or forums

# 3 Spatial Data Mapping

*Python environment:*

*Format of code:*

Input *Data:*

Output *Data:*

### 3.1 Import and initialise the spatial data

### 3.2 Set up the canvas

### 3.3 Classify the spatial data and plot the result

### 3.4 Design map element

### 3.5 Export the map

- Anything else that needs to be set up to run scripts.
1. Running scripts
a. Which scripts to run
b. How to run scripts
c. Command-line arguments or input files
d. Examples of expected output and interpretation

# Useful Links

### Software Download

Anaconda: [https://www.anaconda.com/download/](https://www.anaconda.com/download/)

VS code: [https://code.visualstudio.com/](https://code.visualstudio.com/)

Git: [https://git-scm.com/](https://git-scm.com/)

### Python Library Documentation

Pandas: [https://pandas.pydata.org/docs/user_guide/index.html](https://pandas.pydata.org/docs/user_guide/index.html)

Geopandas: [https://geopandas.org/en/stable/docs.html](https://geopandas.org/en/stable/docs.html)

Matplotlib: [https://matplotlib.org/stable/index.html](https://matplotlib.org/stable/index.html)

Cartopy: [https://scitools.org.uk/cartopy/docs/latest/getting_started/index.html](https://scitools.org.uk/cartopy/docs/latest/getting_started/index.html)

Numpy: [https://numpy.org/doc/](https://numpy.org/doc/)

Mapclassify: [https://pysal.org/mapclassify/tutorial.html](https://pysal.org/mapclassify/tutorial.html)
