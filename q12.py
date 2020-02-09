##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas as pd
c0=pd.read_csv('tbl0.tsv', delimiter='\t')
c2=pd.read_csv('tbl2.tsv', delimiter='\t')

a2=c2.groupby(['_c0']).sum()

j=0
for i in a2.index:
    a2['_c1']=c0.loc[a2.index]['_c1']
    
    j=j+1
    
a3=a2.groupby('_c1').sum()
print(a3['_c5b'])