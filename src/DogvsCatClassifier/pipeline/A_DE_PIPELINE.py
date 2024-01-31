from DogvsCatClassifier.config.configuration import ConfigurationManager
from DogvsCatClassifier.components.DataIngestion import DataIngestion
from DogvsCatClassifier import logger



STAGE_NAME = "Data ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.load_file()
        data_ingestion.extract_zipfile()

if __name__ =="__main__":
    try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
    except Exception as e:
        logger.exception(e)
        raise e
