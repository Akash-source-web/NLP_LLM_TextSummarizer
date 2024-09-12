#Creating pipeline for the Data Transformation

from TextSummarizerLLM.config.configuration import ConfigrationManager
from TextSummarizerLLM.components.data_transformation import DataTransformation
from TextSummarizerLLM.logging import logger

class DataTransformationTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigrationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert() 