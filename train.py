import pandas as pd
import numpy as np
import fnmatch
from zipfile import ZipFile, Path
import glob
import os
from utils import *
import config
from sklearn.model_selection import  train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle

#### ******************************************** ####
#### Get data and save it into a list od dataframes ####
list_of_folders = os.listdir('dataset/Annotated Data')
dataframes_list = []
for i in range(len(list_of_folders)):
    path = 'dataset/Annotated Data/'+list_of_folders[i]
    temp_df = pd.concat(map(pd.read_csv, glob.glob(path +'/'+ '*.csv')), axis = 0, join = 'inner')
    dataframes_list.append(temp_df)

#### ******************************************** ####
# set index to start from 1
df_list = set_index(dataframes_list)

# find windows that have magnitude of accelerations across three dimensions > threshold
over_ths = threshold_detect(config.threshold, df_list, config.w_t * config.Fs)

# Extract features of over_threshold windows
df_feat = feature_extract(over_ths)
df_feat['label'] = ['y' if 'FOL' in df['label'].values or 'FKL' in df['label'].values or 'BSC' in df['label'].values or 'SDL' in df['label'].values\
                    else 'n' for df in over_ths]

#### ******************************************** ####
#### train data ####
data = df_feat.dropna()[['mean', 'max', 'min', 'range', 'std', 'SMA', 'rms']]
y = df_feat.dropna()['label']
# split test and train data
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2, random_state = 0)
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

# save the model
pickle.dump(clf, open('fall_model', 'wb'))