import read_fits
from urlgrabber import urlgrab
import urllib2
import json
import numpy as np
from scipy import interpolate

# grabs spectrum from sdss and reads into a variable spec_data
#usage:
#spec1=Spectrum(plate=276,fiber=627,mjd=51909)  intialize class
#spec1.fetch_data_self() fetch data from sdss (not downloaded)
#spec1.download_data_self() download data from sdss  
#spec1.read_data_self()   reads spectrum from a downloaded file

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
        Url='http://api.sdss3.org/spectrum?plate='+str(plate)+'&fiber='+str(fiber)+'&mjd='+str(mjd)+'&format=json'
        urlgrab(Url,filename=dat_file)

    def fetch_data_self(self):
        Url='http://api.sdss3.org/spectrum?plate='+str(self.plate)+'&fiber='+str(self.fiber)+'&mjd='+str(self.mjd)+'&format=json'
        url_op=urllib2.urlopen(Url)
#        specd=json.load(url_op)
        self.spec_data=json.load(url_op)


    def download_data_self(self):
        Url='http://api.sdss3.org/spectrum?plate='+str(self.plate)+'&fiber='+str(self.fiber)+'&mjd='+str(self.mjd)
        urlgrab(Url,filename=self.dat_file)                                                                                           

        
    def read_data_self(self):
        read_file=read_fits.Read_fits(FileName=self.dat_file,col_names=self.col_names)
        self.spec_data=read_file.read_data()
        
        
    def read_data(dat_file,col_names):
        read_file=read_fits.Read_fits(FileName=dat_file,col_names=col_names)
        spec_data=read_file.read_data()
        return spec_data

    
    def plot_spec(self,label):
        fig,ax = plt.subplots(1,1,figsize=(20,5))
        xmin = min(self.spec_data['wavelengths'])
        xmax = max(self.spec_data['wavelengths'])
        ax.set_xlim(xmin,xmax)
#        ax.set_title(title)
        ax.set_xlabel("Wavelength",fontsize=20)
        ax.set_ylabel("Flux",fontsize=20)
        ax.plot(self.spec_data['wavelengths'],self.spec_data['flux'],label=label)
        ax.legend()
        

    def spec_coadd(self,spec1): #spec1 is list of spectra to co add
        self.spec_data=spec1[0].spec_data.copy()
        Flux_all=np.zeros(np.array(spec1[0].spec_data['flux']).shape)

        for i in range (len(spec1)):
           Flux_all=np.column_stack((Flux_all,np.array(spec1[i].spec_data['flux'])))
            
        Flux_all=np.delete(Flux_all,0,axis=-1)    
        self.spec_data['flux']=np.mean(Flux_all,axis=-1)

        
    def spec_interpolate(self,spec): #spec is spectrum to which self will be interpolated
        flux_new=interpolate.interp1d(np.array(self.spec_data['wavelengths']),np.array(self.spec_data['flux']),kind='linear',bounds_error=False)
        self.spec_data['wavelengths']=spec.spec_data['wavelengths']
        self.spec_data['flux']=flux_new(spec.spec_data['wavelengths'])
        

#np.sort(spec1.spec_data.keys())

