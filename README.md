# Live-Pollution-Mapping
<h3>How to use:</h3><br>
asciinema : https://asciinema.org/a/VFC2rjPvV48OZXjGnUfiaE2In

<h4>Errors while running:</h4>

Sometimes you may get the following error while running pollution.py file :<br>
<code>Traceback (most recent call last):
  File "pollution.py", line 25, in <module>
    grid_z0 = griddata(np.asarray(points), values, (grid_x, grid_y), method='nearest')
  File "/usr/local/lib/python3.6/dist-packages/scipy/interpolate/ndgriddata.py", line 206, in griddata
    raise ValueError("invalid number of dimensions in xi")
ValueError: invalid number of dimensions in xi
</code>
<br><br>
To troubleshoot this simply rerun the program.. Looks like it's a bug in matplotlib. :)
