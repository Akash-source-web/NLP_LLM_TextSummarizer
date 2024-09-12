#Creating pipeline for the Model Training

from TextSummarizerLLM.config.configuration import ConfigrationManager
from TextSummarizerLLM.components.model_trainer import ModelTrainer
from TextSummarizerLLM.logging import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigrationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()