import gpxpy

gpx_filename = "hike.gpx"
gpx = gpxpy.parse(open(gpx_filename))

print("")
print("distance:", gpx.length_3d(), "m")
print("duration:", gpx.get_duration(), "s")
print("started:", gpx.get_time_bounds()[0])
print("ended:",   gpx.get_time_bounds()[1])
print("elevation extremes:", gpx.get_elevation_extremes()[:], "m")
print("Max speed: ", gpx.get_moving_data()[-1], "m/s")
print("Boundaries: ", [bla for bla in gpx.get_bounds()])
