import pandas as pd
import numpy as np
import os 
import glob 
import re
import xml.etree.ElementTree as et 
import matplotlib.pyplot as plt




class RNASeq :
    def __init__(self, path=''):
        self.__data_matrix = []
        if(path!=''):
            pdList = []
            for fname in glob.glob(path+"/*.txt"):
                df  =  pd.read_table(fname)
                sample_name = re.search("GSM\d+", fname).group()

                df.rename(index= df["gene/TE"], inplace = True)
                df.drop(columns=df.columns[0], axis=1, inplace=True)
                df.rename(columns={ df.columns[0]:sample_name}, inplace = True)
                pdList.append(df)
    
            self.data_matrix = pd.concat(pdList, axis=1)
            self.data_matrix = self.data_matrix.transpose()
            
            
    def get_value(self, gene, sample):
        return self.data_matrix.loc[sample][gene]
    
    def calculate_mean(self):
        mean = self.data_matrix.mean(axis = 0)
        mean = mean[(mean != 0)]
        return mean
    
    def calculate_median(self):
        med = self.data_matrix.median(axis = 0)
        med = med[med != 0]
        return med
    
    def calculate_std(self):
        std = self.data_matrix.std(axis = 0)
        std = std[std != 0]
        return std
    
    def calculate_cv(self):
        cv = self.calculate_std().divide(self.calculate_mean())
        cv_sorted = cv.dropna().sort_values(ascending=False)
        return cv_sorted
    
    def print_hist(self):
        ax = plt.figure()
        cv = self.calculate_cv
        t = [i for i in range(len(cv))]
        ax.plot(t, cv)
        ax.savefig("Histogramme.png")
        
        
        



class annotation :
    def __init__(self, xmlpath=''):
        self.data_annotation = pd.DataFrame(columns = ['Sample_id', 'Cns_subregion'])
        if(xmlpath != ''):
            xtree = et.parse(xmlpath) # create a variable containing the xml in a tree shape
            xroot = xtree.getroot() # get the root of the tree to start the exploration of the tree/xml
            # for each element named "sample" that can be found from the root
            for child in xroot.iter("{http://www.ncbi.nlm.nih.gov/geo/info/MINiML}Sample"):
                temp_sample_id = child.attrib['iid'] # the attribut of this node contains the sample id ()
                
                # for each element named "Characteristics" that can be found from the current sample
                for child2 in child.iter("{http://www.ncbi.nlm.nih.gov/geo/info/MINiML}Characteristics"):
                    if(child2.attrib["tag"] == "cns subregion"):
                        temp_cns_subregion = child2.text.replace('\n', '')
                              
                temp_df = pd.DataFrame({'Sample_id': [temp_sample_id], 'Cns_subregion': [temp_cns_subregion]})
                
            
                self.data_annotation = pd.concat([self.data_annotation, temp_df])
            
                
            self.data_annotation.set_index('Sample_id', inplace = True)
            
            
            
    
    
    def get_annotation(self, sampleid):
        return self.data_annotation.loc[sampleid]['Cns_subregion']

    def get_frame(self):
        return self.data_annotation 



