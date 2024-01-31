from DogvsCatClassifier.constants import *


from DogvsCatClassifier.utils.common import read_yaml, create_directories, save_json
from DogvsCatClassifier.entity.config_entity import DataIngestionConfig,ModelTrainerConfig,ModelEvaluationConfig
import os


class ConfigurationManager:
    def __init__(
         self,
         config_filepath = CONFIG_FILE_PATH,
         params_filepath = PARAMS_FILE_PATH):

         self.config =  read_yaml(config_filepath)
         self.params =  read_yaml(params_filepath)   
         create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_destination=config.source_destination,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_model_trainer_config(self)-> ModelTrainerConfig:
         config =self.config.model_trainer
         params =self.params

         create_directories([config.root_dir])

         model_trainer_config = ModelTrainerConfig(
               root_dir=config.root_dir,
               train_data_path=config.train_data_path,
               test_data_path=config.test_data_path,
               model_name=config.model_name,
               batch_size=params.batch_size,
               image_width=params.image_width,
               image_height=params.image_height,
               inner_activation =params.inner_activation,
               epoch_val=params.epoch_val,
               loss_func=params.loss_func,
               optimizer=params.optimizer,
               neurons_no=params.neurons_no

          )

         return model_trainer_config
        
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:

        config =self.config.model_evaluation
        params =self.params

        create_directories([config.root_dir])
        eval_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            
            mlflow_uri=config.mlflow_uri,
            all_params=self.params,
            test_data_path=config.test_data_path,
            batch_size=params.batch_size,
            image_width=params.image_width,
            image_height=params.image_height,
            metric_file_name=config.metric_file_name,
            model_path= config.model_path
            
            
            

        )
        return eval_config