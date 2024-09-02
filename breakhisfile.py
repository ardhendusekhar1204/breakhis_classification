from PIL import Image
import torch
import pandas as pd
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
def label_tag(img_label):

    ref={'benign':0,'malignant':1}

class BreakhisDataset:
    def __init__(self, transforms=transforms.ToTensor(),path='/home/ardhendu/Desktop/breakhis_classification/data-train.csv'):
        #store the inputs and outputs
        self.path=path
        self.transforms=transforms
        self.df=pd.read_csv(self.path)

    def __len__(self):
        return len(self.df)

    #get a row at an index
    def __getitem__(self,idx):
        one_row=self.df.loc[idx,'path']
        img=Image.open(one_row)
        label=torch.tensor((self.df.loc[idx,'label']))  #use label_tag(self.df.loc[idx,'label']) if your csv is not having numeric for class
        if self.transforms is not None:
            img=self.transforms(img)
        return img,label
        #return(img)
