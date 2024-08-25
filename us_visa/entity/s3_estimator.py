from us_visa.cloud_storage.aws_storage import SimpleStorageService
from us_visa.exception import USvisaException
from us_visa.entity.estimator import USvisaModel
import sys, os
from pandas import DataFrame
import pickle


class USvisaEstimator:
    """
    This class is used to save and retrieve us_visas model in s3 bucket and to do prediction
    """

    def __init__(self, model_dir = '/opt/ml/model/'):
        """
        :param bucket_name: Name of your model bucket
        :param model_path: Location of your model in bucket
        """
        #self.bucket_name = bucket_name
        #print(self.bucket_name)
        #self.s3 = SimpleStorageService()
        #print('after simplestorageservice function')
        self.model_dir = model_dir
        self.model_path =  os.path.join(self.model_dir, 'model.pkl')
        self.loaded_model:USvisaModel=None
        #self.s3 = SimpleStorageService()


    # def is_model_present(self,model_path):
    #     try:
    #         return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
    #     except USvisaException as e:
    #         print(e)
    #         return False

    def load_model(self,)->USvisaModel:
        """
        Load the model from the model_path
        :return:
        """

        try:
            if os.path.exists(self.model_path):
                # Load the model from the local directory
                with open(self.model_path, 'rb') as model_file:
                    model = pickle.load(model_file)
            else:
                # Fallback: Load the model from S3
                model = self.s3.load_model('model.pkl', bucket_name=self.s3.bucket_name)
            
            return model
        except Exception as e:
            raise USvisaException(e, sys) from e

    def save_model(self,from_file,remove:bool=False)->None:
        """
        Save the model to the model_path
        :param from_file: Your local system model path
        :param remove: By default it is false that mean you will have your model locally available in your system folder
        :return:
        """
        try:
            self.s3.upload_file(from_file,
                                to_filename=self.model_path,
                                bucket_name=self.bucket_name,
                                remove=remove
                                )
        except Exception as e:
            raise USvisaException(e, sys)


    def predict(self,dataframe:DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            return self.loaded_model.predict(dataframe=dataframe)
        except Exception as e:
            raise USvisaException(e, sys)       