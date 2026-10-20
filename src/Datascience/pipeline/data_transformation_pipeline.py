from src.Datascience import logger
from src.Datascience.config.configuration import ConfigurationManager
from src.Datascience.components.data_transformation import DataTransformation
from pathlib import Path

STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt")) as f:
                content = f.read().split(" ")[-1]

                if content == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(
                        config=data_transformation_config
                    )
                    data_transformation.train_test_splitting()
                    logger.info("Data Transformation step completed successfully")

                else:
                    logger.error("Data Transformation step failed")
                    raise Exception("Data Transformation step failed")
        except Exception as e:
            logger.error(
                f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<"
            )
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
        pipeline = DataTransformationTrainingPipeline()
        pipeline.initiate_data_transformation()
        logger.info(f">>>>>>>>>>>>>>>>>>Completed {STAGE_NAME}<<<<<<<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.error(
            f">>>>>>>>>>>>>>>>>>Error in {STAGE_NAME}: {e}<<<<<<<<<<<<<<<<<<<<<<<"
        )
        raise e
