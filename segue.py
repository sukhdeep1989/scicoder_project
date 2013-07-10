#!/Users/jhyoon/anaconda/bin/python

from astropy.io import fits

fits = fits.open("../ssppOut-dr9.fits",memmap=True)

print fits[1].header[20]
tbdata = fits[1].data
feh = tbdata.field("FEH_ADOP")
dist = tbdata.field("DIST_ADOP")
v = tbdata.field("RV_ADOP")
fits.close()

inx = ((feh > -9999) & (dist > -9999) & (v > -9999))
feh = feh[inx)]
dist = dist[inx]
v = v[inx]



#print fits[1].data["FEH_ADOP",0]
#fits[1].header["FEH_ADOP","DIST_ADOP","RV_ADOP"]


