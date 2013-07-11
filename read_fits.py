import sys
from astropy.io import fits
import numpy as np

class Read_fits():
    FileName=''
    col_names=[]
    data_out=np.array([])

    def __init__(self,FileName='',col_names=''):
        self.FileName=FileName
        self.col_names=col_names

    def read_data(self):
        Data = fits.open(self.FileName,memmap=True)
        tbdata = Data[1].data
        i=0
        good=np.array([])

        for name in col_names:
            col=np.array(tbdata.field(self.col_names[i]))
            temp_good=np.array(col>-9999)
            good=good&temp_good
            self.data_out=np.vstack((self.data_out,col))

        Data.close()

        return self.data_out

    def read_data(FileName,col_names):
        Data = fits.open(FileName,memmap=True)
        tbdata = Data[1].data
        data_out=[]
        good=np.array([])
        for name in col_names:
            col=np.array(tbdata.field(name))
            temp_good=np.array(col>-9999)
            self.data_out=np.vstack((self.data_out,col))
            good=good&temp_good

        Data.close()

        return data_out


dat1=Read_fits(FileName="/home/sukh/sci_coder/ssppOut-dr9.fits",col_names=['FEH_ADOP'])
dat1.read_data()
