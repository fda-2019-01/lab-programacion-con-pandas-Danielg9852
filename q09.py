##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd
cs=pd.read_csv('tbl0.tsv', delimiter='\t', encoding='utf-8')


a=cs.groupby('_c1')['_c2'].apply(list)

a=pd.DataFrame(a).reset_index()
a=a.rename(columns={'_c2':'lista','_c1':'_c0' })
j=0
for i in a['lista']:
    i.sort()
    s=":".join(map(str, i))
    
    a['lista'][j]=s
    j=j+1


print(a)
