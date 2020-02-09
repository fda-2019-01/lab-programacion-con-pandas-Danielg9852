##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
cs=pd.read_csv('tbl2.tsv', delimiter='\t')
aa=[]
for i in cs['_c5b']:
    aa.append(str(i))

cs['a']=aa
cs['lista']=cs['_c5a']+':'+cs['a']

b=cs.groupby('_c0')['lista'].apply(list)

b=pd.DataFrame(b).reset_index()


j=0
for i in b['lista']:
    i.sort()
    s=",".join(i)
    
    b['lista'].loc[j]=s
    j=j+1

print(b)
