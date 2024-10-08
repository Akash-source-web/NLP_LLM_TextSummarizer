import os
import urllib.request as request
import zipfile
from TextSummarizerLLM.utils.common import get_size
from TextSummarizerLLM.logging import logger
from pathlib import Path
from TextSummarizerLLM.entity import DataIngestionConfig


# Create code for Data Ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Download the file from the source
        # This is a placeholder function and should be implemented based on the actual source of the data
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f'{filename} download! with following info: \n{headers}')
        else:
            logger.info(f'file already exists of size: {get_size(Path(self.config.local_data_file))}')


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extract the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)