import read_fits
from urlgrabber import urlgrab

# grabs spectrum from sdss and reads into a variable spec_data
#usage:
#spec1=Spectrum(plate=276,fiber=627,mjd=51909)  intialize class
#spec1.fetch_data_self() fetch data from sdss
#spec1.read_data()   reads spectrum from downloaded file

class Spectrum():
    dat_file=''
    plate=0
    fiber=0
    mjd=0
    spec_data=[]
    col_names=[]

    def __init__(self,plate=0,fiber=0,mjd=0):
        self.plate=plate
        self.fiber=fiber
        self.mjd=mjd
        self.dat_file="spectrum_"+str(plate)+"_"+str(fiber)+"_"+str(mjd)+".fits"
        self.col_names=['loglam','flux']

    def fetch_data(plate,fiber,mjd,dat_file):
        Url='http://api.sdss3.org/spectrum?plate='+str(plate)+'&fiber='+str(fiber)+'&mjd='+str(mjd)
        urlgrab(Url,filename=out_file)

    def fetch_data_self(self):
        Url='http://api.sdss3.org/spectrum?plate='+str(self.plate)+'&fiber='+str(self.fiber)+'&mjd='+str(self.mjd)
        urlgrab(Url,filename=self.dat_file)

        
    def read_data(self):
        read_file=read_fits.Read_fits(FileName=self.dat_file,col_names=self.col_names)
        self.spec_data=read_file.read_data()
        
        

    
    
