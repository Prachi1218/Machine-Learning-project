import os
import sys
import numpy as np
import pandas as pd
from src.pipeline.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, "wb") as file_obj:
        dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)    
    
def evaluate_models(X_train, y_train, X_test, Y_test, models):
    try: 
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )      
        
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i] 
            
            model.fit(X_train, y_train)
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
            
        return report 
    except Exception as e:
        raise CustomException(e, sys)   
             