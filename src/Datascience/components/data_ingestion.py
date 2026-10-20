import os
import urllib.request as request
import zipfile
from src.Datascience import logger
from src.Datascience.entity.config_entity import DataIngestionConfig

# update the data ingestion component


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # downloading the data
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_url, filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info:\n{header}")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        """
        Zip_file_path: str
        Extract the zip file into the directory
        function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
