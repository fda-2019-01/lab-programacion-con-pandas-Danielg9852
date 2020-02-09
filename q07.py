##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

import pandas as pd
cs=pd.read_csv('tbl0.tsv', delimiter='\t', encoding='utf-8')

cs['suma']=cs['_c0']+cs['_c2']

print(cs)