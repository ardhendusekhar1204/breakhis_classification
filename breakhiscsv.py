import os
import pandas as pd
top='/home/Drive4/drive2/ardhendubapu/breakhis/'
data_record={'path':[],'slide_name':[],'label':[]}
for root, directories, files in os.walk(top, topdown=False):
    for name in files:
        data_record['slide_name'].append(name)
        data_record['path'].append(os.path.join(root,name))
        data_record['label'].append(root.split('/')[-1])
df=pd.DataFrame(data_record)
df.label[df.label=='benign']=0
df.label[df.label=='malignant']=1
df.to_csv('breakhis_data.csv',index=False)   
