import pandas as pd
import numpy as np
import os
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav
import pickle

label = -1;
result = [];

knn = pickle.load(open('knn.sav', 'rb'))

for subdir, dirs, files in os.walk('tests'):

    label=label+1;

    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav"):

            command = subdir.replace('data\\', '')
            line = [label, command]

            (rate, sig) = wav.read(filepath)
            mfcc_feat = mfcc(sig, rate)
            d_mfcc_feat = delta(mfcc_feat, 2)
            fbank_feat = logfbank(sig, rate)

            features = fbank_feat[37, :]
            line.extend(features)

            result.append(line)


result = pd.DataFrame(result, columns=['label','command','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','f22','f23','f24','f25','f26'])


from sklearn.neighbors import KNeighborsClassifier

data = result

feature_names = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','f22','f23','f24','f25','f26']

X = data[feature_names]

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X)

y_pred = knn.predict(X_train)


i=-1;
for subdir, dirs, files in os.walk('test_dataK'):
    for file in files:
        i+=1;
        print("For:\t", file , "\t predicted:\t" , y_pred[i] )
