##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
cs=pd.read_csv('tbl0.tsv', delimiter='\t', encoding='utf-8')

a=cs.groupby(['_c1']).max()
print(a['_c2'])
