##
## Imprima la cantidad de registros por cada letra
## de la columna _c1 de la tabla tbl0
##
import pandas as pd
cs=pd.read_csv('tbl0.tsv', delimiter='\t', encoding='utf-8')

b=cs.groupby(['_c1']).count()
print(b['_c0'])
