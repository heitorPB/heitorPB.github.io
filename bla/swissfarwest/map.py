import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.patheffects as PathEffects
from matplotlib.patches import Ellipse
import geotiler
import gpxpy

gpx_filename = "hike.gpx"
gpx = gpxpy.parse(open(gpx_filename))

bbox = [gpx.get_bounds().min_longitude - 0.002,
        gpx.get_bounds().min_latitude  - 0.002,
        gpx.get_bounds().max_longitude + 0.002,
        gpx.get_bounds().max_latitude  + 0.002]

fig = plt.figure(figsize=(13, 13))
ax = plt.subplot(111)

# download tiles from OSM
mm = geotiler.Map(extent = bbox, zoom = 16)
img = geotiler.render_map(mm)

myMap = Basemap(llcrnrlon=bbox[0], llcrnrlat=bbox[1],
                urcrnrlon=bbox[2], urcrnrlat=bbox[3],
                projection='merc', ax=ax)
myMap.imshow(img, interpolation='lanczos', origin='upper')

# plot hike
points = gpx.get_points_data()
lon = [p[0].longitude for p in points]
lat = [p[0].latitude  for p in points]
index = [p.point_no for p in points] # to color sequentially each point

x, y = myMap(lon, lat) # map (long, lat) to (x,y) coordinates in plot
ax.scatter(x, y, c = index, s = 4, cmap='brg')

# add some texts and arrows with style
t1 = ax.annotate('France', xy=(.01, .96), xycoords='axes fraction',
                 horizontalalignment='left', fontsize = 20,
                 verticalalignment='bottom', fontname = 'monospace')
t2 = ax.annotate('Switzerland', xy=(.99, .96), xycoords='axes fraction',
                 horizontalalignment='right', fontsize = 20,
                 verticalalignment='bottom', fontname = 'monospace')
el = Ellipse((2, -1), 0.5, 0.5)
t3 = ax.annotate('Border', xy=(.61, .90), xycoords='axes fraction',
                 xytext=(.5, .96), textcoords='axes fraction',
                 horizontalalignment='center', fontsize = 20,
                 verticalalignment='bottom', fontname = 'monospace',
                 arrowprops=dict(arrowstyle="simple",
                                 fc="black", ec="none",
                                 patchB=el,
                                 connectionstyle="arc3,rad=0.3"))
t4 = ax.annotate("Switzerland's\nwestest point", xy=myMap(5.9559555, 46.1323555),
                 xytext=(.3, .42), textcoords='axes fraction',
                 horizontalalignment='center', fontsize = 20,
                 verticalalignment='bottom', fontname = 'monospace',
                 arrowprops=dict(arrowstyle="simple",
                                 fc="black", ec="none",
                                 patchB=el,
                                 connectionstyle="arc3,rad=0.3"))
for t in [t1, t2, t3, t4]:
    t.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w', alpha = 0.666)])


plt.savefig('map.png', quality = 100, bbox_inches = 'tight')
plt.close()