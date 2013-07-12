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
	
	if RA is not None:
	
		RA_bottom = RA-width/2.
		RA_top = RA+width/2.
		DEC_bottom = DEC-height/2.
		DEC_top = DEC+height/2.
	
		idx = [i for i in (RA[i]<RA_top) & (RA[i]>RA_bottom) & (DEC[i]<DEC_top) & (DEC[i]>DEC_bottom)]
		
		return SPECOBJID[idx]	
	
	