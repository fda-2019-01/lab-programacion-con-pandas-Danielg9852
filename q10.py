##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
cs=pd.read_csv('tbl1.tsv', delimiter='\t', encoding='utf-8')


b=cs.groupby('_c0')['_c4'].apply(list)

b=pd.DataFrame(b).reset_index()
b=b.rename(columns={'_c4':'lista'})
j=0

for i in b['lista']:
    i.sort()
    s=",".join(map(str, i))
    
    b['lista'][j]=s
    j=j+1

print(b)

