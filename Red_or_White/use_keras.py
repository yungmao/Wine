from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from Red_or_White.dataService import dataframe,redwine,whitewine

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

classifications = 2 #Białe i czerwone
df = dataframe()
df['Gatunek'] = np.where(df['Gatunek'] == 'Czerwone wino', 1, df['Gatunek']) #Klasa 1 - wino czerwone
df['Gatunek'] = np.where(df['Gatunek'] == 'Białe wino', 0, df['Gatunek']) #Klasa 0 - wino białe

X = df[df.columns[:-1]]
X= X.to_numpy()
Y = df['Gatunek']
Y = Y.to_numpy()
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.7, random_state=23)
y_train = keras.utils.to_categorical(y_train, classifications)
y_test = keras.utils.to_categorical(y_test, classifications)


model = Sequential()
model.add(Dense(8, input_dim=11, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(classifications, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer="adam", metrics=['binary_accuracy', 'categorical_accuracy'])
model.fit(x_train, y_train, batch_size=15, epochs=200, validation_data=(x_test, y_test))

redtest=redwine()
redtest = redtest[redtest.columns[:-1]]
redprediction = model.predict(redtest)
redprediction = np.array(redprediction)
sum = 0
for i in redprediction:
    if i[0]>i[1]:
        sum+=1
print(100-sum/(redprediction.size/2))

whitetest=whitewine()
whitetest = whitetest[whitetest.columns[:-1]]
whiteprediction = model.predict(whitetest)
whiteprediction = np.array(whiteprediction)
sum = 0
for i in whiteprediction:
    if i[0]<i[1]:
        sum+=1
print(100-sum/(whiteprediction.size/2))