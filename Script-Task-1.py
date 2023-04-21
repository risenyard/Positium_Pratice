import requests

url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_countries.zip"
r = requests.get(url, allow_redirects=True)

open('ne_50m_admin_0_countries.zip', 'wb').write(r.content)

import cartopy
import cartopy.io.shapereader as shpreader

shapename = 'admin_0_countries'
countries_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapename)

import geopandas as gpd
import requests

url = "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip"
r = requests.get(url, allow_redirects=True)
open('ne_50m_admin_0_countries.zip', 'wb').write(r.content)