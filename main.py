import os
import sys

from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

from network_security.components.data_ingestion import DataIngestion

from network_security.entity.config import (
    TrainingPipelineConfig,
    DataIngestionConfig
)

from network_security.entity.artifact import (
    DataIngestionArtifact
)

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)