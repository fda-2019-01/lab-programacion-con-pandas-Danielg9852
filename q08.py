##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd
cs=pd.read_csv('tbl0.tsv', delimiter='\t', encoding='utf-8')
a=[]
for i in cs['_c3']:
    a.append(i[0:4])
cs['ano']=a

print(cs)