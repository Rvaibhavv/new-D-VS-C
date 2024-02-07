import numpy as np
from tensorflow import keras
from keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
        def __init__(self):
            pass

        def predict(self,filename):

            model =load_model(os.path.join("artifacts/model_trainer","model.h5"))
            try:
                imagename = filename
                
                test_image = image.load_img(imagename, target_size = (256,256))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis = 0)
                result = model.predict(test_image)
                print(result)
                if result == 0:
                    prediction = 'Cat'
                    return prediction
                else:
                    prediction = 'Dog'
                    return prediction
            except Exception as e:
                 print("error loading image:",e)
                     