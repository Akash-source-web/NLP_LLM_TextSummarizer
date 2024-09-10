from TextSummarizerLLM.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
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