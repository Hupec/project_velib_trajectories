import os
import random
import pandas
from pyensae.datasource import download_data
from manydataapi.velib import DataCollectJCDecaux as DataVelibCollect
from pyquickhelper.loghelper import str2datetime
import matplotlib.pyplot as plt

class Data_:
    
    # contient uniquement une fonction pour récuperer les données du fichier velib disponible sur 
    
    def getdata_(self,whereto):
        download_data('velib_synthetique.zip', website='xdtd', whereTo=whereto)
        download_data('besancon.df.txt.zip', website='xdtd', whereTo=whereto)
