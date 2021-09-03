import pandas as pd
import numpy as np

def set_index(dataframes_list):
    df_list = []
    for df in dataframes_list:
        new_index = pd.RangeIndex(1, len(df) + 1)
        df_list.append(df.set_index(new_index))
    return df_list


def threshold_detect(threshold, df_list, w):
    index = []
    for df in df_list:
        df['sum'] = np.sqrt(df['acc_x'] ** 2 + df['acc_y'] ** 2 + df['acc_z'] ** 2)
        cont = True
        j = 1
        while cont:
            if df.loc[j, 'sum'] > threshold:
                if j + w - 1 <= len(df):
                    cont = True
                    index.append(df.loc[j: j + w - 1])
                    j = j + w
                else:
                    index.append(df.loc[j: ])
                    cont = False
            elif j + 1 < len(df):
                j = j + 1
            else:
                cont = False
    return index


def feature_extract(over_ths_list):
    df_feat = pd.DataFrame()
    df_feat['mean'] = [df['sum'].mean() for df in over_ths_list]
    df_feat['max'] = [df['sum'].max() for df in over_ths_list]
    df_feat['min'] = [df['sum'].min() for df in over_ths_list]
    df_feat['range'] = [df['sum'].max() - df['sum'].min() for df in over_ths_list]
    df_feat['std'] = [df['sum'].std() for df in over_ths_list]
    df_feat['SMA'] = [(abs(df['acc_x']) + abs(df['acc_y']) + abs(df['acc_z'])).sum() for df in over_ths_list]
    df_feat['rms'] = [np.sqrt(((df['acc_x'] ** 2) + (df['acc_y'] ** 2) + (df['acc_z'] ** 2)).sum()) for df in
                      over_ths_list]
    return df_feat