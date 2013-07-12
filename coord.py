#!/Users/jhyoon/anaconda/bin/python


import math
import astropy.units as u

def coord_convert(l,b,dist):  
    deg2rad = math.pi/180.
   
    x = dist*map(math.sin,b*deg2rad)*map(math.cos,l*deg2rad)-8.*u.kpc
    y = dist*map(math.sin,b*deg2rad)*map(math.sin,l*deg2rad)
    z = dist*map(math.cos,b*deg2rad)
    print x.shape
    dist_galactic = map(math.sqrt,x**2.+y**2.+z**2.)
    return [x,y,z,dist_galactic]

