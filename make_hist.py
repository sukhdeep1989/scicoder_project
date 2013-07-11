import matplotlib.pyplot as plt 
import numpy as np
#import sys


def make_hist(input_data):
	hist_num = len(input_data)
	fig,ax = plt.subplots(hist_num,1,figsize=(10,10))

	for i in range(hist_num):
		xmin[i] = min(input_data[i,:])
		xmax[i] = max(input_data[i,:])
		ax[i].hist(input_data[i,:],40)
		ax[i].set_xlim(xmin[i],xmax[i])
		ax[i].set_xlabel(label,fontsize=20)
		fig.subplots_adjust(hspace=0.3)
	print 'done'	

