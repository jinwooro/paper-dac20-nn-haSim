from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import pandas as pd
import numpy as np


data = pd.read_csv('./train_data_large.csv')
features = data[['cstate','x_out']]
label =  data[['next_state']]

model = Sequential()
model.add(Dense(10, input_dim=2, kernel_initializer='random_uniform', activation='tanh'))
model.add(Dense(5, kernel_initializer='random_uniform', activation='tanh'))
model.add(Dense(1, kernel_initializer='random_uniform', activation='linear'))
model.summary()

model.compile(loss='mae', optimizer='adam', metrics=['mae', 'mse'])

model.fit(features, label, epochs=1500, batch_size=100,  verbose=1)

model.save('cos.h5')

test_result = model.predict(np.array([[0, 1.0]]))
print(test_result)

model_json = model.to_json()
with open("cos.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("cos_weights.h5")
