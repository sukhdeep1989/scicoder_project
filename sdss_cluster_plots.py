#!/anaconda/bin/python

import astropy.coordinates as coord
import pos_search

with open("../SciCoder.2013.07/data/sdss_clusters.txt") as f:

	lines = f.readlines()
	clusters = []
	for line in lines[1:]:
		clusters.append(line.split(',')[0])
	
	print clusters
	
	n = len(clusters)
	c = [coord.GalacticCoordinates.from_name(ii) for ii in clusters]
	
	