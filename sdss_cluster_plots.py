#!/anaconda/bin/python

import astropy.units as u
from astropy import coordinates as coord
import pos_search
import coord

with open("../SciCoder.2013.07/data/sdss_clusters.txt") as f:

	lines = f.readlines()
	print lines
	clusters = []
	for line in lines[1:]:
		clusters.append(line.split(',')[0])
	
	print clusters
	