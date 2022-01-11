from pyensae.datasource import download_data
from manydataapi.velib import DataCollectJCDecaux as DataVelibCollect
from pyquickhelper.loghelper import str2datetime
class Trajectories:
    
    #objet trajectoire qui permet de construire la trajectoire d'un vélib
    # à partir des données des fichiers fournis par ...
    # les fonctions distance, velocity & velocitymoy
    def __init__(self):
        pass
    
    
    
    def velocity(self,path):
        dist = self.distance(path)
        time = self.time(path)
        # d = []
        # t = []
        # v = []
        
        # for index in dist:
        #         d.append(dist[index])
        # for index in time:
        #         t.append(time[index])
        
        # for i in range(1,len(d)):
        #       print(d[i]/t[i])  
            
        # return v
        v = dict()
        for key,value in dist.items():
            v.update({key:value/time[key]})
        return v

    
    def time (self,path):
        path = path.copy()
        dic = {}
        for index,row in path.iterrows():
            if(row["hours"]>=0.0):
                dic.update({row["idvelo"]:row["hours"]})
        return dic
    
    def distance(self,path):
        path = path.copy()
        dic = {}
        for index,row in path.iterrows():
            if(row["dist"]>=0.0):
                dic.update({row["idvelo"]:row["dist"]})
        return dic
    
    def distancemoy(self,path):
        path = path.copy()
        path["dist"]= path.apply(
            lambda r: DataVelibCollect.distance_haversine(r["lat0"], r["lng0"],
                                                      r["lat1"], r["lng1"]),
        axis=1)
        distmoy = sum(path["dist"])/len(path)
        return distmoy
    
    def velocitymoy(self,path):
        #on copie le tableau afin de travailler dessus sans modifier le tableau d'origine
        path = path.copy()

        path["velocity"] = path["dist"] / path["hours"] # calcul de la vitesse 
                 #DataVelibCollect.distance_haversine est une fonction fournie par JCDEAUX
        # def distance_haversine(lat1, lng1, lat2, lng2):
        #     radius = 6371
        #     dlat = math.radians(lat2-lat1)
        #     dlon = math.radians(lon2-lon1)
        #     a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        #     * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        #     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        #     d = radius * c
        #     return d
        path["dist"]= path.apply(
            lambda r: DataVelibCollect.distance_haversine(r["lat0"], r["lng0"],
                                                      r["lat1"], r["lng1"]),
        axis=1) # apply permet d'appliquer la fonction lambda sur les colonnes "lat0","lng0","lat1" et "lng1"
        moy = sum(path["velocity"]) / len(path)
        return moy
         
        
        
