
import pandas as pd
import numpy as np
vdata=pd.read_csv("D:/data/2021VAERSDATA.csv",encoding="iso-8859-1")
vdata.sample(frac=0.9).to_csv("vdata_sample.csv",index=False)
print(vdata.sample)
vax=pd.read_csv("D:/data/2021VAERSVAX.csv",encoding="iso-8859-1")
vax.sample(frac=0.9).to_csv("vax_sample.csv",index=False)
print(vax.sample)
