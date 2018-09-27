import gpxpy
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

gpx_filename = "hike.gpx"

gps_lat = []
gps_long = []
gps_elevation = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

with open(gpx_filename, 'r') as bla:
    gpx = gpxpy.parse(bla)
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                gps_lat.append(point.latitude)
                gps_long.append(point.longitude)
                gps_elevation.append(point.elevation)


def init():
    N = len(gps_lat)
    for i in range(N - 1):
        ax.plot(gps_long[i:i + 2],           # x coordinate
                gps_lat[i:i + 2],            # y,
                gps_elevation[i:i + 2],      # z
                color=plt.cm.viridis(i / N)) # sequential color

    ax.set_xlabel("longitude")
    ax.set_ylabel("latitude")
    ax.set_zlabel("altitude (meters)")

    return fig,


def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)
anim.save('hike.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
