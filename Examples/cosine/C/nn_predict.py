from keras.models import model_from_json
import numpy as np

json_file = open('cos.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights('cos.h5')

prediction = loaded_model.predict(np.array([[1, 0.5]]))

print(prediction)
