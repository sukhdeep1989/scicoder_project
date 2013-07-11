#!/Users/jhyoon/anaconda/bin/python

import sys
from astropy.io import fits

FileName=sys.argv[1]

Data = fits.open(FileName,memmap=True)

print Data[1].header[20]
tbdata = Data[1].data
feh = tbdata.field("FEH_ADOP")
dist = tbdata.field("DIST_ADOP")
v = tbdata.field("RV_ADOP")
Data.close()

inx = ((feh > -9999) & (dist > -9999) & (v > -9999))
feh = feh[inx)]
dist = dist[inx]
v = v[inx]

import matplotlib.pyplot as plt 

fig,ax = plt.subplots(3,1,figsize=(10,10))
ax[0].hist(feh,40)
ax[0].set_xlim(-4,1)
ax[0].set_xlabel('[FE/H]',fontsize=20)
ax[1].hist(dist,800)
ax[1].set_xlim(0,50)
ax[1].set_xlabel('Distance (kpc =??)',fontsize=20)
ax[2].hist(v,50)
ax[2].set_xlim(-500,500)
ax[2].set_xlabel('V (km/s)',fontsize=20)
fig.subplots_adjust(hspace=0.3)



#print fits[1].data["FEH_ADOP",0]
#fits[1].header["FEH_ADOP","DIST_ADOP","RV_ADOP"]


