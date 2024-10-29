import os
import sys

from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation

from network_security.entity.config import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
)

from network_security.entity.artifact import (
    DataIngestionArtifact,
    DataValidationArtifact,
)

if __name__=="__main__":
    try:
        """
        Data Ingestion
        """
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)
        """
        data validation 
        """
        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact, datavalidationconfig)
        logging.info("Initiate Data Validation")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidationartifact)
        """
        Data Transformation
        """
    except Exception as e:
        raise NetworkSecurityException(e, sys)