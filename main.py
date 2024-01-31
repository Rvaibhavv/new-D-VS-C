from DogvsCatClassifier.pipeline.A_DE_PIPELINE import DataIngestionTrainingPipeline
from DogvsCatClassifier.pipeline.B_MT_PIPELINE import ModelTrainerPipeline
from DogvsCatClassifier.pipeline.C_ME_PIPELINE import ModelEvaluationPipeline
from DogvsCatClassifier import logger

STAGE_NAME = "Data ingestion stage"

try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model trainer stage"

try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model evaluation stage"
try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
except Exception as e:
        logger.exception(e)
        raise e