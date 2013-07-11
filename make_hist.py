import matplotlib.pyplot as plt 
import numpy as np
import sys


def make_hists(*args):
	
	hist_num = len(args)
	
	fig,ax = plt.subplots(hist_num,1,figsize=(10,10))
	
	for i in range(hist_num):
		ax[i].hist(feh,40)
		ax[i].set_xlim(-4,1)
		ax[i].set_xlabel('[FE/H]',fontsize=20)
	
		fig.subplots_adjust(hspace=0.3)
	
	

