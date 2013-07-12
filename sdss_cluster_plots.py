#!/anaconda/bin/python

import astropy.coordinates as coord
import astropy.units as u
import pos_search as pos

with open("../SciCoder.2013.07/data/sdss_clusters.txt") as f:

	lines = f.readlines()
	clusters = []
	for line in lines[1:]:
		clusters.append(line.split(',')[0])
	
	print clusters
	
	n = len(clusters)
	c = [coord.GalacticCoordinates.from_name(ii) for ii in clusters]
	print c
	
for i in range(n):
	pos.pos_search((c[i].l)*u.deg, (c[i].b)*u.deg, 0.5*u.deg, 0.5*u.deg)