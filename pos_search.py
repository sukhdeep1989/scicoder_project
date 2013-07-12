import astropy.units as u

def pos_search(RA=None, DEC=None, width=None, height=None):
	if not hasattr(RA, 'units'):
		raise TypeError('The RA doesn\'t have units!')
	if not hasattr(DEC, 'units'):
		raise TypeError('The DEC doesn\'t have units!')
	if not hasattr(width, 'units'):
		raise TypeError('The width doesn\'t have units!')
	if not hasattr(height, 'units'):
		raise TypeError('The height doesn\'t have units!')
	
	if width is not None:
		w = float(width)*u.Prad
	else:
		print "You did not enter a box width"	
	
	if height is not None:
		h = float(height)*u.Prad
	else:
		print "You did not enter a box height"
	
	if RA is not None:	
		RA = float(RA)*u.Prad
	else:
		print "You did not enter RA"
	
	if DEC is not None:	
		DEC = float(DEC)*u.Prad
	else:
		print "You did not enter DEC"
		
	data = Read_fits(ssppOut-dr9.fits, col_names=['RA', 'DEC', 'SPECOBJID'])
	
	RA_dat = data[0]
	DEC_dat = data[1]
	ID_dat = data[2]	
	RA_bottom = RA-w/2.
	RA_top = RA+w/2.
	DEC_bottom = DEC-h/2.
	DEC_top = DEC+h/2.
	
		idx = [i for i in (RA_dat[i]<RA_top) & (RA_dat[i]>RA_bottom) & (DEC_dat[i]<DEC_top) & (DEC_dat[i]>DEC_bottom)]
		
		in_box = ID_dat[idx]
		
		return in_box	
	
	