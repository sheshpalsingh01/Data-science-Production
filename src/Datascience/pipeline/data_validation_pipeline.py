from src.Datascience.config.configuration import ConfigurationManager
from src.Datascience import logger
from src.Datascience.entity.config_entity import dataValidationConfig
from src.Datascience.components.data_validation import DataValidation


STAGE_NAME =" Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validation_all_columns()

if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
        pipeline = DataValidationTrainingPipeline()
        pipeline.initiate_data_validation()
        logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.error(f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
        raise e
