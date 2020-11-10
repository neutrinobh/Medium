import pandas as pd
import glob

path=r'/home/Documents/Project/data/'
df=pd.concat([pd.read_csv(f, delimiter=r"\s+", names=['W(MeV)','Re','Im']) 
              for f in sorted(glob.glob(path+'*.dat'))], axis=1,sort=False)
