from src.Datascience import logger
from src.Datascience.config.configuration import ConfigurationManager
from src.Datascience.components.model_evaluation import ModelEvaluation
from pathlib import Path

STAGE_NAME ="model_evaluation_stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            logger.error(f"Error in model evaluation pipeline: {e}")
            raise e

if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>Started {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
        pipeline = ModelEvaluationPipeline()
        pipeline.initiate_model_evaluation()
        logger.info(f">>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.error(f">>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
        raise e