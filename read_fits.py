import sys
from astropy.io import fits

class Read_fits():
    FileName=''
    col_names=[]
    data_out=[]

    def __init__(self,FileName='',col_names=''):
        self.FileName=FileName
        self.col_names=col_names

    def read_data(self):
        Data = fits.open(self.FileName,memmap=True)
        tbdata = Data[1].data
        for i in range(len(self.col_names)):
            col=tbdata.field(self.col_names[i])
            temp_good=col>-9999
            if i==0 :
                self.data_out=col
                good=temp_good
            else:
                temp=(self.data_out,col)
                self.data_out=np.column_stack(temp)
                good= good & temp_good

            Data.close()

            return data_out

    def read_data(FileName,col_names):
        Data = fits.open(FileName,memmap=True)
        tbdata = Data[1].data
        data_out=[]
        for i in range(len(col_names)):
            col=tbdata.field(col_names[i])
            temp_good=col>-9999
            if i==0 :
                data_out=col
                good=temp_good
            else:
                temp=(self.data_out,col)
                self.data_out=np.column_stack(temp)
                good= good & temp_good

            Data.close()

            return data_out


dat1=Read_fits(FileName="/home/sukh/sci_coder/ssppOut-dr9.fits",col_names=['FEH_ADOP'])
dat1.read_data()
