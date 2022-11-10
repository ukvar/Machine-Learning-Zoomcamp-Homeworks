import bentoml
from bentoml.io import NumpyNdarray
import numpy as np


model_ref = bentoml.xgboost.get("heart_disease:latest")

model_runner = bentoml.xgboost.get("heart_disease:latest").to_runner()

svc = bentoml.Service("heart_disease", runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray()) 
def classify(input: np.ndarray):
    prediction= model_runner.predict.run(input)
    return prediction
    
# bentoml serve service_midterm.py:svc --reload