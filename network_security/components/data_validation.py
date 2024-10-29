import sys

from network_security.logging.logger import logging
from network_security.exception.exception import NetworkSecurityException

from network_security.entity.config import DataValidationConfig
from network_security.entity.artifact import DataValidationArtifact


class DataValidation:
    def __init__(self, data_validation_config=DataValidationConfig):
        try:
            self.data_validation_config=data_validation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        