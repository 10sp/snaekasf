import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import sklearn as skl 
import pandas as pd
from pgmpy.models import BayesianModel 
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

Attributes = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'heartdisease'] 
heartDisease = pd.read_csv("processed.hungarian.data", names = Attributes)
del heartDisease['ca'] 
del heartDisease['slope'] 
del heartDisease['thal'] 
del heartDisease['oldpeak'] 
heartDisease = heartDisease.replace('?', np.nan)

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('sex', 'fbs'), ('exang', 'trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'), ('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')]) 
model.fit(heartDisease, estimator = MaximumLikelihoodEstimator)

heartDisease_infer = VariableElimination(model)
q = heartDisease_infer.query(variables=['heartdisease'], evidence={'age': 42})
print(q)