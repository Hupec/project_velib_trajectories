import os
import random
import pandas
from pyensae.datasource import download_data
from manydataapi.velib import DataCollectJCDecaux as DataVelibCollect
from pyquickhelper.loghelper import str2datetime
import matplotlib.pyplot as plt
import numpy as np
from Data_ import Data_
from Trajectories import Trajectories

class Main:
    
    
    def main(self):
        if __name__ == "__main__":  # on construit le chemin des fichiers avec des commandes systèmes
         dest = "velib_trajectories_project"
         if not os.path.exists(dest):
             os.makedirs(dest)
        data = Data_()
        data.getdata_(dest)

        # importation des données afin de pouvoir les utiliser
        jeu = os.path.join(dest, "besancon.df.txt")
        jeu = os.path.join(dest, "out_simul_bike_nb1_sp10_data.txt")
        df = pandas.read_csv(jeu, sep="\t", encoding="utf8")
        # conversion des dates
        df["collect_date"] = df.apply(
            lambda r: str2datetime(r["collect_date"]), axis=1)
        path = jeu.replace("_data.", "_path.")
        if path != jeu and os.path.exists(path):
            dfp = pandas.read_csv(path, sep="\t")
            dfp = dfp[dfp["beginend"] == "end"]
            #creaction de trajectories
            traject = Trajectories()
            # print(traject.velocitymoy(dfp))
            # print(traject.distancemoy(dfp))
            #print(traject.distance(dfp))
            #print(traject.time(dfp))
            x,y = [np.array(list(traject.distance(dfp).values())).astype(float),np.array(list(traject.time(dfp).values())).astype(float)]
            #print(x)
            #print(y)
            plt.plot(x,y)
            
            print(traject.velocity(dfp))
            
                    
      
        
         
lunch = Main()
lunch.main()
