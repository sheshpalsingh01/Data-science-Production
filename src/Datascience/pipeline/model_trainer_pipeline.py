from src.Datascience import logger
from src.Datascience.config.configuration import ConfigurationManager
from src.Datascience.components.model_trainer import ModelTrainer
from pathlib import Path

STAGE_NAME ="model_training_stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_training_config)
        model_trainer.train()

if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
        pipeline = ModelTrainingPipeline()
        pipeline.initiate_model_training()
        logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.error(f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
        raise e
    