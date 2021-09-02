from utils import *
import config
import pickle

#### ******************************************** ####
def inference(test_data):
    loaded_model = pickle.load(open('fall_model', 'rb'))
    with open(test_data) as f:
        lines = f.readlines()
    lines = lines[16:]
    data = []
    for line in lines:
        data.append(line.strip().split(','))

    # convert the txt file to dataframe
    df_data = pd.DataFrame(data)
    df_data.columns = ['timestamp', 'acc_x', 'acc_y', 'acc_z']
    df_data = df_data.apply(pd.to_numeric)

    # set index to start from 1
    df_data_set = set_index([df_data])
    # find windows over threshold
    over_ths_test = threshold_detect(config.threshold, df_data_set, config.w_t * config.Fs)
    if len(over_ths_test[0]) == 0:
        return False

    # Extract features of over_threshold windows
    df_data_feat = feature_extract(over_ths_test)

    if 'y' in loaded_model.predict(df_data_feat.dropna()):
        return True
    else:
        return False
