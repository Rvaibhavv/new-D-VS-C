from DogvsCatClassifier.entity.config_entity import DataIngestionConfig
import shutil
import os
import zipfile

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def load_file(self):
        try:
            dataset_loc = self.config.source_destination
            zip_download_dir = self.config.local_data_file
            shutil.copy(dataset_loc,zip_download_dir)
        except Exception as e:
            raise e

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

