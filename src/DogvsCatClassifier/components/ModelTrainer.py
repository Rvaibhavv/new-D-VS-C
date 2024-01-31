import tensorflow as tf
from tensorflow import keras
from keras import models,layers
import os
from DogvsCatClassifier.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config

    def set_train_data(self):
        train_ds = keras.utils.image_dataset_from_directory(
            directory = self.config.train_data_path,
            labels='inferred',
            label_mode='int',
            batch_size=self.config.batch_size,
            image_size=(self.config.image_width,self.config.image_height),
            
            
        )
        

        def process(image,label):
            image = tf.cast(image/255. , tf.float32)
            return image,label
        
        train_ds = train_ds.map(process)
        

        return train_ds
        
        
    def model_design(self):
        cnnmodel = models.Sequential([
            layers.Conv2D(filters=32,kernel_size=(3,3),padding='valid',activation=self.config.inner_activation,input_shape=(self.config.image_width,self.config.image_height,3)),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'),
            
            layers.Conv2D(filters=64,kernel_size=(3,3),padding='valid',activation=self.config.inner_activation),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'),
            
            layers.Conv2D(filters=128,kernel_size=(3,3),padding='valid',activation=self.config.inner_activation),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size=(2,2),strides=2,padding='valid'),
        
            layers.Flatten(),
            layers.Dense(self.config.neurons_no[0],activation=self.config.inner_activation),
            layers.Dropout(0.1),
            layers.Dense(self.config.neurons_no[1],activation=self.config.inner_activation),
            layers.Dropout(0.1),
            layers.Dense(self.config.neurons_no[7],activation='sigmoid')

            ])
        
        cnnmodel.summary()
        return cnnmodel


    def model_compile(self,train_ds,model):
        model.compile(
            optimizer=self.config.optimizer,
            loss=self.config.loss_func,
            metrics=['accuracy']


        )
        model.fit(train_ds,epochs=self.config.epoch_val)

        
        models.save_model(model, os.path.join(self.config.root_dir,self.config.model_name))
        
        


    

    
    
    

    

        

