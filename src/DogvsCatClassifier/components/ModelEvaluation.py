from tensorflow import keras
import tensorflow as tf
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from pathlib import Path
from DogvsCatClassifier.utils.common import save_json
from DogvsCatClassifier.mlfowconfig.mlflowsetup import mlflowset
import shutil

from DogvsCatClassifier.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    def load_pred(self):
        model =self.config.model_path
        model =tf.keras.models.load_model(model)
        return model

    
    def set_and_test(self):
        
        validation_ds =keras.utils.image_dataset_from_directory(
            directory = self.config.test_data_path,
            labels='inferred',
            label_mode='int',
            batch_size=self.config.batch_size,
            image_size=(self.config.image_width,self.config.image_height),

        )
        def process(image,label):
            image = tf.cast(image/255. , tf.float32)
            return image,label
        
        
        validation_ds=validation_ds.map(process)

        return  validation_ds
    
    def evaluate(self,validation_ds):

        model =self.load_pred()
        test_loss, test_accuracy = model.evaluate(validation_ds)
        print('Test accuracy:', test_accuracy)
        print('Test Loss',test_loss)
        score = {"loss": test_loss, "accuracy": test_accuracy}
        save_json(path=Path(self.config.metric_file_name), data=score)
        return test_loss,test_accuracy

    

    def mlflowlogin(self,loss,accuracy):
        # mlflowset()
        model =self.load_pred()
        
        

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run() :
            
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metrics(
                {"loss": loss, "accuracy": accuracy}
            )
            
            
            if tracking_url_type_store != "file":

                
                mlflow.keras.log_model(model, "model", registered_model_name="catvsdogpred")
            else:
                mlflow.keras.log_model(model, "model")
            

