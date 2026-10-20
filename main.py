from src.Datascience import logger
from src.Datascience.pipeline.data_ingestion_pipeline import DataIngestiontrainingPipeline
from src.Datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.Datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.Datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    pipeline = DataIngestiontrainingPipeline()
    pipeline.initiate_data_ingestion()
    logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.error(f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
    raise e


STAGE_NAME_1 =" Data Validation stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    pipeline = DataValidationTrainingPipeline()
    pipeline.initiate_data_validation()
    logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.error(f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
    raise e

STAGE_NAME ="Data Transformation"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.initiate_data_transformation()
    logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.error(f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    pipeline = ModelTrainingPipeline()
    pipeline.initiate_model_training()
    logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.error(f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
    raise e