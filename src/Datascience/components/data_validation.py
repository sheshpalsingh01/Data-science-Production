import os
import pandas as pd
import urllib.request as request
from src.Datascience import logger
from src.Datascience.entity.config_entity import dataValidationConfig



class DataValidation:
    def __init__(self,config:dataValidationConfig):
        self.config = config

    def validation_all_columns(self)->bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols =list(data.columns)

            all_schema = self.config.all_schema.keys()


            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status : {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Data Status : {validation_status}")

            return validation_status
        except Exception as e:
            raise e
    # # Check the datatype
    # def check_data_type(self):
    #     try:
    #         data = pd.read_csv(self.config.unzip_data_dir)
    #         all_column_type

