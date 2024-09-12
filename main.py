from TextSummarizerLLM.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from TextSummarizerLLM.pipeline.stage_02_data_validation import DataValidationTraningPipeline
from TextSummarizerLLM.pipeline.stage_03_data_transformation import DataTransformationTraningPipeline
from TextSummarizerLLM.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizerLLM.logging import logger


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<')
    data_ingestion = DataIngestionTraningPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<\n\nx===========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<')
    data_validation = DataValidationTraningPipeline()
    data_validation.main()
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<\n\nx===========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<')
    data_transformation = DataTransformationTraningPipeline()
    data_transformation.main()
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<\n\nx===========x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Training Stage'
try:
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<')
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<\n\nx===========x')
except Exception as e:
    logger.exception(e)
    raise e
