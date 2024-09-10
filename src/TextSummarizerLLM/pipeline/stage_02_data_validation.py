#Creating pipeline for the data validation

from TextSummarizerLLM.config.configuration import ConfigrationManager
from TextSummarizerLLM.components.data_validation import DataValidation
from TextSummarizerLLM.logging import logger

class DataValidationTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigrationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()  