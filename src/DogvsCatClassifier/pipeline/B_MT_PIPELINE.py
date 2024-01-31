from DogvsCatClassifier.config.configuration import ConfigurationManager
from DogvsCatClassifier.components.ModelTrainer import ModelTrainer
from DogvsCatClassifier import logger


STAGE_NAME = "Model trainer stage"


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config =ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        train_ds=model_trainer.set_train_data()
        model = model_trainer.model_design()
        model_trainer.model_compile(train_ds,model)

if __name__ =="__main__":
    try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
    except Exception as e:
        logger.exception(e)
        raise e