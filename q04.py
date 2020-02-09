##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
cs=pd.read_csv('tbl1.tsv', delimiter='\t', encoding='utf-8')
cs.sort_values(by=['_c4'], inplace=True)
aa = cs.apply(lambda x: x.str.upper() if x.dtype == "object" else x) 

a=aa['_c4'].unique()
c=[]
for i in a:
    c.append(i)

print(c)

