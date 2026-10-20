from src.Datascience import logger
from src.Datascience.pipeline.data_ingestion_pipeline import DataIngestiontrainingPipeline





STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    pipeline = DataIngestiontrainingPipeline()
    pipeline.initiate_data_ingestion()
    logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.error(f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<")
    raise e