# %%
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

# %%
# read the world geometry data exported form Task 1
data = gpd.read_file('Task-2-Data/Task-2-Exported-Geomeries.gpkg')
data.plot()
# transform geodataframe to geometry
geoms=data.geometry

# %%
# establish a canvas
fig = plt.figure(figsize=(10, 5))
# define the crs
crs=ccrs.PlateCarree()
# set up and ax object
ax = fig.add_subplot(1, 1, 1, projection=crs)
# Set the extent and crs of the map
ax.set_extent([-180, 180, -90, 90], crs)

# %%
# 将geodataframe转换为shapely geometry对象，并添加到地图上
#ax.add_geometries(geoms,crs=ccrs.PlateCarree())

# 添加海岸线、边界和地图特征
ax.add_feature(cfeature.COASTLINE)
#ax.add_feature(cfeature.BORDERS)
#ax.add_feature(cfeature.OCEAN)
#ax.add_feature(cfeature.LAKES)
#ax.add_feature(cfeature.LAND)

ax.add_feature(cfeature.NaturalEarthFeature('physical', 'land', '10m', edgecolor='face', facecolor=cfeature.COLORS['land']))
#ax.add_feature(cfeature.NaturalEarthFeature('physical', 'ocean', '10m', edgecolor='face', facecolor=cfeature.COLORS['water']))


# 显示地图
plt.show()



