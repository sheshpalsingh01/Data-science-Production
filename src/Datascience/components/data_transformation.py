import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.Datascience.entity.config_entity import DataTransformationConfig
from src.Datascience.utils.common import logger

class DataTransformation:
    def __init__(
                self,
                config: DataTransformationConfig,
            ):
            self.config = config

        ## Note You can add different data transformation techniques such as Scaler PCA and all
        # you can perform EDA

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        #split the data into training and test sets (.75,0.25)
        train,test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index = False)

        logger.info("splitting data into trainin and testing sets")
        logger.info(f"Training data shape : {train.shape}")
        logger.info(f"Test data shape : {test.shape}")

        print(train.shape)
        print(test.shape)