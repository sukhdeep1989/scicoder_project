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
	
	data = Read_fits(ssppOut-dr9.fits, col_names=['RA', 'DEC', 'SPECOBJID'])
		RA_dat = data[0]
		DEC_dat = data[1]
		ID_dat = data[2]	
		RA_bottom = RA-width/2.
		RA_top = RA+width/2.
		DEC_bottom = DEC-height/2.
		DEC_top = DEC+height/2.
	
		idx = [i for i in (RA_dat[i]<RA_top) & (RA_dat[i]>RA_bottom) & (DEC_dat[i]<DEC_top) & (DEC_dat[i]>DEC_bottom)]
		
		return ID_dat[idx]	
	
	