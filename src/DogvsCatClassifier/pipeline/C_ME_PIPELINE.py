from DogvsCatClassifier.config.configuration import ConfigurationManager
from DogvsCatClassifier.components.ModelEvaluation import ModelEvaluation
from DogvsCatClassifier import logger


STAGE_NAME = "Model evaluation stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(model_eval_config)
        validation_ds = model_evaluation.set_and_test()
        loss,accuracy = model_evaluation.evaluate(validation_ds)
        model_evaluation.mlflowlogin(loss,accuracy)

if __name__ =="__main__":
    try:
        logger.info(f".....stage {STAGE_NAME} started ....")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"..... stage {STAGE_NAME} completed .....")
    except Exception as e:
        logger.exception(e)
        raise e