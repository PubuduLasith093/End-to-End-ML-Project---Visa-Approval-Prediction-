from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys


from us_visa.pipline.training_pipeline import TrainPipeline


pipline  = TrainPipeline()
pipline.run_pipeline()